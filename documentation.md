id: 67f9368ad05265d2d8e155e2_documentation
summary: Portfolio Optimization Examples Using Financial Toolbox Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab Streamlit Application: A Developer's Guide

This codelab provides a comprehensive guide to understanding and potentially extending the QuLab Streamlit application. QuLab is designed as an educational tool demonstrating key concepts in quantitative finance, including efficient frontiers, Sharpe ratio maximization, and dollar-neutral hedge fund strategies. This codelab will walk you through the application's structure, page navigation, and individual page functionalities. By the end of this guide, you'll have a clear understanding of how the application is built and how to customize it for your own educational or demonstrative purposes.

## Setting Up Your Development Environment
Duration: 00:05

Before diving into the code, ensure you have the following:

1.  **Python:**  Python 3.6 or higher is recommended.
2.  **Streamlit:** Install using pip: `pip install streamlit`

    ```console
    pip install streamlit
    ```
3.  **Code Editor:** A code editor like VS Code, PyCharm, or Sublime Text.

## Understanding the Application Structure
Duration: 00:10

The QuLab application is structured as follows:

*   `app.py`: This is the main entry point of the application. It handles the overall layout, page navigation, and footer.
*   `application_pages/`: This directory contains individual Python files for each page of the application (e.g., `page1.py`, `page2.py`, `page3.py`).

This modular structure allows for easy expansion and maintenance of the application.

## Exploring the Main Application File (app.py)
Duration: 00:15

Let's examine the code in `app.py`:

```python
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Your code goes here
page = st.sidebar.selectbox(label="Navigation", options=["Page 1", "Page 2", "Page 3"])

if page == "Page 1":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3":
    from application_pages.page3 import run_page3
    run_page3()

# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
```

**Key Components:**

*   `st.set_page_config`: Configures the page title and layout (wide mode).
*   `st.sidebar.image`: Displays the QuantUniversity logo in the sidebar.
*   `st.sidebar.divider`: Adds a visual separator in the sidebar.
*   `st.title`: Sets the main title of the application.
*   `st.divider`: Adds a horizontal line to visually separate content.
*   `st.sidebar.selectbox`: Creates a dropdown menu in the sidebar for navigation.  The options are "Page 1", "Page 2", and "Page 3".
*   `if/elif/else` block:  Dynamically imports and runs the corresponding page based on the user's selection in the `selectbox`.
*   `st.write` and `st.caption`:  Display the copyright notice and disclaimer at the bottom of the page.

## Page Navigation Logic
Duration: 00:10

The core of the application's navigation lies within the `if/elif/else` block.  When a user selects a page from the sidebar's dropdown menu, the corresponding Python file from the `application_pages/` directory is imported, and its `run_pageX()` function is executed.  This dynamic import mechanism allows for a clean separation of concerns, with each page's content and logic residing in its own dedicated file.

## Examining the Individual Pages
Duration: 00:15

Each page (Page 1, Page 2, and Page 3) follows a similar structure. Let's look at `application_pages/page1.py` as an example:

```python
import streamlit as st

def run_page1():
    st.header("Page 1: Efficient Frontier")
    st.write("This page will display the efficient frontier.")
```

Each page's Python file defines a `run_pageX()` function that is called by `app.py` when the user navigates to that page.  Currently, each page simply displays a header and a placeholder text. The crucial step is to populate each of these run_page functions with actual code that performs the quantitative finance functionality.

## Implementing the Efficient Frontier (Page 1)
Duration: 00:30

Let's enhance `application_pages/page1.py` to display a basic efficient frontier.  This will require some numerical computation and plotting.  We'll use `numpy` for numerical operations and `matplotlib` for plotting.  First install the required libraries:

```console
pip install numpy matplotlib
```

Now, modify `application_pages/page1.py`:

```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run_page1():
    st.header("Page 1: Efficient Frontier")

    # Sample data (replace with your actual data)
    num_assets = 5
    num_portfolios = 100
    risk_free_rate = 0.01

    # Generate random returns and covariance matrix
    np.random.seed(42)  # for reproducibility
    returns = np.random.rand(num_assets) * 0.2
    covariance_matrix = np.random.rand(num_assets, num_assets)
    covariance_matrix = np.triu(covariance_matrix) + np.triu(covariance_matrix, k=1).transpose()
    covariance_matrix = covariance_matrix * 0.1


    # Generate random portfolios
    weights = np.random.rand(num_portfolios, num_assets)
    weights /= np.sum(weights, axis=1, keepdims=True)

    # Calculate portfolio returns and risks
    portfolio_returns = np.dot(weights, returns)
    portfolio_risks = np.zeros(num_portfolios)
    for i in range(num_portfolios):
        portfolio_risks[i] = np.sqrt(np.dot(weights[i].T, np.dot(covariance_matrix, weights[i])))

    # Create the efficient frontier plot
    fig, ax = plt.subplots()
    ax.scatter(portfolio_risks, portfolio_returns, marker='o', s=10, alpha=0.3)
    ax.set_xlabel('Risk (Standard Deviation)')
    ax.set_ylabel('Return')
    ax.set_title('Efficient Frontier')
    ax.grid(True)

    # Display the plot in Streamlit
    st.pyplot(fig)
```

