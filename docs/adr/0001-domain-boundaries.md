# ADR 0001: Domain boundaries

- Status: Accepted
- Date: 2026-07-26

## Context

The desktop gateway contains protocols, routing, credentials, storage, Electron code, and user-interface code.

Direct imports between these concerns make provider changes dangerous. They also make tests depend on frameworks.

## Decision

Use inward dependencies:

- The domain is pure.
- The application uses ports and domain rules.
- Providers convert canonical protocols.
- Infrastructure supplies storage and local HTTP.
- Desktop code connects services and shows public state.

Repository checks prevent invalid import directions.

## Results

- Routing tests do not require Electron, a network, or SQLite.
- Providers cannot change account selection.
- Renderer code cannot read credentials or process APIs.
- The code needs explicit adapters and service constructors.
