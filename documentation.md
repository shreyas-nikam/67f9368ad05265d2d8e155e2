id: 67f9368ad05265d2d8e155e2_documentation
summary: Portfolio Optimization Examples Using Financial Toolbox Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Streamlit Portfolio Optimization Codelab

This codelab guides you through a Streamlit application designed to visualize key concepts in portfolio optimization.  We'll explore asset risks and returns, the efficient frontier, and how to target specific risk and return profiles. This application is valuable for understanding Modern Portfolio Theory (MPT) and its practical implications.  The application provides interactive visualizations that make these concepts more accessible.

## Application Overview
Duration: 00:05

This Streamlit application consists of three pages, each focusing on a different aspect of portfolio optimization:

*   **Page 1: Asset Risks and Returns:**  Visualizes the annualized mean returns and standard deviations of individual assets, along with market, cash, and equal-weighted portfolios.
*   **Page 2: Efficient Frontier and Tangent Line:** Illustrates the efficient frontier, the tangent line originating from the risk-free rate (cash), and key portfolio characteristics.
*   **Page 3: Target Return and Risk Portfolios:** Demonstrates how to find portfolios that match specified target return and risk values on the efficient frontier.

The application uses simulated data to represent asset characteristics, allowing you to explore the relationships between risk and return in a portfolio context.  The visualizations are created using Plotly, providing interactive and informative charts.

## Setting up the Application
Duration: 00:10

To run this application, you'll need Python and the following libraries:

*   Streamlit
*   Pandas
*   NumPy
*   Plotly

You can install these libraries using pip:

```console
pip install streamlit pandas numpy plotly
```

The application is structured as follows:

*   `application_pages/page1.py`: Contains the code for Page 1.
*   `application_pages/page2.py`: Contains the code for Page 2.
*   `application_pages/page3.py`: Contains the code for Page 3.

To run the application, you'll need a main script (e.g., `main.py`) that imports and calls the `run_pageX()` functions from each page. Since a main script has not been provided, you can run each page separately using the streamlit run command. For example, to run `page1.py`:

```console
streamlit run application_pages/page1.py
```
You can run each page individually to explore its functionality.

## Page 1: Asset Risks and Returns
Duration: 00:15

This page displays a scatter plot of asset risks (standard deviations) versus their annualized mean returns.  It helps visualize the risk-return profile of individual assets and how they compare to the market, cash, and an equal-weighted portfolio.

**Key Concepts:**

*   **Annualized Mean Return:**  The average return of an asset over a year.
*   **Standard Deviation:** A measure of the volatility or risk of an asset.  Higher standard deviation indicates higher risk.
*   **Market Portfolio:**  Represents a broad market index, such as the S\&P 500.
*   **Cash:** Represents a risk-free asset, such as a Treasury bill.
*   **Equal-Weighted Portfolio:** A portfolio where each asset has the same weight (e.g., if there are 30 assets, each has a weight of 1/30).

**Code Explanation:**

```python
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
```

1.  **Data Simulation:**  The code simulates asset means, covariances, market mean/variance, and cash mean/variance.  This is done using `np.random.rand()` to generate random numbers. Note that ideally, this data would be pulled from an external data source or calculated using historical data.
2.  **Standard Deviation Calculation:** The standard deviation (risk) is calculated as the square root of the variance or the diagonal elements of the covariance matrix.
3.  **Equal-Weighted Portfolio Calculation:** The mean and variance (and therefore standard deviation) of the equal-weighted portfolio are calculated based on the simulated asset means and covariances.
4.  **DataFrame Creation:** A Pandas DataFrame is created to store the returns, risks, and names of each asset, the market, cash, and the equal-weighted portfolio.
5.  **Plotly Scatter Plot:**  A scatter plot is created using `plotly.express` to visualize the risk-return relationship. The `text` argument is used to display the asset names on the plot.
6.  **Streamlit Integration:** The plot is displayed in the Streamlit application using `st.plotly_chart()`.

## Page 2: Efficient Frontier and Tangent Line
Duration: 00:20

This page visualizes the efficient frontier and the tangent line (Capital Allocation Line) originating from the risk-free rate (cash). The efficient frontier represents the set of portfolios that offer the highest expected return for a given level of risk, or the lowest risk for a given level of return. The tangent line represents the optimal allocation between the risk-free asset and the tangency portfolio (the portfolio on the efficient frontier with the highest Sharpe ratio).