**Explanation:**

1.  **Import Libraries:** Import `streamlit`, `numpy`, and `matplotlib`.
2.  **Sample Data:** Create sample data for asset returns and a covariance matrix.  <b>Replace this with your actual financial data.</b>
3.  **Random Portfolios:** Generate random portfolio weights.
4.  **Calculate Returns and Risks:** Calculate the return and risk (standard deviation) for each portfolio.
5.  **Create Plot:** Use `matplotlib` to create a scatter plot of risk vs. return.
6.  **Display Plot:** Use `st.pyplot(fig)` to display the plot in the Streamlit application.

<aside class="negative">
    Remember to replace the sample data with real-world financial data for a more meaningful demonstration. The random data is just for illustrative purposes.
</aside>

## Implementing Sharpe Ratio Maximization (Page 2)
Duration: 00:30

Now let's add content to `application_pages/page2.py` to demonstrate Sharpe Ratio maximization. This will involve optimization to find the portfolio with the highest Sharpe Ratio.  We'll use the `scipy` library for optimization. First install the required libraries:

```console
pip install scipy
```

Modify `application_pages/page2.py`:

```python
import streamlit as st
import numpy as np
from scipy.optimize import minimize

def run_page2():
    st.header("Page 2: Sharpe Ratio Maximization")

    # Sample data (replace with your actual data)
    num_assets = 5
    risk_free_rate = 0.01

    # Generate random returns and covariance matrix
    np.random.seed(42)
    returns = np.random.rand(num_assets) * 0.2
    covariance_matrix = np.random.rand(num_assets, num_assets)
    covariance_matrix = np.triu(covariance_matrix) + np.triu(covariance_matrix, k=1).transpose()
    covariance_matrix = covariance_matrix * 0.1

    # Define the Sharpe Ratio function (to be minimized)
    def sharpe_ratio(weights, returns, covariance_matrix, risk_free_rate):
        portfolio_return = np.sum(returns * weights)
        portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))
        sharpe = (portfolio_return - risk_free_rate) / portfolio_risk
        return -sharpe  # We minimize the negative Sharpe Ratio

    # Define constraints and bounds for optimization
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights must sum to 1
    bounds = tuple((0, 1) for asset in range(num_assets))  # Weights must be between 0 and 1

    # Initial guess for weights
    initial_weights = np.array([1/num_assets] * num_assets)

    # Perform optimization
    result = minimize(sharpe_ratio, initial_weights, args=(returns, covariance_matrix, risk_free_rate),
                       method='SLSQP', bounds=bounds, constraints=constraints)

    # Extract optimal weights
    optimal_weights = result.x

    # Calculate optimal portfolio return and risk
    optimal_return = np.sum(returns * optimal_weights)
    optimal_risk = np.sqrt(np.dot(optimal_weights.T, np.dot(covariance_matrix, optimal_weights)))
    optimal_sharpe_ratio = (optimal_return - risk_free_rate) / optimal_risk

    # Display results
    st.write("Optimal Portfolio Weights:", optimal_weights)
    st.write("Optimal Portfolio Return:", optimal_return)
    st.write("Optimal Portfolio Risk:", optimal_risk)
    st.write("Optimal Sharpe Ratio:", optimal_sharpe_ratio)
```

**Explanation:**

1.  **Import Libraries:** Import `streamlit`, `numpy`, and `scipy.optimize`.
2.  **Sample Data:** Generate sample asset returns and a covariance matrix.
3.  **Sharpe Ratio Function:** Define a function `sharpe_ratio` that calculates the Sharpe Ratio of a given portfolio (defined by its weights). We minimize the negative of the Sharpe Ratio because `scipy.optimize.minimize` is designed for minimization.
4.  **Constraints and Bounds:** Define constraints to ensure that the portfolio weights sum to 1 and bounds to ensure that each weight is between 0 and 1.
5.  **Optimization:** Use `scipy.optimize.minimize` to find the portfolio weights that maximize the Sharpe Ratio, subject to the defined constraints and bounds.
6.  **Display Results:** Display the optimal portfolio weights, return, risk, and Sharpe Ratio using `st.write`.

