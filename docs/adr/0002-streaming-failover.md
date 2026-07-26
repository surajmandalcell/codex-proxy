# ADR 0002: Streaming failover boundary

- Status: Accepted
- Date: 2026-07-26

## Context

Retrying a failed stream on another provider can improve reliability before the client observes output. Retrying after text or a tool call can duplicate content, repeat side effects, or create a response assembled from different models.

## Decision

Buffer non-visible stream metadata. Allow route failover only until the first non-empty text delta or tool call. Heartbeat comments do not establish visibility. After visibility, return an error on the same stream and never invoke another provider.

## Consequences

- Pre-output rate-limit and overload failures remain recoverable.
- Long-running Deep Research can keep connections alive without forfeiting failover safety.
- Partial streams remain partial rather than being silently spliced.
- Tool execution is never duplicated by gateway retry after tool visibility.
