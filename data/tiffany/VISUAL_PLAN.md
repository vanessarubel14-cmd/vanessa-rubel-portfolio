# Tiffany & Wendel Portfolio Visual Plan

## Source boundary

This plan uses `data/tiffany/AUDIT.md` as its sole source of truth. It does not reinterpret the raw files, combine datasets, or resolve discrepancies that the audit left open. The audit covers all 24 current source files and every tab in the included Excel workbooks.

## Strongest verified results

- **Pinterest:** 97,937 impressions from November 1, 2024 through September 15, 2025. This is the cleanest audience result because the export has explicit dates. The final two dates are estimated and must be disclosed.
- **LTK:** the product-link export labeled November 2024–September 2025 contains 138,420 clicks, 4,473 orders, 8,095 items sold, and $67,273.50 in commissions. These are verified totals for the supplied export, not a proven full-account total: exact dates are absent, one duplicated one-click row is present, and the 3,000-row export may be capped.
- **ShopMy:** the export labeled June–September 2025 contains 5,818 clicks, 88 orders, $24,101.25 in order volume, and $3,032.30 in commissions. Its totals are internally consistent, but the exact start and end dates are absent.
- **Styling operations:** 108 unique uncanceled bookings are supported for January 16, 2023 through August 19, 2025. This is valid operational evidence, but it is not selected for the primary portfolio story because the requested focus is content organization, affiliate strategy, product curation, and platform management. The associated $36,726 is listed booking value, not verified collected revenue.

No current source verifies the existing claims of 340K+ product clicks, $90K order volume, 4.8K+ engagements, or 82K total audience.

## Proposed portfolio metrics

Only the first three rows are headline metrics. Supporting metrics belong inside their platform-specific visual or caption; they should not become additional headline cards. Shortened values are truncated where necessary so the displayed number never exceeds the verified value.

| Role | Display label | Exact value | Rounded display value | Platform | Reporting period | Source file | Workbook tab | Calculation method |
|---|---|---:|---:|---|---|---|---|---|
| Headline | Pinterest impressions | 97,937 | 97,937 | Pinterest | Nov. 1, 2024–Sept. 15, 2025 | `Pinterest Analytics 11:24-9:25.csv` | N/A — CSV | Sum the daily `Impressions` values for the explicit date range; retain and disclose the final two estimated dates. |
| Headline | LTK commissions | $67,273.50 | $67.2K | LTK | Export labeled Nov. 2024–Sept. 2025; exact dates absent | `LTK-export11:24-9:25.csv` | N/A — CSV | Sum `commissions` across the supplied product-link rows as exported. Do not silently remove the duplicate row; it has no reported commission effect. |
| Headline | ShopMy order volume | $24,101.25 | $24.1K | ShopMy | Export labeled June–Sept. 2025; exact dates absent | `6:25-9:25 links sm.csv` | N/A — CSV | Sum numeric `Order Volume` values across the 32 rows with reported volume; preserve missing values as missing rather than zero. |
| Supporting | LTK product-link clicks | 138,420 | 138.4K | LTK | Export labeled Nov. 2024–Sept. 2025; exact dates absent | `LTK-export11:24-9:25.csv` | N/A — CSV | Sum the export's click metric across supplied rows. Use the raw audited total and flag the duplicated one-click row. Never substitute `active_links`. |
| Supporting | LTK orders | 4,473 | 4,473 | LTK | Export labeled Nov. 2024–Sept. 2025; exact dates absent | `LTK-export11:24-9:25.csv` | N/A — CSV | Sum `orders` across the supplied product-link rows. |
| Supporting | LTK items sold | 8,095 | 8,095 | LTK | Export labeled Nov. 2024–Sept. 2025; exact dates absent | `LTK-export11:24-9:25.csv` | N/A — CSV | Sum `items_sold` across the supplied product-link rows. |
| Supporting | LTK click-to-order conversion | 3.2315% | 3.23% | LTK | Export labeled Nov. 2024–Sept. 2025; exact dates absent | `LTK-export11:24-9:25.csv` | N/A — CSV | `4,473 orders ÷ 138,420 clicks × 100`. |
| Supporting | ShopMy clicks | 5,818 | 5,818 | ShopMy | Export labeled June–Sept. 2025; exact dates absent | `6:25-9:25 links sm.csv` | N/A — CSV | Sum numeric `Clicks` values; preserve rows with missing clicks as missing. |
| Supporting | ShopMy orders | 88 | 88 | ShopMy | Export labeled June–Sept. 2025; exact dates absent | `6:25-9:25 links sm.csv` | N/A — CSV | Sum numeric `Order Count` values. |
| Supporting | ShopMy commissions | $3,032.30 | $3,032 | ShopMy | Export labeled June–Sept. 2025; exact dates absent | `6:25-9:25 links sm.csv` | N/A — CSV | Sum numeric `Commission` values; preserve missing values as missing. |
| Supporting | ShopMy click-to-order conversion | 1.5125% | 1.51% | ShopMy | Export labeled June–Sept. 2025; exact dates absent | `6:25-9:25 links sm.csv` | N/A — CSV | `88 orders ÷ 5,818 clicks × 100`. |

