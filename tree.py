from pyvis.network import Network

# Create the network (directed = arrows, height in px)
net = Network(height="700px", width="100%", directed=True)

# Disable physics for a cleaner tree layout
net.set_options("""
{
  "layout": {
    "hierarchical": {
      "direction": "UD",
      "sortMethod": "directed"
    }
  },
  "physics": {
    "enabled": false
  }
}
""")
# Add nodes (image, label, tooltip)
net.add_node("A", label="Benchmark", title="Gravity + Hydro only", shape="image", image="images/SF0DC.png")
net.add_node("B", label="Star Formation", title="Adds star formation model", shape="image", image="images/SF1DC.png")
net.add_node("C", label="SN Feedback", title="Adds supernova feedback", shape="image", image="images/SF2DC.png")

# Connect them
net.add_edge("A", "B")
net.add_edge("B", "C")

# Generate the interactive HTML file
#net.show("tree.html")
net.write_html("tree.html", open_browser=False, notebook=False)
