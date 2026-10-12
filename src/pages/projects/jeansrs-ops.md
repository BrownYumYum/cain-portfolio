---
layout: ../../layouts/Layout.astro
title: "JEANSRS.OPS — Central Operations & AI Hub | Cain Anthony Macias"
---

[← Back to Projects](/projects)

# JEANSRS.OPS — Central Operations, Visibility & Autonomous AI Layer

## Problem
Operating across multi-channel B2B distribution environments, legacy ERP platforms (Epicor Eclipse) often create data silos between day-to-day sales tools, federal schedule requirements, field photo uploads, and customer messaging platforms. This fragmentation led to catalog price drift, manual spreadsheet formatting, and delayed field communications.

## Solution
Engineered **JEANSRS.OPS** as a centralized, high-concurrency integration and autonomous operational layer connecting Epicor Eclipse ERP directly with live sales, quoting, field service, and logistics platforms.

## Core Modules & Implementation

### 1. AutoQuotes (AQ) & Eclipse Price Sync
- **3-Step Price Sync & Export Workflow:** Compares Eclipse catalog data against live AutoQuotes feeds to detect cost drift and produce validated import files.
- **Live IDMS-XML Integration:** Connects directly via IDMS-XML (`MassProductInquiry`, `SalesOrderSubmit`) for real-time stock checks, customer price checks, and verified branch availability.
- **Automated Catalog Refresh:** Daily background sync pulling product listings across 820+ manufacturers with chunked upserts to handle high-concurrency catalog refreshes without memory crashes.

### 2. Government & GSA MAS Operations
- **Official FAS Formatting:** Generates the exact 18-column pipe-delimited GSA FAS format required by federal schedule guidelines.
- **Intelligent Auto-Matching:** Features automatic SIN matching, DOD/military PO prefix detection, federal agency mapping, and Industrial Funding Fee (IFF 0.9925) calculation.
- **Price Guardrails:** Preserves approved GSA discount percentages whenever manufacturer list prices fluctuate.

### 3. CRM & Data Hub
- **HubSpot-Style CRM Suite:** Manages companies, contacts, deals, tasks, and activity timelines.
- **Customer Database Sync:** Synced 27,000+ customer accounts from Eclipse into the CRM with instant search and regional filtering.
- **Epicor Grow Integration:** Connects directly to Epicor Grow datasets via OAuth/API for executive business intelligence reporting.

### 4. Operations, Logistics & Field Communications
- **Freight & E-Commerce Audit:** Integrated XPO Freight & Eniture APIs to scan active Shopify products against freight rules and flag missing weight/dimension attributes.
- **CompanyCam Job Photos:** Real-time webhook listener linking job photos directly to customer projects with an approval-gated dispatch queue.
- **M365 Call Reviews & AI Lead Extraction:** Ingests call recordings and transcripts, runs AI call analysis (intent, sentiment, lead potential), and routes leads directly to sales teams.

### 5. Autonomous AI Agent Operations (`/agents`)
- **Multi-Agent Operations Hub:** Built on Claude via the Lovable AI Gateway with a unified server-side tool registry (`agent-tools.server.ts`).
- **Specialized Roles:** Deployed targeted agents—Atlas (Ops Coordinator), Vigil/Sentinel (Catalog Auditing), Keystone (Project Manager), Dispatch (Field Manager), Aegis/Warden (Compliance), Relay (Comms), Forge (Architect), and Summit (Executive Briefing).
- **Human-in-the-Loop Decisions:** High-impact actions queue up in an interactive approval queue before execution.

---

## Core Technical Stack
- **Languages & Frameworks:** Python, Node.js / Express, React, TypeScript
- **Integrations:** Epicor Eclipse (IDMS-XML), HubSpot CRM API, Epicor Grow, Shopify API, ProKeep SMS, CompanyCam Webhooks
- **AI & Cloud Infrastructure:** Claude AI Gateway, Docker, AWS EC2, XPO / Eniture Freight APIs
