id: 67f9368ad05265d2d8e155e2_documentation
summary: Portfolio Optimization Examples Using Financial Toolbox Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab Codelab: Exploring Portfolio Optimization with Streamlit

This codelab guides you through the QuLab Streamlit application, a tool designed to illustrate key concepts in portfolio optimization. Understanding these concepts is crucial for any developer working in finance or investment management.  QuLab allows users to visualize and interact with efficient frontiers, explore the impact of various constraints, and understand the properties of portfolios with maximum Sharpe ratios. This codelab will cover each of the application's pages in detail. The sample data provided allows the user to explore the functionalities of this application without any setup.

## Setting Up Your Environment (Optional)
Duration: 00:05

This step is optional if you just want to understand the code.  If you wish to run the application locally, ensure you have Python installed. Then, install the necessary libraries using pip:

```bash
pip install streamlit numpy pandas plotly
```

## Understanding the `app.py` Structure
Duration: 00:05

The `app.py` file serves as the main entry point for the Streamlit application. It handles the overall layout, navigation, and page routing.

```python
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Your code goes here
page = st.sidebar.selectbox(label="Navigation", options=[
    "Asset Risks and Returns",
    "Efficient Frontier",
    "Efficient Frontier with Tangent Line",
    "Range of Risks and Returns",
    "Efficient Frontier with Targeted Portfolios",
    "Transactions Costs",
    "Turnover Constraint",
    "Tracking-Error Constraint",
    "Combined Turnover and Tracking-Error Constraints",
    "Maximize the Sharpe Ratio",
    "Confirm that Maximum Sharpe Ratio is a Maximum",
    "Illustrate that Sharpe is the Tangent Portfolio",
    "Dollar-Neutral Hedge-Fund Structure"
])

if page == "Asset Risks and Returns":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Efficient Frontier":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Efficient Frontier with Tangent Line":
    from application_pages.page3 import run_page3
    run_page3()
elif page == "Range of Risks and Returns":
    from application_pages.page4 import run_page4
    run_page4()
elif page == "Efficient Frontier with Targeted Portfolios":
    from application_pages.page5 import run_page5
    run_page5()
elif page == "Transactions Costs":
    from application_pages.page6 import run_page6
    run_page6()
elif page == "Turnover Constraint":
    from application_pages.page7 import run_page7
    run_page7()
elif page == "Tracking-Error Constraint":
    from application_pages.page8 import run_page8
    run_page8()
elif page == "Combined Turnover and Tracking-Error Constraints":
    from application_pages.page9 import run_page9
    run_page9()
elif page == "Maximize the Sharpe Ratio":
    from application_pages.page10 import run_page10
    run_page10()
elif page == "Confirm that Maximum Sharpe Ratio is a Maximum":
    from application_pages.page11 import run_page11
    run_page11()
elif page == "Illustrate that Sharpe is the Tangent Portfolio":
    from application_pages.page12 import run_page12
    run_page12()
elif page == "Dollar-Neutral Hedge-Fund Structure":
    from application_pages.page13 import run_page13
    run_page13()

# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
```

Key aspects:

*   **`streamlit as st`**:  Imports the Streamlit library, which is the core framework for building the application.
*   **`st.set_page_config()`**: Configures the page title and layout.  `layout="wide"` makes the app use the full screen width.
*   **`st.sidebar`**: Creates a sidebar for navigation.  It includes a logo, a divider, and a `selectbox`.
*   **`st.title()`/`st.divider()`**: Sets the main title and adds visual separators.
*   **`st.sidebar.selectbox()`**: Creates a dropdown menu in the sidebar, allowing users to select different portfolio optimization scenarios.
*   **Conditional Page Loading**: The `if/elif` block imports and runs the code for each selected page.  This modular approach keeps the main `app.py` file clean.  Each page's code is located in the `application_pages` directory.
*   **Copyright and Caption**:  Adds a footer with copyright information and a disclaimer.

## Navigating the Application

