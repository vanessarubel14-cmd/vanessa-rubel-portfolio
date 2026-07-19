#!/usr/bin/env python3
"""Rebuild the audited Tiffany summary data and static SVG visuals."""

from __future__ import annotations

import csv
import re
import sys
import zipfile
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Iterable, Sequence
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "tiffany" / "raw"
CLEAN = ROOT / "data" / "tiffany" / "clean"
IMAGES = ROOT / "images" / "tiffany-data"

PINTEREST = RAW / "Pinterest Analytics 11:24-9:25.csv"
LTK = RAW / "LTK_Audit_Tiffany.xlsx"
SHOPMY = RAW / "TIFF DATA Shop My.xlsx"

LTK_SHEETS = {
    "summary": "Summary",
    "latest": "brands_1m",
    "ninety": "brands_90d",
}
SHOPMY_SHEETS = {
    "domains": "shop my 90days- performancebysi",
    "orders": "shop my 90days- allorders",
}

EXPECTED = {
    "pinterest": {
        "rows": 319,
        "start": date(2024, 11, 1),
        "end": date(2025, 9, 15),
        "impressions": Decimal("97937"),
    },
    "ltk_latest": {
        "clicks": Decimal("17767"),
        "orders": Decimal("399"),
        "items": Decimal("1050"),
        "commissions": Decimal("8433.73"),
    },
    "ltk_ninety": {
        "clicks": Decimal("62089"),
        "orders": Decimal("1465"),
        "items": Decimal("2882"),
        "commissions": Decimal("18982.43"),
        "duplicate_extras": 1,
    },
    "shopmy": {
        "clicks": Decimal("5948"),
        "orders": Decimal("60"),
        "volume": Decimal("23227.90"),
        "commissions": Decimal("2855.91"),
        "start": date(2025, 5, 2),
        "end": date(2025, 7, 30),
        "duplicate_extras": 3,
    },
}

TOP_FIVE = [
    "rachelcomey.com",
    "tibi.com",
    "auratenewyork.com",
    "chanluu.com",
    "nomasei.com",
]
PARTNER_NAMES = {
    "rachelcomey.com": "Rachel Comey",
    "tibi.com": "Tibi",
    "auratenewyork.com": "Aurate",
    "chanluu.com": "Chan Luu",
    "nomasei.com": "Nomasei",
}

COLOR = {
    "paper": "#FAF9F1",
    "cobalt": "#0212EE",
    "cherry": "#D20001",
    "pink": "#FEC6E9",
    "ink": "#1A1A1A",
    "muted": "#5D5D56",
    "grid": "#D7D7CD",
}

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "p": "http://schemas.openxmlformats.org/package/2006/relationships",
}


class BuildError(RuntimeError):
    pass


def check(label: str, actual: Any, expected: Any) -> None:
    if actual != expected:
        raise BuildError(f"{label} mismatch: calculated {actual}, expected {expected}")


def decimal(value: Any, label: str) -> Decimal:
    if value in (None, "", "-"):
        return Decimal("0")
    try:
        return Decimal(str(value).replace("$", "").replace(",", ""))
    except InvalidOperation as exc:
        raise BuildError(f"Malformed numeric value for {label}: {value!r}") from exc


