# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import matplotlib.pyplot as plt

# # Load trained model
# bundle = joblib.load("final_rain_model.joblib")
# model = bundle["model"]
# threshold = bundle["threshold"]
# features = bundle["features"]

# # Load dataset
# df = pd.read_csv("India_Capitals_Daily_Weather_years.csv", parse_dates=['Date'])

# # Manually predict function
# def predict_manual(max_temp, min_temp, mean_temp, humidity, pressure, windspeed,
#                    cloudcover, rainfall, date, rain_lag1=0, rain_3sum=0):
    
#     dt = pd.to_datetime(date)
#     temp_range = max_temp - min_temp
#     month = dt.month
#     doy = dt.dayofyear
#     is_monsoon = 1 if month in [6,7,8,9] else 0

#     X = np.array([[max_temp, min_temp, mean_temp, humidity, pressure, windspeed,
#                    cloudcover, rainfall, rain_lag1, rain_3sum, temp_range,
#                    month, doy, is_monsoon]])

#     prob = model.predict_proba(X)[0][1] * 100
#     prediction = "🌧️ Rain" if prob >= (threshold * 100) else "☀️ No Rain"

#     return prediction, prob


# # --------------------------------------------------------------
# # Streamlit UI
# # --------------------------------------------------------------

# st.set_page_config(page_title="Rainfall Prediction App", layout="wide")
# st.title("🌦️ India Rainfall Prediction System")

# tab1, tab2 = st.tabs(["🌧️ Prediction", "📊 Visualizations"])


# # ==============================================================
# # 1️⃣ PREDICTION TAB
# # ==============================================================
# with tab1:

#     st.header("🌧️ Predict Rainfall using Manual Inputs")

#     col1, col2 = st.columns(2)

#     with col1:
#         max_temp = st.slider("Max Temperature (°C)", 10, 50, 30)
#         min_temp = st.slider("Min Temperature (°C)", 5, 35, 20)
#         mean_temp = st.slider("Mean Temperature (°C)", 10, 45, 25)
#         humidity = st.slider("Humidity (%)", 0, 100, 70)
#         pressure = st.slider("Pressure (hPa)", 900, 1100, 1005)

#     with col2:
#         windspeed = st.slider("Wind Speed (km/h)", 0, 50, 10)
#         cloudcover = st.slider("Cloud Cover (%)", 0, 100, 40)
#         rainfall = st.slider("Today's Rainfall (mm)", 0, 50, 0)
#         date = st.date_input("Choose Date")

#     if st.button("🔮 Predict Rainfall"):
#         pred, prob = predict_manual(
#             max_temp, min_temp, mean_temp, humidity, pressure, windspeed,
#             cloudcover, rainfall, str(date)
#         )

#         st.success(f"### Prediction: {pred}")
#         st.info(f"### Probability of Rain: {prob:.2f} %")


# # ==============================================================
# # 2️⃣ VISUALIZATION TAB
# # ==============================================================
# with tab2:
#     st.header("📊 Rainfall & Weather Visual Analysis")

#     city = st.selectbox("Choose City", df["City"].unique())
#     df_city = df[df["City"] == city].copy()

#     # Month-wise rainfall
#     st.subheader("🌧️ Month-wise Rainfall")
#     df_city["Month"] = df_city["Date"].dt.month
#     month_rain = df_city.groupby("Month")["Rainfall"].sum()

#     fig, ax = plt.subplots()
#     month_rain.plot(kind="bar", color="skyblue", ax=ax)
#     ax.set_title(f"Monthly Rainfall in {city}")
#     ax.set_xlabel("Month")
#     ax.set_ylabel("Total Rainfall (mm)")
#     st.pyplot(fig)

#     # Season-wise rainfall
#     st.subheader("🌦️ Season-wise Rainfall")

#     def get_season(month):
#         if month in [6,7,8,9]:
#             return "Monsoon"
#         elif month in [10,11]:
#             return "Post-Monsoon"
#         elif month in [12,1,2]:
#             return "Winter"
#         else:
#             return "Summer"

