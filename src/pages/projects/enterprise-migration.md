---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# AutoQuotes-to-HubSpot Synchronization Engine

## Problem
Maintaining synchronized product data across Revealize AutoQuotes and HubSpot required constant manual intervention. Vendor pricing and specifications frequently drifted between systems, causing quote-to-order discrepancies and operational delays.

## Solution
Engineered a custom Python-based ETL pipeline and synchronization engine to automatically reconcile vendor data, pricing, and specifications in real-time across both platforms.

## Impact
* **Eliminated quote-to-order discrepancies** by ensuring real-time data consistency.
* **Reduced manual workload by 15+ hours per week** for the operations team.
* **Indexed and audited 239,000+ unique product models** autonomously to instantly identify missing data.

## System Design & Implementation
Built a dedicated Ubuntu Server to host the synchronization engine, bridging the gap between industrial source data and the CRM.

* **Regex-Based Normalization:** Developed custom data-cleaning functions (`super_clean()`) to strip HTML and normalize unstructured alphanumeric strings.
* **Fuzzy Match Logic:** Engineered a search algorithm (`get_search_terms()`) to decompose complex model strings and accurately match variants across disparate systems.
* **Persistent Cache Architecture:** Implemented a caching layer to store the "Ultimate Master Index," allowing the system to handle massive vendor datasets (312 manufacturers) without API latency.

Technical Evidence: Execution Log  
*This execution log demonstrates the engine autonomously building a master index and auditing live Shopify data to flag missing or mismatched inventory.*

```bash
ubuntu@ubuntu-Inspiron-3668:~$ python3 "/home/ubuntu/cain/AQ Auto/audit_website_aq.py"
--- 📁 Step 1: Loading Approved Vendor IDs ---
Found 312 Manufacturers.

--- 🚀 Step 2: Building ULTIMATE Master Index ---
Loading Ultimate Cache...

Total Unique Models Indexed: 239091

--- 🛒 Step 3: Auditing Shopify Data ---
 MISSING: WL7203 | Walco
