import numpy as np
import pandas as pd
from scipy.optimize import minimize

def momentum_backtest(returns, lookback=20):
    spy_returns = returns["SPY"]

    signal = (spy_returns.rolling(lookback).sum().shift(1) > 0).astype(int)
    strategy_returns = signal * spy_returns

    buy_hold = (1 + spy_returns).cumprod()
    momentum = (1 + strategy_returns).cumprod()

    trading_days = 252
    risk_free_rate = 0.05

    def sharpe(r):
        excess = r.mean() * trading_days - risk_free_rate
        vol = r.std() * np.sqrt(trading_days)
        return excess / vol

    def max_dd(cum):
        peak = cum.cummax()
        return ((cum - peak) / peak).min()

    summary = pd.DataFrame({
        "Annual Return": [
            spy_returns.mean() * trading_days,
            strategy_returns.mean() * trading_days
        ],
        "Annual Volatility": [
            spy_returns.std() * np.sqrt(trading_days),
            strategy_returns.std() * np.sqrt(trading_days)
        ],
        "Sharpe Ratio": [
            sharpe(spy_returns),
            sharpe(strategy_returns)
        ],
        "Max Drawdown": [
            max_dd(buy_hold),
            max_dd(momentum)
        ]
    }, index=["Buy & Hold SPY", "Momentum Strategy"])

    return buy_hold, momentum, summary

def minimum_variance_portfolio(returns):
    n = len(returns.columns)
    cov_matrix = returns.cov() * 252

    def portfolio_vol(weights):
        return np.sqrt(weights @ cov_matrix.values @ weights)

    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}
    bounds = [(0, 1)] * n
    initial_weights = np.array([1 / n] * n)

    result = minimize(
        portfolio_vol,
        initial_weights,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    weights = pd.Series(result.x, index=returns.columns)
    min_vol = result.fun

    portfolio_returns = returns @ weights
    cumulative = (1 + portfolio_returns).cumprod()

    summary = pd.DataFrame({
        "Weight": weights,
        "Weight (%)": (weights * 100).round(2)
    })

    return weights, min_vol, cumulative, summary