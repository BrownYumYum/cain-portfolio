---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# AutoQuotes-to-HubSpot Synchronization Engine

## The Challenge
Maintaining synchronized product data across Revealize AutoQuotes and HubSpot required constant manual intervention. The organization needed an automated solution to reconcile vendor pricing and specifications in real-time.

### Technical Evidence: Execution Log
![Technical Audit Log](/sync-log-screenshot.png)
*Automated audit script indexing 239,091 unique models to identify discrepancies.*

## The Engineering Architecture
I engineered a custom synchronization engine running on a dedicated Ubuntu Server to bridge the gap between industrial source data and the CRM.

**Core Technical Implementations:**
* **Regex-Based Normalization:** Developed a `super_clean()` function using Regular Expressions to strip HTML and normalize alphanumeric strings.
* **Fuzzy Match Logic:** Engineered a `get_search_terms()` algorithm to decompose complex model strings into searchable fragments.
* **Persistent Cache Architecture:** Implemented a JSON-based caching layer to store the "Ultimate Master Index," drastically reducing API latency.

## Production Audit Results

| Title | SKU | Original Model | Vendor |
| :--- | :--- | :--- | :--- |
| Scotch-Brite Griddle Liquid | 1978 | 701 | 3M Purification |
| Carbonless Guest Check Pad | 2110 | 412447 GT363 | Chef Master |
| Black Stacking Side Chair | 123 | 888-11BLK | AAA Furniture |

## The Business Impact
This Linux based engine secured the organization’s pricing integrity. By automating the reconciliation, we eliminated Quote to Order discrepancies and saved the operations team **15+ hours per week**.