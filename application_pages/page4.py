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