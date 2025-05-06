import streamlit as st

# Page config
st.set_page_config(page_title="Portfolio", page_icon="💼", layout="wide")

# Sidebar
st.sidebar.title("M. Suleman")
st.sidebar.subheader("Python Backend Developer")
st.sidebar.write("📧 Email: suleman@example.com")
st.sidebar.write("[GitHub](https://github.com) | [LinkedIn](https://linkedin.com)")

# Main title
st.title("👋 Welcome to My Portfolio")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "👨‍💼 About Me", "📂 Projects", "📞 Contact"])

# Home
with tab1:
    st.header("Hello, I'm M. Suleman")
    st.subheader("Python Backend Developer | Streamlit Enthusiast")
    st.write("This is my personal portfolio built entirely using Streamlit with a simple and clean interface.")

# About Me
with tab2:
    st.header("About Me")
    st.write("I'm passionate about backend development using Python.")
    st.write("Currently learning frameworks like Flask, FastAPI, and working on projects like attendance systems and automation tools.")
    st.write("**Skills:** Python, APIs, Git, Firebase, MySQL, MongoDB")

# Projects
with tab3:
    st.header("My Projects")

    st.subheader("📌 Attendance Tracker App")
    st.write("Built using Flutter for frontend and Firebase for backend. Used for recording student attendance by subject.")

    st.subheader("📌 Face Recognition Attendance System")
    st.write("Python-based app that uses webcam to recognize faces and mark attendance in a CSV file.")

    st.subheader("📌 Amazon Product Listing Automation")
    st.write("Streamlines Amazon product listings and PPC campaigns for sellers.")

# Contact
with tab4:
    st.header("Contact Me")
    st.write("You can reach me via the form below or email me directly.")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Thank you! Your message has been received.")
        else:
            st.warning("Please fill in all fields before sending.")
