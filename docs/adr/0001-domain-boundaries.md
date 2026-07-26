# ADR 0001: Domain boundaries

- Status: Accepted
- Date: 2026-07-26

## Context

A multi-provider desktop proxy combines protocol translation, routing, credentials, persistence, Electron, and UI. Allowing these concerns to import each other directly makes provider changes risky and tests dependent on frameworks.

## Decision

Use inward dependencies:

- Domain is pure.
- Application coordinates ports and domain policy.
- Providers translate canonical protocol contracts.
- Infrastructure implements storage and local HTTP.
- Desktop code composes services and presents public state.

Repository verification enforces forbidden import directions.

## Consequences

- Routing can be tested without network, Electron, or SQLite.
- Providers cannot silently change account-selection policy.
- Renderer code cannot access credentials or process APIs.
- More explicit adapters and service constructors are required.