The application utilizes a sidebar navigation menu, making it easy to explore different portfolio optimization concepts.  Each option in the `selectbox` corresponds to a separate page within the application.

## Page 1: Asset Risks and Returns
Duration: 00:10

This page visualizes the risk and return characteristics of individual assets, along with the market, cash, and an equal-weighted portfolio.

```python
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def run_page1():
    st.header("Asset Risks and Returns")

    # Load the data (replace with actual loading from file if needed)
    # In the original code, the data is loaded using load BlueChipStockMoments
    # For this streamlit app, let's assume the data is stored as numpy arrays or pandas DataFrames

    # Generate synthetic data (based on BlueChipStockMoments.mat)
    np.random.seed(42)  # for reproducibility
    num_assets = 30
    AssetList = [f'Asset {i+1}' for i in range(num_assets)]
    AssetMean = np.random.rand(num_assets) * 0.2  # Annualized mean returns (e.g., 0 to 20%)
    AssetCovar = np.random.rand(num_assets, num_assets)
    AssetCovar = np.triu(AssetCovar) + AssetCovar.T - np.diag(np.diag(AssetCovar)) #Make symmetric
    AssetCovar = AssetCovar * 0.01 # Scale the covariance matrix
    CashMean = 0.03  # Risk-free rate (e.g., 3%)
    CashVar = 0.0001
    MarketMean = 0.10  # Market mean return (e.g., 10%)
    MarketVar = 0.04

    # Calculate standard deviations
    AssetRisk = np.sqrt(np.diag(AssetCovar))
    MarketRisk = np.sqrt(MarketVar)
    CashRisk = np.sqrt(CashVar)

    # Equal-weighted portfolio
    EqualWeight = np.ones(num_assets) / num_assets
    EqualMean = np.sum(EqualWeight * AssetMean)
    EqualRisk = np.sqrt(EqualWeight @ AssetCovar @ EqualWeight)

    # Create a DataFrame for the assets
    asset_data = pd.DataFrame({'Mean Return': AssetMean, 'Risk': AssetRisk}, index=AssetList)

    # Create a scatter plot
    fig = px.scatter(asset_data, x='Risk', y='Mean Return', text=asset_data.index,
                     title='Asset Risks and Returns', labels={'Mean Return': 'Annualized Mean Return', 'Risk': 'Annualized Risk'})
    fig.add_trace(px.scatter(x=[MarketRisk], y=[MarketMean], text=['Market'],
                              labels={'x': 'Risk', 'y': 'Mean Return'}).data[0])
    fig.add_trace(px.scatter(x=[CashRisk], y=[CashMean], text=['Cash'],
                              labels={'x': 'Risk', 'y': 'Mean Return'}).data[0])
    fig.add_trace(px.scatter(x=[EqualRisk], y=[EqualMean], text=['Equal'],
                              labels={'x': 'Risk', 'y': 'Mean Return'}).data[0])

    fig.update_traces(textposition='top center')

    st.plotly_chart(fig, use_container_width=True)
```

Explanation:

*   **Synthetic Data Generation**: The code generates synthetic asset data using `numpy`.  This includes asset means, covariance matrix, risk-free rate, and market characteristics.  Using `np.random.seed(42)` ensures consistent data generation each time the app runs.
*   **Risk and Return Calculation**:  Calculates the risk (standard deviation) from the covariance matrix and defines the return for cash and market.
*   **Equal-Weighted Portfolio**: Calculates the mean return and risk for an equally weighted portfolio.
*   **Data Visualization**: Uses `plotly.express` to create a scatter plot of asset risks and returns.  Markers for the market, cash, and equal-weighted portfolio are added. The `update_traces` function ensures the asset labels are positioned clearly.
*   **Streamlit Integration**:  `st.plotly_chart()` displays the plot in the Streamlit application.

## Page 2: Efficient Frontier
Duration: 00:15

This page displays the efficient frontier, which represents the set of portfolios that offer the highest expected return for a given level of risk or the lowest risk for a given level of expected return.

