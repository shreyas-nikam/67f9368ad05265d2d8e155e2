id: 67f9368ad05265d2d8e155e2_documentation
summary: Portfolio Optimization Examples Using Financial Toolbox Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab Codelab: Portfolio Optimization with Streamlit

## Introduction to QuLab
Duration: 00:05:00

Welcome to the QuLab codelab! This codelab will guide you through the functionalities of the QuLab Streamlit application, a tool designed to illustrate key concepts in portfolio optimization using a financial toolbox.

In today's financial landscape, understanding portfolio optimization is crucial for developers and financial analysts alike. This application provides an interactive and visual way to grasp these complex concepts, making it an invaluable educational resource and a starting point for building more sophisticated financial tools.

**Key Concepts You'll Explore:**

*   **Portfolio Optimization:** Learn the basics of constructing an optimal portfolio to maximize returns for a given level of risk, or minimize risk for a given level of return.
*   **Efficient Frontier:** Understand the concept of the efficient frontier, representing the set of optimal portfolios that offer the highest expected return for a defined level of risk or the lowest risk for a given level of expected return.
*   **Risk and Return:** Visualize the relationship between risk and return for individual assets and portfolios.
*   **Sharpe Ratio:** Explore the Sharpe ratio as a measure of risk-adjusted return and identify the portfolio that maximizes it.
*   **Transaction Costs:** Analyze the impact of transaction costs on portfolio optimization and the efficient frontier.
*   **Target Portfolio Optimization:** Learn how to identify a portfolio on the efficient frontier that best meets specific target return and risk objectives.

By the end of this codelab, you will have a solid understanding of how QuLab works, the financial concepts it demonstrates, and how you can potentially adapt and expand upon it for your own projects.

## Setting up QuLab Application
Duration: 00:03:00

Before diving into the application's features, let's set it up locally. Ensure you have Python and Streamlit installed. If not, install them using pip:

```console
pip install streamlit pandas numpy plotly
```

Once you have the prerequisites, save the provided code snippets into the following files in the same directory:

*   `app.py` (main application)
*   `pages/Overview.py`
*   `pages/EfficientFrontier.py`
*   `pages/TargetPortfolio.py`
*   `pages/TransactionCosts.py`
*   `pages/MaxSharpe.py`

To run the application, navigate to the directory containing `app.py` in your terminal and execute:

```console
streamlit run app.py
```

This command will launch the QuLab application in your web browser. You should see the main page of the application.

## Exploring the Home Page
Duration: 00:02:00

The home page (`app.py`) serves as the entry point to QuLab. It provides a brief introduction to the application and guides users on how to navigate through its different functionalities.

Upon launching QuLab, you will see:

*   **Sidebar:**  On the left sidebar, you'll notice the QuantUniversity logo and a divider, visually branding the application.
*   **Application Title:** The main title "QuLab" is prominently displayed, indicating the name of the application.
*   **Introduction Text:**  A welcoming message explains that QuLab showcases portfolio optimization examples using a financial toolbox. It clearly states that this is a multi-page application and directs users to the sidebar for navigation.
*   **Copyright and Disclaimer:** At the bottom, you'll find a copyright notice and a disclaimer emphasizing the educational purpose of the application and usage restrictions.

**Navigation:**

The key takeaway from the home page is the navigation instruction. Streamlit's multi-page functionality is utilized here, and you can access different sections of QuLab by clicking on the page names listed in the sidebar. These pages correspond to the different portfolio optimization concepts we will explore.

<aside class="positive">
  <b>Tip:</b> Streamlit's multi-page applications are a great way to organize complex dashboards and tools, making them user-friendly and navigable. QuLab effectively uses this feature to separate different aspects of portfolio optimization into distinct pages.
</aside>

## Overview and Data Setup Page
Duration: 00:05:00

Navigate to the "Overview" page from the sidebar. This page (`pages/Overview.py`) provides a foundational understanding of portfolio optimization and sets the stage by generating and visualizing synthetic asset data.

**Page Content:**

