
## Overview

This document outlines the technical specifications for a Streamlit application designed to demonstrate various portfolio optimization concepts using synthetic data. The application aims to replicate the functionality and visualizations presented in the provided MATLAB examples related to portfolio optimization.

## Step-by-Step Generation Process

Here's a detailed breakdown of the steps required to build the Streamlit application:

1.  **Set Up the Data:**
    *   **Description**: Load the synthetic stock data from the `BlueChipStockMoments.mat` file. This file contains asset lists, mean returns, covariance matrix, and risk-free rate information.
    *   **Implementation**:
        *   Use `pandas` to read the `.mat` file.
        *   Extract `AssetList`, `AssetMean`, `AssetCovar`, `CashMean`, `CashVar`, `MarketMean`, and `MarketVar` into appropriate variables.
    *   **Markdown Output**:
        ```markdown
        ### 1. Set Up the Data

        We'll start by loading the synthetic data from the `BlueChipStockMoments.mat` file. This data includes asset information, returns, covariance, and risk-free rate.

        ```

2.  **Create a Portfolio Object:**
    *   **Description**: Instantiate a `Portfolio` object using the loaded data.  Set the asset list and risk-free rate.  Also, set the asset moments (mean and covariance).
    *   **Implementation**:
        *   Use the `Portfolio` class from the Financial Toolbox.
        *   Call the `setAssetMoments()` method to assign the mean and covariance to the `Portfolio` object.
    *   **Markdown Output**:
        ```markdown
        ### 2. Create a Portfolio Object

        Next, we'll create a `Portfolio` object, which will hold our asset data and enable optimization.

        ```

3.  **Set Up Optimization Problem:**
    *   **Description**: Define the default constraints for the portfolio optimization problem, including the "fully-invested" constraint (weights sum to 1) and the "long-only" constraint (no short selling).
    *   **Implementation**:
        *   Use the `setDefaultConstraints()` method of the `Portfolio` object.
    *   **Markdown Output**:
        ```markdown
        ### 3. Set Up Portfolio Optimization Problem

        Now, let's define the standard constraints: fully invested and long-only.

        ```

4.  **Illustrate the Tangent Line to the Efficient Frontier:**
    *   **Description**: Calculate and plot the efficient frontier. Then, calculate the portfolio allocations with cash using `setBudget`. Plot the tangent line that demonstrates the highest sharpe ratio with portfolio allocation with cash.
    *   **Implementation**:
        *   Create a copy of the `Portfolio` object.
        *   Use `setBudget()` to allow allocation between cash (0%) and risky assets (100%).
        *   Use `estimateFrontier()` to obtain the efficient frontier points.
        *   Use `estimatePortMoments()` to get risk and return values for each frontier portfolio.
        *   Plot both efficient frontier with risk assets and efficient frontier with cash as the tangent line.
    *   **Markdown Output**:
        ```markdown
        ### 4. Illustrate the Tangent Line to the Efficient Frontier

        This step visualizes Tobin's Separation Theorem by showing the tangent line from the risk-free asset to the efficient frontier.

        ```

5.  **Obtain Range of Risks and Returns:**
    *   **Description**: Determine the minimum and maximum risk and return values along the efficient frontier.
    *   **Implementation**:
        *   Use the `estimateFrontierLimits()` method to find the risk and return bounds.
        *   Use `estimatePortMoments` to convert to standard deviation/mean
    *   **Markdown Output**:
        ```markdown
        ### 5. Obtain Range of Risks and Returns

        Let's find the range of possible risk and return values on the efficient frontier.

        ```

6.  **Find a Portfolio with a Targeted Return and Targeted Risk:**
    *   **Description**: Find portfolios that match specific target return and risk levels.
    *   **Implementation**:
        *   Use the `estimateFrontierByReturn()` and `estimateFrontierByRisk()` methods to find portfolios that meet the target.
    *   **Markdown Output**:
        ```markdown
        ### 6. Find a Portfolio with a Targeted Return and Targeted Risk

        Now, we'll pinpoint portfolios with specific target return and risk levels on the frontier.

        ```

