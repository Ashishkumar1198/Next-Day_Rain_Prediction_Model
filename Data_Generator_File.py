import requests
import pandas as pd
from datetime import datetime, timedelta

# Dictionary of Indian state & UT capitals
INDIA_CAPITALS = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata",
    "Andaman and Nicobar Islands": "Port Blair",
    "Chandigarh": "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu": "Daman",
    "Delhi": "New Delhi",
    "Jammu and Kashmir": "Srinagar",
    "Ladakh": "Leh",
    "Lakshadweep": "Kavaratti",
    "Puducherry": "Puducherry"
}

def get_coordinates(city):
    """Fetch latitude and longitude using Open-Meteo Geocoding API."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    res = requests.get(url).json()
    if "results" not in res:
        return None, None
    return res["results"][0]["latitude"], res["results"][0]["longitude"]

def fetch_daily_weather(city):
    """Fetch last 1 year of daily weather."""
    lat, lon = get_coordinates(city)
    if lat is None:
        print(f"❌ Coordinates not found for {city}")
        return pd.DataFrame()

    print(f"📍 Fetching daily weather for {city} ({lat}, {lon})")

    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=365)

    url = (
        "https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}&longitude={lon}"
        f"&start_date={start_date}&end_date={end_date}"
        "&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,"
        "relative_humidity_2m_mean,surface_pressure_mean,windspeed_10m_max,"
        "cloudcover_mean,precipitation_sum"
        "&timezone=auto"
    )

    data = requests.get(url).json()

    df = pd.DataFrame({
        "City": city,
        "Date": data["daily"]["time"],
        "Max Temp": data["daily"]["temperature_2m_max"],
        "Min Temp": data["daily"]["temperature_2m_min"],
        "Mean Temp": data["daily"]["temperature_2m_mean"],
        "Humidity": data["daily"]["relative_humidity_2m_mean"],
        "Pressure": data["daily"]["surface_pressure_mean"],
        "WindSpeed": data["daily"]["windspeed_10m_max"],
        "CloudCover": data["daily"]["cloudcover_mean"],
        "Rainfall": data["daily"]["precipitation_sum"],
    })

    # Add RainTomorrow column (shift Rainfall by -1 day)
    rain_next = df["Rainfall"].shift(-1)
    df["RainTomorrow"] = (rain_next > 0).astype(int)

    return df


# ------------ MAIN: Collect for ALL cities into one file ------------ #

all_data = []

for state, capital in INDIA_CAPITALS.items():
    print("\n==============================")
    print(f"STATE: {state} | CAPITAL: {capital}")
    print("==============================")
    
    df = fetch_daily_weather(capital)
    if not df.empty:
        all_data.append(df)

# Combine all cities
final_df = pd.concat(all_data, ignore_index=True)

# Save ONE combined CSV
final_df.to_csv("India_Capitals_Daily_Weather_years.csv", index=False)

print("\n🎉 DONE! Saved file: India_Capitals_Daily_Weather.csv")
