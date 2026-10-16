---
layout: ../../layouts/ProjectLayout.astro
title: "ORION Desktop — Local-First AI Assistant"
description: "An in-development native Windows AI desktop application built with Rust, Tauri, React, and local Ollama inference."
category: "Desktop software & local AI"
---

# ORION Desktop — Starforge Edition

## Overview

**ORION Desktop** is an in-development, local-first AI assistant for Windows. The project explores how to make on-device language models approachable through a polished desktop application, while preserving a clear distinction between ordinary chat and powerful agent actions.

The initial build integrates a local Ollama model through a self-hosted OpenClaw gateway. It combines a Rust/Tauri backend with a React and TypeScript interface, providing the foundation for a consumer-oriented desktop experience with local model discovery, streaming responses, and explicit security boundaries.

## The Problem

Running a local language model often involves separate terminals, server processes, model downloads, and configuration files. Agent frameworks introduce additional complexity because web browsing, file operations, and command execution need different levels of trust.

I wanted to build a desktop application that feels familiar to everyday users without hiding the security decisions that matter.

## Technical Stack

* **Desktop application:** Tauri 2, Rust, React, TypeScript, and CSS.
* **Local inference:** Ollama and a locally installed Gemma 4 12B model.
* **Agent integration:** OpenClaw local gateway, used as an optional integration path under development.
* **Communication:** Local HTTP endpoints and server-sent event (SSE) response streaming.
* **Windows integration:** System tray, global keyboard shortcut, compact/full window modes, and autostart behavior.

## Features Implemented

* **Streaming conversations:** Incremental assistant responses rendered in the chat interface, with request-specific streaming events.
* **Stop generation:** Cancel active response requests and communicate cancellation clearly in the conversation.
* **Model Hub:** Read-only discovery of models installed in Ollama, including model details.
* **Native desktop experience:** Windows tray controls, compact/full presentation, and quick-access keyboard shortcut.
* **Chat presentation:** Markdown responses, syntax-highlighted code blocks, copying, and conversation persistence in local browser storage.
* **Local gateway integration:** A Rust backend connecting to a local OpenClaw gateway with credentials kept out of the frontend.
* **Security hardening:** Reduced agent tool permissions, disabled elevated tools, disabled an unnecessary third-party search extension, and reviewed OpenClaw security audit findings.

## Engineering Decisions

### Separate the interface from inference

The Tauri backend handles local service communication while React focuses on user interactions and streamed output. This separation creates room to support different inference providers without rebuilding the interface.

### Treat permission boundaries as product features

A useful AI assistant should not equate model output with authorization. The planned security controller will mediate operations, require explicit approval for impactful changes, and prevent unapproved actions.

### Preserve an offline-first path

A major design requirement is the option to keep model execution and conversation data local. External search, remote inference, and other network-dependent capabilities are being designed as separately configurable options.

## Roadmap — Planned, Not Yet Implemented

* **Direct Ollama Local Mode:** Chat without requiring an agent gateway.
* **Guided onboarding:** Optional hardware inspection and model recommendations based on device capabilities.
* **Intelligent permissions:** Per-request approval for web searches and selected tools, with revocable remembered preferences.
* **Plan-before-execute automation:** Read-only inspection, a proposed action plan, explicit approval, controlled execution, and verification for tasks such as organizing files.
* **Privacy and customization:** More detailed local/network mode settings, permission history, and expanded model controls.
* **Remote self-hosted inference:** Optional connection to a privately hosted model server.

These features are part of the design direction and should not be mistaken for functionality in the current build.

## Current Status

**Active development.** The desktop application, local-model chat streaming, cancellation, and initial Model Hub are working in the developer environment. The broader agent-permission system, first-run setup experience, and public distribution workflow are still being developed.

## What This Project Demonstrates

ORION combines native desktop engineering, frontend development, local AI integration, asynchronous streaming, operating-system integration, and security-conscious product architecture. It reflects my interest in building usable systems around complex technology—not just connecting a chat interface to a model.
