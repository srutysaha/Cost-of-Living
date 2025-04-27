import streamlit as st
import pandas as pd
import joblib
import requests

# Load saved models
rent_model = joblib.load("rent_pipeline.pkl")
pg_model = joblib.load("pg_price_pipeline.pkl")  # updated pg pipeline
fare_model = joblib.load("fare_pipeline.pkl")

# OpenCage API key
API_KEY = '3c74f1a176c048acaba383a7d8b886b8'

# Static Food Cost (₹ per month)
food_cost_dict = {
    "new delhi": 7000,
    "mumbai": 8000,
    "bangalore": 7500,
    "kolkata": 6000,
    "hyderabad": 6500,
    "pune": 7000
}

# Function to get coordinates using OpenCage API
def get_coordinates_from_opencage(location):
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?q={location}&key={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get('results'):
                lat = data['results'][0]['geometry']['lat']
                lon = data['results'][0]['geometry']['lng']
                return lat, lon
            else:
                st.error(f"No results found for location: {location}")
                return None, None
        else:
            st.error(f"API request failed with status code {response.status_code}")
            return None, None
    except Exception as e:
        st.error(f"Error fetching coordinates: {e}")
        return None, None

# Streamlit App
st.title("Cost of Living Calculator 💸🏡")

# Accommodation Type
choice = st.radio("Choose Accommodation Type", ["🏠 Rent a Home", "🛏️ Live in a PG"])

if choice == "🏠 Rent a Home":
    st.header("🏠 Rent Details")
    bhk = st.number_input("Number of BHK", min_value=1, max_value=5, value=2)
    type_option = st.selectbox("Type", ['Flat', 'Builder', 'Apartment', 'Studio', 'Penthouse', 'House', 'Villa'])
    city = st.selectbox("City", list(food_cost_dict.keys()))
    location = st.text_input("Enter Location (e.g., Area or Locality)", "New Delhi")

    # Get location coordinates
    if location:
        latitude, longitude = get_coordinates_from_opencage(location)
        if latitude and longitude:
            st.success(f"Latitude: {latitude}, Longitude: {longitude}")
    else:
        latitude = st.number_input("Latitude", value=28.52)
        longitude = st.number_input("Longitude", value=77.21)

    furnishing = st.selectbox("Furnishing", ['Semi-Furnished', 'Unfurnished', 'Furnished'])
    bathroom = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2)
    tenant = st.selectbox("Tenant Type", ['Bachelors', 'Bachelors/Family'])
    carpet_area = st.number_input("Carpet Area (sq ft)", min_value=100, max_value=5000, value=1500)

elif choice == "🛏️ Live in a PG":
    st.header("🛏️ PG Details")
    gender = st.selectbox("PG Gender", ['Boys', 'Girls', 'Coed'])
    city = st.selectbox("City", list(food_cost_dict.keys()))
    food_included = st.selectbox("Food Included", ['Food Included', 'Food Charge extra'])
    wifi_available = st.selectbox("Wifi", ['Wifi Available', 'Wifi Not Available'])
    ac_available = st.selectbox("AC", ['AC Available', 'AC Not Available'])
    food_available = st.selectbox("Food Option", ['Food Available', 'Food Not Available'])

# Travel Details
st.header("🚕 Travel Details")

pickup_location = st.text_input("Enter Pickup Location", "South Delhi")
dropoff_location = st.text_input("Enter Drop-off Location", "Delhi")

if pickup_location and dropoff_location:
    pickup_lat, pickup_lon = get_coordinates_from_opencage(pickup_location)
    dropoff_lat, dropoff_lon = get_coordinates_from_opencage(dropoff_location)

    if pickup_lat and pickup_lon and dropoff_lat and dropoff_lon:
        st.success(f"Pickup: {pickup_location} - Latitude: {pickup_lat}, Longitude: {pickup_lon}")
        st.success(f"Dropoff: {dropoff_location} - Latitude: {dropoff_lat}, Longitude: {dropoff_lon}")
    else:
        st.warning("Could not get coordinates for pickup/dropoff.")

passengers = st.slider("Passenger Count", 1, 6, 1)

# Input for extra charges
extra_charge = st.number_input("Enter any extra living cost (₹)", min_value=0, value=0)

# Predict Total Cost
if st.button("Predict Total Cost"):
    total = 0

    # Predict Rent or PG
    if choice == "🏠 Rent a Home":
        rent_input = pd.DataFrame([{
            'BHK': bhk,
            'Type': type_option,
            'Latitude': latitude,
            'Longitude': longitude,
            'City': city,
            'furnishing': furnishing,
            'Bathroom': bathroom,
            'tenant_preferred': tenant,
            'carpet_area': carpet_area
        }])

        rent_pred = rent_model.predict(rent_input)[0]
        st.success(f"✅ Rent Prediction: ₹{int(rent_pred)}")
        total += rent_pred

        # Always add food cost for rent
        food_cost = food_cost_dict.get(city.lower(), 3000)
        st.info(f"🍛 Adding Food Cost (monthly per person): ₹{food_cost}")
        total += food_cost

    elif choice == "🛏️ Live in a PG":
        pg_input = pd.DataFrame([{
            'gender': gender,
            'city': city,
            'food_included': food_included,
            'wifi_available': wifi_available,
            'ac_available': ac_available,
            'food_available': food_available
        }])

        # ✅ NEW: pg_model already includes preprocessor!
        pg_pred = pg_model.predict(pg_input)[0]
        st.success(f"✅ PG Price Prediction: ₹{int(pg_pred)}")
        total += pg_pred

        # Add food cost if food is not included
        if food_included == 'Food Charge extra':
            food_cost = food_cost_dict.get(city.lower(), 3000)
            st.info(f"🍛 Adding Food Cost (Not Included): ₹{food_cost}")
            total += food_cost

    # Predict Uber Fare
    if pickup_lat and pickup_lon and dropoff_lat and dropoff_lon:
        uber_input = pd.DataFrame([{
            'pickup_longitude': pickup_lon,
            'pickup_latitude': pickup_lat,
            'dropoff_longitude': dropoff_lon,
            'dropoff_latitude': dropoff_lat,
            'passenger_count': passengers
        }])
        fare_pred = fare_model.predict(uber_input)[0] * 20
        st.success(f"✅ Travel Fare Prediction: ₹{int(fare_pred)} \n\nNOTE 👉 Private transport is considered; Using Public transport may reduce the fare.")
        total += fare_pred

    # Add the extra charge
    st.info(f"🪙 Adding Extra Living Cost: ₹{extra_charge}")
    total += extra_charge

    # Final Total
    st.markdown("---")
    st.subheader(f"💰 Total Combined Estimated Cost: ₹{int(total)}")
