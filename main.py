import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Rafael Sales")
    content = """
    I’m a dynamic and motivated professional with a strong background in Network Administration, Project Management, and Technical Troubleshooting. I’m known for being organized, communicating effectively, and tackling problems with creative solutions.
What truly drives me is my passion for innovation and my excitement to contribute to the fast-changing world of tech and computer science. I take pride in my attention to detail and my commitment to always improving, whether it’s through learning new skills or finding better ways to approach challenges.
I'm passionate about exploring new cultures through travel, enjoying outdoor activities, and staying active with sports. In my downtime, I unwind with Marvel films and scientific documentaries. I have a strong passion for technology and enjoy exploring how things are created and continuously improved.
Despite my sociable nature, I also appreciate and prioritize 'me time' for personal relaxation and reflection.
    """
    st.info(content)