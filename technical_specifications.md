
# Technical Specifications for Streamlit Financial Toolbox Portfolio Optimization Application

## Overview

This Streamlit application provides an interactive environment for exploring portfolio optimization concepts. It replicates the functionality of the MATLAB Financial Toolbox examples, focusing on mean-variance optimization and extensions such as transaction costs, turnover constraints, and Sharpe ratio maximization. The application utilizes synthetic data (based on `BlueChipStockMoments.mat`), allowing users to experiment with different optimization scenarios. The primary goal is to provide a visual and intuitive understanding of portfolio optimization.

## Step-by-Step Generation Process

1.  **Set Up the Data:**
    *   **Input:**  The application will load the synthetic data from the uploaded (or pre-loaded) `BlueChipStockMoments.mat` dataset. This data contains `AssetList`, `AssetMean`, `AssetCovar`, `CashMean`, `CashVar`, `MarketMean`, and `MarketVar`.
    *   **Processing:** Calculate the standard deviations for market and cash returns.
    *   **Visualization:** A scatter plot showing the annualized mean returns and standard deviations of individual assets.  The market, cash, and equal-weighted portfolios are also plotted.

2.  **Create a Portfolio Object:**
    *   **Code:**
        ```python
        p = Portfolio('AssetList', AssetList, 'RiskFreeRate', CashMean)
        p.setAssetMoments(AssetMean, AssetCovar)
        p = setInitPort(p,1/p.NumAssets)
        ```
    *   **Description:** Instantiate a `Portfolio` object, initializing it with the asset list, risk-free rate (cash mean), and asset moments (mean and covariance). An equal-weighted portfolio is then set as the initial portfolio.

3.  **Set Up the Optimization Problem:**
    *   **Code:**
        ```python
        p = setDefaultConstraints(p)
        ```
    *   **Description:** This applies default constraints, which enforce a fully-invested, long-only portfolio strategy (non-negative weights that sum to 1).

4.  **Illustrate the Tangent Line to the Efficient Frontier:**
    *   **Processing:** Create a copy of the Portfolio object and add a budget constraint that allows allocation between cash (0%) and risky assets (100%). The efficient frontier is then estimated for the modified portfolio.
        ```python
        q = setBudget(p, 0, 1)
        qwgt = estimateFrontier(q,20)
        [qrsk, qret] = estimatePortMoments(q,qwgt)
        ```
    *   **Visualization:** A line plot of the efficient frontier, along with the tangent line originating from the risk-free rate (cash) to the efficient frontier.

5.  **Obtain Range of Risks and Returns:**
    *   **Processing:** Estimate the limits (minimum and maximum) of risks and returns along the efficient frontier.
        ```python
        [rsk, ret] = estimatePortMoments(p, estimateFrontierLimits(p))
        ```
    *   **Output:** Display the minimum and maximum risk and return values in a table or text format.

6.  **Find a Portfolio with a Targeted Return and Targeted Risk:**
    *   **Input:** Provide numeric input fields for `TargetReturn` and `TargetRisk`.
    *   **Processing:** Use the `estimateFrontierByReturn` and `estimateFrontierByRisk` functions to find portfolios that match the specified target values.
        ```python
        awgt = estimateFrontierByReturn(p, TargetReturn/12)
        [arsk, aret] = estimatePortMoments(p,awgt)

        bwgt = estimateFrontierByRisk(p, TargetRisk/sqrt(12))
        [brsk, bret] = estimatePortMoments(p, bwgt)
        ```
    *   **Visualization:** Display a scatter plot of the efficient frontier with the targeted portfolios highlighted.

7.  **Transactions Costs:**
    *   **Input:** Numeric input fields for `BuyCost` and `SellCost`.
    *   **Processing:** Apply the transaction costs to the portfolio object and re-estimate the efficient frontier.
        ```python
        q = setCosts(p, BuyCost, SellCost)
        qwgt = estimateFrontier(q,20)
        [qrsk, qret] = estimatePortMoments(q,qwgt)
        ```
    *   **Visualization:** Overlays the efficient frontier plot with transaction cost on to the efficient frontier plot without transaction cost.