```python
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def run_page2():
    st.header("Efficient Frontier")

    # Load the data (replace with actual loading from file if needed)
    # In the original code, the data is loaded using load BlueChipStockMoments
    # For this streamlit app, let's assume the data is stored as numpy arrays or pandas DataFrames

    # Generate synthetic data (based on BlueChipStockMoments.mat)
    np.random.seed(42)  # for reproducibility
    num_assets = 30
    AssetList = [f'Asset {i+1}' for i in range(num_assets)]
    AssetMean = np.random.rand(num_assets) * 0.2  # Annualized mean returns (e.g., 0 to 20%)
    AssetCovar = np.random.rand(num_assets, num_assets)
    AssetCovar = np.triu(AssetCovar) + AssetCovar.T - np.diag(np.diag(AssetCovar)) #Make symmetric
    AssetCovar = AssetCovar * 0.01 # Scale the covariance matrix
    CashMean = 0.03  # Risk-free rate (e.g., 3%)
    CashVar = 0.0001
    MarketMean = 0.10  # Market mean return (e.g., 10%)
    MarketVar = 0.04

    # Calculate standard deviations
    AssetRisk = np.sqrt(np.diag(AssetCovar))
    MarketRisk = np.sqrt(MarketVar)
    CashRisk = np.sqrt(CashVar)

    # Equal-weighted portfolio
    EqualWeight = np.ones(num_assets) / num_assets
    EqualMean = np.sum(EqualWeight * AssetMean)
    EqualRisk = np.sqrt(EqualWeight @ AssetCovar @ EqualWeight)

    # Portfolio object (Simplified for demonstration)
    class Portfolio:
        def __init__(self, AssetList, RiskFreeRate):
            self.AssetList = AssetList
            self.RiskFreeRate = RiskFreeRate
            self.NumAssets = len(AssetList)

        def setAssetMoments(self, AssetMean, AssetCovar):
            self.AssetMean = AssetMean
            self.AssetCovar = AssetCovar

        def setInitPort(self, initial_weights):
            self.InitPort = initial_weights

        def setDefaultConstraints(self):
            # Long-only, fully invested
            pass  # In a real implementation, add constraint matrices here

    p = Portfolio(AssetList, CashMean)
    p.setAssetMoments(AssetMean, AssetCovar)
    p.setInitPort(np.ones(num_assets) / num_assets)
    p.setDefaultConstraints()

    # Estimate efficient frontier (Simplified)
    def estimateFrontier(p, num_points=20):
        # In a real implementation, this would use an optimization solver
        # Here, we'll generate random portfolios
        weights = np.random.rand(num_points, p.NumAssets)
        weights = weights / np.sum(weights, axis=1, keepdims=True)  # Normalize weights
        return weights

    weights = estimateFrontier(p, 20)

    # Estimate portfolio moments (Simplified)
    def estimatePortMoments(p, weights):
        returns = np.sum(weights * p.AssetMean, axis=1)
        risks = np.array([np.sqrt(w @ p.AssetCovar @ w.T) for w in weights])
        return risks, returns

    risks, returns = estimatePortMoments(p, weights)

    # Create a DataFrame for the efficient frontier
    frontier_data = pd.DataFrame({'Risk': risks, 'Return': returns})

    # Create the plot
    fig = px.line(frontier_data, x='Risk', y='Return', title='Efficient Frontier',
                  labels={'Return': 'Annualized Return', 'Risk': 'Annualized Risk'})

    fig.add_trace(go.Scatter(x=[MarketRisk, CashRisk, EqualRisk], y=[MarketMean, CashMean, EqualMean],
                             mode='markers', name='Markers',
                             marker=dict(size=[10, 10, 10]),
                             text=['Market', 'Cash', 'Equal']))

    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)
```

Explanation:

