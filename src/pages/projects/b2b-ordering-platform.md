---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# Enterprise B2B Ordering Architecture

## The Challenge
Institutional clients were relying on manual ordering processes, creating severe operational bottlenecks and introducing high error rates into tiered pricing models. The objective was to modernize the procurement workflow, eliminate manual data entry, and deploy a scalable digital platform without disrupting existing business operations.

## The Engineering Architecture
I engineered a full stack Django application tailored for complex, account based B2B procurement workflows.

**Core Technical Implementations:**
* **Dynamic Pricing Engine:** Built a custom relational database schema using PostgreSQL to securely process and serve complex, tiered pricing structures based on authenticated account parameters.
* **Cloud Infrastructure:** Architected and deployed the production environment on AWS, utilizing EC2 instances for compute and RDS for database management, ensuring high availability and secure data handling for enterprise traffic.
* **Frontend Compliance:** Engineered the user interface to strictly align with Section 508 accessibility standards, ensuring seamless usability and compliance across all institutional client portals.

## Technical Evidence: Relational Schema & Logic
To ensure data integrity, the system uses a relational mapping between the client's account GUID and the ERP's internal price line.

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