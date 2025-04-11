
# Technical Specifications for Financial Toolbox Portfolio Optimization Streamlit Application

## Overview

This Streamlit application implements the portfolio optimization examples provided in the MATLAB Financial Toolbox documentation.  It allows users to interactively explore portfolio construction concepts such as efficient frontiers, Sharpe ratio maximization, and the impact of constraints.  The application uses synthetic data, mimicking the `BlueChipStockMoments.mat` dataset, and translates the MATLAB code into Python using Streamlit for the user interface and Matplotlib for visualization (adapted for Streamlit display).

## Step-by-Step Generation Process

1.  **Data Loading and Preparation:**
    *   Load the synthetic data from the attached file (`BlueChipStockMoments.mat`).  Since we are using python and not matlab, we will use `numpy` arrays. This data should include:
        *   `AssetList`: A list of asset identifiers (e.g., stock tickers).
        *   `AssetMean`: A numpy array of asset mean returns.
        *   `AssetCovar`: A numpy array of the asset covariance matrix.
        *   `CashMean`: The mean return of the risk-free asset (cash).
        *   `CashVar`: The variance of the risk-free asset (cash).
        *   `MarketMean`: The mean return of the market portfolio.
        *   `MarketVar`: The variance of the market portfolio.
    *   Convert the cash and market variances to standard deviations.

2.  **Portfolio Object Creation:**
    *   Create a `Portfolio` class (or leverage a similar existing library, see below).
    *   Instantiate the `Portfolio` object, passing in the `AssetList`, risk-free rate (`CashMean`), `AssetMean`, and `AssetCovar`.
    *   Implement the `setAssetMoments` method to associate asset moments to the object.
    *   Implement the `setInitPort` method to define an initial portfolio with equal weights for all assets.

3.  **Setting Up the Optimization Problem:**
    *   Implement the `setDefaultConstraints` method to define default portfolio constraints:
        *   Fully invested: Portfolio weights must sum to 1.
        *   Long-only:  Portfolio weights must be non-negative.

4.  **Tangent Line Illustration:**
    *   Implement the `setBudget` method, allowing allocation between a riskless asset (cash) and a risky portfolio (efficient frontier).
    *   Use `estimateFrontier` to calculate efficient portfolios for allocations between 0% and 100% in cash.
    *   Calculate the efficient frontier and tangent line.

5.  **Obtaining Range of Risks and Returns:**
    *   Implement the `estimateFrontierLimits` method to determine the minimum and maximum risk and return values on the efficient frontier.

6.  **Finding Targeted Portfolios:**
    *   Implement the `estimateFrontierByReturn` method to find a portfolio with a specified target return.
    *   Implement the `estimateFrontierByRisk` method to find a portfolio with a specified target risk.

7.  **Transaction Costs:**
    *   Implement the `setCosts` method to incorporate transaction costs (buy and sell costs) into the optimization problem.
    *   Re-calculate the efficient frontier considering transaction costs.

8.  **Turnover & Tracking-Error Constraints:**
    *   Implement `setTurnover` and `setTrackingError` methods.
    *   `setTurnover` limits total buys and sells to a specified amount.
    *   `setTrackingError` limits the portfolio's deviation from a benchmark (tracking) portfolio.
    *   Re-calculate the efficient frontier with turnover and tracking-error constraints.

9.  **Sharpe Ratio Maximization:**
    *   Implement the `estimateMaxSharpeRatio` method to find the portfolio with the maximum Sharpe ratio.
    *   Calculate the efficient frontier with the maximum Sharpe ratio portfolio.

10. **Dollar-Neutral Hedge-Fund Structure:**
    *   Implement the `setBounds` method to define the maximum exposure in long and short positions.
    *   Implement the `setBudget` to set net portfolio position to zero.
    *   Implement the `setOnewayTurnover` to prevent double-counting of long and short positions.
    *   Calculate and visualize the efficient frontier for the dollar-neutral strategy.

11. **Visualization**:
    *   Adapt all the visualizations present in the MATLAB code to Streamlit using `matplotlib` and `st.pyplot`.  The plots should accurately represent asset risks/returns scatter plot, efficient frontier plots (with/without constraints), and Sharpe ratio visualizations.

## Important Definitions, Examples, and Formulae

