# --- START OF FILE love_app_enhanced.py ---

import streamlit as st
import random
from datetime import datetime

# --- Page Configuration (Must be the first Streamlit command) ---
st.set_page_config(
    page_title="For My Love",
    page_icon="💖",  # Cute emoji for the browser tab
    layout="centered" # Can be "wide" or "centered"
)

# --- Customization Section (!!! IMPORTANT: EDIT THESE !!!) ---
HER_NAME = "Sia" # Replace with your girlfriend's name
YOUR_NAME = "Ary" # Replace with your name
HEADER_IMAGE_URL = "https://th.bing.com/th/id/OIP.pO5VnaQ8mru5xN11ajfoVgHaFD?rs=1&pid=ImgDetMain" # Optional: Replace with a cute image/gif URL (e.g., https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWtmdTJqMWhuMnpxbWVwaGNvNjZpcjZwY3psc245ajdnbHZhdTVqdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26FLdmIp6wJr91JAI/giphy.gif)
ANNIVERSARY_DATE = datetime(2024, 12, 4) # Replace with your anniversary date (Year, Month, Day)
FIRST_DATE = datetime(2025, 2, 16)      # Replace with your first date (Year, Month, Day)
# Add more special dates if you like
SPECIAL_DATE_1_NAME = "Our first interaction"
SPECIAL_DATE_1 = datetime(2019, 10, 13)   # Replace (Year, Month, Day)

# --- Message & Content Lists ---
apology_messages = [
    f"I'm so sorry, my dearest {HER_NAME}. Please forgive me. My world is incomplete without your smile.",
    "I apologize from the bottom of my heart. Hurting you is the last thing I ever want to do.",
    f"I’m truly sorry, my love. I promise to learn, grow, and be the partner you deserve. You mean everything to me.",
    "I messed up, and I deeply regret it. Can we talk and make things right? I love you.",
    "Please accept my sincerest apologies. My actions were thoughtless, and I hate that I caused you pain.",
    f"Forgive me, {HER_NAME}. My commitment to making you happy is stronger than ever. I'll work hard to regain your trust.",
    "I know 'sorry' might not be enough, but I mean it with every fiber of my being. I cherish you.",
    "My heart aches knowing I've caused you sadness. I'm truly sorry and I promise to do better.",
    f"Seeing you unhappy hurts me more than anything. I apologize, {HER_NAME}, and I'm dedicated to making us stronger.",
    "I value you and our relationship more than words can say. I am deeply sorry for my mistake."
]

love_messages = [
    f"I love you more than words can capture, {HER_NAME}. You are my everything.",
    f"Every moment with you is a precious gift. You light up my life, my love.",
    f"My heart belongs completely to you, {HER_NAME}. Being with you feels like home.",
    "Your love is the sunshine on my cloudy days. I adore you endlessly.",
    f"Just thinking about you makes me smile. I'm so incredibly lucky to have you, {HER_NAME}.",
    "Falling in love with you was the best decision I ever made.",
    f"You're not just my girlfriend, you're my best friend, my confidante, and my soulmate.",
    f"Thank you for being you, {HER_NAME}. Your kindness, beauty, and spirit amaze me every day.",
    "With you, life is an adventure I never want to end. I love you to the moon and back.",
    f"My love for you grows stronger with each passing day. You complete me, {HER_NAME}."
]

reasons_love = [
    f"I love your infectious laugh, {HER_NAME}. It's the sweetest music to my ears.",
    "I love how your eyes sparkle when you talk about something you're passionate about.",
    f"I love your kindness and the way you care for others, {HER_NAME}.",
    "I love how supportive you are, always encouraging me to be my best self.",
    f"I love the way you make even ordinary moments feel special, {HER_NAME}.",
    "I love your intelligence and your unique perspective on the world.",
    f"I love holding your hand, {HER_NAME}. It just feels right.",
    "I love the cozy feeling of just being in the same room with you.",
    f"I love your strength and resilience, {HER_NAME}. You inspire me.",
    f"I love dreaming about our future together, {HER_NAME}.",
    "I love your smile - it brightens my entire day.",
    f"I love how perfectly we fit together, {HER_NAME}."
]

