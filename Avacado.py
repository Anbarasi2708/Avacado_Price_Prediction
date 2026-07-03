import streamlit as st
import pickle
import pandas as pd

# Load Model
with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load Scaler
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.set_page_config(page_title="Avocado Price Prediction", page_icon="🥑")

st.title("🥑 Avocado Price Prediction")
st.write("Enter the avocado details below.")

# Numerical Inputs
total_volume = st.number_input("Total Volume", min_value=0.0)
avocado_4046 = st.number_input("4046", min_value=0.0)
avocado_4225 = st.number_input("4225", min_value=0.0)
avocado_4770 = st.number_input("4770", min_value=0.0)

total_bags = st.number_input("Total Bags", min_value=0.0)
small_bags = st.number_input("Small Bags", min_value=0.0)
large_bags = st.number_input("Large Bags", min_value=0.0)
xlarge_bags = st.number_input("XLarge Bags", min_value=0.0)

type_value = st.selectbox("Type", ["conventional", "organic"])
year = st.selectbox("Year", [2015, 2016, 2017, 2018])

day = st.slider("Day", 1, 31)
month = st.slider("Month", 1, 12)

region = st.selectbox(
    "Region",
    [
        "Albany","Atlanta","BaltimoreWashington","Boise","Boston",
        "BuffaloRochester","California","Charlotte","Chicago",
        "CincinnatiDayton","Columbus","DallasFtWorth","Denver",
        "Detroit","GrandRapids","GreatLakes",
        "HarrisburgScranton","HartfordSpringfield","Houston",
        "Indianapolis","Jacksonville","LasVegas","LosAngeles",
        "Louisville","MiamiFtLauderdale","Midsouth","Nashville",
        "NewOrleansMobile","NewYork","Northeast",
        "NorthernNewEngland","Orlando","Philadelphia",
        "PhoenixTucson","Pittsburgh","Plains","Portland",
        "RaleighGreensboro","RichmondNorfolk","Roanoke",
        "Sacramento","SanDiego","SanFrancisco","Seattle",
        "SouthCarolina","SouthCentral","Southeast","Spokane",
        "StLouis","Syracuse","Tampa","TotalUS","West",
        "WestTexNewMexico"
    ]
)

if st.button("Predict Price"):

    type_encoded = 0 if type_value == "conventional" else 1

    regions = [
        "Albany","Atlanta","BaltimoreWashington","Boise","Boston",
        "BuffaloRochester","California","Charlotte","Chicago",
        "CincinnatiDayton","Columbus","DallasFtWorth","Denver",
        "Detroit","GrandRapids","GreatLakes",
        "HarrisburgScranton","HartfordSpringfield","Houston",
        "Indianapolis","Jacksonville","LasVegas","LosAngeles",
        "Louisville","MiamiFtLauderdale","Midsouth","Nashville",
        "NewOrleansMobile","NewYork","Northeast",
        "NorthernNewEngland","Orlando","Philadelphia",
        "PhoenixTucson","Pittsburgh","Plains","Portland",
        "RaleighGreensboro","RichmondNorfolk","Roanoke",
        "Sacramento","SanDiego","SanFrancisco","Seattle",
        "SouthCarolina","SouthCentral","Southeast","Spokane",
        "StLouis","Syracuse","Tampa","TotalUS","West",
        "WestTexNewMexico"
    ]

    data = {
        "Total Volume":[total_volume],
        "4046":[avocado_4046],
        "4225":[avocado_4225],
        "4770":[avocado_4770],
        "Total Bags":[total_bags],
        "Small Bags":[small_bags],
        "Large Bags":[large_bags],
        "XLarge Bags":[xlarge_bags],
        "type":[type_encoded],
        "year":[year],
        "Day":[day],
        "Month":[month]
    }

    for r in regions:
        data["region_" + r] = [1 if region == r else 0]

    input_df = pd.DataFrame(data)

    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)

    st.success(f"Predicted Average Price: ${prediction[0]:.2f}")