import plotly.express as px


def create_funding_map(
    df_filtrado,
    map_scale,
):
    funding_by_country = (
        df_filtrado
        .groupby("Country")[
            "Funding_Amount_USD"
        ]
        .sum()
        .reset_index()
    )

    funding_by_country[
        "Funding_Billions"
    ] = (
        funding_by_country[
            "Funding_Amount_USD"
        ]
        / 1e9
    )

    country_to_iso = {
        "USA": "USA",
        "United States": "USA",
        "US": "USA",
        "UK": "GBR",
        "United Kingdom": "GBR",
        "Germany": "DEU",
        "Canada": "CAN",
        "Australia": "AUS",
        "India": "IND",
        "Singapore": "SGP",
        "Brazil": "BRA",
        "France": "FRA",
        "Italy": "ITA",
        "Spain": "ESP",
        "Japan": "JPN",
        "China": "CHN",
        "South Korea": "KOR",
        "Mexico": "MEX",
        "Argentina": "ARG",
        "Chile": "CHL",
        "Colombia": "COL",
        "Peru": "PER",
        "South Africa": "ZAF",
        "Nigeria": "NGA",
        "Egypt": "EGY",
        "Israel": "ISR",
        "Turkey": "TUR",
        "Russia": "RUS",
        "Switzerland": "CHE",
        "Sweden": "SWE",
        "Norway": "NOR",
        "Denmark": "DNK",
        "Finland": "FIN",
        "Netherlands": "NLD",
        "Belgium": "BEL",
        "Portugal": "PRT",
        "Greece": "GRC",
        "Poland": "POL",
        "Czech Republic": "CZE",
        "Hungary": "HUN",
        "Austria": "AUT",
        "Ireland": "IRL",
        "New Zealand": "NZL",
    }

    funding_by_country["ISO"] = (
        funding_by_country[
            "Country"
        ].map(country_to_iso)
    )

    funding_map = (
        funding_by_country
        .dropna(subset=["ISO"])
    )

    fig = px.choropleth(
        funding_map,
        locations="ISO",
        color="Funding_Billions",
        hover_name="Country",
        color_continuous_scale=map_scale,
        labels={
            "Funding_Billions": "US$ Bilhões"
        },
        projection="natural earth",
    )

    return fig


def create_industry_evolution_chart(
    df_filtrado,
    qualitative_palette,
):
    evolution = (
        df_filtrado
        .groupby(
            [
                "Year",
                "Industry",
            ]
        )
        .size()
        .reset_index(
            name="Count"
        )
    )

    fig = px.line(
        evolution,
        x="Year",
        y="Count",
        color="Industry",
        markers=True,
        color_discrete_sequence=qualitative_palette,
    )

    return fig


def create_valuation_boxplot(
    df_filtrado,
    qualitative_palette,
):
    fig = px.box(
        df_filtrado,
        x="Industry",
        y="Valuation_USD",

        labels={
            "Valuation_USD": "Valuation (USD)",
            "Industry": "",
        },

        color="Industry",

        color_discrete_sequence=qualitative_palette,
    )

    return fig
    
def create_ranking_chart(
    ranking,
):
    fig = px.bar(
        ranking,
        x="Metric",
        y="Industry",
        orientation="h",
    )

    return fig