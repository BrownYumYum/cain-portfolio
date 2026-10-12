---
layout: ../../layouts/ProjectLayout.astro
title: "JEANSRS.OPS — Enterprise Operations Platform"
description: "A technical case study of an ERP-connected operations platform with catalog synchronization, compliance workflows, and human-approved AI."
category: "Enterprise systems · Current build"
---

# JEANSRS.OPS

<p class="case-subtitle">An operations control layer connecting legacy ERP data, pricing intelligence, field communication, and human-supervised AI workflows.</p>

<div class="case-build-status">
  <span class="case-build-dot" aria-hidden="true"></span>
  <strong>Current project</strong>
  <span>·</span>
  <span>Architecture and features evidenced by the codebase</span>
</div>

<div class="case-proof-grid" aria-label="Implementation details verified in source">
  <div class="case-proof">
    <strong>18</strong>
    <span>integration / automation hook routes</span>
  </div>
  <div class="case-proof">
    <strong>200</strong>
    <span>records per catalog upsert chunk</span>
  </div>
  <div class="case-proof">
    <strong>Human-first</strong>
    <span>approval queue for consequential AI actions</span>
  </div>
</div>

## The problem

A B2B distributor runs on multiple systems: a legacy ERP, manufacturer catalog feeds, quoting, customer communications, field-service tools, and reporting workflows. The problem is not simply moving data. It is making information **consistent, actionable, and reviewable** without adding more manual work.

JEANSRS.OPS is the application I’m building to connect those workflows in one operations interface. The goal is to make pricing changes visible, keep records in sync, and give teams a controlled place to review what happens next.

## Architecture at a glance

<section class="case-architecture" aria-label="Simplified system architecture">
  <div class="case-architecture-heading">
    <span>INTEGRATION MAP</span>
    <span>SIMPLIFIED / NO CUSTOMER DATA</span>
  </div>
  <div class="case-architecture-flow">
    <div class="case-architecture-column">
      <span class="case-architecture-label">01 / INPUTS</span>
      <div class="case-architecture-node"><strong>Epicor Eclipse</strong><small>ERP · XML / relay</small></div>
      <div class="case-architecture-node"><strong>AutoQuotes</strong><small>Manufacturer catalog feeds</small></div>
      <div class="case-architecture-node"><strong>External services</strong><small>CRM · field · commerce</small></div>
    </div>
    <span class="case-architecture-arrow" aria-hidden="true">→</span>
    <div class="case-architecture-column case-architecture-core">
      <span class="case-architecture-label">02 / CONTROL LAYER</span>
      <div class="case-architecture-node case-architecture-main"><small>OPERATIONS PLATFORM</small><strong>JEANSRS.OPS</strong><span>Server functions + shared data</span></div>
      <div class="case-architecture-node case-architecture-sub"><strong>Validation + reconciliation</strong><small>Deduplicate · compare · review</small></div>
    </div>
    <span class="case-architecture-arrow" aria-hidden="true">→</span>
    <div class="case-architecture-column">
      <span class="case-architecture-label">03 / WORKFLOWS</span>
      <div class="case-architecture-node"><strong>Pricing operations</strong><small>Comparison · exports</small></div>
      <div class="case-architecture-node"><strong>Compliance + CRM</strong><small>Reporting · records</small></div>
      <div class="case-architecture-node"><strong>AI-assisted operations</strong><small>Tool access · approvals</small></div>
    </div>
  </div>
  <div class="case-architecture-guard"><span aria-hidden="true">✓</span> Human decision gates <span class="case-architecture-guard-separator">/</span> Logged agent runs <span class="case-architecture-guard-separator">/</span> Reviewable outputs</div>
</section>

## What stands out technically

<div class="case-capability-grid">
  <div class="case-capability">
    <span class="case-capability-index">01 / DATA INTEGRITY</span>
    <h3>Batch-safe catalog synchronization</h3>
    <p>The vendor sync deduplicates model keys and writes products in 200-record chunks, reducing duplicate-key conflicts and keeping large imports more manageable.</p>
  </div>
  <div class="case-capability">
    <span class="case-capability-index">02 / LEGACY INTEGRATION</span>
    <h3>ERP data without a rebuild</h3>
    <p>Server-side Eclipse integrations support XML-based product and branch inquiries, a relay option, and comparison workflows alongside AutoQuotes pricing data.</p>
  </div>
  <div class="case-capability">
    <span class="case-capability-index">03 / HUMAN OVERSIGHT</span>
    <h3>AI agents with boundaries</h3>
    <p>Agents receive selected tools, can delegate focused tasks, and write run history. Sensitive actions are routed through approval decisions rather than being treated as unrestricted automation.</p>
  </div>
  <div class="case-capability">
    <span class="case-capability-index">04 / COMPLIANCE WORKFLOWS</span>
    <h3>Structured reporting, not spreadsheets</h3>
    <p>The GSA workflow builds an 18-column export, combines rule-based classification with review flags, and provides a way to inspect records requiring attention.</p>
  </div>
</div>

## Engineering decisions

### 1. Separate the integration layer from the interface

The application uses **React, TypeScript, and TanStack Start** for the user experience and server functions for backend operations. This keeps ERP credentials and external service calls on the server side, while the UI focuses on actionable states: searches, exceptions, approvals, and exports.

### 2. Make catalog imports predictable

The catalog sync handles duplicate model numbers before upserts and processes records in defined chunks. The code includes vendor-feed import, matching, and ERP-facing comparison paths. This is a more dependable approach than moving raw API responses directly into operations.

### 3. Treat AI actions as workflows, not magic

The agent runner filters a tool registry according to each agent’s enabled tools. It records executions and supports child-task delegation. A **decision request** can pause the workflow for a person; approved-action tools are made available in the resumed decision path.

This is the part I find especially important: an AI assistant can surface evidence and recommend an action, but the application still needs to make ownership and approval explicit.

### 4. Build around existing business tools

The project has dedicated modules for **AutoQuotes, Epicor Eclipse, CRM workflows, ProKeep, CompanyCam, Shopify, and Microsoft 365**. The shared interface aims to reduce tool-switching without replacing the systems the business already relies on.

## Technology snapshot

<div class="case-stack-grid">
  <div><span>APPLICATION</span><strong>React · TypeScript · TanStack Start</strong></div>
  <div><span>DATA & AUTH</span><strong>Supabase · PostgreSQL</strong></div>
  <div><span>INTEGRATION</span><strong>XML · REST APIs · webhooks</strong></div>
  <div><span>AI WORKFLOWS</span><strong>AI SDK · tool registry · approval queue</strong></div>
</div>

## What this project demonstrates

- **Business systems thinking:** designing around a real operational process, not an isolated feature.
- **Practical data engineering:** normalization, catalog matching, batch imports, and reconciliation.
- **Full-stack execution:** multiple application areas sharing backend services, data models, and permissions.
- **Risk-aware automation:** decision gates, review states, and recorded agent activity.

<p class="case-privacy-note">Portfolio note: This is a simplified overview based on the uploaded code snapshot. It does not publish company records, credentials, or proprietary implementation code. The presence of a feature in the repository does not, by itself, establish production usage or measured business outcomes.</p>
