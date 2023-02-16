from pathlib import Path
from tkinter import PROJECTING

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Serghei Covalciuc"
PAGE_ICON = ":wave:"
NAME = "Serghei Covalciuc"
DESCRIPTION = """
I am a hardworking, honest individual. I am a good timekeeper, always willing to learn new skills.
"""
EMAIL = "sergiu199393@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://youtube.com/",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Certificate of Successfully completed the Learn & GitHub Course   
- ✔️ Certificate of Successfully completed the Learn the Command Line Course 
- ✔️ Cerco Certificate in Systems & Networking (CCSN)
- ✔️ CompTIA Network+ 
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Cerco IT Ltd | Cerco Certificate in Systems & Networking (UCSN)**")
st.write("2023")
st.write(
    """
- ► PC Operating Systems, PC Hardware, Device Resources, BIOS/CMOS. Number systems. 
- ► Installation & Configuration, Troubleshooting, Command Line Commands, Performed on a variety of Microsoft Windows platforms.
- ► Topologies & Protocols, Security, Resource Sharing, Network Administration, Peer-to-Peer & Client/Server, TCP/IP Networking, Networking Services, Configuration and Troubleshooting. 
WiFi installation, use and testing. Domain Membership & Policies.
- ► Motherboards, CPUs, Memory, Device Installation, Upgrading and Configuring, Diagnostics. Troubleshooting. 
Biometric recognition devices. Laptop Maintenance
- ► Standards, Ports and Modem Configurations, Dial-up Networking & xDSL, Remote Desktop, Intranet/Internet, Routers/Gateways, Troubleshooting.
- ► Laser/Matrix/Inkjet Printer Principles, Removal and Replacement Procedures, Local and Network Printers, Troubleshooting.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)



