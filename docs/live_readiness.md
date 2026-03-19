# Live readiness

- **Project:** Compute Wallet Rail
- **Track:** PayWithLocus
- **Latest verification:** `verified`
- **Execution mode:** `offline_prepared`
- **Generated at:** `2026-03-19T03:52:18+00:00`

## Trust boundaries

- **PayWithLocus** — `rest_json` — Create bounded subaccounts and controlled spend flows.
- **Bankr Gateway** — `rest_json` — Route inference through cost-aware model selection.
- **Slice** — `rest_json` — Drive checkout hooks and storefront policy changes.
- **Celo** — `contract_call` — Settle stablecoin-native transfers on Celo rails.
- **ERC-8004 Receipts** — `contract_call` — Anchor identity, task receipts, and reputation updates.
- **Lido** — `contract_call` — Route staking yield through guarded treasury actions.
- **ENS** — `contract_call` — Publish human-readable coordination and identity receipts.

## Offline-ready partner paths

- **Celo** — prepared_contract_call
- **ERC-8004 Receipts** — prepared_contract_call
- **Lido** — prepared_contract_call
- **ENS** — prepared_contract_call

## Live-only partner blockers

- **PayWithLocus**: LOCUS_API_KEY, LOCUS_PAYMENT_URL — https://docs.locus.finance/
- **Bankr Gateway**: BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL — https://bankr.bot/
- **Slice**: SLICE_API_KEY, SLICE_HOOK_URL — https://docs.slice.so/

## Highest-sensitivity actions

- `bankr_gateway_compute_route` — Bankr Gateway — Use Bankr Gateway for a bounded action in this repo.

## Exact next steps

- Copy .env.example to .env and fill the required keys.
- Deploy the contract with forge script script/Deploy.s.sol --broadcast for LocusSpendController.
- Run python3 scripts/run_agent.py to produce a dry run for locus_payments.
- Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
- Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
