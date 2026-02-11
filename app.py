import streamlit as st

import pandas as pd


# st.header("welcome to class", anchor=False)
# st.title("Hello, Streamlit!")
# st.write("Welcome to your first Streamlit app.")

# st.sidebar.title("Side Menu")
# name = st.sidebar.text_input("Enter your name")
# st.sidebar.write(f"My name is {name}")



# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# with left_column:
#     left_column.button('Press me!')
#     name = st.text_input("Enter your name:")
#     checkbox = st.checkbox("Show greeting")
#     radio = st.radio("Choose a greeting style:", ("Formal", "Casual"))
#     date = st.date_input("Select a date:")
#     color = st.color_picker("Pick a color:", "#00f900")
#     image = st.file_uploader("Upload an image:", type=["png", "jpg", "jpeg"])
#     select = st.select_slider("select",("Formal", "Casual", "Native"))





# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")
#     image = st.image("/Users/mac/Documents/blue.jpeg","image")
#     # audio = st.audio("/Users/mac/Documents/sample-3s.mp3") 
#     video = st.video("/Users/mac/Downloads/SUPER EAGLES.mp4")


#     st.write("Here's our first attempt at using data to create a table:")
#     st.write(pd.DataFrame({
#         'first column': [1, 2, 3, 4],
#         'second column': [10, 20, 30, 40]
#     }))


# first, second = st.columns(2)

# with first:
#     name = st.text_area("What is your name")
#     st.write(name)

# with second:
#     audio = st.audio_input("audio")
#     chat = st.chat_input("enter your name")
#     if chat:
#         st.write(chat)