The three headline metrics are not additive. They describe different platform metrics over different reporting periods and must not be presented as a combined total or a ranked platform comparison.

## Claims to remove or replace

| Existing claim | Decision | Audit-supported treatment |
|---|---|---|
| `340K+ Product clicks` | **Exclude — based on the wrong metric.** | The near-match is 344,020 LTK `active_links`, which is not clicks. If click performance is needed, use 138,420 product-link clicks from the LTK export labeled Nov. 2024–Sept. 2025, with its limitations disclosed. |
| `$90K Order volume` | **Exclude — unsupported.** | The largest ShopMy snapshot is $51,980.60 but has no reporting period. The strongest period-labeled result is $24,101.25 for the export labeled June–Sept. 2025. LTK does not provide order volume. |
| `4.8K+ Engagements` | **Exclude — unsupported.** | The only audited engagement result is 134 engagements in a restricted two-board Pinterest table; it does not support a portfolio-wide engagement claim. |
| `82K total audience` | **Exclude — unsupported.** | The available early daily audience series has 12 missing dates and daily values from 7 to 86; those values cannot be added into a total audience claim. |
| `102K+ impressions` | **Replace.** | Use **97,937 Pinterest impressions, Nov. 1, 2024–Sept. 15, 2025**. The source and period are appropriate for the case study, provided the final two estimated dates are disclosed. Do not round this to 98K or 102K+. |

## Headline metric selection

Use three headline metrics, each attached to its own platform section rather than displayed as a comparative scoreboard:

1. **97,937 Pinterest impressions** — the strongest explicit-date audience result.
2. **$67.2K LTK commissions** — a meaningful affiliate outcome from the supplied export labeled November 2024–September 2025.
3. **$24.1K ShopMy order volume** — a distinct commerce outcome from the supplied export labeled June–September 2025.

The LTK click, order, item, and conversion values should support the LTK visual, not compete as extra cards. ShopMy clicks, orders, commissions, and conversion should be handled the same way.

## Visual specifications

### Visual 1 — Pinterest performance over time

- **Chart type:** Daily line chart with a seven-day moving-average overlay.
- **Title:** `Pinterest visibility across the content calendar`
- **Metric and dimensions:** Daily impressions by date; raw daily series plus seven-day moving average.
- **Source file and tab:** `Pinterest Analytics 11:24-9:25.csv`; N/A — CSV.
- **Reporting period:** November 1, 2024–September 15, 2025.
- **Filtering and calculation rules:** Use only the dated impression series. Sum daily impressions to 97,937. Calculate the moving average from the daily values without filling absent dates unless the chart-building audit confirms that a date is truly missing. Visually distinguish the final two estimated dates. Do not add saves, outbound clicks, engagements, or audience values to impressions.
- **Exact data labels:** Fixed callout: `97,937 total impressions`. Period label: `Nov. 1, 2024–Sept. 15, 2025`. Final two points: `Estimated`. Any point-level tooltip must show the source's exact daily value rather than a rounded abbreviation.
- **Viewer insight:** Vanessa's organized Pinterest publishing and platform management are accompanied by a measurable visibility record over time, without overstating audience size or engagement or claiming a trend before the chart is produced.

### Visual 2 — LTK product curation and affiliate performance

