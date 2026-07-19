# Tiffany performance data audit

Audit rerun: 2026-07-14  
Scope: read-only review of every current performance source in `data/tiffany/raw/`, every Excel sheet, and every claim currently displayed in `project-tiffany-wendel.html`.

## Change summary from the previous audit

- The current raw folder contains **24 performance files** plus `.DS_Store` system metadata.
- **16 files are new**, **8 were reviewed previously**, and the previously reviewed duplicate `Pinterest Analytics overview 20240928-20241028 2.csv` is no longer present.
- The new CSV counterparts for the established 30-day/90-day LTK, ShopMy, and LTK earnings exports repeat the same underlying metrics; they are not additional performance periods.
- The strongest genuinely new affiliate source is `LTK-export11:24-9:25.csv`: 138,420 clicks, 4,473 orders, 8,095 items sold, and $67,273.50 commissions. Its exact dates are not embedded in the file, the filename implies November 2024–September 2025, and it contains one exact duplicated 1-click row.
- The strongest new ShopMy snapshot is `links.csv`: 16,117 clicks, 167 orders, $51,980.60 order volume, and $6,727.38 commissions. It has no reporting-period metadata; its newest link was created 2025-08-23, which is not a valid report start or end date.
- `events-export.csv` adds 108 unique, uncanceled styling bookings dated 2023-01-16–2025-08-19. Listed prices total $36,726 across 104 priced bookings, but the file does not prove payment collection and this is service-booking value, not affiliate order volume.
- **No previously unsupported website claim is fully verified by the new files.** The 340K click claim remains based on the wrong metric; $90K order volume, 4.8K engagements, and 82K audience remain unsupported; 102K+ impressions remains partially supported by a verified 97,937-impression period.
- No raw data, website file, image, or chart was modified. This audit is the only updated file.

## Audit rules and assumptions

- A hyphen (`-`) is treated as missing/not applicable, not automatically as zero.
- `Created On` in ShopMy exports is a link-creation date, not the performance-reporting window.
- LTK product/link exports have no date column. A period is accepted only when explicitly stated in a filename or a paired export; ambiguous labels such as `tp`, `active links`, and `LTK-export` are not interpreted as periods.
- Conversion is recalculated as `total orders / total clicks`; row-level conversion percentages are not averaged.
- “Duplicate” distinguishes exact whole-row duplicates from repeated products, URLs, SKUs, merchants, or earnings lines. No suspected duplicate is removed.
- ShopMy 90-day order volume includes negative returns and is therefore net order volume, not clean gross sales.
- Cross-platform metrics are not assumed equivalent. Pinterest outbound clicks, LTK clicks, ShopMy clicks, impressions, engagements, audience, saves, and `active_links` remain separate definitions.

## 1. Current source inventory

“New” means the filename was not in the previous nine-file audit. “Reviewed” means it was already present. `.DS_Store` is excluded because it is macOS metadata, not a performance source.