#     df_city["Season"] = df_city["Month"].apply(get_season)
#     season_rain = df_city.groupby("Season")["Rainfall"].sum()

#     fig2, ax2 = plt.subplots()
#     season_rain.plot(kind="bar", color="orange", ax=ax2)
#     ax2.set_title(f"Season-wise Rainfall in {city}")
#     ax2.set_ylabel("Total Rainfall (mm)")
#     st.pyplot(fig2)

#     # Last 30 days rainfall trend
#     st.subheader("📈 Rainfall Trend (Last 30 Days)")

#     df_30 = df_city.tail(30)

#     fig3, ax3 = plt.subplots()
#     ax3.plot(df_30["Date"], df_30["Rainfall"], marker="o")
#     ax3.set_title(f"Last 30 Days Rainfall in {city}")
#     ax3.set_ylabel("Rainfall (mm)")
#     ax3.set_xlabel("Date")
#     st.pyplot(fig3)

#     # Humidity vs Rainfall
#     st.subheader("💧 Humidity vs Rainfall Relationship")

#     fig4, ax4 = plt.subplots()
#     ax4.scatter(df_city["Humidity"], df_city["Rainfall"], alpha=0.5)
#     ax4.set_xlabel("Humidity (%)")
#     ax4.set_ylabel("Rainfall (mm)")
#     ax4.set_title(f"Humidity vs Rainfall in {city}")
#     st.pyplot(fig4)



# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import plotly.express as px
# import plotly.graph_objects as go

# # Load trained model
# bundle = joblib.load("final_rain_model.joblib")
# model = bundle["model"]
# threshold = bundle["threshold"]
# features = bundle["features"]

# # Load dataset
# df = pd.read_csv("India_Capitals_Daily_Weather_years.csv", parse_dates=['Date'])

# # Manually predict function
# def predict_manual(max_temp, min_temp, mean_temp, humidity, pressure, windspeed,
#                    cloudcover, rainfall, date, rain_lag1=0, rain_3sum=0):
    
#     dt = pd.to_datetime(date)
#     temp_range = max_temp - min_temp
#     month = dt.month
#     doy = dt.dayofyear
#     is_monsoon = 1 if month in [6,7,8,9] else 0

#     X = np.array([[max_temp, min_temp, mean_temp, humidity, pressure, windspeed,
#                    cloudcover, rainfall, rain_lag1, rain_3sum, temp_range,
#                    month, doy, is_monsoon]])

#     prob = model.predict_proba(X)[0][1] * 100
#     prediction = "🌧️ Rain" if prob >= (threshold * 100) else "☀️ No Rain"

#     return prediction, prob


# # --------------------------------------------------------------
# # Streamlit UI
# # --------------------------------------------------------------

# st.set_page_config(page_title="Rainfall Prediction App", layout="wide")
# st.title("🌦️ India Rainfall Prediction System")

# tab1, tab2 = st.tabs(["🌧️ Prediction", "📊 Visualizations"])


# # ==============================================================
# # 1️⃣ PREDICTION TAB (same as before)
# # ==============================================================
# with tab1:

#     st.header("🌧️ Predict Rainfall using Manual Inputs")

#     col1, col2 = st.columns(2)

#     with col1:
#         max_temp = st.slider("Max Temperature (°C)", 10, 50, 30)
#         min_temp = st.slider("Min Temperature (°C)", 5, 35, 20)
#         mean_temp = st.slider("Mean Temperature (°C)", 10, 45, 25)
#         humidity = st.slider("Humidity (%)", 0, 100, 70)
#         pressure = st.slider("Pressure (hPa)", 900, 1100, 1005)

#     with col2:
#         windspeed = st.slider("Wind Speed (km/h)", 0, 50, 10)
#         cloudcover = st.slider("Cloud Cover (%)", 0, 100, 40)
#         rainfall = st.slider("Today's Rainfall (mm)", 0, 50, 0)
#         date = st.date_input("Choose Date")

#     if st.button("🔮 Predict Rainfall"):
#         pred, prob = predict_manual(
#             max_temp, min_temp, mean_temp, humidity, pressure, windspeed,
#             cloudcover, rainfall, str(date)
#         )

