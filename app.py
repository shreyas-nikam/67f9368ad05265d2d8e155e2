
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Your code goes here
page = st.sidebar.selectbox(label="Navigation", options=["Efficient Frontier", "Targeted Portfolios", "Transaction Costs", "Turnover Constraint", "Tracking-Error Constraint", "Combined Constraints", "Maximize Sharpe Ratio", "Confirm Sharpe Ratio", "Tangent Portfolio", "Dollar-Neutral Hedge-Fund"])

if page == "Efficient Frontier":
    from application_pages.efficient_frontier import run_efficient_frontier
    run_efficient_frontier()
elif page == "Targeted Portfolios":
    from application_pages.targeted_portfolios import run_targeted_portfolios
    run_targeted_portfolios()
elif page == "Transaction Costs":
    from application_pages.transaction_costs import run_transaction_costs
    run_transaction_costs()
elif page == "Turnover Constraint":
    from application_pages.turnover_constraint import run_turnover_constraint
    run_turnover_constraint()
elif page == "Tracking-Error Constraint":
    from application_pages.tracking_error_constraint import run_tracking_error_constraint
    run_tracking_error_constraint()
elif page == "Combined Constraints":
    from application_pages.combined_constraints import run_combined_constraints
    run_combined_constraints()
elif page == "Maximize Sharpe Ratio":
    from application_pages.maximize_sharpe_ratio import run_maximize_sharpe_ratio
    run_maximize_sharpe_ratio()
elif page == "Confirm Sharpe Ratio":
    from application_pages.confirm_sharpe_ratio import run_confirm_sharpe_ratio
    run_confirm_sharpe_ratio()
elif page == "Tangent Portfolio":
    from application_pages.tangent_portfolio import run_tangent_portfolio
    run_tangent_portfolio()
elif page == "Dollar-Neutral Hedge-Fund":
    from application_pages.dollar_neutral_hedge_fund import run_dollar_neutral_hedge_fund
    run_dollar_neutral_hedge_fund()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