*   **`Portfolio` Class**:  A simplified `Portfolio` class is defined to store asset information, the risk-free rate, and portfolio constraints.  In a real-world application, this class would include methods for optimization and constraint handling.
*   **`estimateFrontier()` Function**:  Generates random portfolio weights.  This is a simplification; a real efficient frontier would be generated using an optimization solver to find the optimal portfolio for each risk level. The random portfolio weights are normalized such that they sum to 1.
*   **`estimatePortMoments()` Function**: Calculates the risk and return for a given set of portfolio weights.
*   **Plotting**: Uses `plotly.express` to plot the efficient frontier and adds markers for the market, cash, and equal-weighted portfolio. The `showlegend=False` argument hides the legend to reduce clutter.

## Page 3: Efficient Frontier with Tangent Line
Duration: 00:15

This page extends the previous one by adding a tangent line to the efficient frontier. The tangent line represents the capital allocation line, and the point of tangency represents the portfolio with the highest Sharpe ratio.

```python
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def run_page3():
    st.header("Efficient Frontier with Tangent Line")

    # Load the data (replace with actual loading from file if needed)
    # In the original code, the data is loaded using load BlueChipStockMoments
    # For this streamlit app, let's assume the data is stored as numpy arrays or pandas DataFrames

    # Generate synthetic data (based on BlueChipStockMoments.mat)
    np.random.seed(42)  # for reproducibility
    num_assets = 30
    AssetList = [f'Asset {i+1}' for i in range(num_assets)]
    AssetMean = np.random.rand(num_assets) * 0.2  # Annualized mean returns (e.g., 0 to 20%)
    AssetCovar = np.random.rand(num_assets, num_assets)
    AssetCovar = np.triu(AssetCovar) + AssetCovar.T - np.diag(np.diag(AssetCovar)) #Make symmetric
    AssetCovar = AssetCovar * 0.01 # Scale the covariance matrix
    CashMean = 0.03  # Risk-free rate (e.g., 3%)
    CashVar = 0.0001
    MarketMean = 0.10  # Market mean return (e.g., 10%)
    MarketVar = 0.04

    # Calculate standard deviations
    AssetRisk = np.sqrt(np.diag(AssetCovar))
    MarketRisk = np.sqrt(MarketVar)
    CashRisk = np.sqrt(CashVar)

    # Equal-weighted portfolio
    EqualWeight = np.ones(num_assets) / num_assets
    EqualMean = np.sum(EqualWeight * AssetMean)
    EqualRisk = np.sqrt(EqualWeight @ AssetCovar @ EqualWeight)

    # Portfolio object (Simplified for demonstration)
    class Portfolio:
        def __init__(self, AssetList, RiskFreeRate):
            self.AssetList = AssetList
            self.RiskFreeRate = RiskFreeRate
            self.NumAssets = len(AssetList)

        def setAssetMoments(self, AssetMean, AssetCovar):
            self.AssetMean = AssetMean
            self.AssetCovar = AssetCovar

        def setInitPort(self, initial_weights):
            self.InitPort = initial_weights

        def setDefaultConstraints(self):
            # Long-only, fully invested
            pass  # In a real implementation, add constraint matrices here

        def setBudget(self, min_cash, max_cash):
            self.min_cash = min_cash
            self.max_cash = max_cash

    p = Portfolio(AssetList, CashMean)
    p.setAssetMoments(AssetMean, AssetCovar)
    p.setInitPort(np.ones(num_assets) / num_assets)
    p.setDefaultConstraints()

    # Estimate efficient frontier (Simplified)
    def estimateFrontier(p, num_points=20):
        # In a real implementation, this would use an optimization solver
        # Here, we'll generate random portfolios
        weights = np.random.rand(num_points, p.NumAssets)
        weights = weights / np.sum(weights, axis=1, keepdims=True)  # Normalize weights
        return weights

    def estimatePortMoments(p, weights):
        returns = np.sum(weights * p.AssetMean, axis=1)
        risks = np.array([np.sqrt(w @ p.AssetCovar @ w.T) for w in weights])
        return risks, returns

    # Tangent Line
    q = Portfolio(AssetList, CashMean)
    q.setAssetMoments(AssetMean, AssetCovar)
    q.setBudget(0, 1)  # Budget constraint
    qwgt = estimateFrontier(q, 20)
    qrsk, qret = estimatePortMoments(q, qwgt)

    weights = estimateFrontier(p, 20)
    risks, returns = estimatePortMoments(p, weights)

    # Create a DataFrame for the efficient frontier
    frontier_data = pd.DataFrame({'Risk': risks, 'Return': returns})

    # Create a DataFrame for the tangent efficient frontier
    tangent_frontier_data = pd.DataFrame({'Risk': qrsk, 'Return': qret})


    # Create the plot
    fig = px.line(frontier_data, x='Risk', y='Return', title='Efficient Frontier with Tangent Line',
                  labels={'Return': 'Annualized Return', 'Risk': 'Annualized Risk'})

    fig.add_trace(go.Scatter(x=tangent_frontier_data['Risk'], y=tangent_frontier_data['Return'], mode='lines', name='Tangent Frontier'))

    fig.add_trace(go.Scatter(x=[MarketRisk, CashRisk, EqualRisk], y=[MarketMean, CashMean, EqualMean],
                             mode='markers', name='Markers',
                             marker=dict(size=[10, 10, 10]),
                             text=['Market', 'Cash', 'Equal']))

    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)
```

