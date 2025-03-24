import streamlit as st
import plotly.graph_objects as go

st.title("Manual Layout: Galaxy Tree")

fig = go.Figure()

nodes = [
    {"name": "Benchmark", "x": 0.1, "y": 0.5},
    {"name": "Star Formation", "x": 0.3, "y": 0.5},
    {"name": "SN Feedback", "x": 0.5, "y": 0.5},
    {"name": "Protostellar", "x": 0.7, "y": 0.5},
    {"name": "AGN", "x": 0.9, "y": 0.5}
]

# Add rectangles for each node
for node in nodes:
    fig.add_shape(
        type="rect",
        x0=node["x"] - 0.05, x1=node["x"] + 0.05,
        y0=node["y"] - 0.1, y1=node["y"] + 0.1,
        line=dict(color="black"),
        fillcolor="lightblue"
    )
    fig.add_annotation(
        x=node["x"], y=node["y"],
        text=node["name"],
        showarrow=False,
        font=dict(size=12)
    )

# Draw arrows
for i in range(len(nodes) - 1):
    fig.add_annotation(
        x=nodes[i+1]["x"] - 0.05, y=nodes[i+1]["y"],
        ax=nodes[i]["x"] + 0.05, ay=nodes[i]["y"],
        xref="x", yref="y",
        axref="x", ayref="y",
        showarrow=True,
        arrowhead=2
    )

fig.update_layout(
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    title="Manual Simulation Evolution Tree",
    height=300,
    margin=dict(l=0, r=0, t=40, b=0)
)

st.plotly_chart(fig, use_container_width=True)