**Key Concepts:**

*   **Efficient Frontier:**  The set of optimal portfolios that offer the highest expected return for a defined level of risk or the lowest risk for a given level of expected return.
*   **Tangent Line (Capital Allocation Line):**  A line tangent to the efficient frontier at the tangency portfolio. It represents the optimal combinations of the risk-free asset and the tangency portfolio.
*   **Risk-Free Rate:**  The return on a risk-free asset, such as a Treasury bill (represented here by `CashMean`).
*   **Sharpe Ratio:** A measure of risk-adjusted return, calculated as (Portfolio Return - Risk-Free Rate) / Portfolio Standard Deviation. The tangency portfolio has the highest Sharpe Ratio of all possible portfolios.

**Code Explanation:**

```python
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
```

1.  **Data Simulation:**  Similar to Page 1, asset means and covariances are simulated.  The `CashMean` (risk-free rate) is also defined.
2.  **Portfolio Class:** A `Portfolio` class is defined.  While the methods are defined, they largely do not contain any implementation.  This is a simplification for the purpose of the visualization. In a real-world application, this class would contain the logic for portfolio optimization.
3.  **Efficient Frontier Simulation:**  The code simulates points on the efficient frontier by generating a range of risk and return values.  In a real application, these points would be calculated using an optimization algorithm.
4.  **Tangent Line Simulation:**  The tangent line is simulated using the formula:  `qret = CashMean + (qrsk - 0) * (pret[-1] - CashMean) / prsk[-1]`. This formula calculates the return for a given level of risk along the tangent line, given the risk-free rate and the coordinates of the tangency portfolio.
5.  **Plotly Plot:**  A Plotly line chart is created to display the efficient frontier and the tangent line. Scatter markers are used to represent example portfolios.

## Page 3: Target Return and Risk Portfolios
Duration: 00:20

This page allows you to specify target return and risk values and visualizes portfolios that match those targets on the efficient frontier. This demonstrates how an investor can use the efficient frontier to select a portfolio that meets their specific investment goals.

**Key Concepts:**

*   **Target Return:**  The desired return on an investment portfolio.
*   **Target Risk:**  The acceptable level of risk for an investment portfolio.
*   **Portfolio Selection:** The process of choosing the optimal mix of assets to achieve the desired risk and return profile.

**Code Explanation:**

```python
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
```

1.  **Data Simulation and Portfolio Class:**  As in the previous pages, the code simulates asset data and defines a `Portfolio` class (again, with simplified implementations).
2.  **Efficient Frontier Simulation:**  The efficient frontier is simulated as before.
3.  **Streamlit Input Fields:**  Streamlit's `st.number_input()` function is used to create input fields for the user to specify their target return and target risk.
4.  **Targeted Portfolios (Simulation):** The code calculates the x and y coordinates of the targeted portfolios based on user inputs. In a real-world scenario, finding a portfolio for a specific target might require optimization algorithms, especially if the target falls outside the simulated efficient frontier.
5.  **Plotly Plot:**  A Plotly chart is created to display the efficient frontier, along with markers indicating the target return and target risk portfolios.

## Further Exploration
Duration: 00:05

This codelab provides a basic framework for understanding portfolio optimization concepts using Streamlit.  To further explore this topic, consider the following:

*   **Real-World Data:** Replace the simulated data with real-world stock data from sources like Yahoo Finance or IEX Cloud.
*   **Optimization Algorithms:** Implement optimization algorithms (e.g., quadratic programming) to calculate the efficient frontier and optimal portfolio weights.
*   **Constraints:** Add constraints to the portfolio optimization process, such as sector limits or ESG (Environmental, Social, and Governance) criteria.
*   **Transaction Costs:** Incorporate transaction costs into the optimization process to make it more realistic.
*   **Backtesting:**  Backtest the performance of different portfolio strategies using historical data.
*   **More Robust Portfolio Class:** Implement the methods in the `Portfolio` class to appropriately handle constraints and other aspects of portfolio optimization.

By expanding on this foundation, you can create a more sophisticated and practical portfolio optimization application.