Explanation:

*   **`setBudget()` function**: The `setBudget` function is added to the portfolio object which adds a budget constraint
*   **Tangent Frontier**: The `estimateFrontier()` and `estimatePortMoments()` functions are used to estimate the tangent frontier data
*   **Plotting the Tangent Line**: A second efficient frontier is plotted which serves as the tangent line and is labeled as 'Tangent Frontier'.

## Page 4: Range of Risks and Returns
Duration: 00:10

This page calculates and displays the minimum and maximum possible risk and return values for the given set of assets.

```python
import streamlit as st
import numpy as np
import pandas as pd

def run_page4():
    st.header("Range of Risks and Returns")

    # Load the data (replace with actual loading from file if needed)
    # In the original code, the data is loaded using load BlueChipStockMoments
    # For this streamlit app, let's assume the data is stored as numpy arrays or pandas DataFrames

    # Generate synthetic data (based on BlueChipStockMoments.mat)
    np.random.seed(42)  # for reproducibility
    num_assets = 30
    AssetList = [f'Asset {i+1}' for i in range(num_assets)]
    AssetMean = np.random.rand(num_assets) * 0.2  # Annualized mean returns (e.g., 0 to 20%)
    AssetCovar = np.random.rand(num_assets, num_assets)
    AssetCovar = np.triu(AssetCovar) + AssetCovar.T - np.diag(np.diag(AssetCovar)) #Make symmetric
    AssetCovar = AssetCovar * 0.01 # Scale the covariance matrix
    CashMean = 0.03  # Risk-free rate (e.g., 3%)
    CashVar = 0.0001
    MarketMean = 0.10  # Market mean return (e.g., 10%)
    MarketVar = 0.04

    # Calculate standard deviations
    AssetRisk = np.sqrt(np.diag(AssetCovar))
    MarketRisk = np.sqrt(MarketVar)
    CashRisk = np.sqrt(CashVar)

    # Equal-weighted portfolio
    EqualWeight = np.ones(num_assets) / num_assets
    EqualMean = np.sum(EqualWeight * AssetMean)
    EqualRisk = np.sqrt(EqualWeight @ AssetCovar @ EqualWeight)

    # Portfolio object (Simplified for demonstration)
    class Portfolio:
        def __init__(self, AssetList, RiskFreeRate):
            self.AssetList = AssetList
            self.RiskFreeRate = RiskFreeRate
            self.NumAssets = len(AssetList)

        def setAssetMoments(self, AssetMean, AssetCovar):
            self.AssetMean = AssetMean
            self.AssetCovar = AssetCovar

        def setInitPort(self, initial_weights):
            self.InitPort = initial_weights

        def setDefaultConstraints(self):
            # Long-only, fully invested
            pass  # In a real implementation, add constraint matrices here


    p = Portfolio(AssetList, CashMean)
    p.setAssetMoments(AssetMean, AssetCovar)
    p.setInitPort(np.ones(num_assets) / num_assets)
    p.setDefaultConstraints()

    # Estimate frontier limits (Simplified)
    def estimateFrontierLimits(p):
        # In a real implementation, this would use an optimization solver
        # Here, we'll return the min and max possible weights
        min_weights = np.zeros(p.NumAssets)
        max_weights = np.zeros(p.NumAssets)
        min_weights[np.argmin(p.AssetMean)] = 1  # Invest in asset with lowest mean return (min return)
        max_weights[np.argmax(p.AssetMean)] = 1  # Invest in asset with highest mean return (max return)
        return np.vstack((min_weights, max_weights))


    def estimatePortMoments(p, weights):
        returns = np.sum(weights * p.AssetMean, axis=1)
        risks = np.array([np.sqrt(w @ p.AssetCovar @ w.T) for w in weights])
        return risks, returns

    # Calculate min and max risk/return
    frontier_limits = estimateFrontierLimits(p)
    rsk, ret = estimatePortMoments(p, frontier_limits)

    # Display the results
    st.write("Minimum Risk:", rsk[0])
    st.write("Minimum Return:", ret[0])
    st.write("Maximum Risk:", rsk[1])
    st.write("Maximum Return:", ret[1])
```

