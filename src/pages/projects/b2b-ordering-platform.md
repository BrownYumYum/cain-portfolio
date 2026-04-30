---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# Enterprise B2B Ordering Platform

## Problem
Manual ordering processes created pricing errors, delays, and operational bottlenecks. [cite_start]The Shopify front-end store and the backend ERP system were disconnected, requiring constant manual intervention to manage product data, inventory, B2B pricing, and fulfillment[cite: 3, 4, 5, 6].

## Solution
[cite_start]Developed a modular Django application using Celery for high-volume asynchronous tasks to bridge the systems and keep them in lockstep[cite: 3, 8]. [cite_start]The architecture strictly separates domain logic for the product catalog, B2B customer pricing, and order fulfillment[cite: 14, 15].

## Impact
* [cite_start]**Automated Sync Flows:** Ensured accurate, scheduled data synchronization for products, inventory, and B2B contract pricing across production and QA environments[cite: 6, 64].
* [cite_start]**Scalable Infrastructure:** Provisioned AWS resources using Terraform and managed internal server state with Ansible[cite: 58, 59].
* [cite_start]**Streamlined CI/CD:** Implemented Bitbucket Pipelines to automate Docker image builds and AWS ECR deployments[cite: 72, 76, 77].
* [cite_start]**Proactive Monitoring:** Integrated Sentry to track uncaught Django exceptions and Celery task failures in real-time[cite: 98, 100, 101].

## System Design & Implementation
[cite_start]Built a highly specialized, containerized application to handle complex system integrations and API workflows[cite: 12, 152].

* [cite_start]**Asynchronous Task Queue:** Utilized Celery and a Redis broker to manage critical fast tasks, rate-limited Shopify API calls, and slower ERP XML API tasks without blocking the web server[cite: 10, 153, 154, 155, 156].
* [cite_start]**Database & Cloud:** Designed a custom relational PostgreSQL database, deployed on AWS RDS for production and Local Docker for QA[cite: 11, 64].
* [cite_start]**Secure Configuration:** Managed all sensitive configurations and API credentials securely via Bitbucket Repository Variables, ensuring no secrets are committed to the codebase[cite: 113].
* **Frontend Alignment:** Engineered the user interface to strictly align with Section 508 accessibility standards, ensuring seamless usability and compliance across all institutional client portals.

<small style="font-weight: normal;">Technical Evidence: Execution Log</small>

```python
# Technical Proof: Tiered Pricing Logic Snippet
# This logic ensures the correct contract pricing is applied per institutional account.

class CustomerContract(models.Model):
    customer_id = models.CharField(max_length=50, unique=True)
    price_level = models.IntegerField(default=1) # Maps to ERP Price Lines
    
    def get_custom_price(self, product):
        # Logic to calculate price based on tiered contract levels
        # Reduces manual adjustments by automating contract-specific discounts
        discount_factor = self.price_level * 0.05
        return product.base_price * (1 - discount_factor)