*   **Title and Description:** The page title "Overview and Data Setup" clearly indicates its purpose.  A markdown description explains that this page offers an overview of portfolio optimization techniques and visualizes synthetic data simulating "BlueChipStockMoments".
*   **Synthetic Data Generation:** The core functionality here is the generation of synthetic data.
    *   **`numpy.random.seed(42)`:**  This line ensures reproducibility by setting a seed for NumPy's random number generator.
    *   **Asset Parameters:** The code defines parameters for 30 assets, including:
        *   `AssetList`: A list of asset names (Asset 1, Asset 2, ... Asset 30).
        *   `AssetMean`: Randomly generated mean returns for each asset, uniformly distributed between 0.05 and 0.15.
        *   `AssetCovar`: A randomly generated covariance matrix, ensuring it is symmetric and has realistic diagonal values (variances).
    *   **Calculation of Risk and Return:** The code extracts the mean returns (`mret`) and standard deviations (risks, `mrsk`) from the generated data.
*   **Data Visualization:**
    *   **Pandas DataFrame:** The generated data is organized into a Pandas DataFrame for easy manipulation and plotting.
    *   **Plotly Scatter Plot:** A scatter plot is created using Plotly Express to visualize the relationship between risk and return for each asset. The x-axis represents "Risk," the y-axis represents "Return," and each asset is labeled on the plot.
    *   **`st.plotly_chart(fig, use_container_width=True)`:** This Streamlit command displays the Plotly chart in the application, making it responsive to container width.

**Understanding the Visualization:**

The scatter plot on this page is crucial. It visually represents the risk-return profile of individual assets. Each point on the plot is an asset, with its position determined by its expected return (y-axis) and risk (x-axis).  Assets with higher expected returns and lower risks are generally more desirable. This visualization helps in understanding the basic inputs needed for portfolio optimization – expected returns and risks (and covariances between assets, although not directly visualized here).

<aside class="positive">
  <b>Best Practice:</b> Using synthetic data, as demonstrated here, is a great way to prototype and test financial applications without relying on live market data. It allows for controlled experiments and clear demonstrations of concepts.
</aside>

## Efficient Frontier Page
Duration: 00:04:00

Navigate to the "Efficient Frontier" page from the sidebar. This page (`pages/EfficientFrontier.py`) introduces the concept of the efficient frontier and visualizes a dummy efficient frontier.

**Page Content:**

*   **Title and Description:** The page title "Efficient Frontier" clearly indicates its focus.  The markdown description explains that this page illustrates a dummy efficient frontier generated using synthetic data.
*   **Dummy Efficient Frontier Data:**
    *   **`risks = np.linspace(0.05, 0.30, 50)`:**  Generates 50 risk values evenly spaced between 0.05 and 0.30. These represent portfolio risk levels.
    *   **`returns = 0.1 + 0.5 * risks`:** Calculates corresponding portfolio returns. This is a simplified linear relationship to create a dummy efficient frontier for demonstration purposes. In reality, the efficient frontier is derived through optimization algorithms.
*   **Visualization:**
    *   **Plotly Graph Object:** Plotly Graph Objects are used for more control over the plot.
    *   **`go.Scatter`:** A scatter trace is added to the figure with `mode='lines'`, creating a line plot of the efficient frontier.
    *   **Plot Customization:**  `fig.update_layout` is used to set the title and axis labels for clarity.
    *   **`st.plotly_chart(...)`:**  The Plotly figure is displayed using Streamlit.

**Understanding the Efficient Frontier:**

The efficient frontier represents the set of portfolios that offer the highest expected return for each level of risk, or the lowest risk for each level of expected return.  In simpler terms, for any given level of risk you are willing to take, the efficient frontier shows the portfolio that gives you the maximum possible return.  Portfolios on the efficient frontier are considered "optimal".

The dummy frontier here is a simplified representation.  In a real-world scenario, the efficient frontier is calculated using optimization techniques that consider asset returns, risks, and covariances.  This page focuses on visually introducing the concept of the efficient frontier as a curve in risk-return space.

<aside class="negative">
  <b>Important Note:</b> The efficient frontier shown on this page is a simplified, dummy representation. It is not derived from actual portfolio optimization calculations using the synthetic asset data from the "Overview" page. It serves purely for illustrative purposes.
</aside>

## Target Portfolio Optimization Page
Duration: 00:06:00

Navigate to the "Target Portfolio Optimization" page from the sidebar. This page (`pages/TargetPortfolio.py`) allows users to interactively define target return and risk levels and see the nearest portfolio on the (dummy) efficient frontier that meets these targets.

