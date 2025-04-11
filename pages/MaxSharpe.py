import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Maximum Sharpe Ratio Portfolio")
st.markdown("""
This page demonstrates the portfolio that maximizes the Sharpe ratio.
""")
# Dummy data for Maximum Sharpe portfolio:
max_sharpe_risk = 0.15
max_sharpe_return = 0.13
risks = np.linspace(0.05, 0.30, 50)
returns = 0.1 + 0.5 * risks

fig = go.Figure()
fig.add_trace(go.Scatter(x=risks, y=returns, mode='lines', name='Efficient Frontier'))
fig.add_trace(go.Scatter(x=[max_sharpe_risk], y=[max_sharpe_return], mode='markers', marker=dict(size=10, color='green'), name='Max Sharpe Portfolio'))
fig.update_layout(title="Maximum Sharpe Ratio Portfolio", xaxis_title="Risk", yaxis_title="Return")
st.plotly_chart(fig, use_container_width=True)
st.write(f"Maximum Sharpe Portfolio -> Risk: {max_sharpe_risk:.2f}, Return: {max_sharpe_return:.2f}")
