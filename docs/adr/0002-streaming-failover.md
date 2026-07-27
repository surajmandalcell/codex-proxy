# ADR 0002: Streaming failover boundary

- Status: Accepted
- Date: 2026-07-26

## Context

A second provider can recover a stream before the client receives output.

A retry after visible output can duplicate text or tool effects. It can also mix output from different models.

## Decision

Buffer stream metadata that is not visible. Permit failover only before the first text delta or tool call.

Heartbeat comments do not start the visible-output state.

After visible output starts, return the error on the same stream. Do not call another provider.

## Results

- The gateway can recover from a pre-output rate limit.
- Deep Research can send heartbeats without changing the failover rule.
- A partial stream stays partial.
- A gateway retry cannot repeat a visible tool call.
