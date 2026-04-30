# 📈 Quant Risk Portfolio 

Quantitative risk and performance analysis of U.S. equities using Python.
Built to analyze, backtest, and optimize a portfolio of major stocks
using real financial mathematics.

---

## 🔍 Overview

This project performs a full quantitative risk analysis on 5 major U.S. equities:
**SPY, AAPL, MSFT, GOOGL, AMZN** using daily price data from 2010 to 2025.

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
quant-risk-portfolio/
├── main.py              # Entry point — runs everything
├── data.py              # Downloads and processes price data
├── metrics.py           # Computes all risk & performance metrics
├── strategy.py          # Momentum backtest + portfolio optimization
├── visualizations.py    # All 8 interactive Plotly charts
└── requirements.txt     # Dependencies
```

---

## 📌 Key Findings

| Ticker | Annual Return | Annual Volatility | Sharpe Ratio | Max Drawdown |
|--------|--------------|------------------|--------------|--------------|
| AAPL   | 24.44%       | 27.87%           | 0.70         | -45.94%      |
| AMZN   | 23.31%       | 32.65%           | 0.56         | -61.89%      |
| MSFT   | 19.34%       | 25.58%           | 0.56         | -40.61%      |
| GOOGL  | 16.66%       | 27.26%           | 0.43         | -47.95%      |
| SPY    | 12.82%       | 17.10%           | 0.46         | -35.75%      |

---

## 📈 Strategy Comparison: Momentum vs Buy & Hold

| Strategy              | Annual Return | Volatility | Sharpe Ratio | Max Drawdown |
|----------------------|--------------|------------|--------------|--------------|
| Buy & Hold (SPY)     | 12.82%       | 17.10%     | 0.46         | -35.75%      |
| Momentum Strategy    | 8.38%        | 10.46%     | 0.32         | -13.60%      |

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
Aspiring Quant 

