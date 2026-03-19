# Compute Wallet Rail

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-PayWithLocus
- **Primary track:** PayWithLocus
- **Overlap targets:** Bankr Gateway, Slice, Celo, ERC-8004 Receipts, Lido stETH Treasury, ENS
- **Primary contract:** LocusSpendController
- **Primary operator module:** locus_payments
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A controlled Base payment rail that creates bounded subaccounts for compute, commerce, and operations while preserving auditable spend envelopes.

## Track evidence

- `artifacts/onchain_intents/celo_payment_settle.json`
- `artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json`
- `artifacts/onchain_intents/lido_yield_route.json`
- `artifacts/onchain_intents/ens_ens_publish.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "Compute Wallet Rail",
  "track": "PayWithLocus",
  "plan_id": "0x579d8c8a070fbbdbd829a9b41e66d613e3a5b9a682d9be9ce6a57d8c920d9200",
  "simulation_hash": "0xa5b5bb379d2c7756b0cee0a534e4b9226232f46898a9a71b042e9c2b18356308",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/celo_payment_settle.json",
    "artifacts/onchain_intents/erc_8004_receipts_receipt_anchor.json",
    "artifacts/onchain_intents/lido_yield_route.json",
    "artifacts/onchain_intents/ens_ens_publish.json"
  ],
  "partner_statuses": {
    "PayWithLocus": "awaiting_credentials",
    "Bankr Gateway": "awaiting_credentials",
    "Slice": "awaiting_credentials",
    "Celo": "prepared_contract_call",
    "ERC-8004 Receipts": "prepared_contract_call",
    "Lido": "prepared_contract_call",
    "ENS": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:18+00:00"
}
```