7.  **Transaction Costs:**
    *   **Description**: Introduce transaction costs (buying and selling costs) and observe their impact on the efficient frontier.
    *   **Implementation**:
        *   Use the `setCosts()` method to apply transaction costs to the `Portfolio` object.
        *   Estimate frontier with and without transaction costs.
        *   Plot efficient frontiers with/without costs.
    *   **Markdown Output**:
        ```markdown
        ### 7. Transaction Costs

        Here, we'll add transaction costs and see how they change the efficient frontier.

        ```

8.  **Turnover Constraint:**
    *   **Description**: Impose a constraint on portfolio turnover to limit trading activity.
    *   **Implementation**:
        *   Use `setTurnover()` function to constraint to a fraction that cannot be exceeded
    *   **Markdown Output**:
        ```markdown
        ### 8. Turnover Constraint

        We'll add a turnover constraint to limit how much the portfolio composition can change.

        ```

9.   **Tracking-Error Constraint:**
    *   **Description**: Constrain the portfolio to track a specified benchmark portfolio with a limited tracking error.
    *   **Implementation**:
        *   Use `setTrackingError()` method to set benchmark.
    *   **Markdown Output**:
        ```markdown
        ### 9. Tracking-Error Constraint

        We'll add a tracking-error constraint to limit the deviation from a benchmark portfolio.

        ```

10. **Combined Turnover and Tracking-Error Constraints:**
    *   **Description**:  Combine both turnover and tracking error constraints.
    *   **Implementation**:
        *   Implement by combining `setTurnover` and `setTrackingError` function
    *   **Markdown Output**:
        ```markdown
        ### 10. Combined Turnover and Tracking-Error Constraints

        We'll combine both the turnover and tracking-error constraints.

        ```

11. **Maximize the Sharpe Ratio:**
    *   **Description**: Identify the portfolio on the efficient frontier that maximizes the Sharpe ratio (risk-adjusted return).
    *   **Implementation**:
        *   Use the `estimateMaxSharpeRatio()` method to find the optimal portfolio.
    *   **Markdown Output**:
        ```markdown
        ### 11. Maximize the Sharpe Ratio

        Now, we'll find the portfolio with the highest Sharpe Ratio.

        ```

12. **Confirm that Maximum Sharpe Ratio is a Maximum:**
    *   **Description**: Show that the sharpe ratio is the max. This is done by plotting all portfolios and seeing that the tangent portfolio is located at the max
    *   **Implementation**:
        *   Plot efficient portfolios and plot their sharpe ratios.
        *   See that the max sharpe ratio is located where sharpe is the highest
    *   **Markdown Output**:
        ```markdown
        ### 12. Confirm that Maximum Sharpe Ratio is a Maximum

        We'll confirm that the found portfolio indeed maximizes the Sharpe ratio.

        ```

13. **Illustrate that Sharpe is the Tangent Portfolio:**
    *   **Description**: Plot efficient portfolios and demonstrate that sharpe is the tangency portfolio (portfolio that maximizes sharpe)
    *   **Implementation**:
        *   Use estimateMaxSharpeRatio to calculate Sharpe
    *   **Markdown Output**:
        ```markdown
        ### 13. Illustrate that Sharpe is the Tangent Portfolio

        We'll visually confirm that the maximum Sharpe ratio portfolio is the tangency portfolio.

        ```

14. **Dollar-Neutral Hedge-Fund Structure:**
    *   **Description**: Create a dollar-neutral portfolio, where the combined long and short positions sum to zero.
    *   **Implementation**:
        *   Use `setBounds`, `setBudget`, `setOnewayTurnover` to create a dollar-neutral portoflio
    *   **Markdown Output**:
        ```markdown
        ### 14. Dollar-Neutral Hedge-Fund Structure

        Finally, we'll construct a dollar-neutral hedge fund portfolio.

        ```

## Important Definitions, Examples, and Formulae

Here are some crucial definitions, examples, and formulas relevant to the application:

*   **Portfolio**: A collection of assets (e.g., stocks, bonds, cash).

*   **Mean Return**: The average return of an asset over a specific period.  Represented as *μ*.  For example, if a stock returns 10%, 12%, and 8% in three years, its mean return is (10 + 12 + 8) / 3 = 10%.

