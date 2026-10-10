
# Import libraries for data handling, visualization and the app
import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

# Configure the page title and browser icon
st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

# Display the page heading and sidebar heading
st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")

# Introduce the dataset and its source
st.write(
    """This demo shows how to use `st.write` to visualize Pandas DataFrames.
(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)"""
)


# Cache the data so it does not reload after every interaction
@st.cache_data
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")


try:
    # Load the agricultural production dataset
    df = get_UN_data()

    # Allow users to select countries for comparison
    countries = st.multiselect(
        "Choose countries",
        list(df.index),
        ["China", "United States of America"]
    )

    if not countries:
        # Display a message when no country is selected
        st.error("Please select at least one country.")
    else:
        # Select the countries and convert figures to billions
        data = df.loc[countries]
        data /= 1000000.0

        # Display the selected agricultural production data
        st.write(
            "### Gross Agricultural Production ($B)",
            data.sort_index()
        )

        # Reshape the dataset for visualization with Altair
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={
                "index": "year",
                "value": "Gross Agricultural Product ($B)"
            }
        )

        # Create an area chart comparing agricultural production
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.3)
            .encode(
                x="year:T",
                y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                color="Region:N",
            )
        )

        # Display the interactive chart
        st.altair_chart(chart, use_container_width=True)

except URLError as e:
    # Explain when the external dataset cannot be accessed
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
        """
        % e.reason
    )