| Status | Source file | Platform | Reporting period | Level of detail | Important columns and available metrics |
|---|---|---|---|---|---|
| Reviewed | `Pinterest Analytics overview 20240928-20241028.csv` | Pinterest | Explicit 2024-09-28–2024-10-28 | Daily audience plus restricted top-board and top-pin summaries | `Date`, `Total audience`; board impressions, engagement, pin clicks, outbound clicks, saves; pin impressions |
| Reviewed | `Pinterest Analytics 11:24-9:25.csv` | Pinterest | Explicit 2024-11-01–2025-09-15 | Daily account-level impressions; board/pin sections say “Not enough data” | `Date`, `Impressions`; final-date estimate warning |
| New | `events-export.csv` | Calendly / styling services | Event starts 2023-01-16–2025-08-19 | Booking/event level, 108 rows | Event type, start/end, created date, canceled flag, price, currency, event UUID; also contains names, emails, phone numbers, and free-text notes |
| Reviewed | `LTK-export-1month-links.xlsx` | LTK | “1 month”; inferred 2025-07-02–2025-07-31 | Product/link level, 2,933 data rows | Product, advertiser, SKU, price, URL, clicks, commissions, orders, items sold, active links, conversion rates |
| New | `LTK-export-1month-links.csv` | LTK | Same inferred 30-day period | CSV repetition of the preceding metrics | Same 15 columns and totals as the workbook |
| New | `LTK-export-1month-brands.csv` | LTK | Same inferred 30-day period | Retailer/advertiser level, 326 rows | Advertiser, clicks, commissions, orders, items sold, conversion rates |
| New | `LTK-export-90days-links.csv` | LTK | Inferred 2025-05-02–2025-07-31 | Product/link level, 3,000 rows | Same product/link metrics as the 30-day file |
| New | `LTK-export-90days-brands.csv` | LTK | Inferred 2025-05-02–2025-07-31 | Retailer/advertiser level, 423 rows | Advertiser, clicks, commissions, orders, items sold, conversion rates |
| Reviewed | `TIFF DATA LTK.xlsx` | LTK | 30-day and 90-day periods above | Six tabs: advertiser, product/link, and post levels for both periods | Brand/link/post dimensions with clicks, commissions, orders, items sold, active links, conversion rates |
| Reviewed | `LTK_Audit_Tiffany.xlsx` | LTK | Same 30-day and 90-day periods | Derived summary/top-ten workbook plus normalized copies of raw tabs | Summary clicks, orders, conversion, commissions, average commission/order; copied brand/link/post metrics |
| New | `LTK active links .csv` | LTK | **Unknown**; no date field or interpretable period label | Product/link snapshot, 3,000 rows | Clicks, commissions, orders, items sold, active links and product metadata |
| New | `LTK-export tp.csv` | LTK | **Unknown**; `tp` is not defined | Product/link snapshot, 3,000 rows | Same LTK link metrics |
| New | `LTK-export.csv` | LTK | **Unknown** | Product/link snapshot, 1,398 rows | Same LTK link metrics |
| New | `LTK-export11:24-9:25.csv` | LTK | Filename-implied November 2024–September 2025; exact dates absent | Product/link snapshot, 3,000 rows | Same LTK link metrics; strongest extended-period affiliate evidence |
| Reviewed | `LTK-earnings-export-05-02-2025-07-31-2025.xlsx` | LTK | Filename 2025-05-02–2025-07-31; actual rows 2025-05-03–2025-07-31 | Earnings-line ledger, 3,748 rows; no transaction ID | Date, brand, type, product, retailer link, status, commission, payment |
| New | `LTK-earnings-export-05-02-2025-07-31-2025.csv` | LTK | Same period as the workbook | CSV repetition of the same earnings ledger | Same columns, malformed row, duplicate groups, and totals |
| New | `LTK-earnings-export-06-30-2025-07-31-2025.csv` | LTK | Filename 2025-06-30–2025-07-31; actual rows 2025-07-01–2025-07-31 | Earnings-line subset, 1,357 rows | Same earnings fields; exact multiset subset of the longer ledger |
| Reviewed | `TIFF DATA Shop My.xlsx` | ShopMy | 30-day actual order dates 2025-07-02–2025-07-30; 90-day actual order dates 2025-05-02–2025-07-30 | Six tabs: order, link, and domain levels for both periods | Orders: amount, commission, code, status. Links/domains: clicks, orders, volume, earned. |
| New | `shop my 1month- links.csv` | ShopMy | Same inferred 30-day period | Product/link-level CSV repetition, 145 rows | Created date, title, clicks, order count, order volume, commissions, merchant, short URL |
| New | `shop my 90 days- links.csv` | ShopMy | Same inferred 90-day period | Product/link-level CSV repetition, 403 rows | Same link columns and totals as the workbook tab |
| Reviewed | `6_25-9_25 links sm.xlsx` | ShopMy | Filename-implied June 2025–September 2025; exact dates absent | Product/link level, 1,173 rows | Clicks, orders, order volume, commissions, merchant, short URL, collection and destination URL |
| New | `6:25-9:25 links sm.csv` | ShopMy | Same filename-implied period | CSV repetition of the preceding workbook | Same rows and metric values |
| New | `links shop my.csv` | ShopMy | **Unknown**; creation dates 2023-11-14–2025-08-22 are not a report period | Link-level snapshot, 1,265 rows | Clicks, orders, order volume, commissions and link metadata |
| New | `links.csv` | ShopMy | **Unknown**; creation dates 2023-11-14–2025-08-23 are not a report period | Later link-level snapshot, 1,300 rows | Same metrics; 35 more rows than `links shop my.csv` on a net basis |

