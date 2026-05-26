# 🦁 Crypto Alpha Hunter

Real-time cryptocurrency intelligence system for detecting whale movements, arbitrage opportunities, and market alpha before it goes mainstream.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Features

### Core Intelligence
- **Whale Tracker** — Monitor 500+ whale wallets across chains in real-time
- **Smart Money Flow** — Detect accumulation/distribution patterns using on-chain data
- **Mempool Scanner** — Watch pending	txns for sandwich opportunities
- **Rug Detector** — Honeypot checks, honeypot.is API, GoPlus security scores
- **Volume Analyzer** — Anomaly detection for unusual trading volume

### Trading Automation
- **MEV Bot** — Sandwich attack detection and auto-frontrun
- **Arbitrage Finder** — Cross-DEX price differential detection
- **Liquidator** — Underwater position monitoring
- **Order Book Sniper** — Limit order fill detection

### NFT Intelligence  
- **Mint Sniper** — Raydium/Orca new pool detection
- **Whale Flipper** — Track whale NFT purchases
- **Floor Monitor** — Collection floor price tracking
- **Holder Analysis** — Distribution and wash trade detection

### Multi-Chain Support
- Solana ✓
- Ethereum ✓
- Base ✓
- Arbitrum ✓
- Optimism ✓
- BSC ✓
- Avalanche ✓

## 🛠 Tech Stack

- Python 3.12+ (async/await)
- ClickHouse (analytics DB)
- Redis (caching)
- Telegram Bot (alerts)
- Alchemy/QuickNode RPC

## 📦 Installation

```bash
git clone https://github.com/cecesmaya/crypto-alpha-hunter.git
cd crypto-alpha-hunter
pip install -r requirements.txt
cp config.yaml.example config.yaml
# Edit config with your API keys
python -m src.scanner
```

## 🔐 Configuration

```yaml
# config.yaml
telegram:
  bot_token: "YOUR_BOT_TOKEN"
  alert_chat_ids:
    - "YOUR_CHAT_ID"

chains:
  solana:
    rpc: "YOUR_SOLANA_RPC"
    ws: "YOUR_SOLANA_WS"
  ethereum:
    rpc: "YOUR_ETH_RPC"

whale_lists:
  solana:
    - "7xKX.."
    - "GDHu.."
  ethereum:
    - "0xAAA.."
    - "0xBBB.."

alerts:
  min_volume_usd: 10000
  min_movement_pct: 50
```

## 📊 Dashboard

Access via Telegram:
- `/start` — Initialize
- `/track <wallet>` — Add wallet to watchlist  
- `/alert` — Configure alerts
- `/status` — System status
- `/stats` — Activity summary

## 📋 Example Alerts

```
🦋 WHALE ALERT
━━━━━━━━━━━━━━━━━━
Token: JUPyiwrYJFGPxLVP6FtvWF
Amount: 245,000 SOL ($1.2M)
Type: ACCUMULATION
Tx: https://solscan.io/xxx
━━━━━━━━━━━━━━━━━━

🥷 SNIPER ALERT
━━━━━━━━━━━━━━━━━━
Pool: NEW PUMP TOKEN
Type: PAIR_CREATED
Liquidity: $850K
MC: $3.4M
Mint Auth: Burned ✅
━━━━━━━━━━━━━━━━━━
```

## 🔒 Security

- All private keys stored encrypted (Fernet)
- RPC rates limiting
- Auto-retry with exponential backoff
- Circuit breaker for API failures

## 📜 License

MIT License — See LICENSE file.

---

Built with AI agents. Running 24/7 on VPS.
Detecting alpha before it hits CT tweets.