#         st.success(f"### Prediction: {pred}")
#         st.info(f"### Probability of Rain: {prob:.2f} %")


# # ==============================================================
# # 2️⃣ VISUALIZATION TAB (Plotly Beautiful Charts)
# # ==============================================================
# with tab2:
#     st.header("📊 Rainfall & Weather Visual Analysis")

#     city = st.selectbox("Choose City", df["City"].unique())
#     df_city = df[df["City"] == city].copy()

#     # __________________________________________________________
#     # 🌧️ Month-wise Rainfall (Plotly Bar Chart)
#     # __________________________________________________________
#     st.subheader("🌧️ Month-wise Rainfall")

#     df_city["Month"] = df_city["Date"].dt.month
#     month_rain = df_city.groupby("Month")["Rainfall"].sum().reset_index()

#     fig = px.bar(
#         month_rain,
#         x="Month",
#         y="Rainfall",
#         color="Rainfall",
#         color_continuous_scale="Blues",
#         title=f"Monthly Rainfall in {city}",
#         labels={"Rainfall": "Total Rainfall (mm)"}
#     )
#     fig.update_layout(template="plotly_white")
#     st.plotly_chart(fig, use_container_width=True)

#     # __________________________________________________________
#     # 🌦️ Season-wise Rainfall (Plotly Donut)
#     # __________________________________________________________
#     st.subheader("🌦️ Season-wise Rainfall")

#     def get_season(month):
#         if month in [6,7,8,9]:
#             return "Monsoon"
#         elif month in [10,11]:
#             return "Post-Monsoon"
#         elif month in [12,1,2]:
#             return "Winter"
#         else:
#             return "Summer"

#     df_city["Season"] = df_city["Month"].apply(get_season)
#     season_rain = df_city.groupby("Season")["Rainfall"].sum().reset_index()

#     fig2 = px.pie(
#         season_rain,
#         names="Season",
#         values="Rainfall",
#         hole=0.45,
#         title=f"Season-wise Rainfall in {city}",
#         color_discrete_sequence=px.colors.qualitative.Set3
#     )
#     fig2.update_layout(template="plotly_white")
#     st.plotly_chart(fig2, use_container_width=True)

#     # __________________________________________________________
#     # 📈 Last 30 Days Rainfall Trend (Plotly Line Chart)
#     # __________________________________________________________
#     st.subheader("📈 Rainfall Trend (Last 30 Days)")

#     df_30 = df_city.tail(30)

#     fig3 = px.line(
#         df_30,
#         x="Date",
#         y="Rainfall",
#         markers=True,
#         title=f"Last 30 Days Rainfall — {city}",
#         color_discrete_sequence=["royalblue"]
#     )
#     fig3.update_layout(template="plotly_white")
#     st.plotly_chart(fig3, use_container_width=True)

#     # __________________________________________________________
#     # 💧 Humidity vs Rainfall (Plotly Scatter)
#     # __________________________________________________________
#     st.subheader("💧 Humidity vs Rainfall Relationship")

#     fig4 = px.scatter(
#         df_city,
#         x="Humidity",
#         y="Rainfall",
#         size="Rainfall",
#         color="Rainfall",
#         color_continuous_scale="Viridis",
#         opacity=0.6,
#         title=f"Humidity vs Rainfall — {city}",
#         labels={"Humidity": "Humidity (%)", "Rainfall": "Rainfall (mm)"}
#     )
#     fig4.update_layout(template="plotly_white")
#     st.plotly_chart(fig4, use_container_width=True)



# app.py (final)
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

# ------------------------------
# Load model bundle & data
# ------------------------------
bundle = joblib.load("final_rain_model.joblib")  
model = bundle["model"]
threshold = bundle["threshold"]
MODEL_FEATURES = bundle["features"]            
# Load dataset (must exist)
DF_PATH = "India_Capitals_Daily_Weather_years.csv"
df = pd.read_csv(DF_PATH, parse_dates=["Date"])


df.columns = df.columns.str.strip()

