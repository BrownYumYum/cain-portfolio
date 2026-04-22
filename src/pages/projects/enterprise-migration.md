---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# Epicor Eclipse to HubSpot/Prokeep Migration & Audit

## The Challenge
Transitioning 500,000+ records from a legacy Epicor Eclipse ERP required a migration strategy that prioritized data integrity and zero downtime. 

## The Engineering Architecture
I developed a closed loop validation pipeline utilizing a standalone Python application functioning as a persistent **Flask Audit Server**.

**Core Technical Implementations:**
* **Persistent Monitoring:** Engineered `audit_server.py` to act as a background daemon on Ubuntu, providing 100% technical traceability during the migration.
* **OAuth & API Security:** Programmatically managed the Shopify OAuth flow to retrieve secure access tokens and interface with the REST Admin API.
* **Recursive Pagination:** Implemented a link-parsing algorithm to traverse Shopify's paginated headers, ensuring 100% variant capture for large datasets.

## Technical Deep-Dive: The Audit Logic
The Flask engine reconstructed live product URLs for instant verification of data integrity.

```python
# Validation logic from audit_server.py
for p in products:
    title = p.get('title', 'N/A')
    handle = p.get('handle', '')
    live_link = f"https://{STORE_WEB_DOMAIN}/products/{handle}"
    for v in p.get('variants', []):
        writer.writerow([title, v.get('sku', 'N/A'), v.get('price', 'N/A'), live_link])