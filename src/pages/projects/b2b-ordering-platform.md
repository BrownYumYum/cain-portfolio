---
layout: ../../layouts/Layout.astro
---

[← Back to Systems](/projects)

# Enterprise B2B Ordering Platform

## Problem
Manual ordering processes created pricing errors, delays, and operational bottlenecks for institutional clients. Tiered pricing structures were especially prone to inconsistencies, requiring frequent manual corrections.

## Solution
Developed a full-stack Django platform that automated account-based ordering and pricing logic, eliminating manual data entry and enforcing contract-level pricing rules across all transactions.

## Impact
* **Reduced pricing errors** and manual intervention.
* **Improved order processing speed** and accuracy.
* **Enabled scalable, self-service** procurement workflows.

## System Design & Implementation
Built a full-stack Django application to support complex, account-based procurement workflows with automated pricing logic.

* **Dynamic Pricing Engine:** Designed a relational database schema to support dynamic, contract-based pricing tied to customer accounts.
* **Cloud Infrastructure:** Deployed the platform on AWS (EC2 + RDS) to ensure reliability, scalability, and secure data handling.
* **Frontend Engineered:** Engineered the user interface to strictly align with Section 508 accessibility standards, ensuring seamless usability and compliance across all institutional client portals.

## Technical Example: Pricing Logic
This logic ensures contract-specific pricing is automatically applied, eliminating manual adjustments and reducing pricing inconsistencies.

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
