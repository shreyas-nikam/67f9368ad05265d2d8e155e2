
import streamlit as st

st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

# Your code goes here
page = st.sidebar.selectbox(label="Navigation", options=["Page 1", "Page 2", "Page 3"])

if page == "Page 1":
    try:
        from application_pages.page1 import run_page1
        run_page1()
    except Exception as e:
        st.error(f"An error occurred while loading Page 1: {e}")
elif page == "Page 2":
    try:
        from application_pages.page2 import run_page2
        run_page2()
    except Exception as e:
        st.error(f"An error occurred while loading Page 2: {e}")
elif page == "Page 3":
    try:
        from application_pages.page3 import run_page3
        run_page3()
    except Exception as e:
        st.error(f"An error occurred while loading Page 3: {e}")
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
