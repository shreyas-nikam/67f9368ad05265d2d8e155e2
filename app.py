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