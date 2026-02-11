import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

st.title("Data vizualization App")
st.set_page_config(page_title="Data Viz App", layout="wide")

with st.expander("About this app"):
    data = pd.read_csv("train.csv")
    # data = st.file_uploader("Upload your CSV file", type=["csv"])
    # if data is not None:
    #     data = pd.read_csv(data)    

    st.write(data)

left_column, right_column = st.columns(2)

with left_column:
    st.header("Data Table")
    st.dataframe(data)

    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

    with tab1:
        st.subheader("Gender Analysis")
        gender = data['Sex'].value_counts()
        st.dataframe(gender)
        # st.bar_chart(gender)
        
    with tab2:
        st.subheader("Age Analysis")
        age_tab1, age_tab2 = st.tabs(["Age Stats", "Age Chart"])
        with age_tab1:
            age = data['Age'].describe()
            st.dataframe(age)
        with age_tab2:
            st.markdown("### Gender with the Highest Age")
            age_gender = data.groupby('Sex')['Age'].max()
            st.write(age_gender)

    with tab3:
        st.markdown("### Gender by the number of Survived Distribution")
        # data["Diealive"] = data["Survived"].map({0: "Non-survived", 1: "Survived"})
        data["alive_status"] = np.where(data["Survived"]==1, "Survived", "Non-survived")
        survived_gender = pd.pivot_table(data, index='Sex', columns='alive_status', values='PassengerId', aggfunc='count')
        st.dataframe(survived_gender)


# ---------------------------second column---------------------------
with right_column:
    st.header("Data Visualization")
    
    st.subheader("Passenger Class Distribution")
    pclass = data['Pclass'].value_counts()
    st.bar_chart(pclass)   


    tab_rig , tab_rig2 = st.tabs(["Survival Status", "Age Distribution"])

    with tab_rig:
        st.subheader("Survival Status Distribution")
        survived = data['Survived'].value_counts()
        # st.pie_chart(survived)
        st.bar_chart(survived)
        
    with tab_rig2:
        st.subheader("Age Distribution Histogram")      
        # st.histogram(data['Age'].dropna(), bins=30)

       


    # st.bar_chart(age)
    # st.line_chart(age)
    # st.area_chart(age)
    # st.pyplot(age)
    # st.altair_chart(age)
    # st.vega_lite_chart(age)
    # st.plotly_chart(age)
    # st.bokeh_chart(age)
    # st.deck_gl_chart(age)
    # st.map(age)
    # st.folium_chart(age)
    # st.graphviz_chart(age)
    # st.echarts_chart(age)
    # st.pydeck_chart(age)
    # st.cufflinks_chart(age)
    # st.gapminder_chart(age)
    # st.gauge_chart(age)
    # st.metric_chart(age)
    # st.heatmap(age)
    # st.scatter_chart(age)
    # st.line_chart(age)
    # st.area_chart(age)
    # st.bar_chart(age)
    # st.pie_chart(age)
    # st.histogram(age) 