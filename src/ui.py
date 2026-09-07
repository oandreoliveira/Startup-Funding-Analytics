import streamlit as st


# ==========================================================
# TEMA DOS GRÁFICOS
# ==========================================================
def apply_chart_theme(
    fig,
    title,
    height=400,
    showlegend=True,
):
    fig.update_layout(
        height=height,

        margin=dict(
            l=18,
            r=18,
            t=62,
            b=18,
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family='Inter, "Segoe UI", Arial, sans-serif',
            color="#A8B3C7",
            size=12,
        ),

        title=dict(
            text=title,
            x=0.03,
            xanchor="left",
            y=0.95,
            font=dict(
                color="#F8FAFC",
                size=16,
                family='Inter, "Segoe UI", Arial, sans-serif'
            ),
        ),

        hoverlabel=dict(
            bgcolor="#172236",
            bordercolor="rgba(148,163,184,.22)",
            font=dict(
                color="#F8FAFC",
                size=12,
            ),
        ),

        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            borderwidth=0,
            font=dict(
                color="#A8B3C7",
                size=11,
            ),
            title_font=dict(
                color="#A8B3C7",
                size=11,
            ),
        ),

        showlegend=showlegend,
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(148, 163, 184, 0.10)",
        zeroline=False,
        linecolor="rgba(148,163,184,.12)",

        tickfont=dict(
            color="#A8B3C7",
        ),

        title_font=dict(
            color="#A8B3C7",
        ),

        automargin=True,
    )

    fig.update_yaxes(
        showgrid=False,
        zeroline=False,
        linecolor="rgba(148,163,184,.12)",

        tickfont=dict(
            color="#A8B3C7",
        ),

        title_font=dict(
            color="#A8B3C7",
        ),

        automargin=True,
    )

    return fig


# ==========================================================
# KPI CARD
# ==========================================================
def metric_card(
    value,
    label,
    sub,
    accent,
    card_bg,
):
    st.markdown(
        f"""
        <div class="metric-card" style="--accent:{accent}; --card-bg:{card_bg};">
            <div class="metric-accent"></div>
            <div class="card-value">{value}</div>
            <div class="card-label">{label}</div>
            <div class="card-sub">{sub}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )