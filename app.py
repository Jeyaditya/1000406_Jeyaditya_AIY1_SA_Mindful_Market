import streamlit as st
import pandas as pd
from datetime import datetime
import math
import os

# ----------- CONFIG ----------- #
st.set_page_config(page_title="Mindful Market", layout="wide")

# ----------- COUNTRY & DISTRICTS ----------- #
COUNTRIES = {
    "India": {"coords": (22.5937, 78.9629), "districts": ["Delhi","Mumbai","Chennai","Bangalore","Hyderabad","Kolkata","Pune","Jaipur","Ahmedabad","Kochi"]},
    "United States": {"coords": (37.0902, -95.7129), "districts": ["New York","Los Angeles","Chicago","Houston","Phoenix","Dallas","San Diego","San Jose","Austin","Seattle"]},
    "China": {"coords": (35.8617, 104.1954), "districts": ["Beijing","Shanghai","Shenzhen","Guangzhou","Chengdu","Wuhan","Hangzhou","Xi’an","Nanjing","Tianjin"]},
    "United Kingdom": {"coords": (55.3781, -3.4360), "districts": ["London","Manchester","Birmingham","Liverpool","Leeds","Sheffield","Bristol","Oxford","Cambridge","Nottingham"]},
    "Australia": {"coords": (-25.2744, 133.7751), "districts": ["Sydney","Melbourne","Brisbane","Perth","Adelaide","Canberra","Hobart","Darwin","Gold Coast","Newcastle"]},
    "Germany": {"coords": (51.1657, 10.4515), "districts": ["Berlin","Munich","Hamburg","Frankfurt","Cologne","Stuttgart","Dusseldorf","Leipzig","Bonn","Dresden"]},
    "France": {"coords": (46.6034, 1.8883), "districts": ["Paris","Lyon","Marseille","Nice","Toulouse","Bordeaux","Lille","Nantes","Strasbourg","Montpellier"]},
    "Japan": {"coords": (36.2048, 138.2529), "districts": ["Tokyo","Osaka","Kyoto","Nagoya","Yokohama","Kobe","Hiroshima","Fukuoka","Sendai","Sapporo"]}
}

# ----------- PRODUCT DATA ----------- #
REAL_WORLD_FACTORS = {
    "Clothing": 0.62,
    "Shoes": 0.95,
    "Electronics": 2.8,
    "Groceries": 0.33,
    "Accessories": 0.48
}

# ----------- SESSION STATE ----------- #
if "purchases" not in st.session_state:
    st.session_state.purchases = []

# ----------- FUNCTIONS ----------- #
def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))

def calculate_co2(product, price, user_country, shipper_country):
    base = price * REAL_WORLD_FACTORS.get(product, 0.5)
    lat1, lon1 = COUNTRIES[user_country]["coords"]
    lat2, lon2 = COUNTRIES[shipper_country]["coords"]
    distance = haversine(lat1, lon1, lat2, lon2)
    transport = distance * 0.015
    total = base + transport
    eco = total <= 50
    return round(total, 2), round(distance, 2), eco

# ----------- SIDEBAR ----------- #
st.sidebar.markdown("### Navigate")
tab = st.sidebar.radio("", ["Home", "Purchase History"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Eco Badges")
st.sidebar.write("🌱 Eco Starter")
st.sidebar.write("♻ Conscious Buyer")
st.sidebar.write("🌍 Climate Hero")

# ----------- LAYOUT ----------- #
left, main, right = st.columns([1, 6, 2])

# ----------- ECO SCORE CALCULATION ----------- #
total_impact = sum(p.get("Impact", 0) for p in st.session_state.purchases)
eco_score = max(0, min(100 - (total_impact / 500) * 100, 100))

# ----------- BADGE & MASCOT LOGIC ----------- #
if eco_score < 35:
    mascot_img = "images/sad_fox.png"
    speech = "Let’s try greener choices "
elif eco_score < 70:
    mascot_img = "images/neutral_fox.png"
    speech = "Try to improve more! Don't loose hope, keep going "
else:
    mascot_img = "images/proud_fox.png"
    speech = "Amazing! You're saving the planet "
bar_color = "red" if eco_score < 35 else "orange" if eco_score < 70 else "green"

# ----------- RIGHT COLUMN UI ----------- #
with right:
    st.markdown("###  Eco Status")

    # ---- CSS Animation applied to container ---- #
    st.markdown("""
    <style>
    .mascot-container {
        animation: bounce 2s infinite;
        text-align: center;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
    }

    .speech {
        background: black;
        padding: 8px;
        border-radius: 10px;
        font-size: 13px;
        margin-bottom: 6px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)

    # ---- Speech bubble ---- #
    st.markdown(f"<div class='speech'> {speech}</div>", unsafe_allow_html=True)

    # ---- Mascot image (Streamlit-safe) ---- #
    with st.container():
        st.markdown("<div class='mascot-container'>", unsafe_allow_html=True)
        if os.path.exists(mascot_img):
            st.image(mascot_img, width=300) 
        else:
            st.write("🦊")
        st.markdown("</div>", unsafe_allow_html=True)

    # ---- Progress bar ---- #
    st.markdown(
        f"""
        <div style="width:100%; background:#ddd; border-radius:12px; height:16px; margin-top:8px;">
            <div style="
                width:{eco_score}%;
                background:{bar_color};
                height:16px;
                border-radius:12px;
                transition: width 0.5s;">
            </div>
        </div>
        <p style="text-align:center; font-size:12px;">Eco Score: {eco_score:.1f}%</p>
        """,
        unsafe_allow_html=True
    )


# ----------- MAIN CONTENT ----------- #
with main:
    st.title(" Mindful Market")

    if tab == "Home":
        st.subheader("Add a Purchase")
        c1, c2 = st.columns(2)
        with c1:
            user_country = st.selectbox("Your Country", COUNTRIES.keys())
            user_district = st.selectbox("Your District", COUNTRIES[user_country]["districts"])
        with c2:
            shipper_country = st.selectbox("Shipper Country", COUNTRIES.keys())
            shipper_district = st.selectbox("Shipper District", COUNTRIES[shipper_country]["districts"])

        p1, p2 = st.columns(2)
        with p1:
            product = st.selectbox("Product Type", REAL_WORLD_FACTORS.keys())
        with p2:
            price = st.number_input("Price ₹", min_value=1, step=1)

        if st.button("Add Purchase"):
            total, distance, eco = calculate_co2(product, price, user_country, shipper_country)
            st.session_state.purchases.append({
                "Product": product,
                "Price": price,
                "Impact": total,
                "Distance": distance,
                "Eco": eco,
                "Date": datetime.now()
            })
            st.success(f"Added! CO₂ Impact ≈ {total} kg")

    if tab == "Purchase History":
        st.subheader("Purchase History")
        if st.session_state.purchases:
            df = pd.DataFrame(st.session_state.purchases)
            if "Distance" not in df.columns: df["Distance"] = 0
            if "Eco" not in df.columns: df["Eco"] = False
            df["Eco Friendly"] = df["Eco"].apply(lambda x: "Yes 🌱" if x else "No ❌")
            df["Mascot"] = df["Eco"].apply(lambda x: "🦊😊" if x else "🦊😟")

            st.dataframe(
                df[["Mascot","Product","Price","Impact","Distance","Eco Friendly","Date"]],
                use_container_width=True
            )
        else:
            st.info("No purchases yet.")