8.  **Turnover Constraint:**
    *   **Input:** Numeric input field for `Turnover` (maximum turnover rate).
    *   **Processing:** Add a turnover constraint to the portfolio object and compute the efficient frontier.
        ```python
        q = setTurnover(p, Turnover)
        [qwgt,qbuy,qsell] = estimateFrontier (q,20)
        [qrsk, qret] = estimatePortMoments (q, qwgt)
        ```
    *   **Visualization:** Plots the efficient frontier with the turnover constraint overlaid on the unconstrained efficient frontier. Also display the total purchases and sales.

9.  **Tracking-Error Constraint:**
    *   **Processing:** Define a tracking portfolio using a subset of assets.  Add a tracking-error constraint to the portfolio object, specifying the maximum allowable tracking error and the tracking portfolio weights. Estimate the efficient frontier.
    ```python
    ii = [15, 16, 20, 21, 23, 25, 27, 29, 30]
    TrackingError = 0.05/sqrt(12)
    TrackingPort = zeros(30, 1)
    TrackingPort(ii) = 1
    TrackingPort = (1/sum (TrackingPort)) *TrackingPort

    q = setTrackingError (p, TrackingError, TrackingPort)
    qwgt = estimateFrontier(q,20)
    [qrsk, qret] = estimatePortMoments (q,qwgt)
    [trsk, tret] = estimatePortMoments (q, TrackingPort)
    ```
    *   **Visualization:** Overlays efficient frontier with tracking error contraint on the unconstrained efficient frontier.

10. **Combined Turnover and Tracking-Error Constraints:**
    *   **Input:** Numeric input field for `Turnover`. The `TrackingPort` is carried from the previous section.
    *   **Processing:** Combines both Turnover and Tracking Error Constraints.
    *   **Visualization:** Overlays efficient frontier with the combined contraints on the unconstrained efficient frontier.

11. **Maximize the Sharpe Ratio:**
    *   **Processing:** Use the `estimateMaxSharpeRatio` function to find the portfolio that maximizes the Sharpe ratio.
        ```python
        swgt = estimateMaxSharpeRatio(p)
        [srsk, sret] = estimatePortMoments(p,swgt)
        ```
    *   **Visualization:** Plot the efficient frontier and highlight the maximum Sharpe ratio portfolio. The lower graph shows the risk to sharpe ratio on the efficient frontier to illustrate where the Sharpe Ratio is maximized.

12. **Confirm that Maximum Sharpe Ratio is a Maximum:**
    *   **Description:** Plot the Sharpe ratio for each portfolio along the efficient frontier, showing that the calculated maximum Sharpe ratio is indeed the highest point. This is shown through two subplots that each have efficient frontier and sharpe ratios respectively.

13. **Illustrate that Sharpe is the Tangent Portfolio:**
    *   **Description:** Demonstrate Tobin's separation theorem again by adding a budget constraint on the portfolio, making it a tangent portfolio.
    *   **Visualization:** Superimposes an efficient frontier of a "tangency portfolio" to demonstrate that the portfolio that maximizes the Sharpe Ratio also lies on this frontier.

14. **Dollar-Neutral Hedge-Fund Structure:**
    *   **Input:** Numeric input field for `Exposure`.
    *   **Processing:** Set the bounds for assets to lie between -Exposure and Exposure, set the budget constraint to 0, and utilize the oneway turnover for long and short restrictions.
    ```python
    Exposure = 1
    q = setBounds (p, - Exposure, Exposure)
    q = setBudget(q, 0, 0)
    q = setOneway Turnover (q, Exposure, Exposure, 0)
    [qwgt,qlong,qshort] = estimateFrontier (q,20)
    [qrsk, qret] = estimatePortMoments (q, qwgt)
    ```
    *   **Visualization:** Show the efficient frontier for dollar-neutral portfolio with tangency portfolio
## Important Definitions, Examples, and Formulae

*   **Portfolio:** A collection of assets held by an investor.
*   **Asset:** A financial instrument, such as a stock or bond, that has value.
*   **Return:** The profit or loss made on an investment over a period of time, usually expressed as a percentage.
*   **Risk:** The uncertainty of future returns on an investment, often measured by standard deviation or variance.
*   **Mean Return:** The average return of an asset or portfolio over a period of time.  Calculated as:

    $\mu = \frac{1}{n} \sum_{i=1}^{n} r_i$

    where $r_i$ are the individual returns and $n$ is the number of returns.

