import streamlit as st
from pathlib import Path
from src.data import load_data
from src.filters import render_filters, apply_filters
from src.metrics import calculate_metrics
from src.charts import (
    create_funding_map,
    create_industry_evolution_chart,
    create_valuation_boxplot,
    create_ranking_chart,
)
from src.ui import apply_chart_theme, metric_card

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "Startup_Funding_Analytics_150k.csv"
IMAGE_FILE = BASE_DIR / "assets" / "Logo.png"


st.set_page_config(
    page_title="Dashboard - Startup Funding",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# DESIGN SYSTEM
# ==========================================================
BG = "#0B1220"
BG_ALT = "#0E1728"
SIDEBAR_BG = "#0A101C"
PANEL = "#111C2E"
PANEL_HOVER = "#152238"
BORDER = "rgba(148, 163, 184, 0.16)"
TEXT = "#F8FAFC"
TEXT_MUTED = "#A8B3C7"
TEXT_SOFT = "#7F8CA3"
GRID = "rgba(148, 163, 184, 0.10)"

BLUE = "#3B82F6"
CYAN = "#22D3EE"
VIOLET = "#8B5CF6"
AMBER = "#F59E0B"
EMERALD = "#10B981"
ROSE = "#F43F5E"


# ==========================================================
# PALETAS DOS GRÁFICOS
# ==========================================================
QUALITATIVE = [
    "#5B6E8C",
    "#7A6F9B",
    "#5F8F87",
    "#A48762",
    "#8C6570",
    "#627D9D",
    "#786C82",
    "#6F8779",
]

BAR_PALETTE = [
    "#1E3A5F",
    "#2563EB",
    "#3B82F6",
    "#4F46E5",
    "#6366F1",
    "#7C3AED",
    "#8B5CF6",
]

MAP_SCALE = [
    [0.00, "#172554"],
    [0.20, "#1E3A8A"],
    [0.45, "#1D4ED8"],
    [0.70, "#0284C7"],
    [1.00, "#22D3EE"],
]


# ==========================================================
# CSS
# ==========================================================
CSS_FILE = BASE_DIR / "assets" / "style.css"

css = CSS_FILE.read_text(
    encoding="utf-8"
)

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True,
)


# ==========================================================
# DATA
# ==========================================================
df = load_data(DATA_FILE)


# ==========================================================
# SIDEBAR
# ==========================================================
(
    pais_selecionado,
    industria_selecionada,
    ano_inicial,
    ano_final,
    metrica_ranking,
) = render_filters(df)

# ==========================================================
# APLICAÇÃO DOS FILTROS
# ==========================================================
df_filtrado = apply_filters(
    df,
    pais_selecionado,
    industria_selecionada,
    ano_inicial,
    ano_final,
)

(
    total_startups,
    total_investimento,
    media_valuation,
    percentual_unicornios,
) = calculate_metrics(df_filtrado)

# ==========================================================
# KPI CARDS
# ==========================================================
with st.container():

    col1, col2, col3, col4 = st.columns(4)

    # ------------------------------------------------------
    # KPI 1
    # ------------------------------------------------------
    with col1:

        metric_card(
            f"{total_startups:,}",
            "Total Startups",
            f"{ano_inicial}–{ano_final}",
            CYAN,
            "#102F4A",
        )

    # ------------------------------------------------------
    # KPI 2
    # ------------------------------------------------------
    with col2:

        metric_card(
            f"${total_investimento:.1f}B",
            "Total Investimento",
            "Capital acumulado no recorte",
            ROSE,
            "#3A202B",
        )

    # ------------------------------------------------------
    # KPI 3
    # ------------------------------------------------------
    with col3:

        metric_card(
            f"${media_valuation:.1f}B",
            "Média Valuation",
            "Média das empresas filtradas",
            AMBER,
            "#3B3018",
        )

    # ------------------------------------------------------
    # KPI 4
    # ------------------------------------------------------
    with col4:

        metric_card(
            f"{percentual_unicornios:.1f}%",
            "Unicórnios",
            "Participação no recorte",
            VIOLET,
            "#302044",
        )