<aside class="positive">
    Experiment with different optimization methods within `scipy.optimize.minimize` to see how they affect the results. The 'SLSQP' method is a good general-purpose option for constrained optimization problems.
</aside>

## Implementing a Dollar-Neutral Hedge Fund Strategy (Page 3)
Duration: 00:30

Finally, let's implement a simplified dollar-neutral hedge fund strategy in `application_pages/page3.py`.  This involves taking both long and short positions in different assets to minimize market exposure.

Modify `application_pages/page3.py`:

```python
import streamlit as st
import numpy as np
import pandas as pd

def run_page3():
    st.header("Page 3: Dollar-Neutral Hedge Fund")

    # Sample data (replace with your actual data)
    num_assets = 5
    np.random.seed(42)
    returns = pd.DataFrame(np.random.randn(100, num_assets), columns=[f'Asset {i+1}' for i in range(num_assets)])

    # Define long/short positions (replace with your strategy)
    # This is a very basic example: Long Asset 1, Short Asset 2
    positions = pd.DataFrame(0, index=returns.index, columns=returns.columns)
    positions['Asset 1'] = 1  # Long position in Asset 1
    positions['Asset 2'] = -1 # Short position in Asset 2

    # Calculate portfolio returns
    portfolio_returns = (positions.shift(1) * returns).sum(axis=1)
    portfolio_returns.fillna(0, inplace=True)  # Handle NaN values

    # Calculate cumulative returns
    cumulative_returns = (1 + portfolio_returns).cumprod()

    # Create a plot of cumulative returns
    st.line_chart(cumulative_returns)

    # Display some performance metrics
    st.write("Total Return:", cumulative_returns.iloc[-1])
    st.write("Volatility:", portfolio_returns.std())
    st.write("Sharpe Ratio:", portfolio_returns.mean() / portfolio_returns.std())
```

**Explanation:**

1.  **Import Libraries:** Import `streamlit`, `numpy`, and `pandas`.  We use `pandas` to handle time series data.
2.  **Sample Data:** Generate random returns for multiple assets using `pandas`.  <b>Replace this with actual historical price data.</b>
3.  **Define Positions:** Create a `pandas` DataFrame to represent long and short positions in each asset.  In this simple example, we take a long position in Asset 1 and a short position in Asset 2.  A more sophisticated strategy would involve dynamically adjusting these positions based on market conditions.
4.  **Calculate Portfolio Returns:** Calculate the daily portfolio returns by multiplying the shifted positions (to avoid look-ahead bias) by the asset returns.
5.  **Calculate Cumulative Returns:** Calculate the cumulative returns of the portfolio.
6.  **Create Plot:** Use `st.line_chart` to display the cumulative returns over time.
7.  **Display Performance Metrics:** Calculate and display the total return, volatility (standard deviation), and Sharpe Ratio of the portfolio.

<aside class="negative">
The provided dollar-neutral strategy is extremely simplistic. A real-world implementation would require more sophisticated techniques for asset selection, position sizing, and risk management.
</aside>

## Running the Application
Duration: 00:05

To run the application, navigate to the directory containing `app.py` in your terminal and execute the following command:

```console
streamlit run app.py
```

This will start the Streamlit server and open the application in your web browser.

## Customization and Further Development
Duration: 00:15

The QuLab application provides a basic framework for demonstrating quantitative finance concepts. You can customize and extend it in many ways, including:

*   **Data Integration:** Connect to real-time or historical financial data sources (e.g., APIs, databases).
*   **Advanced Strategies:** Implement more sophisticated trading strategies, risk management techniques, and portfolio optimization algorithms.
*   **Interactive Controls:** Add more interactive widgets (e.g., sliders, input boxes) to allow users to adjust parameters and explore different scenarios.
*   **Visualization:** Enhance the visualizations with more informative charts and graphs.
*   **Backtesting Framework:** Develop a backtesting framework to evaluate the performance of different strategies over historical data.

## Conclusion

This codelab has provided a comprehensive overview of the QuLab Streamlit application. By understanding the application's structure, page navigation, and individual page functionalities, you are now well-equipped to customize and extend it for your own educational or demonstrative purposes. Remember to replace the sample data with real-world data and explore different quantitative finance techniques to create a truly insightful and valuable tool.