The previously audited exact duplicate `Pinterest Analytics overview 20240928-20241028 2.csv` is absent from the current folder. Its removal does not remove unique evidence.

## 2. Excel workbook and sheet inspection

All six current Excel workbooks and all 24 tabs were inspected. Row counts exclude the header.

| Workbook | Sheet/tab | Rows | Level and metrics |
|---|---|---:|---|
| `6_25-9_25 links sm.xlsx` | `625-925 links sm` | 1,173 | ShopMy product/link metrics: clicks, order count, order volume, commissions |
| `LTK-earnings-export-05-02-2025-07-31-2025.xlsx` | `LTK-earnings-export-05-02-2025-` | 3,748 | Earnings lines: sale commissions, returns, payments and fees |
| `LTK-export-1month-links.xlsx` | `LTK-export-1month-links` | 2,933 | LTK product/link performance |
| `TIFF DATA LTK.xlsx` | `LTK-export-1month-brands` | 326 | 30-day advertiser performance |
| `TIFF DATA LTK.xlsx` | `LTK-export-1month-links` | 2,933 | 30-day product/link performance; the worksheet used range also contains two trailing blank rows |
| `TIFF DATA LTK.xlsx` | `LTK-export-1month-posts` | 30 | 30-day post attribution |
| `TIFF DATA LTK.xlsx` | `LTK-export-90days-brands` | 423 | 90-day advertiser performance |
| `TIFF DATA LTK.xlsx` | `LTK-export-90days-links` | 3,000 | 90-day product/link performance |
| `TIFF DATA LTK.xlsx` | `LTK-export-90days-posts` | 97 | 90-day post attribution |
| `LTK_Audit_Tiffany.xlsx` | `Summary` | 2 | Derived 30/90-day KPIs |
| `LTK_Audit_Tiffany.xlsx` | `Top_Brands_1m` | 10 | Derived top-ten advertisers |
| `LTK_Audit_Tiffany.xlsx` | `Top_Posts_1m` | 10 | Derived top-ten posts |
| `LTK_Audit_Tiffany.xlsx` | `links_1m` | 2,933 | Normalized copy of 30-day links |
| `LTK_Audit_Tiffany.xlsx` | `posts_1m` | 30 | Copy of 30-day posts |
| `LTK_Audit_Tiffany.xlsx` | `brands_1m` | 326 | Normalized copy of 30-day advertisers |
| `LTK_Audit_Tiffany.xlsx` | `links_90d` | 3,000 | Normalized copy of 90-day links |
| `LTK_Audit_Tiffany.xlsx` | `posts_90d` | 97 | Copy of 90-day posts |
| `LTK_Audit_Tiffany.xlsx` | `brands_90d` | 423 | Normalized copy of 90-day advertisers |
| `TIFF DATA Shop My.xlsx` | `shop my 1month- allorders` | 18 | 30-day order ledger |
| `TIFF DATA Shop My.xlsx` | `shop my 1month- links` | 145 | 30-day link performance |
| `TIFF DATA Shop My.xlsx` | `shop my 1month- performancebysi` | 55 | 30-day domain/retailer performance |
| `TIFF DATA Shop My.xlsx` | `shop my 90 days- links` | 403 | 90-day link performance |
| `TIFF DATA Shop My.xlsx` | `shop my 90days- allorders` | 60 | 90-day order ledger |
| `TIFF DATA Shop My.xlsx` | `shop my 90days- performancebysi` | 113 | 90-day domain/retailer performance |

