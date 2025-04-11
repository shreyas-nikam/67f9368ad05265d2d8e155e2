import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Target Portfolio Optimization")
st.markdown("""
Adjust target return and target risk parameters to identify and highlight the nearest portfolio on the efficient frontier.
""")
target_return = st.number_input("Target Return (annualized)", min_value=0.0, value=0.12, step=0.01)
target_risk = st.number_input("Target Risk (annualized standard deviation)", min_value=0.0, value=0.18, step=0.01)

# Dummy efficient frontier:
risks = np.linspace(0.05, 0.30, 50)
returns = 0.1 + 0.5 * risks

# Identify the portfolio on the frontier nearest to the user's target:
dist = np.sqrt((returns - target_return)**2 + (risks - target_risk)**2)
idx = np.argmin(dist)
portfolio_risk = risks[idx]
portfolio_return = returns[idx]

fig = go.Figure()
fig.add_trace(go.Scatter(x=risks, y=returns, mode='lines', name='Efficient Frontier'))
fig.add_trace(go.Scatter(x=[portfolio_risk], y=[portfolio_return], mode='markers', marker=dict(size=10, color='red'), name='Target Portfolio'))
fig.update_layout(title="Efficient Frontier with Target Portfolio", xaxis_title="Risk", yaxis_title="Return")
st.plotly_chart(fig, use_container_width=True)
st.write(f"Target portfolio risk: {portfolio_risk:.2f}, return: {portfolio_return:.2f}")
