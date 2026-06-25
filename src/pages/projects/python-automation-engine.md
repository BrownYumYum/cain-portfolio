---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# Enterprise Data Engine: AutoQuotes, Epicor & HubSpot Synchronization

## Problem
Maintaining synchronized product data across Revealize AutoQuotes, legacy ERP systems (Epicor Eclipse), and HubSpot required constant manual intervention. The organization needed an automated, high-volume solution to reconcile vendor pricing and specifications in real-time, preventing operational bottlenecks and critical pricing discrepancies.

## Solution
Engineered a comprehensive Django-based Python ETL pipeline hosted on an AWS EC2 Ubuntu instance. This architecture autonomously processes third-party API data, normalizes it for legacy systems, and leverages a MongoDB Atlas backend to ensure seamless data alignment across all platforms.

## Impact
* **Eliminated quote-to-order discrepancies** by ensuring real-time data consistency across enterprise systems.
* **Reduced manual workload by 15+ hours per week** for the operations team by automating the daily generation of pricing files.
* **Indexed and audited 239,000+ unique product models** autonomously to instantly identify missing or mismatched data.
* **Proactive Price Monitoring:** Automated a daily watchdog script that detects exact-penny price fluctuations and triggers transaction email alerts to stakeholders via the Mandrill API.

## System Design & Implementation
Built a dedicated Ubuntu Server to host the synchronization engine, bridging the gap between industrial source data and the CRM.

* **Scalable MongoDB Batch Processing:** Optimized database insertion performance by processing and pushing records in batches of 1,000 to the MongoDB Atlas cluster, significantly reducing API latency.
* **ERP Data Normalization:** Developed a strict mapping protocol that automatically converts dynamic JSON API responses into an exact 52-column legacy CSV format required for Epicor Eclipse pricing updates.
* **Regex-Based Normalization:** Developed robust data-cleaning utilities using Python’s `re` module to ensure high-fidelity inputs across heterogeneous database schemas.
* **Fuzzy Match Logic:** Engineered a `get_search_terms()` algorithm to decompose complex model strings into searchable fragments.
* **Persistent Cache Architecture:** Architected a JSON-based caching layer to store historical obsolete product logic, preventing redundant API calls and rate-limit bottlenecks.

## Technical Example: Audit Log & Reconciliation Results
The engine autonomously builds a master index, flags discrepancies, and normalizes the data into a clean, actionable audit report.

![Technical Audit Log](/sync-log-screenshot.png)  
*Automated audit script indexing 239,091 unique models to identify discrepancies.*

```python
import re

def super_clean(data_string):
    """
    Normalizes complex model strings for high-fidelity database indexing.
    """
    # Strip HTML and normalize special characters
    cleaned = re.sub('<[^<]+?>', '', data_string)
    return ' '.join(cleaned.split()).upper()
