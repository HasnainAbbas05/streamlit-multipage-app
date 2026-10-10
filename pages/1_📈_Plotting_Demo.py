
# Import the libraries needed for plotting and animation
import streamlit as st
import time
import numpy as np

# Configure this page's browser title and icon
st.set_page_config(page_title="Plotting Demo", page_icon="📈")

# Display the page heading and sidebar heading
st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")

# Explain what this demo does
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

# Create a progress bar and status message in the sidebar
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Generate the initial random value
data = np.random.randn(1, 1)

# Create an empty chart container and draw the first point
chart = st.empty()
chart.line_chart(data)

# Add random values and update the chart over approximately 5 seconds
for i in range(1, 101):
    new_rows = data[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    data = np.concatenate([data, new_rows])

    # Update the progress message, chart and progress bar
    status_text.text("%i%% Complete" % i)
    chart.line_chart(data)
    progress_bar.progress(i)
    time.sleep(0.05)

# Remove the progress bar when the animation finishes
progress_bar.empty()

# Clicking this button reruns the page and restarts the animation
st.button("Re-run")
