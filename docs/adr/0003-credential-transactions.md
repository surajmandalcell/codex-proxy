# ADR 0003: Credential and configuration transactions

- Status: Accepted
- Date: 2026-07-26

## Context

Configuration and encrypted secrets are separate files. A credential replacement cannot be committed atomically across both files with a single rename.

## Decision

Use commit ordering that never leaves persisted configuration pointing to missing secret material:

- Add: create secret, commit config, remove new secret if config fails.
- Replace: create new secret, commit config, then remove old secret.
- Remove: commit config removal, then remove secret.

Provider edits ignore renderer-supplied public account arrays and preserve internal account secret references.

## Consequences

A failed cleanup can leave an encrypted orphan, which is safer than a live dangling reference. Tests cover config failure and preservation of internal credential state.
