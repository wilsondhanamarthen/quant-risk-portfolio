# 📈 Quant Portfolio Analysis

Quantitative risk and performance analysis of U.S. equities using Python.
Built to analyze, backtest, and optimize a portfolio of major stocks
using real financial mathematics.

---

## 🔍 Overview

This project performs a full quantitative risk analysis on 5 major U.S. equities:
**SPY, AAPL, MSFT, GOOGL, AMZN** using daily price data from 2015 to 2024.

It goes beyond simple analysis by implementing a **momentum trading strategy backtest**
and a **minimum variance portfolio optimizer** — core concepts in quantitative finance.

---

## 📊 Features

- **Risk Metrics** — Sharpe ratio (with risk-free rate), annualized return & volatility, skewness, kurtosis
- **Value at Risk** — Both Historical VaR and Parametric VaR at 95% confidence
- **Drawdown Analysis** — Rolling max drawdown over the full period
- **Rolling Volatility** — 30-day and 90-day annualized rolling volatility
- **Momentum Strategy Backtest** — Signal-based strategy vs Buy & Hold SPY comparison
- **Minimum Variance Portfolio** — Scipy optimization to find lowest-risk asset allocation
- **Interactive Charts** — All 8 visualizations built with Plotly (dark theme, hover, zoom)

---

## 📁 Project Structure

```
quant-portfolio-analysis/
├── main.py              # Entry point — runs everything
├── data.py              # Downloads and processes price data
├── metrics.py           # Computes all risk & performance metrics
├── strategy.py          # Momentum backtest + portfolio optimization
├── visualizations.py    # All 8 interactive Plotly charts
└── requirements.txt     # Dependencies
```

---

## 📉 Key Findings (2015–2024)

| Ticker | Annual Return | Sharpe Ratio | Max Drawdown |
|--------|--------------|--------------|--------------|
| AAPL   | 24.4%        | 0.698        | -45.9%       |
| AMZN   | 23.3%        | 0.561        | -61.9%       |
| MSFT   | 19.3%        | 0.561        | -40.6%       |
| SPY    | 12.8%        | 0.457        | -35.8%       |
| GOOGL  | 16.7%        | 0.428        | -47.9%       |

**Momentum Strategy vs Buy & Hold SPY:**

| Strategy | Sharpe Ratio | Max Drawdown |
|----------|--------------|--------------|
| Buy & Hold SPY | 0.457 | -35.8% |
| Momentum Strategy | 0.323 | -13.6% |

> The momentum strategy underperforms on raw returns but significantly
> reduces drawdown — showing the classic risk/return tradeoff in action.

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/wilsondhanamarthen/quant-risk-portfolio.git
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the project
```bash
python main.py
```

Charts will automatically open in your browser as interactive `.html` files.

---

## 🛠️ Tech Stack

- **Python 3.12**
- **yfinance** — market data
- **numpy / pandas** — data processing
- **scipy** — portfolio optimization
- **plotly** — interactive visualizations

---

## 📚 Concepts Covered

- Log returns vs simple returns
- Sharpe ratio with risk-free rate adjustment
- Historical vs Parametric Value at Risk
- Maximum drawdown calculation
- Rolling volatility (square root of time rule)
- Momentum signal generation and backtesting
- Mean-variance portfolio optimization (Markowitz)

---

## 👤 Author

**Wilson Dhana Marthen**
Aspiring Quant Trader/Researcher

