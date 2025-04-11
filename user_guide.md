id: 67f9368ad05265d2d8e155e2_user_guide
summary: Portfolio Optimization Examples Using Financial Toolbox User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Portfolio Optimization and Risk Management Codelab

This codelab guides you through a Streamlit application designed to illustrate key concepts in portfolio optimization and risk management. The application allows you to visualize asset risks and returns, explore the efficient frontier, and identify portfolios that meet specific risk and return targets. Understanding these concepts is crucial for making informed investment decisions and managing portfolio risk effectively.

## Understanding Asset Risks and Returns

Duration: 00:05

This step focuses on the first page of the application, which visualizes the relationship between risk and return for individual assets, the market, cash, and an equally-weighted portfolio. The key concept here is that higher potential returns typically come with higher risk.

1.  **Accessing the Page:** Navigate to "Page 1" in the application.
2.  **Interpreting the Scatter Plot:**  The scatter plot displays assets based on their annualized mean returns (y-axis) and standard deviations (x-axis). Each point represents an asset, with its label indicating the asset's name.
3.  **Analyzing Asset Positions:**  Observe the positions of different assets on the plot. Assets with higher returns and higher risk will be located towards the top right, while those with lower returns and lower risk will be towards the bottom left. Notice where "Market", "Cash", and "Equal" portfolios fall in terms of risk and return.  "Cash" typically has low risk and low return, while the "Market" portfolio aims for higher returns with correspondingly higher risk. The "Equal" weighted portfolio falls somewhere in between, representing a simple diversification strategy.

<aside class="positive">
<b>Tip:</b> Pay close attention to the spread of assets on the plot. A wider spread indicates a greater diversity in risk and return profiles.
</aside>

## Exploring the Efficient Frontier and Tangent Line

Duration: 00:10

This step guides you through the second page, which visualizes the efficient frontier and the tangent line. The efficient frontier represents the set of portfolios that offer the highest expected return for a given level of risk, or the lowest risk for a given level of expected return. The tangent line helps identify the portfolio with the highest Sharpe ratio (risk-adjusted return).

1.  **Accessing the Page:** Navigate to "Page 2" in the application.
2.  **Understanding the Efficient Frontier:**  The curved line on the plot is the efficient frontier. Portfolios on this line are considered "efficient" because they provide the best possible risk-return trade-off.
3.  **Interpreting the Tangent Line:** The straight line that touches the efficient frontier is the tangent line. The point where the tangent line touches the efficient frontier represents the portfolio with the highest Sharpe ratio. This is the portfolio that gives you the most return for the amount of risk you are taking, given the risk-free rate.
4.  **Analyzing Portfolio Positions:**  The plot also shows example positions of "Market", "Cash" and "Equal" weighted portfolios. Notice how these portfolios compare to the efficient frontier. An efficient portfolio will always lie on the efficient frontier, meaning that the "Market","Cash" and "Equal" portfolios as plotted are not efficient.

<aside class="negative">
<b>Warning:</b> Remember that the efficient frontier is based on historical data and assumptions about future returns and risks. Actual results may vary.
</aside>

## Identifying Target Return and Risk Portfolios

Duration: 00:10

This step focuses on the third page, which demonstrates how to identify portfolios that meet specific target return and risk values on the efficient frontier.

1.  **Accessing the Page:** Navigate to "Page 3" in the application.
2.  **Setting Target Values:**  Use the `Target Return (%)` and `Target Risk (%)` input fields to specify your desired portfolio return and risk levels.  For example, you might set a target return of 15% and a target risk of 10%.
3.  **Analyzing Targeted Portfolios:** The plot will display markers indicating the positions of the targeted portfolios based on your input values. Observe where these portfolios fall in relation to the efficient frontier. If a target falls on the efficient frontier, it represents an achievable optimal portfolio based on the data used. If it falls below the frontier, it is not achievable given the risk, and if it falls above the frontier, it may not be optimal.
4. **Experiment with different risk/return values**: Change the values of the target return and risk and see how the position of the green and red dots change.

<aside class="positive">
<b>Tip:</b> This page allows you to explore the feasibility of achieving specific investment goals given the available assets and their risk-return profiles.
</aside>