## 3. Repeated exports and source comparisons

The following are repeated representations and must not be added together:

- `6:25-9:25 links sm.csv` has the same 1,173 rows and identical metric values as `6_25-9_25 links sm.xlsx`.
- `LTK-earnings-export-05-02-2025-07-31-2025.csv` has the same row count and identical commission/payment values as its `.xlsx` counterpart, including the malformed row.
- `LTK-earnings-export-06-30-2025-07-31-2025.csv` is an exact multiset subset of the longer earnings export for 2025-07-01–2025-07-31: all 1,357 rows already occur in the longer file.
- The new 30-day and 90-day LTK brand/link CSVs have zero metric-cell differences from their corresponding `TIFF DATA LTK.xlsx` tabs. `LTK_Audit_Tiffany.xlsx` and the standalone 30-day workbook are additional copies/normalizations of the same data.
- `shop my 1month- links.csv` and `shop my 90 days- links.csv` have zero metric-cell differences from their corresponding `TIFF DATA Shop My.xlsx` tabs.
- `links shop my.csv` and `links.csv` are successive, overlapping ShopMy snapshots, not separate channels. They have identical orders, order volume, and commission totals. The later file has 35 more rows and 20 more total clicks; 1,262 short URLs are shared, 3 occur only in the earlier file, 38 occur only in the later file, and nine shared links changed clicks.
- The four undated/loosely dated LTK link snapshots are not exact copies. They have different product sets and totals: the 90-day and `LTK active links .csv` files share 2,770 URLs but differ in performance; `LTK-export tp.csv`, `LTK-export.csv`, and `LTK-export11:24-9:25.csv` also have only partial URL overlap. They must remain separate snapshots with their period limitations.

## 4. Missing, malformed, duplicate and conflicting data

### Pinterest

- The early audience series is blank on 12 of 31 dates. The 19 populated daily values range from 7 to 86; their sum of 520 is not a unique period audience.
- The early board table contains only two ranked rows: 2,454 impressions, 134 engagements, 115 pin clicks, 26 outbound clicks and 1 save. The export warns that board/pin tables are restricted subsets.
- The long file has 319 daily values totaling 97,937 impressions. Values for 2025-09-14 and 2025-09-15 are estimated.
- The current folder contains no complete Pinterest engagement, saves, outbound-click, or unique-audience total.

### LTK aggregate exports

- The 30-day advertiser and link views reconcile at 17,767 clicks, 399 orders, 1,050 items sold and $8,433.73 commissions.
- The 90-day advertiser view reports 62,089 clicks, 1,465 orders and 2,882 items sold; the link view reports 47,972 clicks, 1,433 orders and 2,842 items sold. The link view is lower by 14,117 clicks, 32 orders and 40 items. Both report $18,982.43 commissions.
- The 90-day advertiser export contains one exact duplicate `Negative Underwear` row, adding 1 click and no orders/commission. Raw total: 62,089 clicks; strict exact-row-deduplicated alternative: 62,088. It is not deleted.
- The extended `LTK-export11:24-9:25.csv` contains one exact duplicated `Flat Mule in Black Raffia` row with 1 click and no orders/commission. Raw total: 138,420 clicks; exact-row-deduplicated alternative: 138,419.
- The extended file has exactly 3,000 rows and no companion advertiser-level export. This may be a platform row cap; the data cannot prove that 138,420 is a complete account-level click total. Treat it as the total of the supplied product-link export.
- `LTK-export.csv` has two exact duplicate groups, five involved rows and three excess rows. The excess rows add 5 clicks and no orders/commission. Its reporting period is unknown, so neither raw nor deduplicated totals are portfolio-ready.
- `LTK active links .csv` and `LTK-export tp.csv` have no exact whole-row duplicates. All LTK link snapshots contain repeated URLs/SKUs/product labels that may be variants or tracking records; they are not safe to deduplicate by name alone.
- Each major LTK link export includes an aggregate row with missing product/image/price/URL but real Amazon performance. Do not drop it. Missing SKU counts range from 876 to 1,816; missing descriptions range from 14 to 63 depending on the file.
- The 30-day `active_links` sum is 344,020. This is not clicks. Other snapshots have active-link sums from 1,823,796 to 16,454,077, showing why this field cannot support a click claim.
- The four ambiguous LTK snapshots conflict and cannot be assigned periods from their totals alone:

