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