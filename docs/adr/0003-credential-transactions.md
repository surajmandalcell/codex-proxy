# ADR 0003: Credential transaction order

- Status: Accepted
- Date: 2026-07-26

## Context

Configuration and encrypted secrets use separate files. One file rename cannot commit both files.

## Decision

Use this order for each operation:

- Add: Create the secret. Commit the configuration. Remove the new secret if the commit fails.
- Replace: Create the new secret. Commit the configuration. Remove the old secret.
- Remove: Commit the configuration change. Remove the old secret.

Provider edits ignore public account arrays from the renderer. They keep internal secret references.

## Results

A failed cleanup can leave an encrypted orphan. This result is safer than a live reference to missing secret data.

Tests cover configuration failure and internal credential preservation.