| Source | Period quality | Clicks | Orders | Items | Commissions | Active links |
|---|---|---:|---:|---:|---:|---:|
| `LTK active links .csv` | Unknown | 48,073 | 1,447 | 2,864 | $18,433.97 | 1,850,859 |
| `LTK-export tp.csv` | Unknown | 103,334 | 2,950 | 5,190 | $41,960.95 | 6,441,723 |
| `LTK-export.csv` | Unknown | 83,519 | 1,286 | 2,370 | $16,060.64 | 2,007,142 |
| `LTK-export11:24-9:25.csv` | Filename-implied Nov 2024–Sep 2025 | 138,420 | 4,473 | 8,095 | $67,273.50 | 16,454,077 |

### LTK earnings

- The 90-day earnings ledger contains 2,789 sale-commission, 935 return, 12 payment and 12 payment-fee rows. Positive commissions total $30,543.81; returns total -$11,615.96; the stored commission column nets to $18,927.85.
- One 2025-05-17 CSV row has only eight fields: the retailer link is embedded in `Product`, `Open` shifts into the link field, `$13.44` shifts into `Status`, and `Commission` is blank. The workbook carries the same malformed content. Treating $13.44 as commission would yield $18,941.29, still $41.14 below the 90-day aggregate $18,982.43.
- The full ledger has 450 exact repeated groups, 1,143 involved rows and 693 excess rows. The July subset has 172 repeated groups, 420 involved rows and 248 excess rows. Without a transaction or line-item ID, they may be separate identical items and cannot be removed safely.
- The July ledger nets to $8,747.61 commissions, $313.88 above the 30-day LTK aggregate. Restricting it to July 2–31 still gives $8,711.40, $277.67 above the aggregate. Different attribution/return logic remains unresolved.

### ShopMy

- The established 30-day views reconcile at 1,272 clicks, 18 orders, $3,436.00 order volume and $437.05 commission.
- The established 90-day views reconcile at 5,948 clicks, 60 orders, $23,227.90 net order volume and $2,855.91 commission.
- The 90-day order ledger includes two -$114.50 return rows and two -$14.60 commission adjustments. Positive order amounts total $23,456.90; returns reduce the reported net volume to $23,227.90.
- The 30-day order ledger has two exact duplicate groups (two excess rows). The 90-day ledger contains those groups plus one duplicated return group (three excess rows total). No transaction ID exists, and the domain/link totals include these rows, so no duplicate is removed.
- `6:25-9:25 links sm.csv` and its workbook have no exact duplicate rows or short URLs. They contain 34 missing titles, 99 missing merchants, 853 links without numeric clicks and 1,141 without numeric order/volume/commission values.
- `links shop my.csv` and `links.csv` have no exact rows or short-URL duplicates. They are highly overlapping snapshots with unknown reporting periods. Their identical $51,980.60 volume and $6,727.38 commission totals must not be added.
- `links.csv` is the later snapshot and totals 16,117 clicks, 167 orders, $51,980.60 order volume and $6,727.38 commission. It is stronger evidence of the amount than the prior audit had, but not of any dated claim.

### Styling bookings

