import streamlit as st
import os
from PIL import Image
image = Image.open('nbapicture.jpg')

st.image(image)
with st.expander("History of NBA"):
    st.write("""
        The National Basketball Association, or NBA, is a professional basketball league comprised of 30 teams across 
        North America featuring the best basketball players in the world.
    """)
with st.expander("What is ELo Ranking?"):
    st.write("""
            Elo ratings keep track of the final score of each game, 
where the game was played, and when the game was played. A 1500 Elo rating is the average
and starting rating. This score changes as the season progresses adding or subtracting to 
account for the team’s performance.
        """)
with st.expander("Currently, who is the leading NBA team?"):
    st.write("""
    As per 'Points Per Game' stats, Memphis Grizzlies leads the leaderboard with a 112.5 points""")
