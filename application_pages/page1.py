
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import math

def run_page1():
    st.title("Page 1: Asset Risks and Returns")
    st.markdown("This page visualizes the annualized mean returns and standard deviations of individual assets, along with the market, cash, and equal-weighted portfolios.")

    # Simulate data from BlueChipStockMoments.mat
    AssetList = ['Asset' + str(i) for i in range(1, 31)]
    AssetMean = np.random.rand(30) * 0.2  # Random means between 0 and 0.2
    AssetCovar = np.random.rand(30, 30) * 0.01 # Random covariances
    AssetCovar = np.triu(AssetCovar) + np.triu(AssetCovar, 1).T # Make it symmetric
    np.fill_diagonal(AssetCovar, np.random.rand(30) * 0.05) # Ensure diagonal is non-zero

    CashMean = 0.05
    CashVar = 0.0001
    MarketMean = 0.12
    MarketVar = 0.02

    # Calculate standard deviations
    AssetStd = np.sqrt(np.diag(AssetCovar))
    MarketStd = math.sqrt(MarketVar)
    CashStd = math.sqrt(CashVar)

    # Equal-weighted portfolio (assuming equal weight on assets only)
    EqualWeight = np.array([1/30] * 30)
    EqualMean = np.sum(EqualWeight * AssetMean)
    EqualCovar = np.dot(EqualWeight.T, np.dot(AssetCovar, EqualWeight))
    EqualStd = math.sqrt(EqualCovar)


    # Create DataFrame for the plot
    data = pd.DataFrame({
        'Return': AssetMean,
        'Risk': AssetStd,
        'Asset': AssetList
    })

    # Add market, cash, and equal-weighted portfolios
    data = data.append({
        'Return': MarketMean,
        'Risk': MarketStd,
        'Asset': 'Market'
    }, ignore_index=True)
    data = data.append({
        'Return': CashMean,
        'Risk': CashStd,
        'Asset': 'Cash'
    }, ignore_index=True)
    data = data.append({
        'Return': EqualMean,
        'Risk': EqualStd,
        'Asset': 'Equal'
    }, ignore_index=True)

    # Create scatter plot using Plotly
    fig = px.scatter(data, x='Risk', y='Return', text='Asset', title='Asset Risks and Returns')
    fig.update_traces(textposition='top center')
    st.plotly_chart(fig, use_container_width=True)

run_page1()