*   **Covariance Matrix**: A matrix that describes the relationships between the returns of different assets in a portfolio.  The element *σ<sub>ij</sub>* represents the covariance between asset *i* and asset *j*. If two assets tend to move in the same direction, their covariance is positive; if they move in opposite directions, it's negative.

*   **Risk-Free Rate**: The theoretical rate of return of an investment with zero risk.  Often proxied by the return on government bonds.

*   **Efficient Frontier**: The set of portfolios that offer the highest expected return for a given level of risk or the lowest risk for a given level of expected return.

*   **Sharpe Ratio**: A measure of risk-adjusted return, calculated as:

    ```
    Sharpe Ratio = (R_p - R_f) / σ_p
    ```

    Where:

    *   *R<sub>p</sub>* = Portfolio return
    *   *R<sub>f</sub>* = Risk-free rate
    *   *σ<sub>p</sub>* = Portfolio standard deviation (risk)

*   **Tobin's Separation Theorem**: States that all investors, regardless of their risk aversion, should hold the same portfolio of risky assets (the tangency portfolio) and adjust their risk exposure by holding different amounts of the risk-free asset.

*   **Transaction Costs**: The expenses incurred when buying or selling assets, expressed as a percentage of the transaction value.

*   **Turnover**: A measure of the trading activity in a portfolio, typically calculated as the sum of the absolute values of buys and sells, divided by the total portfolio value.  For example, if a portfolio has \$1,000,000 and the sum of buys and sells is \$200,000, the turnover is 20%.

*   **Tracking Error**:  The standard deviation of the difference between the portfolio's return and the benchmark's return. A low tracking error suggests the portfolio closely follows the benchmark.

*   **Dollar-Neutral**: A portfolio construction technique where the aggregate long exposure is equal to the aggregate short exposure, resulting in a net exposure of zero.  Used in hedge funds to isolate specific investment strategies.

## Libraries and Tools

The following Python libraries will be essential for building the Streamlit application:

*   **Streamlit**: For creating the interactive web application interface.
*   **Pandas**: For data manipulation and loading data from files (`.mat` in this case).
*   **NumPy**: For numerical computations, especially working with arrays and matrices (mean, covariances).
*   **Matplotlib/Plotly**: For creating the visualizations (graphs of efficient frontiers, asset distributions, etc.). If translating from MATLAB, Matplotlib is a good starting point. Plotly offers interactive visualizations.
*   **SciPy**: Might be needed for numerical optimization or certain financial calculations.
*   **Financial Toolbox:** This may be an optional component depending if this can be converted to existing Python packages such as PyPortfolioOpt or QuantLib.

These specifications provide a comprehensive guide for building the Streamlit application for portfolio optimization. Remember to convert the Matplotlib code from the MATLAB examples to Streamlit using functions like `st.pyplot()` or by using Plotly.


### Appendix Code in matlab that you need to convert to python