- **Chart type:** Ranked horizontal bar chart of top product rows by commission, with clicks and orders as secondary labels.
- **Title:** `LTK performance across curated affiliate links`
- **Metric and dimensions:** Commission by product/link row, ranked descending; secondary dimensions are clicks and orders. Treat any aggregate Amazon row as `Aggregate / unattributed`, separate from named products.
- **Source file and tab:** `LTK-export11:24-9:25.csv`; N/A — CSV.
- **Reporting period:** Export labeled November 2024–September 2025; exact dates are not present in the file.
- **Filtering and calculation rules:** Rank the supplied rows by reported commission. Do not use `active_links` as clicks. Do not silently delete the duplicated one-click row; flag it in the methodology. Keep the aggregate Amazon row separate so it is not mistaken for a single curated product. Do not combine this export with the overlapping 30-day or 90-day LTK files. Because the audit does not enumerate the top row values, the final ranked selection and labels must be populated directly from this named source during chart production and checked back to the audited totals.
- **Exact data labels:** Each bar must show the exact product/link label, exact commission to cents, exact clicks, and exact orders from that row. Fixed footer labels: `138,420 product-link clicks`, `4,473 orders`, `8,095 items sold`, `$67,273.50 commissions`, and `3.2315% click-to-order conversion`. Do not abbreviate the bar labels. No product-specific value should be invented from the audit narrative.
- **Viewer insight:** The viewer should see that Vanessa's product organization and curation were tied to measurable downstream actions and commission, while understanding that the supplied export may not prove a complete account total.

### Visual 3 — ShopMy link efficiency

- **Chart type:** Scatter plot: clicks on the horizontal axis, order volume on the vertical axis, and commission as bubble size.
- **Title:** `Curated ShopMy links connected traffic to measurable order volume`
- **Metric and dimensions:** One point per eligible link row; clicks, order volume, commission, merchant, and product title.
- **Source file and tab:** `6:25-9:25 links sm.csv`; N/A — CSV.
- **Reporting period:** Export labeled June–September 2025; exact dates are not present in the file.
- **Filtering and calculation rules:** Plot only the 32 rows with numeric order volume. Preserve missing values rather than converting them to zero. Use merchant and title only when present; label missing fields as `Merchant not reported` or `Title not reported`. Do not compare the plot's scale or efficiency directly with LTK or Pinterest. Do not merge it with the undated ShopMy snapshot or overlapping 30-day and 90-day exports.
- **Exact data labels:** Point-level tooltip: exact product title, merchant, clicks, order count, order volume to cents, and commission to cents. Fixed footer labels: `5,818 clicks`, `88 orders`, `$24,101.25 order volume`, `$3,032.30 commissions`, and `1.5125% click-to-order conversion`. The audit does not enumerate individual row values, so all point labels must be generated from the named source during chart production and verified against these totals.
- **Viewer insight:** The chart should show which curated links produced commercial outcomes, supporting a story about active product selection and affiliate platform management rather than a cross-platform popularity contest.

### Visual deferred from the primary story

The audited styling-session mix could support a fourth horizontal bar chart using `events-export.csv`, but it is not recommended for this implementation. Its January 2023–August 2025 period is much broader than the affiliate exports, and it shifts the narrative from content and affiliate management to service operations. It can be reconsidered if the case study later adds a clearly separated client-services section. Any such chart must use only anonymized aggregate counts and must not expose booking PII or describe $36,726 as collected revenue.

## Metrics that need visible context

- **$67,273.50 LTK commissions and 138,420 clicks are technically verified for the supplied export, but may mislead if described as a complete account result.** The period comes from the filename, exact dates are absent, the file contains exactly 3,000 rows, and the audit warns that the export may be capped.
- **$24,101.25 ShopMy order volume is technically verified, but may mislead if presented with exact calendar dates.** The June–September 2025 period is filename-implied, and the export is a link-level report rather than a transaction ledger.
- **97,937 Pinterest impressions are appropriate for the case study, but the last two daily values are estimated.** The chart and methodology note must make that visible.
- **The LTK and ShopMy conversion rates are useful within their own platform sections, but not for platform ranking.** The exports differ in structure, coverage, and reporting period.
- **108 uncanceled bookings are verified, but they cover a different operational story and a much longer date range.** Do not place them beside the affiliate metrics as if the results are directly comparable.

## Page layout proposal for `project-tiffany-wendel.html`

### 1. Hero and role framing