# ==========================================================
# GRÁFICOS — LINHA 1
# ==========================================================
with st.container():

    st.markdown(
        '<h3 class="section-title">'
        'Análise Geográfica e Setorial'
        '</h3>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    # ======================================================
    # MAPA
    # ======================================================
    with col1:

        fig1 = create_funding_map(
            df_filtrado,
            MAP_SCALE,
        )

        apply_chart_theme(
            fig1,
            "Capital Captado por País (US$ Bilhões)",
            height=400,
            showlegend=False,
        )

        fig1.update_layout(

            geo=dict(
                bgcolor="rgba(0,0,0,0)",
                showframe=False,
                showcoastlines=False,
                showland=True,
                landcolor="#172236",
                showcountries=True,
                countrycolor="#334155",
                countrywidth=0.7,
                showocean=True,
                oceancolor="#0E1728",
                showlakes=True,
                lakecolor="#0E1728",
                projection_scale=1.03,
            ),

            coloraxis_colorbar=dict(
                title="US$ B",
                thickness=9,
                len=0.62,
                x=0.98,
                outlinewidth=0,

                tickfont=dict(
                    color=TEXT_MUTED,
                    size=10,
                ),

                title_font=dict(
                    color=TEXT_MUTED,
                    size=10,
                ),
            ),
        )

        fig1.update_traces(

            marker_line_color="#0B1220",
            marker_line_width=0.55,

            hovertemplate=(
                "<b>%{hovertext}</b>"
                "<br>US$ %{z:.2f} bi"
                "<extra></extra>"
            ),
        )

        st.plotly_chart(
            fig1,
            use_container_width=True,
            config={
                "displayModeBar": False
            },
        )

       # ======================================================
    # RANKING DINÂMICO
    # ======================================================
    with col2:

        if metrica_ranking == "Investimento":

            ranking = (
                df_filtrado
                .groupby("Industry")[
                    "Funding_Amount_USD"
                ]
                .sum()
                .reset_index()
            )

            ranking["Metric"] = (
                ranking[
                    "Funding_Amount_USD"
                ]
            )

            titulo_ranking = (
                "Investimento por Indústria"
            )

            eixo_x = "Investimento (USD)"

            hover_template = (
                "<b>%{y}</b>"
                "<br>US$ %{x:,.0f}"
                "<extra></extra>"
            )

        elif metrica_ranking == "Número de Startups":

            ranking = (
                df_filtrado
                .groupby("Industry")
                .size()
                .reset_index(
                    name="Startup_Count"
                )
            )

            ranking["Metric"] = (
                ranking[
                    "Startup_Count"
                ]
            )

            titulo_ranking = (
                "Número de Startups por Indústria"
            )

            eixo_x = "Startups"

            hover_template = (
                "<b>%{y}</b>"
                "<br>%{x:,.0f} startups"
                "<extra></extra>"
            )

        else:

            ranking = (
                df_filtrado
                .groupby("Industry")[
                    "Valuation_USD"
                ]
                .mean()
                .reset_index()
            )

            ranking["Metric"] = (
                ranking[
                    "Valuation_USD"
                ]
            )

            titulo_ranking = (
                "Valuation Médio por Indústria"
            )

            eixo_x = "Valuation Médio (USD)"

            hover_template = (
                "<b>%{y}</b>"
                "<br>US$ %{x:,.0f}"
                "<extra></extra>"
            )

        ranking = ranking.sort_values(
            "Metric",
            ascending=True,
        )

        values = (
            ranking["Metric"]
            .tolist()
        )

        if (
            len(values) > 1
            and max(values) != min(values)
        ):

            normalized = [

                (
                    v - min(values)
                )
                / (
                    max(values)
                    - min(values)
                )

                for v in values
            ]

        else:

            normalized = [
                0.65
            ] * len(values)

        colors = [

            BAR_PALETTE[
                min(
                    int(
                        n
                        * (
                            len(BAR_PALETTE)
                            - 1
                        )
                    ),
                    len(BAR_PALETTE)
                    - 1,
                )
            ]

            for n in normalized
        ]

        fig2 = create_ranking_chart(
            ranking,
        )

        apply_chart_theme(
            fig2,
            titulo_ranking,
            height=400,
            showlegend=False,
        )

        fig2.update_traces(

            marker=dict(
                color=colors,

                line=dict(
                    color="rgba(255,255,255,.08)",
                    width=1,
                ),
            ),

            opacity=0.96,

            hovertemplate=hover_template,
        )

        fig2.update_xaxes(
            title_text=eixo_x,
            tickformat="~s",
        )

        fig2.update_yaxes(

            showgrid=False,

            categoryorder="array",

            categoryarray=(
                ranking[
                    "Industry"
                ].tolist()
            ),
        )

        st.plotly_chart(
            fig2,
            use_container_width=True,
            config={
                "displayModeBar": False
            },
        )
# ==========================================================
# GRÁFICOS — LINHA 2
# ==========================================================
with st.container():

    st.markdown(
        '<h3 class="section-title">'
        'Evolução e Distribuição'
        '</h3>',
        unsafe_allow_html=True,
    )

    col3, col4 = st.columns(2)

    # ======================================================
    # LINHAS
    # ======================================================
    with col3:

        fig3 = create_industry_evolution_chart(
            df_filtrado,
            QUALITATIVE,
        )

        apply_chart_theme(
            fig3,
            "Evolução Temporal por Indústria",
            height=400,
            showlegend=True,
        )

        fig3.update_traces(
            line=dict(
                width=2
            ),

            marker=dict(
                size=4
            ),

            opacity=0.82,
        )

        fig3.update_xaxes(
            showgrid=False,
            title_text="",
        )

        fig3.update_yaxes(

            showgrid=True,
            gridcolor=GRID,
            title_text="Quantidade",
        )

        st.plotly_chart(
            fig3,
            use_container_width=True,
            config={
                "displayModeBar": False
            },
        )

    # ======================================================
    # BOX PLOT
    # ======================================================
    with col4:

        fig4 = create_valuation_boxplot(
            df_filtrado,
            QUALITATIVE,
        )

        apply_chart_theme(
            fig4,
            "Distribuição de Valuation por Setor",
            height=400,
            showlegend=False,
        )

        fig4.update_traces(

            line=dict(
                width=1.1
            ),

            marker=dict(
                size=2.5,
                opacity=0.35,
            ),
        )

        fig4.update_xaxes(
            showgrid=False,
            tickangle=-25,
        )

        fig4.update_yaxes(

            showgrid=True,
            gridcolor=GRID,
            tickformat="~s",
        )

        st.plotly_chart(
            fig4,
            use_container_width=True,
            config={
                "displayModeBar": False
            },
        )
# ==========================================================
# RODAPÉ
# ==========================================================
with st.container():

    st.markdown("---")

    st.markdown(
        f"""
        <p
            style='
                text-align:center;
                color:{TEXT_MUTED};
                font-size:13px;
            '
        >
            Dashboard desenvolvido para Atividade 2 -
            Pós em Engenharia de Dados
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <p
            style='
                text-align:center;
                color:{TEXT_SOFT};
                font-size:11px;
            '
        >
            Fonte: Startup Funding Analytics Dataset (Kaggle)
        </p>
        """,
        unsafe_allow_html=True,
    )