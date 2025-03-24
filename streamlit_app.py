import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide", page_title="Galaxy Simulation Tree")

st.title("Galaxy Simulation Evolution Tree")

names = [
    "Benchmark", 
    "Benchmark/Star Formation", 
    "Benchmark/Star Formation/SN Feedback", 
    "Benchmark/Star Formation/SN Feedback/Protostellar", 
    "Benchmark/Star Formation/SN Feedback/Protostellar/AGN"
]

fig = px.treemap(
    names=names,
    path=[names],
    title="Click to Explore the Simulation Lineage"
)

st.plotly_chart(fig, use_container_width=True)
