# QuLab: Portfolio Optimization Examples Using Financial Toolbox

This repository contains a Streamlit multi-page application that demonstrates portfolio optimization techniques inspired by MATLAB Financial Toolbox examples.

## Features

- Interactive data visualizations using Plotly.
- Synthetic data generation to simulate BlueChipStockMoments.
- Multipage navigation covering:
  - Overview and Data Setup
  - Efficient Frontier Visualization
  - Target Portfolio Optimization
  - Transaction Costs Impact Analysis
  - Maximum Sharpe Ratio Portfolio

## Getting Started

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   streamlit run app.py
   ```

## Docker

A Dockerfile is provided. To build and run the Docker container:

   ```
   docker build -t qulab .
   docker run -p 8501:8501 qulab
   ```

© 2025 QuantUniversity. All Rights Reserved.
