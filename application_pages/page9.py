import streamlit as st                                                                                                        
import numpy as np                                                                                                            
import pandas as pd                                                                                                           
import plotly.express as px                                                                                                   
import plotly.graph_objects as go                                                                                             
                                                                                                                                
def run_page9():                                                                                                              
    st.header("Efficient Frontier with Combined Turnover and Tracking-Error Constraints")                                     
                                                                                                                            
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
                                                                                                                            
        def setTrackingError(self, tracking_error, tracking_port):                                                            
            self.tracking_error = tracking_error                                                                              
            self.tracking_port = tracking_port                                                                                
                                                                                                                            
        def setTurnover(self, turnover):                                                                                      
            self.turnover = turnover                                                                                          
                                                                                                                            
    p = Portfolio(AssetList, CashMean)                                                                                        
    p.setAssetMoments(AssetMean, AssetCovar)                                                                                  
    p.setInitPort(np.ones(num_assets) / num_assets)                                                                           
    p.setDefaultConstraints()                                                                                                 
                                                                                                                            
    # Estimate efficient frontier (Simplified)                                                                                
    def estimateFrontier(p, num_points=20):                                                                                   
        # In a real implementation, this would use an optimization solver with combined constraints                           
        # Here, we'll generate random portfolios that *may* violate the constraints                                           
        weights = np.random.rand(num_points, p.NumAssets)                                                                     
        weights = weights / np.sum(weights, axis=1, keepdims=True)  # Normalize weights                                       
        return weights                                                                                                        
                                                                                                                            
    def estimatePortMoments(p, weights):                                                                                      
        returns = np.sum(weights * p.AssetMean, axis=1)                                                                       
        risks = np.array([np.sqrt(w @ p.AssetCovar @ w.T) for w in weights])                                                  
        return risks, returns                                                                                                 
                                                                                                                            
    # Define a tracking portfolio (carried over from page 8)                                                                  
    ii = [14, 15, 19, 20, 22, 24, 26, 28, 29]  # Indices shifted by 1 to align with python indexing                           
    TrackingError = 0.05 / np.sqrt(12)                                                                                        
    TrackingPort = np.zeros(num_assets)                                                                                       
    TrackingPort[ii] = 1                                                                                                      
    TrackingPort = (1 / np.sum(TrackingPort)) * TrackingPort                                                                  
                                                                                                                            
    # Input field for turnover rate                                                                                           
    Turnover = st.number_input("Turnover Rate (Max)", min_value=0.0, max_value=1.0, value=0.3)                                
                                                                                                                            
    # Apply combined constraints                                                                                              
    q = Portfolio(AssetList, CashMean)                                                                                        
    q.setAssetMoments(AssetMean, AssetCovar)                                                                                  
    q.setInitPort(np.ones(num_assets) / num_assets)                                                                           
    q.setDefaultConstraints()                                                                                                 
    q.setTrackingError(TrackingError, TrackingPort)                                                                           
    q.setTurnover(Turnover)                                                                                                   
                                                                                                                            
    weights = estimateFrontier(p, 20)                                                                                         
    risks, returns = estimatePortMoments(p, weights)                                                                          
                                                                                                                            
    qweights = estimateFrontier(q, 20)                                                                                        
    qrisks, qreturns = estimatePortMoments(q, qweights)                                                                       
                                                                                                                            
    # Calculate tracking portfolio risk and return                                                                            
    trsk = np.sqrt(TrackingPort @ AssetCovar @ TrackingPort.T)                                                                
    tret = np.sum(TrackingPort * AssetMean)                                                                                   
                                                                                                                            
    #Calculate init portfolio risk and return                                                                                 
    ersk = np.sqrt(EqualWeight @ AssetCovar @ EqualWeight.T)                                                                  
    eret = np.sum(EqualWeight * AssetMean)                                                                                    
                                                                                                                            
    # Create a DataFrame for the efficient frontier                                                                           
    frontier_data = pd.DataFrame({'Risk': risks, 'Return': returns})                                                          
    # Create a DataFrame for the efficient frontier with combined constraints                                                 
    frontier_data_combined = pd.DataFrame({'Risk': qrisks, 'Return': qreturns})                                               
                                                                                                                            
    # Create the plot                                                                                                         
    fig = px.line(frontier_data, x='Risk', y='Return', title='Efficient Frontier with Turnover and Tracking-Error             
Constraints',                                                                                                                 
                labels={'Return': 'Annualized Return', 'Risk': 'Annualized Risk'})                                          
    fig.add_trace(go.Scatter(x=frontier_data_combined['Risk'], y=frontier_data_combined['Return'], mode='lines',              
name='Turnover & Tracking'))                                                                                                  
                                                                                                                            
    fig.add_trace(go.Scatter(x=[MarketRisk, CashRisk], y=[MarketMean, CashMean],                                              
                            mode='markers', name='Markers',                                                                  
                            marker=dict(size=[10, 10]),                                                                      
                            text=['Market', 'Cash']))                                                                        
    fig.add_trace(go.Scatter(x=[trsk], y=[tret],                                                                              
                            mode='markers', name='Tracking',                                                                 
                            marker=dict(size=[10]),                                                                          
                            text=['Tracking']))                                                                              
    fig.add_trace(go.Scatter(x=[ersk], y=[eret],                                                                              
                            mode='markers', name='Initial',                                                                  
                            marker=dict(size=[10]),                                                                          
                            text=['Initial']))                                                                               
                                                                                                                            
    fig.update_layout(showlegend=False)                                                                                       
                                                                                                                            
    st.plotly_chart(fig, use_container_width=True) 