import pandas as pd
import streamlit as st

@st.cache_data
def load_data(data_file):
    df = pd.read_csv(data_file)

    df = df[
        [
            "Industry",
            "Country",
            "Total_Funding_USD",
            "Valuation_USD",
            "Funding_Amount_USD",
            "Unicorn_Flag",
            "Year",
        ]
    ].copy()

    df = df.dropna(
        subset=[
            "Year",
            "Industry",
            "Country",
        ]
    ).copy()

    df["Year"] = pd.to_numeric(
        df["Year"],
        errors="coerce",
    )

    df = df.dropna(
        subset=["Year"]
    ).copy()

    df["Year"] = df["Year"].astype(int)

    return df