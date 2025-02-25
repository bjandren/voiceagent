# Project Structure

## Overview

Outline the architectural and file structure for the SaaS-based AI customer support agent project. This document covers both the frontend and backend aspects along with integration points.

## Frontend (Hosted on Vercel)

- **Framework:** React with Node.js environment.
- **UI Library:** Shadcn component library.
- **Directory Structure:**
  - `/src`
    - `/components` – Reusable UI components.
    - `/pages` – Page-level components corresponding to routes.
    - `/styles` – Global styles and theme configuration (including the defined color palette).
    - `/hooks` – Custom React hooks.
    - `/utils` – Utility functions and constants.
  - `/public` – Static assets (images, fonts).

## Backend

- **Primary Language:** Python (using FastAPI or Flask for RESTful APIs).
- **Concurrent Processing:** Asynchronous processing with asyncio.
- **Directory Structure:**
  - `/app`
    - `/api` – Endpoint definitions.
    - `/models` – Data models representing the database schema.
    - `/services` – Business logic and integration with telephony (Twilio) and voice synthesis (Elevenlabs).
    - `/utils` – Helper functions and common utilities.
  - `/config` – Configuration files (e.g., database, environment variables).
  - `/tests` – Unit and integration tests.

## Microservices (Optional)

- **Node.js Services:** For real-time features (e.g., handling notifications, event processing).
- **Directory Structure:**
  - `/services`
    - `/realtime` – Event-driven service for real-time notifications.
    - `/integrations` – Connectors for external systems (CRM, work order systems).

## Integration Points

- **Telephony:** Twilio for managing incoming/outgoing calls and SMS alerts.
- **Voice Synthesis:** Elevenlabs for generating lifelike voice responses.
- **Database:** Supabase (PostgreSQL) with Drizzle ORM for data access.
- **APIs:** RESTful endpoints to connect with external property management and CRM systems.

## DevOps & Deployment

- **CI/CD:** Automated pipelines for testing, building, and deployment.
- **Monitoring:** Logging and performance monitoring tools.
- **Scalability:** Design for horizontal scaling on Vercel (frontend) and containerized backend services.
