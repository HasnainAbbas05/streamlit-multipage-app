
# Import the Streamlit library
import streamlit as st

# Configure the main page title and icon
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Display the main welcome heading
st.write("# Welcome to Streamlit! 👋")

# Show instructions in the sidebar
st.sidebar.success("Select a demo above.")

# Display the welcome message and useful links
st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.

    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!

    ### Want to learn more?

    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community forums](https://discuss.streamlit.io)

    ### See more complex demos

    - Use a neural net to [analyze the Udacity Self-driving Car Image
      Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
)
