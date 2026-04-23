---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# AutoQuotes-to-HubSpot Synchronization Engine

## Problem
Maintaining synchronized product data across Revealize AutoQuotes and HubSpot required constant manual intervention. The organization needed an automated solution to reconcile vendor pricing and specifications in real-time to prevent operational bottlenecks and discrepancies.

## Solution
Engineered a custom Python-based ETL pipeline and synchronization engine to automatically reconcile vendor data, pricing, and specifications across both platforms without manual input.

## Impact
* **Eliminated quote-to-order discrepancies** by ensuring real-time data consistency across enterprise systems.
* **Reduced manual workload by 15+ hours per week** for the operations team.
* **Indexed and audited 239,000+ unique product models** autonomously to instantly identify missing or mismatched data.

## System Design & Implementation
Built a dedicated Ubuntu Server to host the synchronization engine, bridging the gap between industrial source data and the CRM.

* **Regex-Based Normalization:** Developed a `super_clean()` function using Regular Expressions to strip HTML and normalize alphanumeric strings.
* **Fuzzy Match Logic:** Engineered a `get_search_terms()` algorithm to decompose complex model strings into searchable fragments.
* **Persistent Cache Architecture:** Implemented a JSON-based caching layer to store the "Ultimate Master Index," drastically reducing API latency.

## Technical Example: Audit Log & Reconciliation Results
The engine autonomously builds a master index, flags discrepancies, and normalizes the data into a clean, actionable audit report.

![Technical Audit Log](/sync-log-screenshot.png)  
*Automated audit script indexing 239,091 unique models to identify discrepancies.*

**Production Audit Results:**

| Title | SKU | Original Model | Vendor |
| :--- | :--- | :--- | :--- |
| Scotch-Brite Griddle Liquid | 1978 | 701 | 3M Purification |
| Carbonless Guest Check Pad | 2110 | 412447 GT363 | Chef Master |
