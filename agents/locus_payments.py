"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "Compute Wallet Rail",
  "track": "PayWithLocus",
  "pitch": "A controlled Base payment rail that creates bounded subaccounts for compute, commerce, and operations while preserving auditable spend envelopes.",
  "overlap_targets": [
    "Bankr Gateway",
    "Slice",
    "Celo",
    "ERC-8004 Receipts",
    "Lido stETH Treasury",
    "ENS"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
