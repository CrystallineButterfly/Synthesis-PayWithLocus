# Compute Wallet Rail

- **Repo:** [Synthesis-PayWithLocus](https://github.com/CrystallineButterfly/Synthesis-PayWithLocus)
- **Primary track:** PayWithLocus
- **Category:** payments
- **Primary contract:** `LocusSpendController`
- **Primary module:** `locus_payments`
- **Submission status:** audited and offline-demo ready; optional live partner credentials unlock network execution.

## What this repo does

A controlled Base payment rail that creates bounded subaccounts for compute, commerce, and operations while preserving auditable spend envelopes.

## Why this build matters

The project creates bounded subaccount payment plans for compute, commerce, and operations. A controller contract emits spend envelopes and reconciliation receipts while the Python side prepares Base/Locus payment bundles ready for live credentials.

## Submission fit

- **Primary track:** PayWithLocus
- **Overlap targets:** Bankr Gateway, Slice, Celo, ERC-8004 Receipts, Lido stETH Treasury, ENS
- **Partners covered:** PayWithLocus, Bankr Gateway, Slice, Celo, ERC-8004 Receipts, Lido, ENS

## Idea shortlist

1. Yield-Funded Locus Subaccounts
2. Pay-Per-Use Agent Wallets
3. Treasury-Controlled Checkout Mesh

## System graph

```mermaid
flowchart TD
    Signals[Discover signals]
    Planner[Agent runtime]
    DryRun[Dry-run artifact]
    Contract[LocusSpendController policy contract]
    Verify[Verify and render submission]
    Signals --> Planner --> DryRun --> Contract --> Verify
    Contract --> paywithlocus[PayWithLocus]
    Contract --> bankr_gateway[Bankr Gateway]
    Contract --> slice[Slice]
    Contract --> celo[Celo]
    Contract --> erc_8004_receipts[ERC-8004 Receipts]
    Contract --> lido[Lido]
```

## Repository contents

| Path | What it contains |
| --- | --- |
| `src/` | Shared policy contracts plus the repo-specific wrapper contract. |
| `script/Deploy.s.sol` | Foundry deployment entrypoint for the policy contract. |
| `agents/` | Python runtime, project spec, env handling, and partner adapters. |
| `scripts/` | Terminal entrypoints for run, demo planning, and submission rendering. |
| `docs/` | Architecture, credentials, security notes, and demo steps. |
| `submissions/` | Generated `synthesis.md` snippet for this repo. |
| `test/` | Foundry tests for the Solidity control layer. |
| `tests/` | Python tests for runtime and project context. |
| `agent.json` | Submission-facing agent manifest. |
| `agent_log.json` | Local execution log and status trail. |

## Autonomy loop

1. Discover signals relevant to the repo track and its overlap targets.
2. Build a bounded plan with per-action and compute caps.
3. Persist a dry-run artifact before any live execution.
4. Enforce onchain policy through the guarded contract wrapper.
5. Verify outputs, update receipts, and render submission material.

## Current readiness

- **Latest verification:** `verified` at `2026-03-19T03:52:18+00:00`
- **Execution mode:** `offline_prepared`
- **Offline-prepared partners:** Celo (prepared_contract_call), ERC-8004 Receipts (prepared_contract_call), Lido (prepared_contract_call), ENS (prepared_contract_call)
- **Live credential blockers:** PayWithLocus, Bankr Gateway, Slice
- **Audit docs:** `docs/audit.md`, `docs/live_readiness.md`

## Most sensitive actions

- `bankr_gateway_compute_route` (Bankr Gateway, high)

## Live blocker details

- **PayWithLocus** — LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **Bankr Gateway** — BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/
- **Slice** — SLICE_API_KEY, SLICE_HOOK_URL — https://docs.slice.so/

## Latest evidence artifacts

- `artifacts/onchain_intents/celo_payment_settle.json`
- `artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json`
- `artifacts/onchain_intents/lido_yield_route.json`
- `artifacts/onchain_intents/ens_ens_publish.json`

## Security controls

- Admin-managed allowlists for targets and selectors.
- Per-action caps, daily caps, cooldown windows, and a principal floor.
- Reporter-only receipt anchoring and proof attachment.
- Env-only secrets; no committed private keys or partner tokens.
- Pause switch plus dry-run-first execution flow.

## Action catalog

| Action | Partner | Purpose | Max USD | Sensitivity |
| --- | --- | --- | --- | --- |
| `paywithlocus_subaccount_pay` | PayWithLocus | Use PayWithLocus for a bounded action in this repo. | $120 | medium |
| `bankr_gateway_compute_route` | Bankr Gateway | Use Bankr Gateway for a bounded action in this repo. | $10 | high |
| `slice_checkout_hook` | Slice | Use Slice for a bounded action in this repo. | $35 | medium |
| `celo_payment_settle` | Celo | Use Celo for a bounded action in this repo. | $150 | low |
| `erc_8004_receipts_receipt_anchor` | ERC-8004 Receipts | Use ERC-8004 Receipts for a bounded action in this repo. | $1 | medium |
| `lido_yield_route` | Lido | Use Lido for a bounded action in this repo. | $200 | medium |
| `ens_ens_publish` | ENS | Use ENS for a bounded action in this repo. | $5 | low |

## Local terminal flow (Anvil + Sepolia)

```bash
export SEPOLIA_RPC_URL=https://sepolia.infura.io/v3/YOUR_KEY
anvil --fork-url "$SEPOLIA_RPC_URL" --chain-id 11155111
cp .env.example .env
# keep private keys only in .env; TODO.md stays local-only too
forge script script/Deploy.s.sol --rpc-url "$RPC_URL" --broadcast
python3 scripts/run_agent.py
python3 scripts/render_submission.py
```

## Commands

```bash
python3 -m unittest discover -s tests
forge test
python3 scripts/run_agent.py
python3 scripts/plan_live_demo.py
python3 scripts/render_submission.py
```

## Credentials

| Partner | Variables | Docs |
| --- | --- | --- |
| PayWithLocus | LOCUS_API_KEY, LOCUS_PAYMENT_URL | https://docs.locus.finance/ |
| Bankr Gateway | BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL | https://bankr.bot/ |
| Slice | SLICE_API_KEY, SLICE_HOOK_URL | https://docs.slice.so/ |
| Celo | CELO_RPC_URL | https://docs.celo.org/ |
| ERC-8004 Receipts | RPC_URL | https://eips.ethereum.org/EIPS/eip-8004 |
| Lido | RPC_URL | https://docs.lido.fi/ |
| ENS | ENS_NAME | https://docs.ens.domains/ |

## Live demo plan

1. Copy .env.example to .env and fill the required keys.
2. Deploy the contract with forge script script/Deploy.s.sol --broadcast for LocusSpendController.
3. Run python3 scripts/run_agent.py to produce a dry run for locus_payments.
4. Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
5. Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
