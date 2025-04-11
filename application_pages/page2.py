
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math

def run_page2():
    st.title("Page 2: Efficient Frontier and Tangent Line")
    st.markdown("This page illustrates the efficient frontier, the tangent line originating from the risk-free rate, and key portfolio characteristics.")

    # Simulate data (same as Page 1)
    AssetList = ['Asset' + str(i) for i in range(1, 31)]
    AssetMean = np.random.rand(30) * 0.2
    AssetCovar = np.random.rand(30, 30) * 0.01
    AssetCovar = np.triu(AssetCovar) + np.triu(AssetCovar, 1).T
    np.fill_diagonal(AssetCovar, np.random.rand(30) * 0.05)

    CashMean = 0.05
    CashVar = 0.0001

    # Portfolio object simulation
    class Portfolio:
        def __init__(self, AssetList, RiskFreeRate):
            self.AssetList = AssetList
            self.RiskFreeRate = RiskFreeRate
            self.NumAssets = len(AssetList)
            self.InitPort = None  # Initial portfolio weights
            self.AssetMean = None
            self.AssetCovar = None
            self.Bounds = None
        def setAssetMoments(self, AssetMean, AssetCovar):
            self.AssetMean = AssetMean
            self.AssetCovar = AssetCovar
        def setInitPort(self, InitPort):
            self.InitPort = InitPort
        def setDefaultConstraints(self):
            # Long-only, fully invested
            self.Bounds = [(0, None) for _ in range(self.NumAssets)]  # Non-negative weights
        def setBudget(self, min_budget, max_budget):
            pass
        def setCosts(self, BuyCost, SellCost):
            pass
        def setTurnover(self, Turnover):
            pass
        def setTrackingError (self, TrackingError, TrackingPort):
            pass
        def setBounds(self, minBound, maxBound):
            pass
        def setOnewayTurnover(self, Turnover, InitPort):
            pass

    p = Portfolio(AssetList, CashMean)
    p.setAssetMoments(AssetMean, AssetCovar)
    p.setInitPort(np.array([1/30] * 30))
    p.setDefaultConstraints()

    # Efficient Frontier Simulation
    num_portfolios = 20
    prsk = np.linspace(0.05, 0.2, num_portfolios)  # Example risk values
    pret = np.linspace(0.07, 0.25, num_portfolios) # Example return values

    # Tangent Line Simulation
    qrsk = np.linspace(0.05, 0.15, num_portfolios) # Example tangent risk values
    qret = CashMean + (qrsk - 0) * (pret[-1] - CashMean) / prsk[-1] # Tangent line

    # Create the plot
    fig = go.Figure()

    # Efficient Frontier line
    fig.add_trace(go.Scatter(x=prsk, y=pret, mode='lines', name='Efficient Frontier'))

    # Tangent Line
    fig.add_trace(go.Scatter(x=qrsk, y=qret, mode='lines', name='Tangent Line'))

    # Market, Cash, Equal Scatter (simulated)
    fig.add_trace(go.Scatter(x=[0.14, 0.01, 0.1], y=[0.15, CashMean, 0.12], mode='markers', name='Portfolios',
                             marker=dict(size=8)))

    fig.update_layout(title='Efficient Frontier with Tangent Line',
                      xaxis_title='Portfolio Risk',
                      yaxis_title='Portfolio Return')

    st.plotly_chart(fig, use_container_width=True)

run_page2()
