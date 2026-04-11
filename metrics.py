import numpy as np
import pandas as pd

RISK_FREE_RATE = 0.05
TRADING_DAYS = 252

def compute_metrics(returns):
    mean_daily = returns.mean()
    daily_vol = returns.std()

    annual_return = mean_daily * TRADING_DAYS
    annual_vol = daily_vol * np.sqrt(TRADING_DAYS)
    sharpe_ratio = (annual_return - RISK_FREE_RATE) / annual_vol
    skewness = returns.skew()
    kurtosis = returns.kurtosis()

    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_drawdown = drawdown.min()

    var_historical = -returns.quantile(0.05)
    var_parametric = -(mean_daily - 1.645 * daily_vol)

    results = pd.DataFrame({
        "Annual Return":     annual_return,
        "Annual Volatility": annual_vol,
        "Sharpe Ratio":      sharpe_ratio,
        "Skewness":          skewness,
        "Kurtosis":          kurtosis,
        "Max Drawdown":      max_drawdown,
        "VaR 95% (Hist)":   var_historical,
        "VaR 95% (Param)":  var_parametric,
    })

    return results, drawdown, cumulative

def compute_rolling_vol(returns):
    vol_30 = returns.rolling(30).std() * np.sqrt(TRADING_DAYS)
    vol_90 = returns.rolling(90).std() * np.sqrt(TRADING_DAYS)
    return vol_30, vol_90 