import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Transaction Costs Impact")
st.markdown("""
Modify transaction cost parameters to see their impact on the efficient frontier.
""")
buy_cost = st.number_input("Buy Cost", min_value=0.0, value=0.002, step=0.0005)
sell_cost = st.number_input("Sell Cost", min_value=0.0, value=0.002, step=0.0005)

# Dummy frontier data with transaction cost impact:
risks = np.linspace(0.05, 0.30, 50)
# Assume that transaction costs reduce returns linearly:
returns = 0.1 + 0.5 * risks - (buy_cost + sell_cost) * 10

fig = go.Figure()
fig.add_trace(go.Scatter(x=risks, y=returns, mode='lines', name='Frontier with Transaction Costs'))
fig.update_layout(title="Efficient Frontier with Transaction Costs", xaxis_title="Risk", yaxis_title="Return")
st.plotly_chart(fig, use_container_width=True)
