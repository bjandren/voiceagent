# Database Design

## Overview

Design the database to support the AI customer support agent's core functionality. The database will store configuration data, call logs, ticket information, and integration data.

## Key Tables & Schemas

### 1. Companies

- **company_id** (Primary Key)
- **name**
- **contact_info**
- **configuration** (JSON for custom settings, knowledge base links, escalation rules)

### 2. Agents

- **agent_id** (Primary Key)
- **company_id** (Foreign Key)
- **phone_number**
- **status** (active/inactive)
- **created_at**

### 3. Calls

- **call_id** (Primary Key)
- **agent_id** (Foreign Key)
- **tenant_id** (if applicable)
- **start_time**
- **end_time**
- **transcript** (Text from Speech-to-Text)
- **resolution_type** (direct resolution, escalated)

### 4. Tickets

- **ticket_id** (Primary Key)
- **call_id** (Foreign Key)
- **ticket_type** (information, administrative, on-site, acute)
- **status** (open, in progress, resolved)
- **created_at**
- **updated_at**
- **details** (JSON for additional context)

### 5. Integrations

- **integration_id** (Primary Key)
- **company_id** (Foreign Key)
- **system_type** (CRM, work order, etc.)
- **api_key**
- **configuration** (JSON)
- **created_at**

## Additional Considerations

- Use Supabase (PostgreSQL) for the relational database.
- Employ Drizzle as the ORM for type-safe queries.
- Plan for horizontal scaling and include indexing on key fields (e.g., call timestamps, company_id) for performance.
