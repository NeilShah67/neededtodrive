import streamlit as st
from openai import OpenAI
key = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.set_page_config(page_title="Driving Usage")
st.title("Driving Usage")
st.write("This program calculates how much money you spend on gas to go to a single place every month and how many miles you drive to that place every month.")
home=st.text_input("What is your home address:",key="home")
place=st.text_input("Where is one place you go on a regular basis every month:",key="place")
often=st.number_input("How often to you go to this place every week:",key="often")
mpg=st.number_input("What is your car's MPG:",key="mpg")
station=st.text_input("What gas station do you normally go to:",key="station")
prompt = (
    f" Make all of this one clean sentence give me the answer with no explanation and have all the information nesscary that i am about to give you but remeber no explanation(account for round trip): Calculate the amount of miles you drive every month round trip from {home} "
    f"to {place} if you go to this place {often} times a week, "
    f"also if your car's mpg is {mpg} and the price of a gallon of gas is the average price of one gallon of gas at the {station} closest to {home}, "
    "how much money do you spend every month (account for round trip)."
)
response=key.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
    {"role":"system","content":"You are a helpful assistant."},
    {"role":"user","content":prompt}
]
)
answer=response.choices[0].message.content
st.write(answer)