# ------------------------------
# Small UI theme / background
# ------------------------------
st.set_page_config(page_title="Rainfall Prediction Dashboard", layout="wide")
st.markdown(
    """
    <style>
        .reportview-container {background: #F5F7FA;}
        .sidebar .sidebar-content {background: #EAF1F8;}
        header {background: transparent;}
        h1,h2,h3,h4 {color: #2C3E50;}
        .stButton>button {background-color: #2B7A78; color: white;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "🌧️ Prediction",
        "🤖 Auto Prediction (City Based)",
        "📊 Visualizations",
        # "🔍 Correlation Heatmap",
        "📈 Actual vs Predicted"
    ],
)

st.title("🌦️ India Rainfall Prediction Dashboard")

def build_feature_vector_from_inputs(max_temp, min_temp, mean_temp, humidity, pressure,
                                     windspeed, cloudcover, rainfall, date,
                                     rain_lag1=0, rain_3sum=0, city_name=None):
    dt = pd.to_datetime(date)
    temp_range = max_temp - min_temp
    month = int(dt.month)
    doy = int(dt.dayofyear)
    is_monsoon = 1 if month in [6,7,8,9] else 0

    # base values dictionary with raw and derived features
    base = {
        "Max Temp": max_temp,
        "Min Temp": min_temp,
        "Mean Temp": mean_temp,
        "Humidity": humidity,
        "Pressure": pressure,
        "WindSpeed": windspeed,
        "CloudCover": cloudcover,
        "Rainfall": rainfall,
        "Rain_lag1": rain_lag1,
        "Rain_3sum": rain_3sum,
        "Temp_range": temp_range,
        "Month": month,
        "DayOfYear": doy,
        "IsMonsoon": is_monsoon
    }

    row = []
    for col in MODEL_FEATURES:
        if col in base:
            row.append(base[col])
        elif col.startswith("City_"):
            
            if city_name is None:
                row.append(0)
            else:
                
                if col == f"City_{city_name}":
                    row.append(1)
                else:
                    if col == f"City_{city_name.replace(' ', '_')}":
                        row.append(1)
                    else:
                        row.append(0)
        else:
            row.append(0)
    return np.array(row).reshape(1, -1)


def prepare_df_features(df_local):
    """Add commonly used derived features to a dataframe (non-destructive)"""
    tmp = df_local.copy()
    tmp["Rain_lag1"] = tmp["Rainfall"].shift(1).fillna(0)
    tmp["Rain_3sum"] = tmp["Rainfall"].rolling(3, min_periods=1).sum().shift(1).fillna(0)
    tmp["Temp_range"] = tmp["Max Temp"] - tmp["Min Temp"]
    tmp["Month"] = tmp["Date"].dt.month
    tmp["DayOfYear"] = tmp["Date"].dt.dayofyear
    tmp["IsMonsoon"] = tmp["Month"].isin([6,7,8,9]).astype(int)
    return tmp

# ------------------------------
# Prediction page (manual)
# ------------------------------
if page == "🌧️ Prediction":
    st.header("🌧️ Manual Prediction")
    st.write("Use sliders to provide today's weather values and predict whether it will rain tomorrow.")

    col1, col2 = st.columns(2)
    with col1:
        max_temp = st.slider("Max Temperature (°C)", 5, 50, 30)
        min_temp = st.slider("Min Temperature (°C)", 0, 40, 20)
        mean_temp = st.slider("Mean Temperature (°C)", 5, 45, 25)
        humidity = st.slider("Humidity (%)", 0, 100, 70)
        pressure = st.slider("Pressure (hPa)", 900, 1100, 1005)
    with col2:
        windspeed = st.slider("Wind Speed (km/h)", 0, 50, 10)
        cloudcover = st.slider("Cloud Cover (%)", 0, 100, 40)
        rainfall = st.slider("Today's Rainfall (mm)", 0.0, 200.0, 0.0, step=0.1)
        date = st.date_input("Date")

    city_opt = st.selectbox("City (optional, improves prediction)", np.insert(df["City"].unique(), 0, ""))
    if city_opt == "":
        city_opt = None

    if st.button("🔮 Predict (Manual)"):
        Xvec = build_feature_vector_from_inputs(
            max_temp, min_temp, mean_temp, humidity, pressure,
            windspeed, cloudcover, rainfall, date,
            rain_lag1=rainfall, rain_3sum=rainfall, city_name=city_opt
        )
        prob = model.predict_proba(Xvec)[0][1] * 100
        label = "🌧️ Rain" if prob >= (threshold * 100) else "☀️ No Rain"
        st.success(f"Prediction: {label}")
        st.info(f"Probability of Rain: {prob:.2f}%")

# ------------------------------
# Auto Prediction page (uses latest row)
# ------------------------------
elif page == "🤖 Auto Prediction (City Based)":
    st.header("🤖 Auto Prediction — Use Latest Available Weather for a City")
    city_list = df["City"].unique()
    selected_city = st.selectbox("Choose City", city_list)

    df_latest = df[df["City"] == selected_city].sort_values("Date").tail(1)
    if df_latest.shape[0] == 0:
        st.warning("No data for this city.")
    else:
        latest = df_latest.iloc[0]
        st.write("Latest weather (from dataset):")
        st.table(latest[["Date", "Max Temp", "Min Temp", "Mean Temp", "Humidity", "Pressure", "WindSpeed", "CloudCover", "Rainfall"]])

        if st.button("🔮 Predict for Selected City (Auto)"):
            Xvec = build_feature_vector_from_inputs(
                latest["Max Temp"], latest["Min Temp"], latest["Mean Temp"],
                latest["Humidity"], latest["Pressure"], latest["WindSpeed"],
                latest["CloudCover"], latest["Rainfall"], latest["Date"],
                rain_lag1=latest["Rainfall"], rain_3sum=latest["Rainfall"], city_name=selected_city
            )
            prob = model.predict_proba(Xvec)[0][1] * 100
            label = "🌧️ Rain" if prob >= (threshold * 100) else "☀️ No Rain"
            st.success(f"Prediction: {label}")
            st.info(f"Probability of Rain: {prob:.2f}%")

# ------------------------------
# Visualizations page
# ------------------------------
elif page == "📊 Visualizations":
    st.header("📊 Visualizations — Rain & Weather")

    city = st.selectbox("Choose City", df["City"].unique())
    df_city = df[df["City"] == city].copy()
    df_city = prepare_df_features(df_city)

    # Month-wise rainfall
    st.subheader("🌧️ Month-wise Rainfall")
    month_rain = df_city.groupby(df_city["Date"].dt.month)["Rainfall"].sum().reset_index()
    month_rain.columns = ["Month", "Rainfall"]
    fig = px.bar(month_rain, x="Month", y="Rainfall", color="Rainfall", color_continuous_scale="Blues",
                 title=f"Monthly Rainfall — {city}", labels={"Rainfall": "Total Rainfall (mm)"})
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    # Season-wise donut
    st.subheader("🌦️ Season-wise Rainfall")
    df_city["Season"] = df_city["Month"].apply(lambda m: "Monsoon" if m in [6,7,8,9] else ("Post-Monsoon" if m in [10,11] else ("Winter" if m in [12,1,2] else "Summer")) )
    season_rain = df_city.groupby("Season")["Rainfall"].sum().reset_index()
    fig2 = px.pie(season_rain, names="Season", values="Rainfall", hole=0.45, title=f"Season-wise Rainfall — {city}",
                  color_discrete_sequence=px.colors.qualitative.Set3)
    fig2.update_layout(template="plotly_white")
    st.plotly_chart(fig2, use_container_width=True)

    # Last 30 days line
    st.subheader("📈 Last 30 Days Rainfall Trend")
    df_30 = df_city.tail(30)
    fig3 = px.line(df_30, x="Date", y="Rainfall", markers=True, title=f"Last 30 Days — {city}", color_discrete_sequence=["royalblue"])
    fig3.update_layout(template="plotly_white")
    st.plotly_chart(fig3, use_container_width=True)

    # Humidity vs Rainfall scatter
    st.subheader("💧 Humidity vs Rainfall")
    fig4 = px.scatter(df_city, x="Humidity", y="Rainfall", size="Rainfall", color="Rainfall",
                      color_continuous_scale="Viridis", title=f"Humidity vs Rainfall — {city}")
    fig4.update_layout(template="plotly_white")
    st.plotly_chart(fig4, use_container_width=True)

    st.header("🔍 Correlation Heatmap (Interactive)")
    corr_df = df[["Max Temp","Min Temp","Mean Temp","Humidity","Pressure","WindSpeed","CloudCover","Rainfall"]].corr()
    fig = px.imshow(corr_df, text_auto=True, color_continuous_scale="RdBu_r", title="Correlation Heatmap")
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
    

# ------------------------------
# Correlation heatmap page
# ------------------------------
# elif page == "🔍 Correlation Heatmap":
#     st.header("🔍 Correlation Heatmap (Interactive)")

#     corr_df = df[["Max Temp","Min Temp","Mean Temp","Humidity","Pressure","WindSpeed","CloudCover","Rainfall"]].corr()
#     fig = px.imshow(corr_df, text_auto=True, color_continuous_scale="RdBu_r", title="Correlation Heatmap")
#     fig.update_layout(template="plotly_white")
#     st.plotly_chart(fig, use_container_width=True)

# ------------------------------
# Actual vs Predicted page
# ------------------------------
elif page == "📈 Actual vs Predicted":
    st.header("📈 Actual vs Predicted Rainfall (Last 60 Days)")

    city = st.selectbox("Choose City for Comparison", df["City"].unique(), key="avp_city")
    df_city = df[df["City"] == city].copy()
    df_city = prepare_df_features(df_city)
    df_last60 = df_city.tail(60).copy()

    # Build predictions
    feature_cols = ['Max Temp','Min Temp','Mean Temp','Humidity','Pressure','WindSpeed',
                    'CloudCover','Rainfall','Rain_lag1','Rain_3sum','Temp_range',
                    'Month','DayOfYear','IsMonsoon']

    # Ensure feature columns exist (if not, try to adapt)
    available = [c for c in feature_cols if c in df_last60.columns]
    preds = []
    for _, row in df_last60.iterrows():
        # build vector with city dummy info so model receives same shape as training
        Xvec = build_feature_vector_from_inputs(
            row["Max Temp"], row["Min Temp"], row["Mean Temp"], row["Humidity"], row["Pressure"],
            row["WindSpeed"], row["CloudCover"], row["Rainfall"], row["Date"],
            rain_lag1=row.get("Rain_lag1", 0), rain_3sum=row.get("Rain_3sum", 0), city_name=row["City"]
        )
        prob = model.predict_proba(Xvec)[0][1] * 100
        preds.append(prob)
    df_last60["Pred_Prob"] = preds
    df_last60["Pred_Scaled"] = df_last60["Pred_Prob"] / 5.0   # scale for visualization

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_last60["Date"], y=df_last60["Rainfall"], mode="lines+markers",
                             name="Actual Rainfall", line=dict(color="royalblue", width=3)))
    fig.add_trace(go.Scatter(x=df_last60["Date"], y=df_last60["Pred_Scaled"], mode="lines+markers",
                             name="Predicted Prob (scaled)", line=dict(color="orange", width=3, dash="dash")))
    fig.update_layout(title=f"Actual vs Predicted Rainfall — {city}", xaxis_title="Date", yaxis_title="Rainfall / Scaled Probability",
                      template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    # also show data table
    st.subheader("Table: Actual vs Predicted (Last 60 Days)")
    st.dataframe(df_last60[["Date","Rainfall","Pred_Prob"]].rename(columns={"Pred_Prob":"Predicted_Probability(%)"}))

# ------------------------------
# Footer / About
# ------------------------------
st.markdown("---")
st.markdown("**Notes:** Model probabilities are calibrated. Predicted probability is shown in %; for chart comparison the probability is scaled visually.")
st.markdown("Built with ❤️ using Streamlit and Plotly.")