**Page Content:**

*   **Title and Description:** The title "Target Portfolio Optimization" and the markdown description clearly explain the page's functionality.
*   **Interactive Input:**
    *   **`st.number_input("Target Return ...")`:** A Streamlit number input widget allows users to specify their target annualized return. The `min_value`, `value`, and `step` parameters control the input range and increment.
    *   **`st.number_input("Target Risk ...")`:** Similarly, a number input widget is provided for users to set their target annualized risk (standard deviation).
*   **Dummy Efficient Frontier (Replicated):** The code replicates the same dummy efficient frontier data generation as in the "Efficient Frontier" page to have a frontier to work with.
*   **Target Portfolio Identification:**
    *   **Distance Calculation:**  The code calculates the Euclidean distance between each point on the efficient frontier and the user's target risk-return point.
    *   **Nearest Portfolio:** `np.argmin(dist)` finds the index of the point on the efficient frontier that has the minimum distance to the target.
    *   **Portfolio Risk and Return Extraction:** The risk and return of the nearest portfolio are extracted from the `risks` and `returns` arrays using the identified index.
*   **Visualization with Target Portfolio Highlight:**
    *   **Efficient Frontier Plot:** The efficient frontier is plotted as a line plot, similar to the "Efficient Frontier" page.
    *   **Target Portfolio Marker:** A red marker is added to the plot using `go.Scatter` with `mode='markers'`. This marker highlights the identified target portfolio on the efficient frontier.
    *   **Plot Customization:** Title and axis labels are set.
    *   **`st.plotly_chart(...)`:** The Plotly figure is displayed.
*   **Output Display:**
    *   **`st.write(f"Target portfolio risk: ...")`:**  The risk and return of the identified target portfolio are displayed below the chart using `st.write`.

**Interactivity and Learning:**

This page is highly interactive. By adjusting the "Target Return" and "Target Risk" inputs, users can observe how the highlighted "Target Portfolio" marker moves along the efficient frontier. This visually demonstrates how different investment objectives (target return and risk) lead to different portfolio choices on the efficient frontier.  It helps understand that portfolio selection is about finding a balance between desired return and acceptable risk.

<aside class="positive">
  <b>Interactive Elements:</b> Streamlit's input widgets are powerful tools for creating interactive applications that allow users to explore "what-if" scenarios and gain deeper insights from data and models.
</aside>

## Transaction Costs Impact Page
Duration: 00:05:00

Navigate to the "Transaction Costs Impact" page from the sidebar. This page (`pages/TransactionCosts.py`) demonstrates the effect of transaction costs on the efficient frontier.

**Page Content:**

*   **Title and Description:** The title "Transaction Costs Impact" and the markdown description clearly state the page's objective.
*   **Interactive Transaction Cost Input:**
    *   **`st.number_input("Buy Cost ...")`:** A number input allows users to set the buy transaction cost as a decimal value (e.g., 0.002 for 0.2%).
    *   **`st.number_input("Sell Cost ...")`:**  Similarly, a number input is provided for setting the sell transaction cost.
*   **Dummy Frontier Data with Transaction Costs:**
    *   **`risks = np.linspace(0.05, 0.30, 50)`:** Generates risk values as before.
    *   **`returns = 0.1 + 0.5 * risks - (buy_cost + sell_cost) * 10`:**  Calculates returns, but this time, it subtracts a term representing the impact of transaction costs.  The `(buy_cost + sell_cost) * 10` part is a simplified way to model the reduction in returns due to transaction costs.  The factor of 10 is arbitrary and for demonstration – in a real model, the impact would be calculated based on portfolio turnover and transaction costs.
*   **Visualization:**
    *   **Efficient Frontier Plot (with Transaction Costs):** The efficient frontier, now adjusted for transaction costs, is plotted as a line plot using Plotly.
    *   **Plot Customization:** Title and axis labels are set.
    *   **`st.plotly_chart(...)`:** The Plotly figure is displayed.

**Understanding Transaction Cost Impact:**

Transaction costs are the expenses incurred when buying or selling assets. They reduce the net returns of a portfolio. This page demonstrates how transaction costs shift the efficient frontier downwards.  Higher transaction costs lead to lower net returns for any given level of risk, resulting in a less favorable efficient frontier.

