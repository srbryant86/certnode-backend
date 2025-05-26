
# CertNode Federated Vault Primer

Each federated node contains:
- `vault_node.json` – contains vault ID, sync URI, parent vault

Sample:
{
  "node_id": "certnode-acme-001",
  "parent_vault": "https://certnode.io/vault.json",
  "sync_uri": "https://acme.org/vault.json"
}
