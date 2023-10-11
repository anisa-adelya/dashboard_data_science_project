import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe
def create_season_df(df):
    byseason_df = df.groupby(by="season").instant.nunique().reset_index()
    byseason_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byseason_df

def create_yr_df(df):
    byyr_df = df.groupby(by="yr").instant.nunique().reset_index()
    byyr_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byyr_df

def create_workingday_df(df):
    byworkingday_df = df.groupby(by="workingday").instant.nunique().reset_index()
    byworkingday_df.rename(columns={
        "instant": "sum"
    }, inplace=True)
    
    return byworkingday_df

def create_weathersit_df(df):
    byweathersit_df = df.groupby(by="weathersit").instant.nunique().reset_index()
    byweathersit_df.rename(columns={
        "instant": "sum"
    }, inplace=True)

    return byweathersit_df

# Mengambil dataset yang sudah melalui tahap cleansing data
all_df = pd.read_csv("all_data_submission.csv")

datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# Filter dataset berdasarkan tanggal order
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/anisa-adelya/submission_dashboar/blob/main/logo_dashboard.png?raw=true")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

season_df = create_season_df(main_df)
year_df = create_yr_df(main_df)
workingday_df = create_workingday_df(main_df)
weathersit_df = create_weathersit_df(main_df)

st.header('Bike Sharing Dashboard')

# Menampilkan Jumlah User Bike berdasarkan Musin
st.subheader('User Bike Sharing by Season')
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    x="season",
    y="sum",
    data=season_df.sort_values(by="season", ascending=False),
    ax=ax
)
ax.set_title("Number of Bike Sharing by Season", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis="y", labelsize=20)
ax.tick_params(axis="x", labelsize=15)
st.pyplot(fig)

# Menampilkan Jumlah User berdasarkan Tahun
st.subheader("User Bike Sharing by Year")

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    x="yr",
    y="sum",
    data=year_df.sort_values(by="yr", ascending=False),
    ax=ax
)
ax.set_title("Number of Bike Sharing by Year", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis="y", labelsize=20)
ax.tick_params(axis="x", labelsize=15)
st.pyplot(fig)

# Menampilkan Jumlah User Berdasarkan Working Day
st.subheader("User Bike by Working Day")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    x="workingday",
    y="sum",
    data=workingday_df.sort_values(by="workingday", ascending=False),
    ax=ax
)
ax.set_title("Number of Bike Sharing by Working Day", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis="y", labelsize=20)
ax.tick_params(axis="x", labelsize=15)
st.pyplot(fig)

# Menampilkan Jumlah User Berdasarkan Cuaca
st.subheader("User Bike by Weather Sit")

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
    x="weathersit",
    y="sum",
    data=weathersit_df.sort_values(by="weathersit", ascending=False),
    ax=ax
)
ax.set_title("Number of Bike Sharing by Weather Sit", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis="y", labelsize=20)
ax.tick_params(axis="x", labelsize=15)
st.pyplot(fig)