```code
```matlab
load BlueChipStockMoments
mret = MarketMean;
mrsk
sqrt (MarketVar);
cret = CashMean;
crsk = sqrt(CashVar);
```
```code
```matlab
p = Portfolio('AssetList', AssetList, 'RiskFreeRate', CashMean);
p
setAssetMoments (p, AssetMean, AssetCovar);
```
```code
```matlab
p = setInitPort (p,1/p.NumAssets);
[ersk, eret] = estimatePortMoments (p,p. InitPort);
```
```code
```matlab
clf;
portfolioexamples_plot('Asset Risks and Returns',
{'scatter', mrsk, mret, {'Market'}},
{'scatter', crsk, cret, {'Cash'}},
{'scatter', ersk, eret, {'Equal'}},
{'scatter', sqrt(diag (p. AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
p = setDefaultConstraints(p);
pwgt = estimateFrontier(p,20);
[prsk, pret] = estimatePortMoments (p,pwgt);
```
```code
```matlab
clf;
portfolioexamples_plot('Efficient Frontier',
{'line', prsk, pret},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag (p. AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
q = setBudget(p, 0, 1);
qwgt = estimateFrontier (q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
```
```code
```matlab
clf;
portfolioexamples_plot('Efficient Frontier with Tangent Line',
{'line', prsk, pret},
{'line', qrsk, qret, [], [], 1},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], { 'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag (p. AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
[rsk, ret] = estimatePortMoments (p, estimateFrontierLimits (p));
display(rsk)
```
```code
```matlab
display(ret)
```
```code
```matlab
TargetReturn 0.20;
TargetRisk = 0.15;
% Input target annualized return and risk here.
```
```code
```matlab
awgt = estimateFrontierBy Return (p, TargetReturn/12);
[arsk,aret] = estimatePortMoments (p,awgt);

bwgt = estimateFrontierByRisk (p, TargetRisk/sqrt(12));
[brsk, bret] = estimatePortMoments (p, bwgt);
```
```code
```matlab
clf;
portfolioexamples_plot('Efficient Frontier with Targeted Portfolios',
{'line', prsk, pret},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', arsk, aret, {sprintf('%g%% Return', 100*TargetReturn)}},
{'scatter', brsk, bret, {sprintf('%g%% Risk', 100*TargetRisk)}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
aBlotter = dataset ({100*awgt (awgt > 0), 'Weight' }, 'obsnames', p. AssetList(awgt > 0));
displayPortfolio (sprintf('Portfolio with %g%% Target Return', 100*TargetReturn), aBlotter, false);
```
```code
```matlab
bBlotter = dataset ({100*bwgt (bwgt > 0), 'Weight' }, 'obsnames', p. AssetList(bwgt > 0));
displayPortfolio (sprintf('Portfolio with %g%% Target Risk', 100*TargetRisk), bBlotter, false);
```
```code
```matlab
BuyCost = 0.0020;
SellCost = 0.0020;
q = setCosts (p, BuyCost, SellCost);
qwgt = estimateFrontier(q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
```
```code
```matlab
clf;
portfolioexamples_plot('Efficient Frontier with and without Transaction Costs',
{'line', prsk, pret, {'Gross'}, 'b'},
{'line', qrsk, qret, {'Net'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag (p. AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
BuyCost = 0.0020;
SellCost
0.0020;
Turnover = 0.2;
q = setCosts (p, BuyCost, SellCost);
q = setTurnover (q, Turnover);

[qwgt,qbuy,qsell] = estimateFrontier (q,20);
[qrsk, qret] = estimatePortMoments (q, qwgt);
```
```code
```matlab
clf;
portfolioexamples_plot('Efficient Frontier with Turnover Constraint',
{'line', prsk, pret, {'Unconstrained' }, ':b'},
{'line', qrsk, qret, {sprintf('%g%% Turnover', 100*Turnover)}},
{' 'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
displaySumOfTransactions (Turnover, qbuy, qsell)
```
```code
```matlab
ii = [15, 16, 20, 21, 23, 25, 27, 29, 30];
TrackingError = 0.05/sqrt(12);
TrackingPort = zeros(30, 1);
TrackingPort(ii) = 1;
% Indexes of assets to include in the tracking portfolio.
TrackingPort = (1/sum (TrackingPort)) *TrackingPort;
```
```code
```matlab
q = setTrackingError (p, TrackingError, TrackingPort);
qwgt = estimateFrontier(q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
[trsk, tret] = estimatePortMoments (q, TrackingPort);
```
```code
```matlab
clf;
portfolioexamples_plot('Efficient Frontier with 5% Tracking-Error Constraint',
{'line', prsk, pret, {'Unconstrained'}, ':b'},
{'line', qrsk, qret, {'Tracking'}},
{'scatter', [mrsk, crsk], [mret, cret], {'Market', 'Cash'}},
{'scatter', trsk, tret, {'Tracking'}, 'r'});
```
```code
```matlab
Turnover = 0.3;
InitPort = (1/q. NumAssets) *ones (q.NumAssets, 1);
ii = [15, 16, 20, 21, 23, 25, 27, 29, 30];
TrackingError = 0.05/sqrt(12);
TrackingPort = zeros(30, 1);
TrackingPort(ii) = 1;
% Indexes of assets to include in tracking portfolio.
TrackingPort = (1/sum (TrackingPort)) *TrackingPort;
```
```code
```matlab
q = setTurnover (q, Turnover, InitPort);
qwgt = estimateFrontier(q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
[trsk, tret] = estimatePortMoments (q, TrackingPort);
[ersk, eret] = estimatePortMoments (q, InitPort);
```
```code
```matlab
clf;
portfolioexamples_plot('Efficient Frontier with Turnover and Tracking-Error Constraint',
{'line', prsk, pret, {'Unconstrained'}, ':b'},
{'line', qrsk, qret, {'Turnover & Tracking'}},
{'scatter', [mrsk, crsk], [mret, cret], { 'Market', 'Cash'}},
{'scatter', trsk, tret, {'Tracking'}, 'r'},
{'scatter', ersk, eret, {'Initial'}, 'b'});
```
```code
```matlab
p = setInitPort(p, 0);
swgt = estimateMaxSharpeRatio(p);
[srsk, sret] = estimatePortMoments (p,swgt);
```
```code
```matlab
clf;
portfolioexamples_plot('Efficient Frontier with Maximum Sharpe Ratio Portfolio',
{'line', prsk, pret},
{'scatter', srsk, sret, {'Sharpe'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
Blotter = dataset({100*swgt (swgt > 0), 'Weight'}, 'obsnames', AssetList(swgt > 0));
displayPortfolio ('Portfolio with Maximum Sharpe Ratio', Blotter, false);
```
```code
```matlab
psratio = (pret p. RiskFreeRate) ./ prsk;
ssratio (sret p.RiskFreeRate) / srsk;
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
```matlab
q = setBudget(p, 0, 1);
qwgt = estimateFrontier (q,20);
[qrsk, qret] = estimatePortMoments (q,qwgt);
```
```code
```matlab
clf;
portfolioexamples_plot('Efficient Frontier with Maximum Sharpe Ratio Portfolio',
{'line', prsk, pret},
{'line', qrsk, qret, [], [], 1},
{'scatter', srsk, sret, {'Sharpe'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], {'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
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
```matlab
clf;
portfolioexamples_plot('Efficient Frontier with Dollar-Neutral Portfolio',
{'line', prsk, pret, {'Standard' }, 'b:'},
{'line', qrsk, qret, { 'Dollar-Neutral'}, 'b'},
{'scatter', qsrsk, qsret, {'Sharpe'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], { 'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag(p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
Blotter = dataset({100*qswgt (abs(qswgt) > 1.0e-4), 'Weight'},
{100*qslong(abs(qswgt) > 1.0e-4), 'Long'},
{100*qsshort(abs (qswgt) > 1.0e-4), 'Short'},
'obsnames', AssetList(abs (qswgt) > 1.0e-4));
displayPortfolio('Dollar-Neutral Portfolio with Maximum Sharpe Ratio', Blotter, true, 'Dollar-Neutral');
```
```code
```matlab
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
```matlab
clf;
portfolioexamples_plot(sprintf('Efficient Frontier with %g-%g Portfolio',
100*(1 + Leverage), 100*Leverage),
{'line', prsk, pret, {'Standard' }, 'b:'},
{'line', qrsk, qret, {'130-30'}, 'b'},
{'scatter', qsrsk, qsret, {'Sharpe'}},
{'scatter', [mrsk, crsk, ersk], [mret, cret, eret], { 'Market', 'Cash', 'Equal'}},
{'scatter', sqrt(diag (p.AssetCovar)), p. AssetMean, p. AssetList, '.r'});
```
```code
```matlab
Blotter = dataset ({100*qswgt (abs (qswgt) > 1.0e-4), 'Weight'},
{100*qslong(abs (qswgt) > 1.0e-4), 'Long'},
{100*qsshort (abs (qswgt) > 1.0e-4), 'Short'},
'obsnames', AssetList (abs (qswgt) > 1.0e-4));
displayPortfolio (sprintf('%g-%g Portfolio with Maximum Sharpe Ratio', 100* (1 + Leverage), 100* Leverage), Blotter, true, sprintf('%g-%g',
```
```code
```matlab
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
fprintf('%.4f
, [ sum (Blotter. Weight), sum (Blotter. Long), sum (Blotter. Short) ]);
end
end
```