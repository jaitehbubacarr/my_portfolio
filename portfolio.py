import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #111;
            color: #fff;
            font-family: 'Arial';
        }
        .sidebar .sidebar-content {
            background-color: #111;
            color: #fff;
        }
        .css-18e3th9 {
            background-color: #111;
        }
        .css-1d391kg {
            background-color: #111;
        }
        .css-1v3fvcr {
            background-color: #111;
        }
        .css-1a32fsj {
            background-color: #111;
        }
        .css-1aumxhk {
            color: #fff;
        }
        .css-2ykyy6 {
            color: #fff;
        }
        .css-1cpxqw2 {
            color: #fff;
        }
    </style>
    """, unsafe_allow_html=True)

# Title and Header Image
st.title("Bubacarr Jaiteh")
st.image("https://via.placeholder.com/800x400.png?text=Bubacarr+Jaiteh", use_column_width=True)
st.write("## IT Assistant")
st.write("### Results-oriented professional dedicated to excellence in web development, geospatial data management, and analysis.")
st.write("Email: jaitehbubacarr001@gmail.com | Location: Jamisa Estate layout, Brikama | Phone: +220 7249145 / 9229814")
st.write("[Facebook](https://www.facebook.com/bubacarr.jaiteh.1460/)")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Skills", "Education", "Professional Training", "Experience", "Projects", "Contact"])

if options == "Home":
    st.header("Profile")
    st.write("""
    Results-oriented professional dedicated to excellence in web development, geospatial data management, and analysis. Proven success in leading 
    cutting-edge website projects, managing information platforms, and directing spatial data systems. Demonstrates expertise in GIS, drone flight 
    tasks, and comprehensive IT support. Recognized for guiding and instructing students at senior school and tertiary levels. Collaborative team 
    player with skills in capacity building for ITC instructors. Committed to continuous learning and professional development, actively seeking 
    opportunities to contribute skills to dynamic projects in a challenging and growth-oriented environment.
    """)

elif options == "Skills":
    st.header("Skills")
    skills = {
        "Python": 100,
        "WordPress": 90,
        "GeoServer": 85,
        "QGIS": 90,
        "Video Editing": 80,
        "Graphic Designing": 85,
        "Drone Pilot": 70,
        "HTML & CSS": 90,
        "Microsoft Applications": 95,
        "Server Management": 80
    }
    for skill, proficiency in skills.items():
        st.write(f"{skill}: {'█' * (proficiency // 10)} {proficiency}%")

elif options == "Education":
    st.header("Education")
    st.write("""
    - Ongoing | BSc, Information Technology | University of the People | USA
    - 2019 | Advance 2, Information Technology | African Information Technology | Gambia
    - 2018 | Diploma 1, Information Technology | African Information Technology | Gambia
    - 2018 | Diploma, Management Studies | Management Development Institute | Gambia
    - 2017 | Certificate, Management Studies | Management Development Institute | Gambia
    """)

elif options == "Professional Training":
    st.header("Professional Training")
    st.write("""
    - 2023 - Delta Quad Pro #Mapper license course, Vertical Technologies
    - 2023 - GIS in QGIS 3 for beginners, Udemy
    - 2023 - GeoServer from A-Z, Udemy
    - 2023 - Adobe Premiere Pro CC - Essentials Training Course, Udemy
    - 2023 - Hosting Websites with Amazon Lightsail, Udemy
    - 2021 - Graphic Design Masterclass, Udemy
    - 2020 - Introduction to GIS and QGIS 3, Udemy
    - 2020 - Python is Easy fundamentals, Pirple
    - 2020 - Responsive Web Design, freecodecamp
    - 2020 - Frontend Fundamentals, Pirple
    """)

elif options == "Experience":
    st.header("Experience")
    st.write("""
    - **2023 - TO DATE | IT Assistant**
      - Develop the project website and lead the management of the information platform and Gambia Spatial Data System created by the EBA Project. Additionally, took charge of GIS and drone flight tasks for the project.
      - *EbA Gambia Project | Bijilo Annex Layout*

    - **2022 - 2023 | Communication and Outreach Intern**
      - Collaborated closely with the Communication Officer to deliver IT-related support and managed GIS tasks for the project.
      - *EbA Gambia Project | Bijilo Annex Layout*

    - **2019 - 2022 | ICT Instructor**
      - Instructed grade 10 and 11 students according to the West African Examination Syllabus, actively involved in preparing class materials, and delivered effective teaching sessions.
      - *Maahad Senior Secondary School | Brikama*

    - **2012 - 2015 | Voluntary Instructor**
      - Provided instruction to students in ICT and conducted capacity-building sessions for the school's ITC instructors.
      - *African Information Technology Holding Ltd | Brikama*
    """)

elif options == "Projects":
    st.header("Projects")
    st.write("### The projects I've been working on.")
    st.image("https://via.placeholder.com/600x400.png?text=Project+1", caption="Project 1", use_column_width=True)
    st.image("https://via.placeholder.com/600x400.png?text=Project+2", caption="Project 2", use_column_width=True)
    st.image("https://via.placeholder.com/600x400.png?text=Project+3", caption="Project 3", use_column_width=True)

elif options == "Contact":
    st.header("Contact")
    st.write("### Get in touch")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    if st.button("Send"):
        st.write("Thank you for your message!")
