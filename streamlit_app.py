import streamlit as st
import base64

def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(page_title="The Mochima Simulations Evolution Tree", layout="centered")

if "start" not in st.session_state:
    st.session_state.start = False

if "sf_turb" not in st.session_state:
    st.session_state.sf_turb = False




# Title and subtitle
st.markdown("<h1 style='text-align: center;'>The Mochima Simulation</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>An interactive walkthrough of how subgrid physics change a simulated galaxy</h3>", unsafe_allow_html=True)

# Centered Start button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Start Exploration", use_container_width=True):
        st.session_state.start = True

# After click: show image + expanders
if st.session_state.start:
    st.markdown("## Simulation Step 1")
    col1, col2 = st.columns([1, 2])

    with col1:
        img_data = get_base64_image("images/SF0DC.png")
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
        st.markdown("### Included Physics Models")
        with st.expander("🌟 Star Formation"):
            st.write("A fixed star formation efficiency based on gas density thresholds. Stars form in dense, cold regions and the model is calibrated following a Schmidt law.")
        with st.expander("💥 Supernova Feedback"):
            st.write("Delayed Cooling: the cooling of the gas is stopped around the site of a supernova explosion for a predefined calibrated time.")

if st.session_state.start:
    # Add a visual break
    st.markdown("---")

    # Button for next simulation step
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🌀 Introduce turbulence to star formation", use_container_width=True):
            st.session_state.sf_turb = True

    # If clicked, show the next image side-by-side with a line
    if st.session_state.sf_turb:
        st.markdown("## Simulation Step 2")
        col1, col2, col3 = st.columns([1, 0.1, 1])

        with col1:
            st.image("images/SF0DC.png", caption="Benchmark", width=200)

        with col2:
            st.markdown(
                "<div style='height: 200px; border-left: 2px solid gray; margin: auto;'></div>",
                unsafe_allow_html=True
            )

        with col3:
            st.image("images/SF1DC.png", caption="Turbulent SF", width=200)
            with st.expander("🌪️ Turbulent Star Formation"):
                st.write("This model enhances star formation by including the effect of gas turbulence. Dense, turbulent regions are more likely to collapse and form stars.")