Explanation:

*   **`estimateFrontierLimits()` function**: Determines the portfolio weights that would result in the minimum and maximum possible returns. This is done by allocating 100% of the portfolio to the asset with the lowest and highest mean returns, respectively.
*   **Displaying Results**:  Uses `st.write()` to display the calculated minimum and maximum risk and return values in the Streamlit application.

## Page 5: Efficient Frontier with Targeted Portfolios
Duration: 00:15

This page allows the user to input target return and risk levels and visualizes the portfolios that meet those targets on the efficient frontier.

```python
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def run_page5():
    st.header("Efficient Frontier with Targeted Portfolios")

    # Load the data (replace with actual loading from file if needed)
    # In the original code, the data is loaded using load BlueChipStockMoments
    # For this streamlit app, let's assume the data is stored as numpy arrays or pandas DataFrames

    # Generate synthetic data (based on BlueChipStockMoments.mat)
    np.random.seed(42)  # for reproducibility
    num_assets = 30
    AssetList = [f'Asset {i+1}' for i in range(num_assets)]
    AssetMean = np.random.rand(num_assets) * 0.2  # Annualized mean returns (e.g., 0 to 20%)
    AssetCovar = np.random.rand(num_assets, num_assets)
    AssetCovar = np.triu(AssetCovar) + AssetCovar.T - np.diag(np.diag(AssetCovar)) #Make symmetric
    AssetCovar = AssetCovar * 0.01 # Scale the covariance matrix
    CashMean = 0.03  # Risk-free rate (e.g., 3%)
    CashVar = 0.0001
    MarketMean = 0.10  # Market mean return (e.g., 10%)
    MarketVar = 0.04

    # Calculate standard deviations
    AssetRisk = np.sqrt(np.diag(AssetCovar))
    MarketRisk = np.sqrt(MarketVar)
    CashRisk = np.sqrt(CashVar)

    # Equal-weighted portfolio
    EqualWeight = np.ones(num_assets) / num_assets
    EqualMean = np.sum(EqualWeight * AssetMean)
    EqualRisk = np.sqrt(EqualWeight @ AssetCovar @ EqualWeight)

    # Portfolio object (Simplified for demonstration)
    class Portfolio:
        def __init__(self, AssetList, RiskFreeRate):
            self.AssetList = AssetList
            self.RiskFreeRate = RiskFreeRate
            self.NumAssets = len(AssetList)

        def setAssetMoments(self, AssetMean, AssetCovar):
            self.AssetMean = AssetMean
            self.AssetCovar = AssetCovar

        def setInitPort(self, initial_weights):
            self.InitPort = initial_weights

        def setDefaultConstraints(self):
            # Long-only, fully invested
            pass  # In a real implementation, add constraint matrices here

    p = Portfolio(AssetList, CashMean)
    p.setAssetMoments(AssetMean, AssetCovar)
    p.setInitPort(np.ones(num_assets) / num_assets)
    p.setDefaultConstraints()

    # Estimate efficient frontier (Simplified)
    def estimateFrontier(p, num_points=20):
        # In a real implementation, this would use an optimization solver
        # Here, we'll generate random portfolios
        weights = np.random.rand(num_points, p.NumAssets)
        weights = weights / np.sum(weights, axis=1, keepdims=True)  # Normalize weights
        return weights

    def estimatePortMoments(p, weights):
        returns = np.sum(weights * p.AssetMean, axis=1)
        risks = np.array([np.sqrt(w @ p.AssetCovar @ w.T) for w in weights])
        return risks, returns

    def estimateFrontierByReturn(p, target_return):
        #In a real implementation, solve optimization problem to target return
        weights = np.random.rand(p.NumAssets)
        weights = weights / np.sum(weights)
        return weights

    def estimateFrontierByRisk(p, target_risk):
        #In a real implementation, solve optimization problem to target risk
        weights = np.random.rand(p.NumAssets)
        weights = weights / np.sum(weights)
        return weights


    # Input fields for target return and risk
    TargetReturn = st.number_input("Target Return (Annualized)", min_value=0.0, max_value=1.0, value=0.20)
    TargetRisk = st.number_input("Target Risk (Annualized)", min_value=0.0, max_value=1.0, value=0.15)

    # Estimate portfolios for target return and risk
    awgt = estimateFrontierByReturn(p, TargetReturn/12)
    arsk, aret = estimatePortMoments(p, awgt)

    bwgt = estimateFrontierByRisk(p, TargetRisk/np.sqrt(12))
    brsk, bret = estimatePortMoments(p, bwgt)


    weights = estimateFrontier(p, 20)
    risks, returns = estimatePortMoments(p, weights)

    # Create a DataFrame for the efficient frontier
    frontier_data = pd.DataFrame({'Risk': risks, 'Return': returns})

    # Create the plot
    fig = px.line(frontier_data, x='Risk', y='Return', title='Efficient Frontier with Targeted Portfolios',
                  labels={'Return': 'Annualized Return', 'Risk': 'Annualized Risk'})

    fig.add_trace(go.Scatter(x=[MarketRisk, CashRisk, EqualRisk], y=[MarketMean, CashMean, EqualMean],
                             mode='markers', name='Markers',
                             marker=dict(size=[10, 10, 10]),
                             text=['Market', 'Cash', 'Equal']))

    fig.add_trace(go.Scatter(x=[arsk], y=[aret],
                             mode='markers', name='Target Return',
                             marker=dict(size=[10]),
                             text=[f'{100*TargetReturn}% Return']))

    fig.add_trace(go.Scatter(x=[brsk], y=[bret],
                             mode='markers', name='Target Risk',
                             marker=dict(size=[10]),
                             text=[f'{100*TargetRisk}% Risk']))

    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)
```

Explanation:

*   **User Input**: Uses `st.number_input()` to create input fields for the user to specify the target return and risk.
*   **`estimateFrontierByReturn()` and `estimateFrontierByRisk()` functions**:  These functions are placeholders. In a real-world scenario, these would involve solving an optimization problem to find the portfolio that best matches the target return or risk.  Here, they simply generate random weights.
*   **Plotting Target Portfolios**: Adds scatter markers to the plot representing the target return and target risk portfolios.

## Page 6: Efficient Frontier with Transaction Costs
Duration: 00:15

This page allows the user to specify buy and sell transaction costs and visualizes the impact of these costs on the efficient frontier.

