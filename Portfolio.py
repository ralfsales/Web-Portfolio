import streamlit as st
import pandas
from PIL import Image, ImageDraw

st.set_page_config(layout="wide")

def make_circular_image(image_path, size=(300,300)):
    image = Image.open(image_path)
    image = image.resize(size)

    mask = Image.new("L", size, 0)

    draw = ImageDraw.Draw(mask)
    draw.ellipse((0,0,*size), fill=255)

    circular_image = Image.new("RGBA", size)
    circular_image.paste(image, (0,0), mask=mask)
    return circular_image

col1, col2 = st.columns(2)

with col1:
    content = "↖️ Use the menu icon > at the top left to navigate through the available pages."
    st.write(content)
    circular_image = make_circular_image("images/photo.png")
    st.image(circular_image, caption="", width=300)
    st.title("""👨🏼‍💻 Rafael Sales 
    Computer Scientist
    Engineer""")

    st.subheader("Links")
    st.link_button(label="LinkedIn", url="https://www.linkedin.com/in/rafaelguilhemegsales/")
    st.link_button(label="GitHub", url="https://github.com/ralfsales")

with col2:
    content1 = """Hi there! Welcome to My Web Portfolio! \n
    I’m a passionate and driven Computer Scientist with a strong foundation in Network Administration, Project Management, and Software Development.

    I thrive on solving complex problems with creative solutions and am known for my organizational skills, effective communication, and attention to detail.
    What excites me most is the opportunity to contribute to the ever-evolving world of technology, where innovation never stops.

    I’m committed to continuous growth—whether it’s mastering new programming languages, refining my technical expertise, or finding smarter ways to tackle challenges.
    My curiosity and love for learning keep me at the forefront of the fast-paced tech landscape.

    Beyond my professional life, I’m an avid explorer of cultures, a lover of outdoor adventures, and a sports enthusiast.
    When I’m not coding or managing projects, you’ll find me unwinding with Fantasy and Sci-Fi movies, diving into scientific documentaries,
    or tinkering with tech to understand how things are built and improved.

    While I enjoy connecting with others and collaborating on exciting projects, I also value my “me time” for reflection, relaxation, and recharging.
    """

    st.markdown(
        f"""
        <style>
        .light-gray-background {{
            background-color: #f8f9fa;  /* Light gray background */
            padding: 20px;              /* Add padding for better spacing */
            border-radius: 10px;        /* Rounded corners */
            margin: 10px 0;             /* Add margin for spacing */
            line-height: 1.6;           /* Improve readability with line height */
            text-align: justify;
        }}
        </style>
        <div class="light-gray-background">
            {content1.replace("\n", "<br>")}  <!-- Replace newlines with <br> for HTML -->
        </div>
        """,
        unsafe_allow_html=True
    )

content2 = """Below, you can find some of the applications I have developed using a variety of programming languages and technologies,
including Python, Java, C++, JavaScript and more."""

st.markdown(
    f"""
    <style>
    .dark-gray-background {{
        background-color: #333333;  /* Dark gray background */
        color: #ffffff;             /* White text for contrast */
        padding: 20px;              /* Add padding for better spacing */
        border-radius: 10px;        /* Rounded corners */
        margin: 10px 0;             /* Add margin for spacing */
        line-height: 1.6;           /* Improve readability with line height */
        text-align: center;
    }}
    </style>
    <div class="dark-gray-background">
        {content2.replace("\n", "<br>")}  <!-- Replace newlines with <br> for HTML -->
    </div>
    """,
    unsafe_allow_html=True
)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:5].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[6:].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.write(f"[Source Code]({row['url']})")