- `events-export.csv` has 108 unique event UUIDs, zero exact duplicate rows, zero duplicate invitee-email+start+event-type combinations, and every row is marked not canceled.
- Event starts run 2023-01-16–2025-08-19. There are 104 priced rows totaling $36,726 in listed value and 4 rows with missing price/currency.
- One priced row is $1, far below the other listed price points ($75–$500). It may be a promotion, test or manual override; the file does not explain it.
- Listed price does not prove that payment was collected. Do not call $36,726 revenue without payment confirmation.
- The file contains personal data and free-text client notes. Any portfolio visual must aggregate and anonymize it; raw names, emails, phone numbers and notes must not be exposed.

## 5. Reporting-period overlap and metrics that must not be added

1. Do not add CSV and Excel versions of the same export.
2. Do not add LTK 30-day totals to 90-day totals; the 30 days are contained in the 90 days.
3. Do not add LTK advertiser, link and post views within one period; they are overlapping dimensions.
4. Do not add the July earnings subset to the 90-day ledger; every July row is already in the longer file.
5. Do not add earnings-ledger commission to LTK aggregate commission for the same period.
6. Do not add the filename-implied November 2024–September 2025 LTK export to any contained 30/90-day LTK snapshot.
7. Do not add `LTK active links .csv`, `LTK-export tp.csv`, or `LTK-export.csv` to other LTK exports; their periods are unknown and their products overlap.
8. Do not add ShopMy 30-day and 90-day totals.
9. Do not add ShopMy order, link and domain views for the same period.
10. Do not add the filename-labeled June 2025–September 2025 ShopMy export to the 90-day export; the period labels overlap in June–July 2025, and exact days cannot be isolated.
11. Do not add `links shop my.csv` and `links.csv`; they are successive snapshots of substantially the same links and identical monetization totals.
12. Do not add either undated ShopMy snapshot to a period-labeled ShopMy export without knowing its performance window.
13. Do not treat LTK `active_links` as clicks, or add it to clicks.
14. Do not add Pinterest restricted board/pin rows to account-level daily totals.
15. Do not combine Pinterest impressions, engagements, saves, outbound clicks, LTK clicks, ShopMy clicks or booking counts into a single “engagement” or “audience” total.
16. Do not add styling-booking listed value to affiliate order volume; they describe different businesses and units.

The two Pinterest exports do not overlap: the first ends 2024-10-28 and the second starts 2024-11-01, leaving a three-day gap.

## 6. Recommended authoritative source by metric

There is no cross-platform all-purpose source. Every portfolio number must include platform, source and period.

| Metric | Recommended source | Decision |
|---|---|---|
| Clicks | LTK 30/90-day: advertiser CSV/tabs. Extended LTK: `LTK-export11:24-9:25.csv` as best available link-level source, with filename-inferred period and duplicate disclosure. ShopMy period-labeled source: `6:25-9:25 links sm.csv` or identical workbook. | Do not use `active_links`. Do not use undated ShopMy snapshots for a period claim. |
| Orders | Same-period LTK advertiser source for 30/90 days; extended LTK link file for the implied longer window. ShopMy order ledger for 30/90 days and period-labeled June–September 2025 link export. | Keep platform/period separate; no order IDs exist in LTK link aggregates. |
| Items sold | LTK advertiser source for 30/90 days; extended LTK link file for the implied longer window. | ShopMy and Pinterest do not provide items sold. |
| Gross sales or order volume | ShopMy `allorders` tabs for 30/90 days; `6:25-9:25 links sm.csv` for the filename-labeled later period. | LTK has no order-value field. Use “net” for the 90-day ShopMy total. `links.csv` has a larger value but no report period. |
| Commissions | LTK aggregate advertiser/link exports for 30/90 days; extended link export for the implied longer period. ShopMy order ledger for 30/90 days and period-labeled link file for the later period. | Use earnings ledgers only for return/status reconciliation because they conflict with aggregates. |
| Conversion rate | Recalculate `orders / clicks` from the same source and period. | Never average row conversion rates or mix a brand total with a link total. |
| Impressions | `Pinterest Analytics 11:24-9:25.csv` daily series | 97,937 for 2024-11-01–2025-09-15; final two days estimated. |
| Engagements | No complete authoritative account total. | The early top-board subset totals 134 only; it cannot verify 4.8K. |
| Audience size | No complete authoritative period total. | The early daily series is incomplete and cannot be summed into unique audience. |
| Saves | No complete authoritative account total. | Only 1 save appears in the two-row restricted top-board table. |
| Outbound clicks | No complete authoritative account total. | Only 26 outbound clicks appear in the two-row restricted top-board table. |

