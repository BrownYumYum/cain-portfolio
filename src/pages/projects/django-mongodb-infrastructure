# Enterprise Data & Pricing Intelligence Engine

## Overview
Architected a high-throughput data synchronization and pricing intelligence platform to manage 200k+ inventory items. This system bridges the gap between third-party API data (AutoQuotes), MongoDB storage, and enterprise ERP systems (Epicor Eclipse), enabling automated business decisions.

## Technical Stack
* **Backend:** Django 6.0 with MongoDB integration (using `pymongo`).
* **Database:** MongoDB Atlas (Cloud) for flexible document-based product schemas.
* **Infrastructure:** AWS EC2 (Ubuntu) running automated `cron` jobs for daily synchronization.
* **Integration:** REST API pipelines, Mandrill transactional email service, and custom CSV-based ERP import protocols.

## Key Engineering Achievements
* **Scalable Import Pipelines:** Developed efficient batch-processing scripts (`import_data.py`) capable of handling 1,000+ row insertions per batch to minimize database load.
* **Intelligent Watchdog Systems:** Built `eclipse_price_watchdog.py` to automate price reconciliation, detect discrepancies, and trigger email alerts to stakeholders.
* **Automated Data Normalization:** Implemented a robust "52-column" CSV mapping protocol to ensure seamless integration between modern JSON-based API data and legacy ERP flat-file requirements.

## Impact
* **Unified Source of Truth:** Centralized disparate data from hundreds of vendors into a high-performance MongoDB architecture.
* **Operational Efficiency:** Automated the daily generation and transmission of pricing files, reducing manual administrative effort to zero.
* **Proactive Monitoring:** Real-time visibility into price fluctuations and obsolete product data, allowing for rapid inventory adjustments.
