import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

# Function to simulate progress
def simulate_progress():
    for i in range(100):
        st.progress(i + 1)
        time.sleep(0.05)

# Set up the Streamlit app
st.set_page_config(page_title="Gym Web App", layout="wide", initial_sidebar_state="expanded")

# Sidebar
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Select here..", ["Home", "Workout Plans", "Our Gym Environment", "Contact"])

# Home Page
if option == "Home":
    st.title("Welcome to Tharmesh power fitness")
    st.write("Here you can see about our gym")
    
    # image
    st.image("gymlogo.jpeg", caption="Gym Image", use_column_width=True)
    
    # video
    st.video("gymvideo.mp4")
    
    # audio
    st.audio("gymaudio.mp3")
    
    # Input widgets
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age",  max_value=120)
    height = st.number_input("Enter your height",  max_value=120)
    weight = st.number_input("Enter your weight",  max_value=100)
    if st.button("Submit"):
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Height: {height}")
        st.write(f"Weight: {weight}")

# Workout Plans Page
elif option == "Workout Plans":
    st.title("Workout Plans")
    st.write("Choose a workout plan from the options below:")
    
    workout_options = ["Strength Training", "Cardio", "body Recomposition"]
    selected_plan = st.selectbox("Select a workout plan", workout_options)
    
    st.write(f"You selected: {selected_plan}")

 

# Gallery Page
elif option == "Our Gym Environment":
    st.title("Our Gym Environment")
    st.write("This is our gym.")
    st.image("gym.jpeg", caption="Gym Image", use_column_width=True)
    st.image("gym1.jpeg", caption="Gym Image", use_column_width=True)
    st.image("gym2.jpeg", caption="Gym Image", use_column_width=True)
    st.image("gym3.jpg", caption="Gym Image", use_column_width=True)
    st.image("gym4.jpg", caption="Gym Image", use_column_width=True)
    
 
# Contact Page
elif option == "Contact":
    st.title("Contact Us")
    st.write("If you want any clarification let me know")
    
    st.write("Email: ravitharmesh@gmail.com")
    st.write("Phone: +94762623110")

    # Display a map (alternative to folium)
    st.write("Here you can see our gym location(Eluthoor,Mannar,Sri Lanka)")
    st.map(pd.DataFrame({
        'lat': [8.9910],
        'lon': [79.8899]
    }))

   
    st.write("Here's a plot of gym attendance:")
    dates = pd.date_range(start='2023-05-01', periods=12, freq='M')
    attendance = np.random.randint(50, 150, size=12)
    fig, ax = plt.subplots()
    ax.plot(dates, attendance, marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel('Attendance')
    ax.set_title('Gym Attendance ')
    st.pyplot(fig)