Keep the opening focused on Vanessa's contribution rather than unsupported scale claims.

Proposed supporting copy:

> Vanessa organized content across Pinterest, LTK, and ShopMy; curated product selections; maintained affiliate platforms; and used performance reporting to refine how products and content were presented.

Do not place a multi-platform total in the hero.

### 2. Remove the existing unsupported metric cards

Remove the cards for:

- `340K+ Product clicks`
- `$90K Order volume`
- `4.8K+ Engagements`

Remove `82K total audience` wherever it appears. Replace `102K+ impressions` with the exact Pinterest result and its explicit period.

### 3. Pinterest evidence section

Place the first headline metric immediately above Visual 1:

- **Card label:** `Pinterest impressions`
- **Card value:** `97,937`
- **Card period:** `Nov. 1, 2024–Sept. 15, 2025`
- **Card note:** `Final two reporting dates are estimated.`

Proposed supporting copy:

> Across the reporting period, the organized Pinterest content program recorded 97,937 impressions. The metric documents visibility without claiming that the export alone proves causation.

Place the Pinterest daily-impressions line chart directly below this copy.

### 4. LTK affiliate strategy section

Place the second headline metric beside the LTK section introduction, not beside the Pinterest or ShopMy metric as a comparison:

- **Card label:** `LTK commissions`
- **Card value:** `$67.2K`
- **Exact-value note:** `$67,273.50 in the supplied export`
- **Card period:** `Export labeled Nov. 2024–Sept. 2025`

Proposed supporting copy:

> Vanessa's LTK work paired product curation with organized affiliate linking. The supplied export records 138,420 product-link clicks, 4,473 orders, and 8,095 items sold, resulting in $67,273.50 in commissions.

Place the ranked LTK product-performance chart below the paragraph. Put the export-cap, date, and duplicate-row caveats immediately beneath the visual rather than hiding them in a distant footnote.

### 5. ShopMy platform-management section

Place the third headline metric at the start of a separate ShopMy section:

- **Card label:** `ShopMy order volume`
- **Card value:** `$24.1K`
- **Exact-value note:** `$24,101.25 in the supplied export`
- **Card period:** `Export labeled June–Sept. 2025`

Proposed supporting copy:

> On ShopMy, curated links connected 5,818 clicks to 88 orders and $24,101.25 in reported order volume, with $3,032.30 in commissions in the supplied period-labeled export.

Place the ShopMy scatter plot below this paragraph. Keep its axes, color, and caption visually distinct from LTK so the page does not imply that the platforms use directly comparable reporting systems.

### 6. Methodology note

Place this note immediately after the final chart:

> **Methodology:** Metrics are reported exactly as audited from their authoritative platform exports and are kept separate by platform and reporting period. Pinterest covers Nov. 1, 2024–Sept. 15, 2025; its final two dates are estimated. The LTK and ShopMy date ranges are taken from export filenames because exact dates are absent. The LTK total is the raw supplied-export total, includes a duplicated one-click row, and may be affected by a 3,000-row export cap. ShopMy missing values were preserved rather than treated as zero. `active_links` was not used as clicks. No cross-platform totals were created.

### 7. Closing contribution statement

Proposed supporting copy:

> The work brought structure to a multi-platform content operation: organizing products, maintaining affiliate destinations, and turning platform reporting into clearer decisions about what to feature and where.

This wording describes Vanessa's contribution without claiming that the available exports prove sole causation.

## Recommended for implementation

**Final headline metrics**

1. `97,937 Pinterest impressions` — Nov. 1, 2024–Sept. 15, 2025; final two dates estimated.
2. `$67.2K LTK commissions` — exact audited value $67,273.50; export labeled Nov. 2024–Sept. 2025; period/completeness caveat required.
3. `$24.1K ShopMy order volume` — exact audited value $24,101.25; export labeled June–Sept. 2025; filename-period caveat required.

**Final visuals**

1. Pinterest daily impressions line chart with seven-day moving average.
2. LTK ranked product-performance bar chart by commission, with clicks and orders.
3. ShopMy link-efficiency scatter plot using clicks, order volume, and commissions.

These metrics and visuals should remain in separate platform sections. Do not add them together, rank the platforms against one another, use `active_links` as clicks, or restore any of the four unsupported claims.
