
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def run_page11():
    st.header("Confirm that Maximum Sharpe Ratio is a Maximum")

    # Load the data (replace with actual loading from file if needed)
    # In the original code, the data is loaded using load BlueChipStockMoments
    # For this streamlit app, let's assume the data is stored as numpy arrays or pandas DataFrames

    # Generate synthetic data (based on BlueChipStockMoments.mat)
    np.random.seed(42)  # for reproducibility
    num_assets = 30
    AssetList = [f'Asset {i+1}' for i in range(num_assets)]
    AssetMean = np.random.rand(num_assets) * 0.2  # Annualized mean returns (e.g., 0 to 20%)
    AssetCovar = np.random.rand(num_assets, num_assets)
    AssetCovar = np.triu(AssetCovar) + AssetCovar.T - np.diag(np.diag(AssetCovar)) #Make symmetric
    AssetCovar = AssetCovar * 0.01 # Scale the covariance matrix
    CashMean = 0.03  # Risk-free rate (e.g., 3%)
    CashVar = 0.0001
    MarketMean = 0.10  # Market mean return (e.g., 10%)
    MarketVar = 0.04

    # Calculate standard deviations
    AssetRisk = np.sqrt(np.diag(AssetCovar))
    MarketRisk = np.sqrt(MarketVar)
    CashRisk = np.sqrt(CashVar)

    # Equal-weighted portfolio
    EqualWeight = np.ones(num_assets) / num_assets
    EqualMean = np.sum(EqualWeight * AssetMean)
    EqualRisk = np.sqrt(EqualWeight @ AssetCovar @ EqualWeight)

    # Portfolio object (Simplified for demonstration)
    class Portfolio:
        def __init__(self, AssetList, RiskFreeRate):
            self.AssetList = AssetList
            self.RiskFreeRate = RiskFreeRate
            self.NumAssets = len(AssetList)

        def setAssetMoments(self, AssetMean, AssetCovar):
            self.AssetMean = AssetMean
            self.AssetCovar = AssetCovar

        def setInitPort(self, initial_weights):
            self.InitPort = initial_weights

        def setDefaultConstraints(self):
            # Long-only, fully invested
            pass  # In a real implementation, add constraint matrices here

    p = Portfolio(AssetList, CashMean)
    p.setAssetMoments(AssetMean, AssetCovar)
    p.setInitPort(np.zeros(num_assets))  # set initial to zero
    p.setDefaultConstraints()

    # Estimate efficient frontier (Simplified)
    def estimateFrontier(p, num_points=20):
        # In a real implementation, this would use an optimization solver
        # Here, we'll generate random portfolios
        weights = np.random.rand(num_points, p.NumAssets)
        weights = weights / np.sum(weights, axis=1, keepdims=True)  # Normalize weights
        return weights

    def estimatePortMoments(p, weights):
        returns = np.sum(weights * p.AssetMean, axis=1)
        risks = np.array([np.sqrt(w @ p.AssetCovar @ w.T) for w in weights])
        return risks, returns

    def estimateMaxSharpeRatio(p):
        # In a real implementation, solve optimization problem to maximize Sharpe Ratio
        weights = np.random.rand(p.NumAssets)
        weights = weights / np.sum(weights)
        return weights

    # Estimate Max Sharpe Ratio
    swgt = estimateMaxSharpeRatio(p)
    srsk, sret = estimatePortMoments(p, swgt)

    weights = estimateFrontier(p, 20)
    risks, returns = estimatePortMoments(p, weights)

    # Calculate Sharpe Ratios
    sharpe_ratios = (returns - p.RiskFreeRate) / risks

    # Create a DataFrame for the efficient frontier
    frontier_data = pd.DataFrame({'Risk': risks, 'Return': returns, 'Sharpe Ratio': sharpe_ratios})

    # Create subplots
    fig = make_subplots(rows=2, cols=1, subplot_titles=("Efficient Frontier", "Sharpe Ratio"))

    # Add efficient frontier plot
    fig.add_trace(go.Scatter(x=frontier_data['Risk'], y=frontier_data['Return'], mode='lines', name='Efficient Frontier'), row=1, col=1)
    fig.add_trace(go.Scatter(x=[srsk], y=[sret], mode='markers', name='Max Sharpe', marker=dict(size=[10]), text=['Sharpe']), row=1, col=1)

    # Add Sharpe Ratio plot
    fig.add_trace(go.Scatter(x=frontier_data['Risk'], y=frontier_data['Sharpe Ratio'], mode='lines', name='Sharpe Ratio'), row=2, col=1)
    fig.add_trace(go.Scatter(x=[srsk], y=[(sret - p.RiskFreeRate) / srsk], mode='markers', name='Max Sharpe', marker=dict(size=[10]), text=['Sharpe']), row=2, col=1)

    # Update layout
    fig.update_layout(title_text="Efficient Frontier and Sharpe Ratio", showlegend=False)
    fig.update_xaxes(title_text="Portfolio Risk", row=1, col=1)
    fig.update_yaxes(title_text="Portfolio Return", row=1, col=1)
    fig.update_xaxes(title_text="Portfolio Risk", row=2, col=1)
    fig.update_yaxes(title_text="Sharpe Ratio", row=2, col=1)

    st.plotly_chart(fig, use_container_width=True)