By adjusting the "Buy Cost" and "Sell Cost" inputs, users can observe how the efficient frontier shifts in response to changes in transaction costs. This highlights the importance of considering transaction costs in portfolio optimization, especially for strategies with high turnover.

<aside class="negative">
  <b>Simplification:</b> The way transaction costs are modeled here is a simplification. In reality, the impact of transaction costs is more complex and depends on factors like trading frequency, asset liquidity, and the specific trading strategy. However, this simplified model effectively demonstrates the general negative impact of transaction costs on portfolio returns.
</aside>

## Maximum Sharpe Ratio Portfolio Page
Duration: 00:04:00

Navigate to the "Maximum Sharpe Ratio Portfolio" page from the sidebar. This page (`pages/MaxSharpe.py`) demonstrates the concept of the Maximum Sharpe Ratio portfolio and visualizes it on the efficient frontier.

**Page Content:**

*   **Title and Description:** The title "Maximum Sharpe Ratio Portfolio" and the markdown description clearly define the page's purpose.
*   **Dummy Maximum Sharpe Portfolio Data:**
    *   **`max_sharpe_risk = 0.15`** and **`max_sharpe_return = 0.13`:** These are hardcoded values representing the risk and return of a hypothetical Maximum Sharpe Ratio portfolio. In a real application, this portfolio would be calculated through optimization.
*   **Dummy Efficient Frontier (Replicated):**  The same dummy efficient frontier data is generated as on previous pages.
*   **Visualization with Max Sharpe Portfolio Highlight:**
    *   **Efficient Frontier Plot:** The dummy efficient frontier is plotted.
    *   **Max Sharpe Portfolio Marker:** A green marker is added to the plot using `go.Scatter` to highlight the Maximum Sharpe Ratio portfolio.
    *   **Plot Customization:** Title and axis labels are set.
    *   **`st.plotly_chart(...)`:** The Plotly figure is displayed.
*   **Output Display:**
    *   **`st.write(f"Maximum Sharpe Portfolio -> Risk: ...")`:** The risk and return of the Maximum Sharpe Portfolio are displayed below the chart.

**Understanding the Maximum Sharpe Ratio Portfolio:**

The Sharpe Ratio is a measure of risk-adjusted return, calculated as (Portfolio Return - Risk-Free Rate) / Portfolio Risk. The Maximum Sharpe Ratio portfolio is the portfolio on the efficient frontier that maximizes this ratio. It represents the portfolio that provides the highest return per unit of risk taken.  It is often considered a desirable portfolio in investment management.

On this page, the Maximum Sharpe Ratio portfolio is pre-defined and visualized on the dummy efficient frontier. In a real application, finding the Maximum Sharpe Ratio portfolio involves optimization techniques that consider the risk-free rate, asset returns, risks, and covariances.

<aside class="positive">
  <b>Sharpe Ratio Importance:</b> The Sharpe Ratio is a widely used metric in finance for evaluating the risk-adjusted performance of investments. Understanding the Maximum Sharpe Ratio portfolio is crucial for portfolio optimization.
</aside>

## Conclusion
Duration: 00:02:00

Congratulations on completing the QuLab codelab! You've now explored the key functionalities of the QuLab Streamlit application and gained insights into fundamental portfolio optimization concepts.

**Key Takeaways:**

*   **Interactive Learning:** QuLab provides an interactive and visual platform for learning about portfolio optimization, making complex concepts more accessible and understandable.
*   **Streamlit for Financial Applications:** This codelab demonstrates how Streamlit can be effectively used to build interactive financial applications and dashboards. Its ease of use and built-in widgets make it ideal for prototyping and educational tools.
*   **Foundation for Further Exploration:** QuLab serves as a solid foundation for further exploration into portfolio optimization. You can expand upon this application by:
    *   Integrating real-world market data.
    *   Implementing actual portfolio optimization algorithms (e.g., Mean-Variance Optimization).
    *   Adding more sophisticated features, such as backtesting, scenario analysis, and different portfolio constraints.
    *   Exploring other financial concepts and models within the Streamlit framework.

We encourage you to experiment with the QuLab code, modify it, and build upon it to deepen your understanding of financial modeling and Streamlit application development. This codelab is just the beginning – the world of financial application development is vast and full of opportunities for innovation!