def cents(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def pct(value: Decimal, places: str = "0.1") -> Decimal:
    return value.quantize(Decimal(places), rounding=ROUND_HALF_UP)


def money(value: Decimal) -> str:
    return "$" + f"{cents(value):,.2f}"


def integer(value: Decimal) -> str:
    return f"{int(value):,}"


def require(path: Path) -> None:
    if not path.is_file():
        raise BuildError(f"Required source file is missing: {path.relative_to(ROOT)}")


def write_csv(path: Path, fields: Sequence[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def excel_column(reference: str) -> int:
    match = re.match(r"([A-Z]+)", reference)
    if not match:
        raise BuildError(f"Malformed Excel cell reference: {reference}")
    result = 0
    for character in match.group(1):
        result = result * 26 + ord(character) - 64
    return result - 1


def shared_strings(archive: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in archive.namelist():
        return []
    root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    return ["".join(node.text or "" for node in item.iterfind(".//m:t", NS))
            for item in root.findall("m:si", NS)]


def workbook_sheet_targets(archive: zipfile.ZipFile) -> dict[str, str]:
    workbook = ET.fromstring(archive.read("xl/workbook.xml"))
    relations = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    targets = {node.attrib["Id"]: node.attrib["Target"] for node in relations}
    result: dict[str, str] = {}
    for sheet in workbook.find("m:sheets", NS) or []:
        relation = sheet.attrib[f"{{{NS['r']}}}id"]
        target = targets[relation].lstrip("/")
        result[sheet.attrib["name"]] = target if target.startswith("xl/") else "xl/" + target
    return result


def read_xlsx_sheet(path: Path, sheet_name: str) -> list[list[Any]]:
    require(path)
    with zipfile.ZipFile(path) as archive:
        targets = workbook_sheet_targets(archive)
        if sheet_name not in targets:
            raise BuildError(f"{path.name} is missing workbook tab {sheet_name!r}")
        strings = shared_strings(archive)
        root = ET.fromstring(archive.read(targets[sheet_name]))
        output: list[list[Any]] = []
        for row_node in root.findall(".//m:sheetData/m:row", NS):
            values: dict[int, Any] = {}
            for cell in row_node.findall("m:c", NS):
                index = excel_column(cell.attrib.get("r", ""))
                kind = cell.attrib.get("t")
                if kind == "inlineStr":
                    value = "".join(node.text or "" for node in cell.iterfind(".//m:t", NS))
                else:
                    node = cell.find("m:v", NS)
                    raw = "" if node is None else node.text or ""
                    if kind == "s" and raw:
                        value = strings[int(raw)]
                    elif kind in {"str", "b", "e"}:
                        value = raw
                    elif raw == "":
                        value = None
                    else:
                        value = decimal(raw, f"{path.name} {sheet_name} {cell.attrib.get('r')}")
                values[index] = value
            if values:
                row = [None] * (max(values) + 1)
                for index, value in values.items():
                    row[index] = value
                output.append(row)
    return output


def table(path: Path, sheet_name: str) -> list[dict[str, Any]]:
    rows = read_xlsx_sheet(path, sheet_name)
    if not rows:
        raise BuildError(f"{path.name} tab {sheet_name!r} is empty")
    header = [str(value) if value is not None else "" for value in rows[0]]
    result = []
    for row in rows[1:]:
        padded = row + [None] * (len(header) - len(row))
        if any(value not in (None, "") for value in padded):
            result.append(dict(zip(header, padded)))
    return result


def require_columns(rows: list[dict[str, Any]], required: Sequence[str], label: str) -> None:
    actual = set(rows[0]) if rows else set()
    missing = [column for column in required if column not in actual]
    if missing:
        raise BuildError(f"{label} is missing required columns: {', '.join(missing)}")


def parse_pinterest() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    require(PINTEREST)
    with PINTEREST.open("r", encoding="utf-8-sig", newline="") as handle:
        source = list(csv.reader(handle))
    header = next((index for index, row in enumerate(source)
                   if row[:2] == ["Date", "Impressions"]), None)
    if header is None:
        raise BuildError("Pinterest source has no Date, Impressions table")
    daily: list[dict[str, Any]] = []
    for source_row, row in enumerate(source[header + 1:], header + 2):
        if not row or not row[0]:
            break
        try:
            day = datetime.strptime(row[0], "%Y-%m-%d").date()
        except ValueError:
            break
        daily.append({
            "date": day,
            "impressions": decimal(row[1], f"Pinterest row {source_row}"),
            "estimate_status": "estimated" if day >= date(2025, 9, 14) else "reported",
            "source_row": source_row,
        })
    check("Pinterest row count", len(daily), EXPECTED["pinterest"]["rows"])
    check("Pinterest start", daily[0]["date"], EXPECTED["pinterest"]["start"])
    check("Pinterest end", daily[-1]["date"], EXPECTED["pinterest"]["end"])
    check("Pinterest impressions", sum(row["impressions"] for row in daily),
          EXPECTED["pinterest"]["impressions"])

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in daily:
        grouped[row["date"].strftime("%Y-%m")].append(row)
    monthly: list[dict[str, Any]] = []
    for month, rows in grouped.items():
        total = sum(row["impressions"] for row in rows)
        monthly.append({
            "month": month,
            "label": rows[0]["date"].strftime("%b %Y"),
            "days_reported": len(rows),
            "impressions": total,
            "average_daily_impressions": cents(total / Decimal(len(rows))),
            "coverage": "partial through Sep. 15" if month == "2025-09" else "full month",
            "estimated_dates": sum(row["estimate_status"] == "estimated" for row in rows),
        })
    return daily, monthly


def aggregate(rows: list[dict[str, Any]], mapping: dict[str, str]) -> dict[str, Decimal]:
    return {name: sum((decimal(row.get(column), f"{column} value") for row in rows),
                      Decimal("0")) for name, column in mapping.items()}


def duplicate_extras(rows: list[dict[str, Any]]) -> int:
    if not rows:
        return 0
    fields = list(rows[0])
    counts = Counter(tuple(row.get(field) for field in fields) for row in rows)
    return sum(count - 1 for count in counts.values() if count > 1)


def parse_ltk() -> tuple[list[dict[str, Any]], dict[str, Decimal]]:
    summary = table(LTK, LTK_SHEETS["summary"])
    latest_rows = table(LTK, LTK_SHEETS["latest"])
    ninety_rows = table(LTK, LTK_SHEETS["ninety"])
    required = ["advertiser_name", "clicks", "commissions", "orders", "items_sold"]
    require_columns(latest_rows, required, f"{LTK.name} {LTK_SHEETS['latest']}")
    require_columns(ninety_rows, required, f"{LTK.name} {LTK_SHEETS['ninety']}")
    mapping = {"clicks": "clicks", "orders": "orders", "items": "items_sold",
               "commissions_raw": "commissions"}
    latest = aggregate(latest_rows, mapping)
    ninety = aggregate(ninety_rows, mapping)
    latest["commissions"] = cents(latest["commissions_raw"])
    ninety["commissions"] = cents(ninety["commissions_raw"])
    for key in ("clicks", "orders", "items", "commissions"):
        check(f"LTK latest {key}", latest[key], EXPECTED["ltk_latest"][key])
        check(f"LTK 90-day {key}", ninety[key], EXPECTED["ltk_ninety"][key])
    check("LTK 90-day duplicate extras", duplicate_extras(ninety_rows),
          EXPECTED["ltk_ninety"]["duplicate_extras"])

    summary_by_period = {row["Period"]: row for row in summary}
    for name, source in [("Last 30 days", latest), ("Last 90 days", ninety)]:
        if name not in summary_by_period:
            raise BuildError(f"LTK Summary tab is missing {name}")
        row = summary_by_period[name]
        check(f"LTK Summary {name} clicks", decimal(row["Clicks"], "summary clicks"), source["clicks"])
        check(f"LTK Summary {name} orders", decimal(row["Orders"], "summary orders"), source["orders"])
        check(f"LTK Summary {name} commissions", cents(decimal(row["Commissions"], "summary commissions")), source["commissions"])
        calculated_conversion = pct(source["orders"] / source["clicks"] * 100, "0.01")
        check(f"LTK Summary {name} conversion", decimal(row["Conversion %"], "summary conversion"), calculated_conversion)
        calculated_average = cents(source["commissions"] / source["orders"])
        check(f"LTK Summary {name} commission per order", decimal(row["Avg Commission / Order"], "summary average"), calculated_average)

    preceding = {key: ninety[key] - latest[key]
                 for key in ("clicks", "orders", "items", "commissions")}
    periods = [
        {
            "period": "Preceding 60 days",
            "reporting_days": Decimal("60"),
            "period_note": "Derived as last 90 days minus last 30 days",
            **preceding,
        },
        {
            "period": "Latest 30 days",
            "reporting_days": Decimal("30"),
            "period_note": "Supplied last-30-days view",
            **{key: latest[key] for key in ("clicks", "orders", "items", "commissions")},
        },
    ]
    for row in periods:
        row["commission_per_day"] = row["commissions"] / row["reporting_days"]
        row["commission_per_order"] = row["commissions"] / row["orders"]
        row["items_per_order"] = row["items"] / row["orders"]
        row["order_conversion_rate"] = row["orders"] / row["clicks"] * 100
    derived = {
        "latest_commission_share": latest["commissions"] / ninety["commissions"] * 100,
        "daily_commission_lift": periods[1]["commission_per_day"] / periods[0]["commission_per_day"] - 1,
        "commission_per_order_ratio": periods[1]["commission_per_order"] / periods[0]["commission_per_order"],
        "items_per_order_ratio": periods[1]["items_per_order"] / periods[0]["items_per_order"],
    }
    return periods, derived


def excel_date(value: Any) -> date:
    if isinstance(value, Decimal):
        return (datetime(1899, 12, 30) + timedelta(days=float(value))).date()
    if isinstance(value, str):
        return datetime.fromisoformat(value).date()
    raise BuildError(f"Malformed Excel date: {value!r}")


def parse_shopmy() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    domains = table(SHOPMY, SHOPMY_SHEETS["domains"])
    orders = table(SHOPMY, SHOPMY_SHEETS["orders"])
    require_columns(domains, ["Domain", "# Links", "Clicks", "Orders", "Volume", "Earned"],
                    f"{SHOPMY.name} {SHOPMY_SHEETS['domains']}")
    require_columns(orders, ["Date", "Merchant", "Domain", "Order Amount USD", "Commission USD", "Status"],
                    f"{SHOPMY.name} {SHOPMY_SHEETS['orders']}")
    totals = aggregate(domains, {"clicks": "Clicks", "orders": "Orders",
                                 "volume": "Volume", "commissions": "Earned"})
    for key in ("clicks", "orders", "volume", "commissions"):
        check(f"ShopMy {key}", totals[key], EXPECTED["shopmy"][key])
    check("ShopMy order ledger row count", len(orders), int(totals["orders"]))
    check("ShopMy order duplicate extras", duplicate_extras(orders),
          EXPECTED["shopmy"]["duplicate_extras"])
    ledger_volume = sum(decimal(row["Order Amount USD"], "order amount") for row in orders)
    ledger_commissions = sum(decimal(row["Commission USD"], "order commission") for row in orders)
    check("ShopMy ledger volume", ledger_volume, totals["volume"])
    check("ShopMy ledger commissions", ledger_commissions, totals["commissions"])
    dates = [excel_date(row["Date"]) for row in orders]
    check("ShopMy first order date", min(dates), EXPECTED["shopmy"]["start"])
    check("ShopMy last order date", max(dates), EXPECTED["shopmy"]["end"])
    if set(str(row["Status"]) for row in orders) != {"active"}:
        raise BuildError("ShopMy 90-day order ledger contains a non-active status")

    ranked = sorted(domains, key=lambda row: decimal(row["Volume"], "domain volume"), reverse=True)
    check("ShopMy top-five domains", [row["Domain"] for row in ranked[:5]], TOP_FIVE)
    cleaned: list[dict[str, Any]] = []
    for rank, row in enumerate(ranked, 1):
        cleaned.append({
            "rank_by_net_order_volume": rank,
            "partner": PARTNER_NAMES.get(str(row["Domain"]), str(row["Domain"])),
            "domain": row["Domain"],
            "links": decimal(row["# Links"], "domain links"),
            "clicks": decimal(row["Clicks"], "domain clicks"),
            "orders": decimal(row["Orders"], "domain orders"),
            "net_order_volume": decimal(row["Volume"], "domain volume"),
            "commissions": decimal(row["Earned"], "domain commissions"),
            "segment": "Top five partners" if rank <= 5 else "All other partners",
        })
    top = aggregate(cleaned[:5], {"clicks": "clicks", "orders": "orders",
                                  "volume": "net_order_volume", "commissions": "commissions"})
    rest = {key: totals[key] - top[key] for key in totals}
    derived = {
        "totals": totals,
        "top": top,
        "rest": rest,
        "shares": {key: top[key] / totals[key] * 100 for key in totals},
        "top_conversion": top["orders"] / top["clicks"] * 100,
        "rest_conversion": rest["orders"] / rest["clicks"] * 100,
        "conversion_ratio": (top["orders"] / top["clicks"]) / (rest["orders"] / rest["clicks"]),
        "top_volume_per_order": top["volume"] / top["orders"],
        "rest_volume_per_order": rest["volume"] / rest["orders"],
        "volume_per_order_ratio": (top["volume"] / top["orders"]) / (rest["volume"] / rest["orders"]),
        "positive_volume": sum(decimal(row["Order Amount USD"], "order amount") for row in orders
                               if decimal(row["Order Amount USD"], "order amount") > 0),
        "negative_volume": sum(decimal(row["Order Amount USD"], "order amount") for row in orders
                               if decimal(row["Order Amount USD"], "order amount") < 0),
    }
    return cleaned, derived


STYLE = f"""
text{{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;fill:{COLOR['ink']}}}
.eyebrow{{font-size:13px;font-weight:700;letter-spacing:1.8px;fill:{COLOR['cherry']}}}
.title{{font-size:34px;font-weight:700;letter-spacing:-.7px;fill:{COLOR['cobalt']}}}
.subtitle{{font-size:15px;fill:{COLOR['muted']}}}
.metric{{font-size:31px;font-weight:700;fill:{COLOR['cobalt']}}}
.metric-sm{{font-size:24px;font-weight:700;fill:{COLOR['cobalt']}}}
.label{{font-size:17px;font-weight:700}}
.small{{font-size:14px;fill:{COLOR['muted']}}}
.axis{{font-size:14px;fill:{COLOR['muted']}}}
.value{{font-size:16.5px;font-weight:700}}
"""


def svg(width: int, height: int, title: str, description: str,
        body: Sequence[str], definitions: str = "") -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        'role="img" aria-labelledby="chart-title chart-description">\n'
        f'<title id="chart-title">{escape(title)}</title>\n'
        f'<desc id="chart-description">{escape(description)}</desc>\n'
        f'<style>{STYLE}</style>\n{definitions}'
        f'<rect width="{width}" height="{height}" rx="8" fill="{COLOR["paper"]}"/>\n'
        + "\n".join(body) + "\n</svg>\n"
    )


def tx(x: float, y: float, value: str, klass: str = "", anchor: str = "start") -> str:
    return (f'<text x="{x:.1f}" y="{y:.1f}" class="{klass}" text-anchor="{anchor}">'
            f'{escape(value)}</text>')


def multiline(x: float, y: float, values: Sequence[str], klass: str,
              line_height: float) -> str:
    spans = "".join(f'<tspan x="{x:.1f}" dy="{0 if index == 0 else line_height}">'
                    f'{escape(value)}</tspan>' for index, value in enumerate(values))
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{klass}">{spans}</text>'


def pinterest_svg(monthly: list[dict[str, Any]], mobile: bool) -> str:
    width, height = (330, 180) if mobile else (360, 180)
    left, right = 12, 12
    body: list[str] = []
    maximum = max(row["impressions"] for row in monthly)
    chart_top, chart_bottom = 16, 124
    chart_w = width - left - right
    gap = 4
    bar_w = (chart_w - gap * (len(monthly) - 1)) / len(monthly)
    for index, row in enumerate(monthly):
        x = left + index * (bar_w + gap)
        height_value = (chart_bottom - chart_top) * float(row["impressions"] / maximum)
        y = chart_bottom - height_value
        fill = "url(#partial)" if row["coverage"].startswith("partial") else COLOR["cobalt"]
        body.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{height_value:.1f}" rx="4" fill="{fill}"/>')
        body.append(tx(x + bar_w / 2, chart_bottom + 17,
                       row["label"].split()[0], "axis", "middle"))
    body.append(tx(left, 166, "Monthly impressions", "small"))
    body.append(tx(width - right, 166, "Sep. partial", "small", "end"))
    definitions = (f'<defs><pattern id="partial" width="8" height="8" patternUnits="userSpaceOnUse" '
                   f'patternTransform="rotate(45)"><rect width="8" height="8" fill="{COLOR["pink"]}"/>'
                   f'<rect width="3" height="8" fill="{COLOR["cherry"]}"/></pattern></defs>\n')
    return svg(width, height, "Pinterest visibility across the content calendar",
               "Monthly Pinterest impressions from November 2024 through September 15, 2025. "
               "The monthly totals sum to 97,937. September is a partial month with 15 dates, and the final two dates are estimated.",
               body, definitions)


def ltk_svg(periods: list[dict[str, Any]], derived: dict[str, Decimal], mobile: bool) -> str:
    width, height = (330, 232) if mobile else (360, 232)
    left, right = 14, 14
    preceding, latest = periods
    body: list[str] = []
    metrics = [
        ("Commission / order", preceding["commission_per_order"], latest["commission_per_order"],
         money, f'{pct(derived["commission_per_order_ratio"], "0.1")}×'),
        ("Items per order", preceding["items_per_order"], latest["items_per_order"],
         lambda value: f'{value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)}',
         f'{pct(derived["items_per_order_ratio"], "0.1")}×'),
        ("Daily commission", preceding["commission_per_day"], latest["commission_per_day"],
         money, f'+{pct(derived["daily_commission_lift"] * 100)}%'),
    ]
    y = 24
    bar_x = left
    bar_w = width - left - right
    for label, before, after, formatter, delta in metrics:
        maximum = max(before, after)
        body.append(tx(left, y, label, "label"))
        body.append(tx(width - right, y, delta, "value", "end"))
        body.append(tx(left, y + 21, f'{formatter(before)} → {formatter(after)}', "value"))
        body.append(f'<rect x="{bar_x}" y="{y + 30}" width="{bar_w}" height="8" rx="4" fill="{COLOR["grid"]}"/>')
        body.append(f'<rect x="{bar_x}" y="{y + 30}" width="{bar_w * float(before / maximum):.1f}" height="8" rx="4" fill="{COLOR["pink"]}"/>')
        body.append(f'<rect x="{bar_x}" y="{y + 42}" width="{bar_w * float(after / maximum):.1f}" height="8" rx="4" fill="{COLOR["cobalt"]}"/>')
        y += 64
    body.append(tx(left, 221, "Preceding 60 days → latest 30 days", "small"))
    return svg(width, height, "Recent LTK orders delivered more value",
               "The latest 30 days generated 44.4 percent of the 90-day commission total. "
               "Compared with the preceding 60 days, commission per order was 21 dollars and 14 cents versus 9 dollars and 90 cents, items per order were 2.63 versus 1.72, and average commission per day was 281 dollars and 12 cents versus 175 dollars and 81 cents.",
               body)


def shopmy_svg(data: dict[str, Any], mobile: bool) -> str:
    width, height = (330, 220) if mobile else (360, 220)
    left, right = 14, 14
    body: list[str] = []
    metrics = [("Click share", "clicks"), ("Order share", "orders"),
               ("Net order volume share", "volume"), ("Commission share", "commissions")]
    start_y = 24
    row_gap = 49
    bar_x = left
    bar_w = width - left - right
    for index, (label, key) in enumerate(metrics):
        y = start_y + index * row_gap
        share = data["shares"][key]
        rest = Decimal("100") - share
        body.append(tx(left, y, label, "label"))
        body.append(tx(width - right, y, f'{pct(share)}% top five', "value", "end"))
        body.append(f'<rect x="{bar_x}" y="{y + 11}" width="{bar_w}" height="17" rx="6" fill="{COLOR["pink"]}"/>')
        body.append(f'<rect x="{bar_x}" y="{y + 11}" width="{bar_w * float(share / 100):.1f}" height="17" rx="6" fill="{COLOR["cobalt"]}"/>')
    return svg(width, height, "A focused set of partners generated outsized value",
               "The top five ShopMy partners by net order volume generated 35.6 percent of clicks, 50 percent of orders, 74.6 percent of net order volume, and 74.0 percent of commissions. Their click-to-order conversion was 1.42 percent versus 0.78 percent for all other partners, and net order volume per order was 577 dollars and 57 cents versus 196 dollars and 70 cents.",
               body)


def write_clean(daily: list[dict[str, Any]], monthly: list[dict[str, Any]],
                ltk_periods: list[dict[str, Any]], ltk_derived: dict[str, Decimal],
                partners: list[dict[str, Any]], shopmy: dict[str, Any]) -> None:
    write_csv(CLEAN / "pinterest_daily_impressions.csv",
              ["date", "impressions", "estimate_status", "source_row"],
              ({**row, "date": row["date"].isoformat()} for row in daily))
    write_csv(CLEAN / "pinterest_monthly_impressions.csv",
              ["month", "label", "days_reported", "impressions",
               "average_daily_impressions", "coverage", "estimated_dates"], monthly)
    write_csv(CLEAN / "ltk_period_comparison.csv",
              ["period", "reporting_days", "period_note", "clicks", "orders", "items",
               "commissions", "commission_per_day", "commission_per_order",
               "items_per_order", "order_conversion_rate"], ltk_periods)
    write_csv(CLEAN / "shopmy_partner_performance.csv",
              ["rank_by_net_order_volume", "partner", "domain", "links", "clicks", "orders",
               "net_order_volume", "commissions", "segment"], partners)
    summary = [
        {"platform": "Pinterest", "metric": "impressions", "exact_value": "97937",
         "display_value": "97,937", "reporting_period": "2024-11-01 through 2025-09-15",
         "source_file": PINTEREST.name, "workbook_tab": "N/A (CSV)",
         "calculation": "Sum 319 daily impression values"},
        {"platform": "LTK", "metric": "latest_30_day_share_of_90_day_commission",
         "exact_value": str(ltk_derived["latest_commission_share"]), "display_value": "44.4%",
         "reporting_period": "Latest 30 days within supplied 90-day view",
         "source_file": LTK.name, "workbook_tab": "Summary; brands_1m; brands_90d",
         "calculation": "8433.73 / 18982.43 x 100"},
        {"platform": "LTK", "metric": "latest_30_day_average_commission_per_day",
         "exact_value": str(ltk_periods[1]["commission_per_day"]), "display_value": "$281.12",
         "reporting_period": "Latest 30 days",
         "source_file": LTK.name, "workbook_tab": "Summary; brands_1m",
         "calculation": "8433.73 / 30"},
        {"platform": "ShopMy", "metric": "top_five_share_of_net_order_volume",
         "exact_value": str(shopmy["shares"]["volume"]), "display_value": "74.6%",
         "reporting_period": "2025-05-02 through 2025-07-30",
         "source_file": SHOPMY.name,
         "workbook_tab": "shop my 90days- performancebysi; shop my 90days- allorders",
         "calculation": "17327.03 / 23227.90 x 100"},
    ]
    write_csv(CLEAN / "metrics_summary.csv",
              ["platform", "metric", "exact_value", "display_value", "reporting_period",
               "source_file", "workbook_tab", "calculation"], summary)


def build() -> None:
    daily, monthly = parse_pinterest()
    ltk_periods, ltk_derived = parse_ltk()
    partners, shopmy = parse_shopmy()
    write_clean(daily, monthly, ltk_periods, ltk_derived, partners, shopmy)
    IMAGES.mkdir(parents=True, exist_ok=True)
    outputs = {
        "pinterest-impressions.svg": pinterest_svg(monthly, False),
        "pinterest-impressions-mobile.svg": pinterest_svg(monthly, True),
        "ltk-recent-value.svg": ltk_svg(ltk_periods, ltk_derived, False),
        "ltk-recent-value-mobile.svg": ltk_svg(ltk_periods, ltk_derived, True),
        "shopmy-partner-concentration.svg": shopmy_svg(shopmy, False),
        "shopmy-partner-concentration-mobile.svg": shopmy_svg(shopmy, True),
    }
    for filename, content in outputs.items():
        (IMAGES / filename).write_text(content, encoding="utf-8")
    print("Tiffany visual build completed successfully.")
    print("Pinterest: 97,937 impressions across 319 dates; 11 monthly totals generated.")
    print("LTK: latest 30 days generated 44.4% of 90-day commission; "
          "$281.12 per day; $21.14 per order; 2.63 items per order.")
    print("ShopMy: top five partners generated 74.6% of net order volume and "
          "74.0% of commissions across the 90-day view.")


def main() -> int:
    try:
        build()
    except (BuildError, KeyError, zipfile.BadZipFile) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