## 7. Independently recalculated major totals

### Dated or filename-labeled performance

| Platform and period | Clicks | Orders | Items sold | Order volume | Commissions | Conversion | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| LTK 30 days, inferred 2025-07-02–2025-07-31 | 17,767 | 399 | 1,050 | Not provided | $8,433.73 | 2.2457% | Advertiser/link totals reconcile |
| LTK 90 days, inferred 2025-05-02–2025-07-31, advertiser view | 62,089 | 1,465 | 2,882 | Not provided | $18,982.43 | 2.3595% | Link view is lower for clicks/orders/items |
| LTK filename-implied Nov 2024–Sep 2025 | 138,420 raw | 4,473 | 8,095 | Not provided | $67,273.50 | 3.2315% | One duplicate 1-click row; exact dates absent |
| ShopMy 30 days, actual orders 2025-07-02–2025-07-30 | 1,272 | 18 | Not provided | $3,436.00 | $437.05 | 1.4151% | AOV $190.89 |
| ShopMy 90 days, actual orders 2025-05-02–2025-07-30 | 5,948 | 60 | Not provided | $23,227.90 net | $2,855.91 | 1.0087% | Net volume/order $387.13 |
| ShopMy filename-implied June–September 2025 | 5,818 | 88 | Not provided | $24,101.25 | $3,032.30 | 1.5125% | Exact dates absent; AOV $273.88 |
| Pinterest 2024-11-01–2025-09-15 | Not an affiliate-click source | — | — | — | — | — | 97,937 impressions; final two days estimated |
| Styling bookings 2023-01-16–2025-08-19 | — | 108 bookings | — | $36,726 listed booking value | Not provided | — | 104 priced; no proof of collection |

### Undated snapshots: report separately, never add

| Source | Clicks | Orders | Items | Order volume | Commissions | Conversion |
|---|---:|---:|---:|---:|---:|---:|
| `LTK active links .csv` | 48,073 | 1,447 | 2,864 | Not provided | $18,433.97 | 3.0100% |
| `LTK-export tp.csv` | 103,334 | 2,950 | 5,190 | Not provided | $41,960.95 | 2.8548% |
| `LTK-export.csv` | 83,519 | 1,286 | 2,370 | Not provided | $16,060.64 | 1.5398% |
| `links shop my.csv` | 16,097 | 167 | Not provided | $51,980.60 | $6,727.38 | 1.0375% |
| `links.csv` | 16,117 | 167 | Not provided | $51,980.60 | $6,727.38 | 1.0362% |

## 8. Recheck of every current website claim

| Website claim | Evidence after expanded audit | Status |
|---|---|---|
| `340K+ Product clicks` / `340K+ combined product clicks` | The exact near-match remains 344,020 **LTK active links** in the 30-day export, not clicks. The strongest newly period-labeled LTK link export has 138,420 clicks. The largest ShopMy snapshot has 16,117 clicks but no report period. These sources overlap or lack aligned periods and are not added. | **Based on the wrong metric.** |
| `$90K Order volume` / `$90K in total order volume` | LTK supplies no order volume. The largest new ShopMy snapshot is $51,980.60 but undated. The strongest period-labeled later ShopMy export is $24,101.25. Adding dated and undated or overlapping snapshots is invalid. | **Unsupported.** |
| `4.8K+ Engagements` | No new Pinterest engagement export was added. Only 134 engagements exist in the restricted two-board table. | **Unsupported.** |
| `82K total audience` | No new audience source was added. The early daily audience series has 12 missing dates and values of 7–86; it is not an 82,000 unique-audience total. | **Unsupported.** |
| `102K+ impressions` | The authoritative daily series verifies 97,937 impressions for 2024-11-01–2025-09-15. The early top-board subset cannot be added. The new LTK files contain clicks, not impressions. | **Partially supported** by 97,937 impressions, not verified at 102K+. |
| `within nine months` | The new extended LTK filename implies roughly November 2024–September 2025, longer than nine months; ShopMy dated exports cover about one or three months; undated snapshots cannot establish a common window. | **Unsupported.** |

