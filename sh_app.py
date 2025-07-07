import streamlit as st
import random

st.title("Superhero Name Creator 🦸‍♂️🦸‍♀️")
st.write("Create your unique superhero identity!")

# Create input components
st.subheader("🎨 Tell us about yourself:")

# Input fields
favorite_color = st.text_input("What's your favorite color?", placeholder="e.g., Blue, Red, Golden")
favorite_animal = st.text_input("What's your favorite animal?", placeholder="e.g., Eagle, Tiger, Dragon")
lucky_number = st.number_input("Choose your lucky number:", min_value=1, max_value=999, value=7)

# Superpower selection
superpowers = [
    "Flying",
    "Invisibility", 
    "Super Strength",
    "Mind Reading",
    "Time Control",
    "Shape Shifting",
    "Laser Vision",
    "Healing Powers",
    "Super Speed",
    "Weather Control"
]

chosen_superpower = st.selectbox("Choose your superpower:", superpowers)

# Generate and display superhero profile when inputs are provided
if favorite_color and favorite_animal:
    st.divider()
    
    # Generate superhero name
    superhero_name = f"The {favorite_color.title()} {favorite_animal.title()} of {lucky_number}"
    
    st.subheader("🦸‍♀️ Your Superhero Profile:")
    
    # Display superhero details
    st.write(f"**Superhero Name:** {superhero_name}")
    st.write(f"**Superpower:** {chosen_superpower}")
    
    # Generate superhero motto
    motto = f"With the spirit of the {favorite_animal.lower()} and the power of {chosen_superpower.lower()}, I protect the innocent!"
    st.write(f"**Superhero Motto:** *{motto}*")
    
    # Bonus: Random catchphrase generator
    st.divider()
    st.subheader("🗣️ Superhero Catchphrases:")
    
    catchphrases = [
        "Justice never sleeps!",
        "Evil shall not prevail!",
        "Time to save the day!",
        "For truth and honor!",
        "Fear not, citizens!",
        "The power is within me!",
        "Darkness cannot hide from light!",
        "Together we are stronger!",
        "Hope is my greatest weapon!",
        "Never give up, never surrender!"
    ]
    
    if st.button("🎲 Generate Random Catchphrase"):
        random_catchphrase = random.choice(catchphrases)
        st.success(f"**{superhero_name} says:** *\"{random_catchphrase}\"*")
    
    # Fun superhero stats
    st.divider()
    st.subheader("📊 Superhero Stats:")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.metric("Power Level", f"{lucky_number * 10}")
    
    with col2:
        st.metric("Hero Rating", f"{min(lucky_number + 85, 100)}/100")


else:
    st.info("👆 Please fill in your favorite color and animal to create your superhero profile!")