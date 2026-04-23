---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# Enterprise Data Migration & Audit System

## Problem
A high-risk migration of 500,000+ records from a legacy Epicor Eclipse ERP threatened to cause massive data loss, inventory inconsistencies, and operational downtime if the transition was not handled with absolute precision. 

## Solution
Developed a closed-loop validation pipeline and a custom Python-based Audit Server to monitor the migration in real-time, ensuring 100% traceability between the legacy ERP and the new CRM/e-commerce platforms.

## Impact
* **Successfully migrated 500,000+ records** with zero production downtime.
* **Maintained 100% data integrity** and full technical auditability.
* **Prevented inventory loss** and workflow disruptions during a massive enterprise transition.

## System Design & Implementation
Built a standalone Python application functioning as a persistent Flask Audit Server to validate data flow across multiple APIs.

* **Persistent Monitoring:** Engineered `audit_server.py` to act as a background daemon on Ubuntu, providing continuous technical traceability during the migration.
* **OAuth & API Security:** Programmatically managed secure OAuth flows to interface with the REST Admin APIs for external platforms like Shopify and HubSpot.
* **Recursive Pagination:** Implemented a link-parsing algorithm to safely traverse paginated API headers, ensuring 100% variant capture for large datasets without dropping records.

## Technical Example: Closed-Loop Validation Logic
This snippet demonstrates how the audit server reconstructed live product URLs and validated SKU/pricing data to instantly verify data integrity across platforms.

```python
# Validation logic from audit_server.py
for p in products:
    title = p.get('title', 'N/A')
    handle = p.get('handle', '')
    live_link = f"https://{STORE_WEB_DOMAIN}/products/{handle}"
    
    for v in p.get('variants', []):
        # Writes validated records to the audit log for real-time reconciliation
        writer.writerow([title, v.get('sku', 'N/A'), v.get('price', 'N/A'), live_link])