### Previously unsupported claims newly verified

**None.** No new file supplies a complete, non-overlapping source for 340K clicks, $90K order volume, 4.8K Pinterest engagements, 82K audience, or 102K+ impressions.

## 9. Recommended portfolio metrics

Use period-specific, platform-specific claims instead of the current cross-platform hero totals:

1. **97,937 Pinterest impressions, 2024-11-01–2025-09-15.** This is the cleanest explicit-date awareness metric; disclose that the final two days are estimated.
2. **138,420 LTK product-link clicks, 4,473 orders, 8,095 items sold and $67,273.50 commissions, filename-implied November 2024–September 2025.** Label the period as inferred from the filename and disclose one duplicated 1-click row. If exact dates cannot be confirmed, present these as “export labeled Nov 2024–Sep 2025,” not “within nine months.”
3. **$24,101.25 ShopMy order volume, 88 orders and $3,032.30 commissions for the filename-labeled June–September 2025 period.** This is weaker than a transaction ledger; the exact dates are absent, but its link totals are internally consistent.
4. **108 uncanceled styling bookings from 2023-01-16–2025-08-19.** Use only if the portfolio story includes the service business. Do not call $36,726 revenue; it is listed booking value without collection evidence.

Do not publish the undated $51,980.60 ShopMy snapshot as a period result until its reporting window is documented.

## 10. Updated visual recommendations

No charts were generated.

### 1. Pinterest daily impressions

- **Chart type:** line chart with seven-day rolling average
- **Metric:** daily impressions; callout total 97,937
- **Source:** `Pinterest Analytics 11:24-9:25.csv`
- **Date range:** 2024-11-01–2025-09-15
- **Calculation:** plot each date/impression pair; mark the final two dates as estimated
- **Story value:** demonstrates sustained reach with the strongest explicit-date source.

### 2. LTK extended-period product performance

- **Chart type:** ranked horizontal bar chart
- **Metric:** top product rows by commission, with clicks/orders as labels
- **Source:** `LTK-export11:24-9:25.csv`
- **Date range:** filename-implied November 2024–September 2025
- **Calculation:** sort product rows by `commissions`; retain the aggregate Amazon row as a separate “unattributed/aggregate” line and flag the duplicated 1-click row rather than silently deleting it
- **Story value:** shows which products and retailers drove the newly verified $67.3K LTK commission total.

### 3. ShopMy period-labeled link efficiency

- **Chart type:** scatter plot
- **Metric:** clicks versus order volume, bubble size = commissions
- **Source:** `6:25-9:25 links sm.csv` (identical metrics to the workbook)
- **Date range:** filename-implied June 2025–September 2025; exact dates absent
- **Calculation:** use the 32 rows with numeric order volume; preserve missing values and label merchant/title in tooltips
- **Story value:** connects product curation to attributable commerce without using the undated $51,980.60 snapshot.

### 4. Styling-session mix, optional

- **Chart type:** horizontal bar chart
- **Metric:** booking count by event type
- **Source:** `events-export.csv`
- **Date range:** 2023-01-16–2025-08-19
- **Calculation:** count unique event UUIDs by `Event Type Name`; exclude all personal fields from the visualization
- **Story value:** provides an accurate service-demand proof point if the case study expands beyond affiliate performance.

## Decision before website edits

The current hero numbers should remain unchanged only as unverified placeholders. A future website edit should either replace them with the period-specific metrics above or obtain source exports that explicitly prove the original cross-platform amounts and common reporting window.
