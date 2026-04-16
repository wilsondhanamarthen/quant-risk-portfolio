from data import get_prices, get_returns
from metrics import compute_metrics, compute_rolling_vol
from strategy import momentum_backtest, minimum_variance_portfolio
from visualizations import (
    plot_rolling_volatility,
    plot_drawdown,
    plot_cumulative_returns,
    plot_return_distribution,
    plot_correlation_heatmap,
    plot_sharpe_ranking,
    plot_momentum_strategy,
    plot_min_variance_weights
)

def main():
    print("📈 Stock Risk Profiler")
    print("=" * 45)

    prices = get_prices()
    returns = get_returns(prices)

    results, drawdown, cumulative = compute_metrics(returns)
    vol_30, vol_90 = compute_rolling_vol(returns)

    buy_hold, momentum, mom_summary = momentum_backtest(returns)
    print("\n--- Momentum Strategy vs Buy & Hold ---")
    print(mom_summary.round(4).to_string())

    weights, min_vol, port_cumulative, weight_summary = minimum_variance_portfolio(returns)
    print("\n--- Minimum Variance Portfolio ---")
    print(f"Minimum Volatility: {min_vol:.4f}")
    print(weight_summary.to_string())

    print("\n--- Risk & Performance Summary ---")
    print(results.round(4).to_string())
    print("\n--- Sharpe Ratio Ranking ---")
    print(results["Sharpe Ratio"].sort_values(ascending=False).round(4))

    print("\nGenerating interactive charts...")
    plot_correlation_heatmap(returns)
    plot_cumulative_returns(cumulative)
    plot_rolling_volatility(vol_30, vol_90)
    plot_drawdown(drawdown)
    plot_return_distribution(returns)
    plot_sharpe_ranking(results)
    plot_momentum_strategy(buy_hold, momentum)
    plot_min_variance_weights(weights)

    print("\n✅ All charts saved as .html files!")
    print("💡 Open them in your browser to interact!")
    print(results.round(4)) 

if __name__ == "__main__":
    main()