*   **Standard Deviation (Risk):** A measure of the dispersion of returns around the mean return.  A higher standard deviation indicates greater risk. Calculated as:

    $\sigma = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (r_i - \mu)^2}$

*   **Covariance:** A measure of how two assets' returns move together.  A positive covariance indicates that the assets tend to move in the same direction, while a negative covariance indicates that they tend to move in opposite directions.

    $Cov(X,Y) = \frac{\sum_{i=1}^{n}(X_i - \bar{X})(Y_i - \bar{Y})}{n-1}$

*   **Efficient Frontier:** The set of portfolios that provide the highest possible expected return for a given level of risk, or the lowest possible risk for a given level of expected return.
*   **Sharpe Ratio:** A measure of risk-adjusted return.  It is calculated as the excess return (return above the risk-free rate) divided by the standard deviation. A higher Sharpe ratio indicates better risk-adjusted performance.

    $Sharpe Ratio = \frac{R_p - R_f}{\sigma_p}$

    where:
    *   $R_p$ = Portfolio return
    *   $R_f$ = Risk-free rate
    *   $\sigma_p$ = Portfolio standard deviation

*   **Risk-Free Rate:** The rate of return on a risk-free investment, such as a government bond.
*   **Long-Only Portfolio:** A portfolio that only contains long positions (i.e., investments that profit from an increase in price).
*   **Fully-Invested Portfolio:** A portfolio where all available capital is invested in assets.
*   **Transaction Costs:** The expenses incurred when buying or selling assets.
*   **Turnover:** A measure of how much of a portfolio is bought or sold over a period of time.
*   **Tracking Error:** A measure of how closely a portfolio's returns match the returns of a benchmark index or tracking portfolio.
*   **Tracking Portfolio:** A portfolio intended to track an index.
*   **Dollar-Neutral Portfolio:** A portfolio with equal long and short positions, resulting in a net investment of zero.

## Libraries and Tools

*   **Streamlit:** The core library for creating the web application. Used for layout, user input, displaying data, and rendering plots. (`st.pyplot()`, `st.sidebar`, `st.number_input`, `st.write`)
*   **NumPy:** Used for numerical computations, especially for creating and manipulating arrays of data.
*   **Pandas:** Utilized for data manipulation and analysis, particularly for creating and displaying DataFrames.
*   **Matplotlib:** Used for creating static, interactive, and animated visualizations in Python. Used for generating the plots, which are then displayed in Streamlit using `st.pyplot()`.
*   **Scikit-learn:**  Could be used for optimization algorithms, however based on the matlab code, core python optimization is done.
*   **Potentially Portfolio Optimization Libraries:**  Libraries such as `PyPortfolioOpt` or `cvxpy` *could* be used, but the problem description implies replication of a matlab framework, so these are not strictly necessary but may simplify portions of the task.



### Appendix Code

