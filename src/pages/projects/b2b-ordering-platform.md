---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# Enterprise B2B Ordering & Fulfillment Platform

## Problem
Disparate systems between the Shopify front-end store and the backend ERP system caused operational bottlenecks, pricing errors, and fulfillment delays. The organization required a scalable, automated architecture to seamlessly manage high-volume B2B product data, inventory synchronization, and institutional contract pricing without manual intervention.

## Solution
Engineered a modular, containerized Django application utilizing Celery for asynchronous task management. This middleware architecture bridges the gap between e-commerce interfaces and legacy ERP databases, strictly separating domain logic for product catalogs, custom B2B pricing, and fulfillment operations.

## Impact
* **Automated Sync Flows:** Eliminated manual data entry by ensuring accurate, scheduled synchronization for products, inventory, and B2B contract pricing across production and QA environments.
* **Scalable Infrastructure:** Provisioned AWS cloud resources using Terraform and managed internal server states with Ansible, ensuring high availability and reliable deployments.
* **Streamlined CI/CD:** Implemented Bitbucket Pipelines to automate Docker image builds and AWS ECR (Elastic Container Registry) deployments.
* **Proactive Monitoring:** Integrated Sentry to track uncaught Django exceptions and Celery task failures in real-time, drastically reducing system downtime and enabling rapid troubleshooting.

## System Design & Implementation
Built a highly specialized application designed to handle complex system integrations, API workflows, and strict institutional compliance standards.

* **Asynchronous Task Queue:** Utilized Celery and a Redis broker to manage critical fast tasks, rate-limited Shopify API calls, and slower ERP XML API tasks without blocking the web server.
* **Database Architecture:** Designed a custom relational PostgreSQL database, deployed on AWS RDS for production and local Docker environments for QA testing.
* **Secure Configuration:** Managed all sensitive configurations and API credentials securely via Bitbucket Repository Variables, ensuring zero-trust secret management.
* **Institutional Compliance:** Engineered the user interface to strictly align with Section 508 accessibility standards, ensuring seamless usability and regulatory compliance across institutional and healthcare client portals.

## Technical Example: Tiered Pricing Automation
This domain logic ensures the correct contract pricing is dynamically applied per institutional account, replacing manual ERP price-line adjustments.

```python
from django.db import models

class CustomerContract(models.Model):
    """
    Maps institutional customer accounts to their specific ERP price lines.
    """
    customer_id = models.CharField(max_length=50, unique=True)
    price_level = models.IntegerField(default=1) 
    
    def get_custom_price(self, product):
        """
        Dynamically calculates pricing based on tiered contract levels,
        automating contract-specific discounts and reducing manual adjustments.
        """
        discount_factor = self.price_level * 0.05
        return product.base_price * (1 - discount_factor)
