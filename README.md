# Compute Wallet Rail

- **Repo:** `Synthesis-PayWithLocus`
- **Primary track:** PayWithLocus
- **Category:** payments
- **Submission status:** implementation ready, waiting for credentials and TxIDs.

A controlled Base payment rail that creates bounded subaccounts for compute, commerce, and operations while preserving auditable spend envelopes.

## Selected concept

The project creates bounded subaccount payment plans for compute, commerce, and operations. A controller contract emits spend envelopes and reconciliation receipts while the Python side prepares Base/Locus payment bundles ready for live credentials.

## Idea shortlist

1. Yield-Funded Locus Subaccounts
2. Pay-Per-Use Agent Wallets
3. Treasury-Controlled Checkout Mesh

## Partners covered

PayWithLocus, Bankr Gateway, Slice, Celo, ERC-8004 Receipts, Lido, ENS

## Architecture

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

## Repository layout

- `src/`: shared policy contracts plus the repo-specific wrapper contract.
- `script/`: Foundry deployment entrypoint.
- `agents/`: Python runtime, partner adapters, and project metadata.
- `scripts/`: CLI utilities for running the loop and rendering submissions.
- `docs/`: architecture, credentials, demo script, and security notes.
- `submissions/`: generated `synthesis.md` snippet for this repo.

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
