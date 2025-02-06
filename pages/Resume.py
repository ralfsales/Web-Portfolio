import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .centered-header {
        text-align: center;
        background-color: #666666;  
        color: #ffffff;             
        padding: 10px;              
        border-radius: 5px;         
        margin: 20px 0; 
    }
    </style>
    <div class="centered-header">
        <h1>My Professional Career 🗃️</h1>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Education")
    st.write("""
    •	HDip in Computer Science at CCT College - Dublin, Ireland.
    CCT College Dublin\n
    •	Bs (Hons) Mechanical Engineering (NFQ level 8) at  Multivix – Vitoria, Brazil.
    Grade: 1 ST Class Honors - Member of the Society of Engineers – CREA/ES
    """)

    st.subheader("Soft Skills")
    st.write(""" 
    Time management and multitasking abilities | Strong interpersonal and collaboration skills| Analytical problem-solving mindset \n
    Self motivated and committed to continuous learning. 
    """)

    st.subheader("Download My Resume")

    file_path = r"C:\Users\rafae\Desktop\Projects for my Portifolio\Portifolio\Rafael Sales - Resume CS.pdf"
    with open(file_path, "rb") as file:
        btn = st.download_button(
            label="📄 Resume File",
            data=file,
            file_name="Rafael Sales - Resume CS.pdf",
            mime="application/pdf"
        )

with col2:
    st.subheader("Tools and Technologies")
    st.markdown(
        """
        <strong>Software Development:</strong> Java, Python, C. <br>
        <strong>Web Development & Frameworks:</strong> HTML, CSS, JavaScript, Node.js, React.js, PHP, Figma. <br>
        <strong>Cloud & Virtualization:</strong> Microsoft Azure, AWS, Cloud Development, Systems Administration, Linux Virtualization, Oracle VM. <br>
        <strong>Cybersecurity & Networking:</strong> Cisco, CompTIA Security+, Network Management, Security Compliance. <br>
        <strong>Project Management:</strong> Agile Development, System Management, Operation and Control Maintenance Management. <br>
        <strong>Database Management:</strong> SAP Databases, MySQL, PostgreSQL, MongoDB. <br>
        <strong>Additional Tools:</strong> AutoCAD, MS Office, Google Workspace, Git, GitHub.
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <style>
    .centered-header {
        text-align: center;
        background-color: #666666;  /* Dark medium gray background */
        color: #ffffff;             /* White text for contrast */
        padding: 10px;              /* Add padding for better spacing */
        border-radius: 5px;         /* Optional: Rounded corners */
        margin: 20px 0;             /* Add margin for spacing */
    }
    </style>
    <div class="centered-header">
        <h2>Work Experience</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .white-background {
        background-color: #ffffff;  /* White background */
        padding: 15px;              /* Add padding for better spacing */
        border-radius: 5px;         /* Optional: Rounded corners */
        margin: 10px 0;             /* Add margin for spacing */
        border: 1px solid #e0e0e0;  /* Optional: Add a light border for definition */
    }
    </style>
    <div class="white-background">
        <p>
            <strong>Support Engineer at Stone Co. - Brazil</strong> | April 2019 – January 2022  <br>
            • Provided technical support for financial software and devices, reducing downtime and optimizing client operations. <br>
            • Diagnosed and repaired equipment issues, ensuring peak performance through software installations and calibrations. <br>
            • Provided exceptional customer support, produced technical reports, prepared quotes, and collaborated with supply chain 
            teams to reduce inventory shortages by 12%.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .light-gray-background {
        background-color: #f8f9fa;  /* Lighter gray background */
        padding: 15px;              /* Add padding for better spacing */
        border-radius: 5px;         /* Optional: Rounded corners */
        margin: 10px 0;             /* Add margin for spacing */
    }
    </style>
    <div class="light-gray-background">
        <p>
            <strong>Mechanical Engineer (Intern) at VLI Logistics - Brazil</strong> | October 2016 - February 2018  <br>
            • Diagnosed machine failures, reducing downtime by 15% and boosting efficiency by 10%, with a focus on quality & safety. <br>
            • Streamlined tool management using KAIZEN, improving maintenance cycles and productivity by 10%. <br>
            • Created technical drawings and BOMs while optimizing processes with MAXIMO, BIM, and SAP.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .white-background {
        background-color: #ffffff;  /* White background */
        padding: 15px;              /* Add padding for better spacing */
        border-radius: 5px;         /* Optional: Rounded corners */
        margin: 10px 0;             /* Add margin for spacing */
        border: 1px solid #e0e0e0;  /* Optional: Add a light border for definition */
    }
    </style>
    <div class="white-background">
        <p>
            <strong>Duty Manager at Tesco - Ireland </strong> | January 2023 – Current  <br>
            • Managed daily cash flow, sales, inventory, and safety compliance, while reducing wait times and preventing shortages. <br>
            • Boosted store performance from 4th to 2nd citywide by enhancing product presentation, cleanliness, and task delegation.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .light-gray-background {
        background-color: #f8f9fa;  /* Light gray background */
        padding: 15px;              /* Add padding for better spacing */
        border-radius: 5px;         /* Optional: Rounded corners */
        margin: 10px 0;             /* Add margin for spacing */
        border: 1px solid #e0e0e0;  /* Optional: Add a light border for definition */
    }
    </style>
    <div class="light-gray-background">
        <p>
            <strong>General Operator at Musgrave - Ireland</strong> | March 2022 – December 2023  <br>
            • Ensuring proper date rotation of all products daily, dramatically boosting inventory accuracy for distribution by 98%, 
            thereby ensuring peak operational efficiency and product quality. <br>
            • Maintaining accurate inventory records and organizing products with proper labelling, resulting in a 15% reduction in 
            stocking errors.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .white-background {
        background-color: #ffffff;  /* White background */
        padding: 15px;              /* Add padding for better spacing */
        border-radius: 5px;         /* Optional: Rounded corners */
        margin: 10px 0;             /* Add margin for spacing */
        border: 1px solid #e0e0e0;  /* Optional: Add a light border for definition */
    }
    </style>
    <div class="white-background">
        <p>
            <strong>Environmental Technician at Exata Projetos - Brazil</strong> | February 2013 - March  <br>
            • Designed sustainable solutions, including impact assessments and technical drawings, improving documentation 
            accuracy by 98% and ensuring compliance with environmental and safety standards. <br>
            • Led projects focused on alternative energy, urban mobility, and eco-friendly construction, reducing environmental impact 
            and promoting sustainability.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)