import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

tickers = ["SPY", "AAPL", "MSFT", "GOOGL", "AMZN"]
data = yf.download(tickers, start="2015-01-01", end="2024-01-01")

returns = np.log(data["Close"] / data["Close"].shift(1))
returns = returns.dropna()

correlation_matrix = returns.corr()
print("Correlation Matrix:\n", correlation_matrix.round(4))

mean_daily_return = returns.mean()
daily_volatility = returns.std()
annual_return = mean_daily_return * 252
annual_volatility = daily_volatility * np.sqrt(252)
sharpe_ratio = annual_return / annual_volatility

skewness = returns.skew()
kurtosis = returns.kurtosis()
VaR_95 = returns.quantile(0.05)
print("\nValue at Risk (95% confidence ):")
print(VaR_95.round(5).to_frame(name="VaR (95%)"))


vol_30 = returns.rolling(30).std() * np.sqrt(252)
vol_90 = returns.rolling(90).std() * np.sqrt(252)

cumulative_returns = (1 + returns).cumprod() 
peak = cumulative_returns.cummax() 
drawdown = (cumulative_returns - peak) / peak
max_drawdown = drawdown.min() 

results = pd.DataFrame({
    "Annual Return": annual_return,
    "Annual Volatility": annual_volatility,
    "Sharpe Ratio": sharpe_ratio,
    "Skewness": skewness,
    "Kurtosis": kurtosis,
    "Max Drawdown": max_drawdown
})

ranking = results.sort_values("Sharpe Ratio", ascending=False)
print("\nSharpe Ratio Ranking:\n", ranking.round(6))


fig, axs = plt.subplots(3, 1, figsize=(8, 7))

axs[0].plot(vol_30)
axs[0].plot(vol_90)
axs[0].set_title("Rolling Volatility")


axs[1].plot(drawdown)
axs[1].set_title("Drawdown Over Time")

axs[2].hist(returns["SPY"], bins=70)
axs[2].set_title("Distribution of Returns")

plt.tight_layout()
plt.show()

