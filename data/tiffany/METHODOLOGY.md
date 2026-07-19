# Tiffany performance visual methodology

Updated: 2026-07-14

Presentation update: the verified Pinterest, LTK, and ShopMy findings are now shown as three compact result-card graphics on one page section. The charts were reduced in height and supporting explanations moved into HTML card copy. Source selection, calculations, duplicate handling, reporting periods, and displayed values are unchanged.

## Build and source controls

`scripts/build_tiffany_visuals.py` reads the authoritative exports identified below, recalculates each displayed result, writes cleaned summary CSVs to `data/tiffany/clean/`, and regenerates desktop and mobile SVGs in `images/tiffany-data/`.

Run from the repository root:

```bash
python3 scripts/build_tiffany_visuals.py
```

The build uses only Python's standard library. It reads Excel workbook XML directly, does not modify any raw file, and stops if a source, tab, required column, audited total, reporting date, duplicate count, or top-five partner list changes.

## Authoritative sources

| Platform | Source file | Workbook tab | Reporting period | Use |
|---|---|---|---|---|
| Pinterest | `Pinterest Analytics 11:24-9:25.csv` | N/A, CSV | Explicit 2024-11-01 through 2025-09-15 | Daily and monthly impressions |
| LTK | `LTK_Audit_Tiffany.xlsx` | `Summary` | Supplied last 30 days and last 90 days | Reconciled clicks, orders, commissions, conversion, and average commission per order |
| LTK | `LTK_Audit_Tiffany.xlsx` | `brands_1m` | Inferred last 30 days | Independent advertiser-level check of clicks, orders, items sold, and commissions |
| LTK | `LTK_Audit_Tiffany.xlsx` | `brands_90d` | Inferred last 90 days | Independent advertiser-level check and source for the 60-day subtraction |
| ShopMy | `TIFF DATA Shop My.xlsx` | `shop my 90days- performancebysi` | 90-day view; matching orders span 2025-05-02 through 2025-07-30 | Domain-level clicks, orders, net order volume, commissions, and top-five selection |
| ShopMy | `TIFF DATA Shop My.xlsx` | `shop my 90days- allorders` | Actual order dates 2025-05-02 through 2025-07-30 | Order-level reconciliation of volume, commission, dates, returns, status, and duplicate rows |

The previous November 2024 to September 2025 LTK product-link export and June to September ShopMy link export are no longer used in portfolio visuals. They remain in `data/tiffany/raw/` unchanged and remain documented in `AUDIT.md`.

## Pinterest calculation and chart decision

- The dated table contains 319 reporting dates from 2024-11-01 through 2025-09-15.
- Daily impressions sum to **97,937**.
- The final two dates, 2025-09-14 and 2025-09-15, are marked estimated by the export.
- Monthly totals are calculated by grouping the dated daily values by calendar month. The 11 monthly totals sum back to 97,937.
- Monthly daily averages were also calculated by dividing each monthly total by its reported date count. They are retained in `pinterest_monthly_impressions.csv` for review.
- The visual uses monthly totals because they add directly to the verified headline value and show delivered visibility. September is patterned and explicitly labeled as a partial 15-day month so its shorter coverage is not mistaken for a full-month decline.
- A daily line and seven-day moving average are no longer used. The dense daily series emphasized volatility and made the partial final month harder to read.

Monthly verification:

| Month | Dates | Impressions | Daily average |
|---|---:|---:|---:|
| Nov. 2024 | 30 | 8,470 | 282.33 |
| Dec. 2024 | 31 | 11,203 | 361.39 |
| Jan. 2025 | 31 | 12,216 | 394.06 |
| Feb. 2025 | 28 | 11,816 | 422.00 |
| Mar. 2025 | 31 | 10,043 | 323.97 |
| Apr. 2025 | 30 | 9,079 | 302.63 |
| May 2025 | 31 | 10,039 | 323.84 |
| Jun. 2025 | 30 | 7,256 | 241.87 |
| Jul. 2025 | 31 | 6,617 | 213.45 |
| Aug. 2025 | 31 | 7,099 | 229.00 |
| Sep. 2025 | 15 | 4,099 | 273.27 |

## LTK period comparison

The authoritative workbook's 30-day advertiser tab reconciles to:

- 17,767 clicks
- 399 orders
- 1,050 items sold
- $8,433.73 commissions

The 90-day advertiser tab reconciles to:

- 62,089 clicks
- 1,465 orders
- 2,882 items sold
- $18,982.43 commissions

The preceding 60-day component is derived by subtracting the latest 30-day values from the 90-day values. The two periods are not added.

| Metric | 90 days | Less latest 30 days | Preceding 60 days |
|---|---:|---:|---:|
| Clicks | 62,089 | 17,767 | 44,322 |
| Orders | 1,465 | 399 | 1,066 |
| Items sold | 2,882 | 1,050 | 1,832 |
| Commissions | $18,982.43 | $8,433.73 | $10,548.70 |

The comparison uses 30 and 60 reporting-day denominators, matching the export labels:

