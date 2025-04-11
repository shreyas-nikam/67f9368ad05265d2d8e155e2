
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def run_page12():
    st.header("Illustrate that Sharpe is the Tangent Portfolio")

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

        def setBudget(self, min_cash, max_cash):
            self.min_cash = min_cash
            self.max_cash = max_cash


    p = Portfolio(AssetList, CashMean)
    p.setAssetMoments(AssetMean, AssetCovar)
    p.setInitPort(np.zeros(num_assets))
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

    # Tangent Line
    q = Portfolio(AssetList, CashMean)
    q.setAssetMoments(AssetMean, AssetCovar)
    q.setBudget(0, 1)  # Budget constraint
    qwgt = estimateFrontier(q, 20)
    qrsk, qret = estimatePortMoments(q, qwgt)

    weights = estimateFrontier(p, 20)
    risks, returns = estimatePortMoments(p, weights)

    # Estimate Max Sharpe Ratio
    swgt = estimateMaxSharpeRatio(p)
    srsk, sret = estimatePortMoments(p, swgt)


    # Create a DataFrame for the efficient frontier
    frontier_data = pd.DataFrame({'Risk': risks, 'Return': returns})

    # Create a DataFrame for the tangent efficient frontier
    tangent_frontier_data = pd.DataFrame({'Risk': qrsk, 'Return': qret})


    # Create the plot
    fig = px.line(frontier_data, x='Risk', y='Return', title='Efficient Frontier with Maximum Sharpe Ratio Portfolio and Tangent Portfolio',
                  labels={'Return': 'Annualized Return', 'Risk': 'Annualized Risk'})

    fig.add_trace(go.Scatter(x=tangent_frontier_data['Risk'], y=tangent_frontier_data['Return'], mode='lines', name='Tangent Frontier'))

    fig.add_trace(go.Scatter(x=[srsk], y=[sret],
                             mode='markers', name='Sharpe',
                             marker=dict(size=[10]),
                             text=['Sharpe']))

    fig.add_trace(go.Scatter(x=[MarketRisk, CashRisk, EqualRisk], y=[MarketMean, CashMean, EqualMean],
                             mode='markers', name='Markers',
                             marker=dict(size=[10, 10, 10]),
                             text=['Market', 'Cash', 'Equal']))

    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)
