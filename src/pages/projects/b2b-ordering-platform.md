---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# Enterprise B2B Ordering Platform

## Problem
Manual ordering processes created pricing errors, delays, and operational bottlenecks. The Shopify front-end store and the backend ERP system were disconnected, requiring constant manual intervention to manage product data, inventory, B2B pricing, and fulfillment.

## Solution
Developed a modular Django application using Celery for high-volume asynchronous tasks to bridge the systems and keep them in lockstep. The architecture strictly separates domain logic for the product catalog, B2B customer pricing, and order fulfillment.

## Impact
* **Automated Sync Flows:** Ensured accurate, scheduled data synchronization for products, inventory, and B2B contract pricing across production and QA environments.
* **Scalable Infrastructure:** Provisioned AWS resources using Terraform and managed internal server state with Ansible.
* **Streamlined CI/CD:** Implemented Bitbucket Pipelines to automate Docker image builds and AWS ECR deployments.
* **Proactive Monitoring:** Integrated Sentry to track uncaught Django exceptions and Celery task failures in real-time.

## System Design & Implementation
Built a highly specialized, containerized application to handle complex system integrations and API workflows.

* **Asynchronous Task Queue:** Utilized Celery and a Redis broker to manage critical fast tasks, rate-limited Shopify API calls, and slower ERP XML API tasks without blocking the web server.
* **Database & Cloud:** Designed a custom relational PostgreSQL database, deployed on AWS RDS for production and Local Docker for QA.
* **Secure Configuration:** Managed all sensitive configurations and API credentials securely via Bitbucket Repository Variables, ensuring no secrets are committed to the codebase.
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
