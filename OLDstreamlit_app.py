import streamlit as st
import base64

# Load the image and convert to base64
def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.set_page_config(page_title="The Mochima Simulations Evolution Tree", layout="centered")

# Title and subtitle
st.markdown("<h1 style='text-align: center;'>The Mochima Simulation</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>An interactive walkthrough of how subgrid physics change a simulated galaxy</h3>", unsafe_allow_html=True)

# Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    start = st.button("🚀 Start Exploration", use_container_width=True)

# Show perfectly centered image
if start:
    img_data = get_base64_image("images/SF0DC.png")

    # Create two columns
    col1, col2 = st.columns([1, 2])  # Wider right side for text

    with col1:
        st.markdown(
                    f"""
                    <div style='text-align: center;'>
                        <img src='data:image/png;base64,{img_data}' width='200'/>
                        <p style='font-style: italic;'>Benchmark Simulation</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                    )
    with col2:
        # Short description
        st.markdown("Models:")

        # Expandable sections
        with st.expander("🌟 Star Formation"):
            st.write("A fixed starformation efficiency based on gas density thresholds. Stars form in dense, cold regions and the model is calibrated following a Schmidt law.")

        with st.expander("💥 Supernova Feedback"):
            st.write("Delayed Cooling, the cooling of the gas is stopped arround the site of a supernova explotion for a predefined calibrated time.")
