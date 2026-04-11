import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

COLORS = ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A"]

def plot_rolling_volatility(vol_30, vol_90):
    fig = make_subplots(rows=1, cols=1)
    for i, col in enumerate(vol_30.columns):
        fig.add_trace(go.Scatter(
            x=vol_30.index, y=vol_30[col],
            name=f"{col} 30d",
            line=dict(color=COLORS[i], width=1.5)
        ))
        fig.add_trace(go.Scatter(
            x=vol_90.index, y=vol_90[col],
            name=f"{col} 90d",
            line=dict(color=COLORS[i], width=1.5, dash="dash")
        ))
    fig.update_layout(
        title="Rolling Annualized Volatility",
        xaxis_title="Date",
        yaxis_title="Volatility",
        hovermode="x unified",
        template="plotly_dark",
        height=500
    )
    fig.write_html("rolling_volatility.html")
    fig.show()

def plot_drawdown(drawdown):
    fig = go.Figure()
    for i, col in enumerate(drawdown.columns):
        fig.add_trace(go.Scatter(
            x=drawdown.index, y=drawdown[col],
            name=col,
            line=dict(color=COLORS[i], width=1.5),
            fill="tozeroy"
        ))
    fig.update_layout(
        title="Drawdown Over Time",
        xaxis_title="Date",
        yaxis_title="Drawdown",
        hovermode="x unified",
        template="plotly_dark",
        height=500
    )
    fig.write_html("drawdown.html")
    fig.show()

def plot_cumulative_returns(cumulative):
    fig = px.line(
        cumulative,
        title="Cumulative Returns (2015-2024)",
        labels={"value": "Growth of $1", "variable": "Ticker"},
        color_discrete_sequence=COLORS,
        template="plotly_dark"
    )
    fig.update_layout(hovermode="x unified", height=500)
    fig.write_html("cumulative_returns.html")
    fig.show()

def plot_return_distribution(returns):
    fig = make_subplots(
        rows=1, cols=len(returns.columns),
        subplot_titles=list(returns.columns)
    )
    for i, col in enumerate(returns.columns):
        fig.add_trace(
            go.Histogram(
                x=returns[col],
                nbinsx=70,
                name=col,
                marker_color=COLORS[i],
                opacity=0.75
            ),
            row=1, col=i+1
        )
    fig.update_layout(
        title="Return Distributions",
        template="plotly_dark",
        showlegend=False,
        height=400
    )
    fig.write_html("return_distributions.html")
    fig.show()

def plot_correlation_heatmap(returns):
    corr = returns.corr().round(2)
    fig = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns.tolist(),
        y=corr.index.tolist(),
        colorscale="RdBu",
        zmid=0,
        text=corr.values,
        texttemplate="%{text}",
        hovertemplate="x: %{x}<br>y: %{y}<br>corr: %{z}<extra></extra>"
    ))
    fig.update_layout(
        title="Correlation Heatmap",
        template="plotly_dark",
        height=500
    )
    fig.write_html("correlation_heatmap.html")
    fig.show()

def plot_sharpe_ranking(results):
    ranking = results["Sharpe Ratio"].sort_values(ascending=True)
    fig = go.Figure(go.Bar(
        x=ranking.values,
        y=ranking.index,
        orientation="h",
        marker_color=COLORS,
        text=ranking.round(3).values,
        textposition="outside"
    ))
    fig.update_layout(
        title="Sharpe Ratio Ranking",
        xaxis_title="Sharpe Ratio",
        template="plotly_dark",
        height=400
    )
    fig.write_html("sharpe_ranking.html")
    fig.show()

def plot_momentum_strategy(buy_hold, momentum):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=buy_hold.index, y=buy_hold,
        name="Buy & Hold SPY",
        line=dict(color="#636EFA", width=2)
    ))
    fig.add_trace(go.Scatter(
        x=momentum.index, y=momentum,
        name="Momentum Strategy",
        line=dict(color="#00CC96", width=2)
    ))
    fig.update_layout(
        title="Momentum Strategy vs Buy & Hold SPY",
        xaxis_title="Date",
        yaxis_title="Growth of $1",
        hovermode="x unified",
        template="plotly_dark",
        height=500
    )
    fig.write_html("momentum_strategy.html")
    fig.show()

def plot_min_variance_weights(weights):
    fig = go.Figure(go.Bar(
        x=weights.index,
        y=weights.values * 100,
        marker_color=COLORS,
        text=[f"{w*100:.1f}%" for w in weights.values],
        textposition="outside"
    ))
    fig.update_layout(
        title="Minimum Variance Portfolio — Optimal Weights",
        xaxis_title="Asset",
        yaxis_title="Weight (%)",
        template="plotly_dark",
        height=400
    )
    fig.write_html("min_variance_weights.html")
    fig.show()