- Latest 30-day commission share: `$8,433.73 / $18,982.43 = 44.4291%`, displayed as **44.4%**.
- Latest 30-day average commission per day: `$8,433.73 / 30 = $281.1243`, displayed as **$281.12**.
- Preceding 60-day average commission per day: `$10,548.70 / 60 = $175.8117`, displayed as **$175.81**.
- Daily commission comparison: `$281.1243 / $175.8117 - 1 = 59.9008%`, displayed as **59.9% higher**.
- Latest 30-day commission per order: `$8,433.73 / 399 = $21.1372`, displayed as **$21.14**.
- Preceding 60-day commission per order: `$10,548.70 / 1,066 = $9.8956`, displayed as **$9.90**.
- Commission per order ratio: `2.1360`, displayed as **2.1x**.
- Latest 30-day items per order: `1,050 / 399 = 2.6316`, displayed as **2.63**.
- Preceding 60-day items per order: `1,832 / 1,066 = 1.7186`, displayed as **1.72**.
- Items per order ratio: `1.5313`, displayed as **1.5x**.

Clicks and orders are retained in the cleaned comparison for auditability. The case study does not claim that traffic, click conversion, or order count increased. The preceding 60-day component has more orders per day and a slightly higher click-to-order conversion rate, so those would contradict the value-per-order story.

The calendar dates are inferred from the export timing and are not stored in the workbook tabs. Public copy therefore uses `latest 30 days` and `preceding 60 days within the supplied 90-day view` instead of presenting inferred dates as explicit platform metadata.

## ShopMy partner concentration

The 90-day domain tab reports 5,948 clicks, 60 orders, $23,227.90 net order volume, and $2,855.91 commissions. The 60-row order tab independently matches the order count, net order volume, and commissions.

The top five partners are selected only by descending net order volume in `shop my 90days- performancebysi`:

1. Rachel Comey
2. Tibi
3. Aurate
4. Chan Luu
5. Nomasei

Their combined results are 2,115 clicks, 30 orders, $17,327.03 net order volume, and $2,114.51 commissions. All other partners combine to 3,833 clicks, 30 orders, $5,900.87 net order volume, and $741.40 commissions.

Displayed shares:

- Clicks: `2,115 / 5,948 = 35.5582%`, displayed as **35.6%**.
- Orders: `30 / 60 = 50.0%`.
- Net order volume: `$17,327.03 / $23,227.90 = 74.5958%`, displayed as **74.6%**.
- Commissions: `$2,114.51 / $2,855.91 = 74.0398%`, displayed as **74.0%**.

Supporting efficiency calculations:

- Top-five click-to-order conversion: `30 / 2,115 = 1.4184%`, displayed as **1.42%**.
- All-other click-to-order conversion: `30 / 3,833 = 0.7827%`, displayed as **0.78%**.
- Conversion ratio: `1.8123`, displayed as **1.8x**.
- Top-five net order volume per order: `$17,327.03 / 30 = $577.57`.
- All-other net order volume per order: `$5,900.87 / 30 = $196.70`.
- Net order volume per order ratio: `2.9364`, displayed as **2.9x**.

The metric is called net order volume because the order ledger includes two negative $114.50 return rows. Positive order amounts total $23,456.90 and the returns reduce the reported total by $229.00 to $23,227.90.

## Duplicate and missing-value handling

- The LTK 90-day advertiser tab contains one exact duplicated `Negative Underwear` row. It contributes one click and no order, item, or commission. The workbook's Summary total includes it, so the visual calculation preserves it. A strict exact-row-deduplicated click total would be 62,088, but clicks are not a headline result in this visual.
- The ShopMy 90-day order ledger contains three exact extra rows across three duplicate groups. No transaction ID is provided, and the domain totals include them. They are preserved rather than silently deleted.
- Hyphens and blanks are treated as missing where the source uses them. They contribute zero only when summing a platform aggregate that explicitly reports no metric for that domain row.
- All 60 ShopMy order rows are marked `active`. No status filter changes the total.
- No transaction, product, partner, or domain is merged across platforms.

## Corrections from the prior implementation

- Removed the LTK extended-export product ranking and its $67.2K commission headline.
- Removed the ShopMy June to September link ranking and its $24.1K order-volume headline.
- Replaced the daily Pinterest line with monthly totals and a clear partial-September treatment.
- Reframed LTK around recent value per order, items per order, and commission per day using one nested 90-day reporting view.
- Reframed ShopMy around top-five partner concentration using the matching 90-day domain and order tabs.
- The unsupported claims `340K+ Product clicks`, `$90K Order volume`, `4.8K+ Engagements`, and `82K total audience` remain excluded.

## Generated outputs

Cleaned CSVs:

- `pinterest_daily_impressions.csv`
- `pinterest_monthly_impressions.csv`
- `ltk_period_comparison.csv`
- `shopmy_partner_performance.csv`
- `metrics_summary.csv`

Portfolio SVGs:

- `pinterest-impressions.svg` and `pinterest-impressions-mobile.svg`
- `ltk-recent-value.svg` and `ltk-recent-value-mobile.svg`
- `shopmy-partner-concentration.svg` and `shopmy-partner-concentration-mobile.svg`

## Interpretation limits

- Pinterest impressions document platform visibility. They do not prove that content organization alone caused every impression.
- LTK compares nested periods inside one platform export. It supports a recent value-per-order story, not a broad claim that every performance metric improved.
- ShopMy concentration shows where value appeared in a 90-day view. It does not prove that the same five partners will lead in future periods.
- LTK commissions, ShopMy net order volume, and Pinterest impressions have different definitions and periods. They are never added or ranked against one another.