virtual_coupons = [
    "🎟️ Good for one heartfelt, uninterrupted listening session.",
    "🎟️ Redeemable for one cozy movie night (your choice of film!).",
    "🎟️ This coupon entitles you to one relaxing back rub.",
    "🎟️ Present this for one chore done by me (no complaints!).",
    "🎟️ Good for one homemade dinner cooked with love.",
    "🎟️ Redeemable for control of the TV remote for an evening.",
    "🎟️ This coupon is good for one spontaneous mini-adventure!",
    "🎟️ Entitles you to one 'Get Out of a Minor Argument Free' card.",
    "🎟️ Present this for 10 minutes of compliments and adoration.",
    "🎟️ Good for one session of planning our next fun date together!"
]

cherished_memories = [
    f"Remember our first video call? I was so nervous but so excited. You looked stunning, {HER_NAME}.",
    f"Thinking about the time we binged splitsvilla? I still laugh every time! You have the best sense of humor, {HER_NAME}.",
    f"That time we DID THAT? It felt so perfect just being with you, {HER_NAME}.",
    f"I'll never forget when we first said I love you to each other. My heart felt like it would burst with happiness.",
    # Add more specific memories here!
]

# --- CSS Styling ---
st.markdown(
    """
    <style>
    /* Import a cute font (optional, ensure the font is web-accessible) */
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;700&display=swap');

    /* Overall body styling */
    body {
        font-family: 'Quicksand', sans-serif; /* Using Quicksand font */
        color: #4a4a4a; /* Dark grey text for readability */
    }

    /* Set background image */
    .stApp {
         background-image: url("data:image/svg+xml,%3Csvg width='52' height='26' viewBox='0 0 52 26' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23fce4ec' fill-opacity='0.4'%3E%3Cpath d='M10 10c0-2.21-1.79-4-4-4-3.314 0-6-2.686-6-6h2c0 2.21 1.79 4 4 4 3.314 0 6 2.686 6 6 0 2.21 1.79 4 4 4 3.314 0 6 2.686 6 6 0 2.21 1.79 4 4 4v2c-3.314 0-6-2.686-6-6 0-2.21-1.79-4-4-4-3.314 0-6-2.686-6-6zm25.464-1.95l8.486 8.486-1.414 1.414-8.486-8.486 1.414-1.414z' /%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
         background-color: #fff0f5; /* Lavender blush fallback */
    }

    /* Title styling */
    h1 {
        font-family: 'Pacifico', cursive; /* Cute handwriting font for main title */
        color: #e91e63; /* Pink color */
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1); /* Subtle shadow */
    }
    h2, h3 {
        font-family: 'Quicksand', sans-serif;
        color: #ad1457; /* Deeper pink */
        text-align: center;
    }

    /* Custom container for messages */
    .message-container {
        background-color: rgba(255, 255, 255, 0.8); /* Slightly transparent white */
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #f06292; /* Pink accent border */
        text-align: center; /* Center text inside the container */
        min-height: 100px; /* Ensure container has some height even when empty */
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .message-text {
        font-size: 1.1em;
        color: #333;
        font-weight: 700; /* Bold text */
    }

    /* Button styling */
    .stButton>button {
        background-image: linear-gradient(to right, #ff8a80, #ff5252); /* Red-pink gradient */
        color: white;
        border-radius: 25px; /* More rounded */
        padding: 12px 28px;
        border: none;
        font-size: 16px;
        font-weight: 700;
        margin: 10px 5px; /* Add some horizontal margin */
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease; /* Smooth transition for hover */
        width: 100%; /* Make buttons fill column width */
    }
    .stButton>button:hover {
        background-image: linear-gradient(to right, #ff5252, #ff1744); /* Darker gradient on hover */
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px); /* Slight lift on hover */
    }
    .stButton>button:active {
        transform: translateY(0px); /* Press down effect */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Styling for date metrics */
    .stMetric {
        background-color: rgba(255, 248, 250, 0.9);
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #f8bbd0; /* Light pink border */
        text-align: center;
    }
    .stMetric > label {
        font-weight: 700; /* Bold label */
        color: #ad1457;
    }
    .stMetric > div {
        font-size: 1.5em; /* Larger value */
        color: #e91e63;
    }

    /* Center image */
    .center-image img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 200px; /* Adjust size as needed */
        border-radius: 50%; /* Make it circular */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True
)

# --- Helper Function ---
def calculate_days(date1, date2):
    return abs((date2 - date1).days)

# --- Initialize Session State ---
if 'current_message' not in st.session_state:
    st.session_state.current_message = ""
if 'current_reason' not in st.session_state:
    st.session_state.current_reason = ""
if 'current_coupon' not in st.session_state:
    st.session_state.current_coupon = ""
if 'current_memory' not in st.session_state:
    st.session_state.current_memory = random.choice(cherished_memories) if cherished_memories else "Add some memories!"

# --- App Layout ---

# Header Image (Optional)
if HEADER_IMAGE_URL:
    st.markdown(f"<div class='center-image'><img src='{HEADER_IMAGE_URL}' alt='Cute Header'></div>", unsafe_allow_html=True)

st.title(f"A Little Something for {HER_NAME} ❤️")
st.markdown(f"### From your loving {YOUR_NAME}")

st.divider()

# --- Apology & Love Messages Section ---
st.header("Messages from My Heart")
st.write(f"Hi my love, sometimes words fail me, but I hope this little app shows you how much I care, how sorry I am when I mess up, and how much I adore you every single day.")

# Create a container for the message display
message_placeholder = st.empty()
message_placeholder.markdown(
    f"<div class='message-container'><span class='message-text'>{st.session_state.current_message or 'Click a button below...'}</span></div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:
    if st.button("I Need to Say Sorry..."):
        st.session_state.current_message = random.choice(apology_messages)
        message_placeholder.markdown(
             f"<div class='message-container'><span class='message-text'>{st.session_state.current_message}</span></div>",
            unsafe_allow_html=True
        )
with col2:
    if st.button("Remind Me You Love Me!"):
        st.session_state.current_message = random.choice(love_messages)
        message_placeholder.markdown(
             f"<div class='message-container'><span class='message-text'>{st.session_state.current_message}</span></div>",
            unsafe_allow_html=True
        )

st.divider()

# --- Reasons I Love You Section ---
st.header("Just a Few Reasons Why...")

reason_placeholder = st.empty()
reason_placeholder.markdown(
    f"<div class='message-container'><span class='message-text'>{st.session_state.current_reason or 'Click for a reason!'}</span></div>",
    unsafe_allow_html=True
)

if st.button("Tell Me Why You Love Me"):
    st.session_state.current_reason = random.choice(reasons_love)
    reason_placeholder.markdown(
        f"<div class='message-container'><span class='message-text'>{st.session_state.current_reason}</span></div>",
        unsafe_allow_html=True
    )

st.divider()

# --- Special Dates Section ---
st.header("Our Journey Together")
today = datetime.now()

col_dates1, col_dates2 = st.columns(2)
with col_dates1:
    st.metric(label="💖 Our Anniversary", value=ANNIVERSARY_DATE.strftime("%B %d, %Y"))
    st.metric(label="Days Since We Met", value=f"{calculate_days(SPECIAL_DATE_1, today)} days")

with col_dates2:
    st.metric(label="✨ Our First Video Call", value=FIRST_DATE.strftime("%B %d, %Y"))
    st.metric(label=f"🗓️ {SPECIAL_DATE_1_NAME}", value=SPECIAL_DATE_1.strftime("%B %d, %Y"))
    # Add more date metrics here if needed

st.divider()

# --- Memory Lane Section ---
st.header("Memory Lane 💭")

memory_placeholder = st.empty()
memory_placeholder.markdown(
    f"<div class='message-container'><span class='message-text'>{st.session_state.current_memory}</span></div>",
    unsafe_allow_html=True
)

if st.button("Remember This?"):
     # Avoid repeating the same memory twice in a row if possible
    new_memory = random.choice(cherished_memories)
    if len(cherished_memories) > 1:
        while new_memory == st.session_state.current_memory:
            new_memory = random.choice(cherished_memories)
    st.session_state.current_memory = new_memory
    memory_placeholder.markdown(
        f"<div class='message-container'><span class='message-text'>{st.session_state.current_memory}</span></div>",
        unsafe_allow_html=True
    )

st.divider()

# --- Virtual Coupon Section ---
st.header("A Little Treat For You")

coupon_placeholder = st.empty()
coupon_placeholder.markdown(
    f"<div class='message-container'><span class='message-text'>{st.session_state.current_coupon or 'Click for a virtual coupon!'}</span></div>",
    unsafe_allow_html=True
)

if st.button("Get a Virtual Coupon!"):
    st.session_state.current_coupon = random.choice(virtual_coupons)
    coupon_placeholder.markdown(
        f"<div class='message-container'><span class='message-text'>{st.session_state.current_coupon}</span></div>",
        unsafe_allow_html=True
    )


st.divider()

# --- Footer ---
st.markdown(f"<h3 style='text-align: center; color: #e91e63;'>Always and forever, {YOUR_NAME}</h3>", unsafe_allow_html=True)

# --- END OF FILE love_app_enhanced.py ---