```code
```code
load BlueChipStockMoments
mret = MarketMean;
mrsk = sqrt (MarketVar);
cret = CashMean;
crsk = sqrt(CashVar);
```
```code
p = Portfolio('AssetList', AssetList, 'RiskFreeRate', CashMean);
p = setAssetMoments (p, AssetMean, AssetCovar);
```
```code
p = setInitPort (p,1/p.NumAssets);
[ersk, eret] = estimatePortMoments (p,p. InitPort);
```
```code
clf;
portfolioexamples_plot('Asset Risks and Returns',
{'scatter', mrsk, mret, {'Market'}},
{'scatter', crsk, cret, {'Cash'}},
{'scatter', ersk, eret, {'Equal'}},
{'scatter', sqrt(diag (p. AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
p = setDefaultConstraints(p);
pwgt = estimateFrontier(p,20);
[prsk, pret] = estimatePortMoments (p,pwgt);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier',
{'line', prsk, pret},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag (p. AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
q = setBudget(p, 0, 1);
qwgt = estimateFrontier (q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier with Tangent Line',
{'line', prsk, pret},
{'line', qrsk, qret, [], [], 1},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], { 'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag (p. AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
[rsk, ret] = estimatePortMoments (p, estimateFrontierLimits (p));
display(rsk)
```
```code
display(ret)
```
```code
TargetReturn 0.20;
TargetRisk = 0.15;
```
```code
awgt = estimateFrontierBy Return (p, TargetReturn/12);
[arsk,aret] = estimatePortMoments (p,awgt);
bwgt = estimateFrontierByRisk (p, TargetRisk/sqrt(12));
[brsk, bret] = estimatePortMoments (p, bwgt);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier with Targeted Portfolios',
{'line', prsk, pret},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', arsk, aret, {sprintf('%g%% Return', 100*TargetReturn)}},
{'scatter', brsk, bret, {sprintf('%g%% Risk', 100*TargetRisk)}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
aBlotter = dataset ({100*awgt (awgt > 0), 'Weight' }, 'obsnames', p. AssetList(awgt > 0));
displayPortfolio (sprintf('Portfolio with %g%% Target Return', 100*TargetReturn), aBlotter, false);
```
```code
bBlotter = dataset ({100*bwgt (bwgt > 0), 'Weight' }, 'obsnames', p. AssetList(bwgt > 0));
displayPortfolio (sprintf('Portfolio with %g%% Target Risk', 100*TargetRisk), bBlotter, false);
```
```code
BuyCost = 0.0020;
SellCost = 0.0020;
q = setCosts (p, BuyCost, SellCost);
qwgt = estimateFrontier(q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier with and without Transaction Costs',
{'line', prsk, pret, {'Gross'}, 'b'},
{'line', qrsk, qret, {'Net'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag (p. AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
BuyCost = 0.0020;
SellCost = 0.0020;
Turnover = 0.2;
q = setCosts (p, BuyCost, SellCost);
q = setTurnover (q, Turnover);
[qwgt,qbuy,qsell] = estimateFrontier (q,20);
[qrsk, qret] = estimatePortMoments (q, qwgt);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier with Turnover Constraint',
{'line', prsk, pret, {'Unconstrained' }, ':b'},
{'line', qrsk, qret, {sprintf('%g%% Turnover', 100*Turnover)}},
{' 'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
displaySumOfTransactions (Turnover, qbuy, qsell)
```
```code
ii = [15, 16, 20, 21, 23, 25, 27, 29, 30];
TrackingError = 0.05/sqrt(12);
TrackingPort = zeros(30, 1);
TrackingPort(ii) = 1;
TrackingPort = (1/sum (TrackingPort)) *TrackingPort;
q = setTrackingError (p, TrackingError, TrackingPort);
qwgt = estimateFrontier(q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
[trsk, tret] = estimatePortMoments (q, TrackingPort);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier with 5% Tracking-Error Constraint',
{'line', prsk, pret, {'Unconstrained'}, ':b'},
{'line', qrsk, qret, {'Tracking'}},
{'scatter', [mrsk, crsk], [mret, cret, eret], {'Market', 'Cash'}},
{'scatter', trsk, tret, {'Tracking'}, 'r'});
```
```code
Turnover = 0.3;
InitPort = (1/q. NumAssets) *ones (q.NumAssets, 1);
ii = [15, 16, 20, 21, 23, 25, 27, 29, 30];
TrackingError = 0.05/sqrt(12);
TrackingPort = zeros(30, 1);
TrackingPort(ii) = 1;
TrackingPort = (1/sum (TrackingPort)) *TrackingPort;
q = setTurnover (q, Turnover, InitPort);
qwgt = estimateFrontier(q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
[trsk, tret] = estimatePortMoments (q, TrackingPort);
[ersk, eret] = estimatePortMoments (q, InitPort);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier with Turnover and Tracking-Error Constraint',
{'line', prsk, pret, {'Unconstrained'}, ':b'},
{'line', qrsk, qret, {'Turnover & Tracking'}},
{'scatter', [mrsk, crsk], [mret, cret, eret], { 'Market', 'Cash'}},
{'scatter', trsk, tret, {'Tracking'}, 'r'},
{'scatter', ersk, eret, {'Initial'}, 'b'});
```
```code
p = setInitPort(p, 0);
swgt = estimateMaxSharpeRatio(p);
[srsk, sret] = estimatePortMoments (p,swgt);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier with Maximum Sharpe Ratio Portfolio',
{'line', prsk, pret},
{'scatter', srsk, sret, {'Sharpe'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
Blotter = dataset({100*swgt (swgt > 0), 'Weight'}, 'obsnames', AssetList(swgt > 0));
displayPortfolio ('Portfolio with Maximum Sharpe Ratio', Blotter, false);
```
```code
psratio = (pret p. RiskFreeRate) ./ prsk;
ssratio = (sret p.RiskFreeRate) / srsk;
clf;
subplot(2,1,1);
plot(prsk, pret, 'LineWidth', 2);
hold on
scatter (srsk, sret, 'g', 'filled');
title('\bfEfficient Frontier');
xlabel('Portfolio Risk');
ylabel('Portfolio Return');
hold off
subplot(2,1,2);
plot(prsk, psratio, 'LineWidth', 2);
hold on
scatter (srsk, ssratio, 'g', 'filled');
title('\bfSharpe Ratio');
xlabel('Portfolio Risk');
ylabel('Sharpe Ratio');
hold off
```
```code
q = setBudget(p, 0, 1);
qwgt = estimateFrontier (q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier with Maximum Sharpe Ratio Portfolio',
{'line', prsk, pret},
{'line', qrsk, qret, [], [], 1},
{'scatter', srsk, sret, {'Sharpe'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag (p. AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
Exposure = 1;
q = setBounds (p, - Exposure, Exposure);
q = setBudget(q, 0, 0);
q = setOneway Turnover (q, Exposure, Exposure, 0);
[qwgt,qlong,qshort] = estimateFrontier (q,20);
[qrsk, qret] = estimatePortMoments (q, qwgt);
[qswgt,qslong, qsshort] = estimateMaxSharpeRatio (q);
[qsrsk, qsret] = estimatePortMoments (q, qswgt);
```
```code
clf;
portfolioexamples_plot('Efficient Frontier with Dollar-Neutral Portfolio',
{'line', prsk, pret, {'Standard' }, 'b:'},
{'line', qrsk, qret, { 'Dollar-Neutral'}, 'b'},
{'scatter', qsrsk, qsret, {'Sharpe'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], { 'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
Blotter = dataset({100*qswgt (abs(qswgt) > 1.0e-4), 'Weight'},
{100*qslong(abs(qswgt) > 1.0e-4), 'Long'},
{100*qsshort(abs (qswgt) > 1.0e-4), 'Short'},
'obsnames', AssetList(abs (qswgt) > 1.0e-4));
displayPortfolio('Dollar-Neutral Portfolio with Maximum Sharpe Ratio', Blotter, true, 'Dollar-Neutral');
```
```code
Leverage = 0.3;
q = setBounds (p, Leverage, 1 + Leverage);
q = setBudget(q, 1, 1);
q = setOneway Turnover (q, 1 + Leverage, Leverage);
[qwgt,qbuy, qsell] = estimateFrontier (q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
[qswgt,qslong, qsshort] = estimateMaxSharpeRatio (q);
[qsrsk, qsret] = estimatePortMoments (q, qswgt);
```
```code
clf;
portfolioexamples_plot(sprintf('Efficient Frontier with %g-%g Portfolio',
100*(1 + Leverage), 100*Leverage),
{'line', prsk, pret, {'Standard' }, 'b:'},
{'line', qrsk, qret, {'130-30'}, 'b'},
{'scatter', qsrsk, qsret, {'Sharpe'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], { 'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
function display SumOfTransactions (Turnover, qbuy, qsell)
fprintf('Sum of Purchases by Portfolio along Efficient Frontier (Max. Turnover %g%%)\n',
100*Turnover);
fprintf('%.4f', 100*sum (qbuy)), sprintf('\n\n');
fprintf('\n')
fprintf('Sum of Sales by Portfolio along Efficient Frontier (Max. Turnover %g%%)\n',
100*Turnover);
fprintf('%.4f', 100*sum(qsell));
end
function display Portfolio (Description, Blotter, LongShortFlag, portfolioType)
fprintf('%s\n', Description);
disp(Blotter);
if (LongShortFlag)
fprintf('Confirm %s Portfolio\n', portfolioType);
fprintf(' (Net, Long, Short)\n');
fprintf('%.4f , [ sum (Blotter. Weight), sum (Blotter. Long), sum (Blotter. Short) ]);
end
end
```