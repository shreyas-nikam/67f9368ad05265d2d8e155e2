
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import math

def run_page3():
    st.title("Page 3: Target Return and Risk Portfolios")
    st.markdown("This page shows how to find portfolios that match specified target return and risk values on the efficient frontier.")

    # Simulate data (same as Page 1 & 2)
    AssetList = ['Asset' + str(i) for i in range(1, 31)]
    AssetMean = np.random.rand(30) * 0.2
    AssetCovar = np.random.rand(30, 30) * 0.01
    AssetCovar = np.triu(AssetCovar) + np.triu(AssetCovar, 1).T
    np.fill_diagonal(AssetCovar, np.random.rand(30) * 0.05)

    CashMean = 0.05

    # Portfolio object simulation (same as Page 2)
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

    # Input fields for Target Return and Target Risk
    TargetReturn = st.number_input("Target Return (%)", min_value=0.0, max_value=0.5, value=0.2, step=0.01)
    TargetRisk = st.number_input("Target Risk (%)", min_value=0.0, max_value=0.5, value=0.15, step=0.01)

    # Targeted Portfolios (simulation)
    arsk = TargetRisk / 100
    aret = TargetReturn / 100
    brsk = TargetRisk / 100
    bret = TargetReturn / 100

    # Create the plot
    fig = go.Figure()

    # Efficient Frontier line
    fig.add_trace(go.Scatter(x=prsk, y=pret, mode='lines', name='Efficient Frontier'))

    # Target Return Portfolio
    fig.add_trace(go.Scatter(x=[arsk], y=[aret], mode='markers', name=f'{TargetReturn}% Return',
                             marker=dict(size=10, color='green')))

    # Target Risk Portfolio
    fig.add_trace(go.Scatter(x=[brsk], y=[bret], mode='markers', name=f'{TargetRisk}% Risk',
                             marker=dict(size=10, color='red')))

    fig.update_layout(title='Efficient Frontier with Targeted Portfolios',
                      xaxis_title='Portfolio Risk',
                      yaxis_title='Portfolio Return')

    st.plotly_chart(fig, use_container_width=True)

run_page3()
