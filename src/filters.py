import streamlit as st


def render_filters(df):
    with st.sidebar:
        st.image(
            "assets/Logo.png",
            use_container_width=True,
        )

        st.markdown("---")
        st.header("Filtros")

        paises_disponiveis = sorted(
            df["Country"].dropna().unique().tolist()
        )

        pais_selecionado = st.selectbox(
            "País",
            ["Todos"] + paises_disponiveis,
        )

        industrias_disponiveis = sorted(
            df["Industry"].dropna().unique().tolist()
        )

        industria_selecionada = st.multiselect(
            "Indústria",
            industrias_disponiveis,
            default=industrias_disponiveis,
        )

        ano_min = int(df["Year"].min())
        ano_max = int(df["Year"].max())

        if ano_min < ano_max:
            ano_inicial, ano_final = st.slider(
                "Período",
                min_value=ano_min,
                max_value=ano_max,
                value=(ano_min, ano_max),
                step=1,
            )
        else:
            ano_inicial = ano_min
            ano_final = ano_max

            st.caption(
                f"Período disponível: {ano_min}"
            )

        metrica_ranking = st.selectbox(
            "Métrica do ranking",
            [
                "Investimento",
                "Número de Startups",
                "Valuation Médio",
            ],
        )

    return (
        pais_selecionado,
        industria_selecionada,
        ano_inicial,
        ano_final,
        metrica_ranking,
    )

def apply_filters(
    df,
    pais_selecionado,
    industria_selecionada,
    ano_inicial,
    ano_final,
):
    df_filtrado = df.copy()

    if pais_selecionado != "Todos":
        df_filtrado = df_filtrado[
            df_filtrado["Country"] == pais_selecionado
        ]

    if industria_selecionada:
        df_filtrado = df_filtrado[
            df_filtrado["Industry"].isin(industria_selecionada)
        ]
    else:
        df_filtrado = df_filtrado.iloc[0:0]

    df_filtrado = df_filtrado[
        df_filtrado["Year"].between(
            ano_inicial,
            ano_final,
        )
    ].copy()

    return df_filtrado