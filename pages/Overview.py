import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.title("Overview and Data Setup")
st.markdown("""
This page provides an overview of portfolio optimization techniques.
Synthetic data simulating BlueChipStockMoments is generated and visualized.
""")

# Generate synthetic data for demonstration:
np.random.seed(42)
num_assets = 30
AssetList = [f"Asset {i+1}" for i in range(num_assets)]
AssetMean = np.random.uniform(0.05, 0.15, num_assets)
AssetCovar = np.random.uniform(0.01, 0.05, (num_assets, num_assets))
AssetCovar = (AssetCovar + AssetCovar.T) / 2  # symmetrize
np.fill_diagonal(AssetCovar, np.random.uniform(0.02, 0.06, num_assets))

mrsk = np.sqrt(np.diag(AssetCovar))
mret = AssetMean

df = pd.DataFrame({"Asset": AssetList, "Return": mret, "Risk": mrsk})
fig = px.scatter(df, x="Risk", y="Return", text="Asset", title="Asset Risks vs Returns")
st.plotly_chart(fig, use_container_width=True)
