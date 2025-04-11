import streamlit as st                                                                                                        
import numpy as np                                                                                                            
import pandas as pd                                                                                                           
import plotly.express as px                                                                                                   
import plotly.graph_objects as go                                                                                             
                                                                                                                                
def run_page13():                                                                                                             
    st.header("Efficient Frontier with Dollar-Neutral Hedge-Fund Structure")                                                  
                                                                                                                            
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
                                                                                                                            
        def setBounds(self, min_bound, max_bound):                                                                            
            self.min_bound = min_bound                                                                                        
            self.max_bound = max_bound                                                                                        
                                                                                                                            
        def setBudget(self, min_budget, max_budget):                                                                          
            self.min_budget = min_budget                                                                                      
            self.max_budget = max_budget                                                                                      
                                                                                                                            
        def setOnewayTurnover(self, long_turnover, short_turnover):                                                           
            self.long_turnover = long_turnover                                                                                
            self.short_turnover = short_turnover                                                                              
                                                                                                                            
    p = Portfolio(AssetList, CashMean)                                                                                        
    p.setAssetMoments(AssetMean, AssetCovar)                                                                                  
    p.setInitPort(np.zeros(num_assets))                                                                                       
    p.setDefaultConstraints()                                                                                                 
                                                                                                                            
    # Estimate efficient frontier (Simplified)                                                                                
    def estimateFrontier(p, num_points=20):                                                                                   
        # In a real implementation, this would use an optimization solver with dollar-neutral constraints                     
        # Here, we'll generate random portfolios that *may* violate the constraints                                           
        weights = np.random.rand(num_points, p.NumAssets)                                                                     
        weights = weights - 0.5  # Shift to allow negative weights (short positions)                                          
        weights = weights / np.sum(np.abs(weights), axis=1, keepdims=True) # normalize the weights so that the abs val sum to 1                                                                                                                          
        return weights                                                                                                        
                                                                                                                            
    def estimatePortMoments(p, weights):                                                                                      
        returns = np.sum(weights * p.AssetMean, axis=1)                                                                       
        risks = np.array([np.sqrt(w @ p.AssetCovar @ w.T) for w in weights])                                                  
        return risks, returns                                                                                                 
                                                                                                                            
    def estimateMaxSharpeRatio(p):                                                                                            
        # In a real implementation, solve optimization problem to maximize Sharpe Ratio                                       
        weights = np.random.rand(p.NumAssets)                                                                                 
        weights = weights = weights - 0.5 #Shift                                                                              
        weights = weights / np.sum(np.abs(weights)) #normalize                                                                
        return weights                                                                                                        
                                                                                                                            
    # Input field for exposure                                                                                                
    Exposure = st.number_input("Exposure", min_value=0.0, max_value=1.0, value=1.0)                                           
                                                                                                                            
    # Apply dollar-neutral constraints                                                                                        
    q = Portfolio(AssetList, CashMean)                                                                                        
    q.setAssetMoments(AssetMean, AssetCovar)                                                                                  
    q.setInitPort(np.zeros(num_assets))                                                                                       
    q.setBounds(-Exposure, Exposure)                                                                                          
    q.setBudget(0, 0)                                                                                                         
    q.setOnewayTurnover(Exposure, Exposure)                                                                                   
    q.setDefaultConstraints() #ensure long-only is false                                                                      
                                                                                                                            
    weights = estimateFrontier(p, 20)                                                                                         
    risks, returns = estimatePortMoments(p, weights)                                                                          
                                                                                                                            
    qweights = estimateFrontier(q, 20)                                                                                        
    qrisks, qreturns = estimatePortMoments(q, qweights)                                                                       
                                                                                                                            
    #Estimate Max Sharpe Ratio                                                                                                
    qswgt = estimateMaxSharpeRatio(q)                                                                                         
    qsrsk, qsret = estimatePortMoments(q, qswgt)                                                                              
                                                                                                                            
    # Create a DataFrame for the efficient frontier                                                                           
    frontier_data = pd.DataFrame({'Risk': risks, 'Return': returns})                                                          
    # Create a DataFrame for the efficient frontier with dollar-neutral constraints                                           
    frontier_data_neutral = pd.DataFrame({'Risk': qrisks, 'Return': qreturns})                                                
                                                                                                                            
    # Create the plot                                                                                                         
    fig = px.line(frontier_data, x='Risk', y='Return', title='Efficient Frontier with Dollar-Neutral Portfolio',              
                labels={'Return': 'Annualized Return', 'Risk': 'Annualized Risk'})                                          
    fig.add_trace(go.Scatter(x=frontier_data_neutral['Risk'], y=frontier_data_neutral['Return'], mode='lines',                
name='Dollar-Neutral'))                                                                                                       
    fig.add_trace(go.Scatter(x=[qsrsk], y=[qsret],                                                                            
                            mode='markers', name='Sharpe',                                                                   
                            marker=dict(size=[10]),                                                                          
                            text=['Sharpe']))                                                                                
                                                                                                                            
    fig.add_trace(go.Scatter(x=[MarketRisk, CashRisk, EqualRisk], y=[MarketMean, CashMean, EqualMean],                        
                            mode='markers', name='Markers',                                                                  
                            marker=dict(size=[10, 10, 10]),                                                                  
                            text=['Market', 'Cash', 'Equal']))                                                               
                                                                                                                            
    fig.update_layout(showlegend=False)                                                                                       
                                                                                                                            
    st.plotly_chart(fig, use_container_width=True)    