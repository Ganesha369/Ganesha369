import streamlit as st
import requests

st.set_page_config(page_title="Ganesha's SDE-1 Hub", layout="wide")

st.title("🚀 SDE-1 Project Live Viewer")
st.sidebar.info("This hub pulls code directly from Ganesha's DSA repositories.")

# The URL link from your profile README will send the 'repo' name here
repo_name = st.query_params.get("repo")

if repo_name:
    st.subheader(f"Running Project: {repo_name}")
    # Raw GitHub URL to get the code
    url = f"https://raw.githubusercontent.com/Ganesha369/{repo_name}/main/main.py"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # This 'exec' runs the project's code as if it were this app
            exec(response.text)
        else:
            st.error(f"Could not find the project code for {repo_name}.")
    except Exception as e:
        st.error(f"An error occurred while loading the app: {e}")
else:
    st.write("### Welcome! Click a 'Live Output' link on Ganesha's profile to see a project in action.")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