*   **Return:** The profit or loss on an investment over a period, typically expressed as a percentage of the initial investment.
    *   Formula: `Return = (Ending Value - Beginning Value) / Beginning Value`
*   **Risk:** The uncertainty associated with an investment's returns, often measured by standard deviation or variance.
    *   **Standard Deviation (σ):** Measures the dispersion of returns around the mean. A higher standard deviation indicates greater risk.
        *   Formula:  `σ = sqrt(Variance)`
    *   **Variance (σ²):**  The average of the squared differences from the mean.
        *   Formula: `σ² = Σ(Return_i - Mean Return)² / N`, where N is the number of data points.
*   **Efficient Frontier:** The set of portfolios that offer the highest expected return for a given level of risk, or the lowest risk for a given level of expected return.
*   **Sharpe Ratio:**  A measure of risk-adjusted return, calculated as the excess return (return above the risk-free rate) divided by the portfolio's standard deviation.
    *   Formula: `Sharpe Ratio = (Portfolio Return - Risk-Free Rate) / Portfolio Standard Deviation`
*   **Risk-Free Rate:** The return on an investment with zero risk, often proxied by the return on government bonds.
*   **Covariance:** Measures how two assets move together. A positive covariance means they tend to move in the same direction, while a negative covariance means they move in opposite directions.
    *   Formula: `Cov(X, Y) = Σ[(X_i - Mean(X)) * (Y_i - Mean(Y))] / (N - 1)`
*   **Portfolio Weights:** The proportion of the total investment allocated to each asset in the portfolio.
*   **Budget Constraint:**  The constraint that the sum of the portfolio weights must equal 1 (or 100%).  Representing full investment of the capital.
    *   Formula: `Σ Weight_i = 1`
*   **Long-Only Constraint:** The constraint that portfolio weights must be non-negative, meaning that short selling is not allowed.
    *   Formula: `Weight_i >= 0`
*   **Fully Invested Constraint:** The sum of all assets is equal to the total capital available.
*   **Turnover Constraint:**  A limit on the amount of trading activity allowed in a portfolio over a period, typically expressed as a percentage of the total portfolio value.  Limits both purchases and sales.
*   **Tracking Error:** The difference between a portfolio's returns and the returns of a benchmark index.
*   **Tracking-Error Constraint:** A limit on the amount of tracking error allowed in a portfolio.
*   **Dollar-Neutral Portfolio:**  A portfolio with equal long and short positions, resulting in a net exposure of zero.
    *   `Sum of Long Positions = Sum of Short Positions`
*   **Leverage:** The use of borrowed capital to increase the potential return of an investment.
*   **Tobin's Separation Theorem (Two Fund Theorem):**  Investors can achieve their optimal portfolio allocation by combining a risk-free asset with a single risky portfolio (the tangency portfolio).

## Libraries and Tools

*   **Streamlit:**  The primary framework for building the interactive web application.  It's used for:
    *   Creating the user interface (UI) with input widgets (e.g., sliders, text boxes) for user-defined parameters.
    *   Displaying visualizations, text, and data tables.
    *   Managing the application's state (e.g., storing user inputs).
    *   Example use in the code: `st.slider()`, `st.pyplot()`, `st.write()`
*   **NumPy:** A fundamental library for numerical computing in Python.  It's used for:
    *   Storing and manipulating numerical data (e.g., asset returns, covariance matrix) in arrays.
    *   Performing mathematical operations on arrays.
    *   Example use in the code: `numpy.array()`, `numpy.mean()`, `numpy.sqrt()`
*   **Matplotlib:**  A library for creating static, interactive, and animated visualizations in Python.  It's used for:
    *   Generating the plots of the efficient frontier, asset risks and returns, and Sharpe ratio.
    *   Customizing plot appearance (e.g., titles, labels, colors).
    *   Example use in the code: `matplotlib.pyplot.plot()`, `matplotlib.pyplot.scatter()`, `matplotlib.pyplot.title()`.  The output is then passed to `st.pyplot()` to display within the Streamlit app.
*   **Pandas (Potentially):** While not explicitly required by the instructions, pandas could be useful for:
    *   Data manipulation and analysis, particularly for loading and working with the data in a tabular format.
    *   Creating dataframes for displaying portfolio weights and asset information.


Generate complete code. Use proper optimization solvers. Do not generate or simulate random results.