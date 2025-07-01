import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Carregar dados
# -----------------------------
df = pd.read_csv("digital_diet_mental_health.csv")

# -----------------------------
# Sidebar: Navegação e Filtros
# -----------------------------
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", ["Visão Geral", "Saúde Mental e Hábitos"])

st.sidebar.header("Filtros Globais")
gender_filter = st.sidebar.multiselect(
    "Gênero",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

location_filter = st.sidebar.multiselect(
    "Localização",
    options=df["location_type"].unique(),
    default=df["location_type"].unique()
)

age_min = int(df["age"].min())
age_max = int(df["age"].max())

age_filter = st.sidebar.slider(
    "Idade",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max)
)

# Aplicar filtros
df_filtered = df[
    (df["gender"].isin(gender_filter)) &
    (df["location_type"].isin(location_filter)) &
    (df["age"] >= age_filter[0]) &
    (df["age"] <= age_filter[1])
]

# -----------------------------
# Documentação e Explicação
# -----------------------------
st.title("Dashboard Digital Diet & Saúde Mental")

st.markdown("""
**Objetivo:**  
Explorar como hábitos digitais e estilo de vida impactam indicadores de saúde mental.

**Como navegar:**  
Escolha a página e aplique filtros na barra lateral.

**Como os filtros funcionam:**  
Todos os gráficos respeitam os filtros aplicados (gênero, localização e idade).
""")

# -----------------------------
# Página: Visão Geral
# -----------------------------
if page == "Visão Geral":
    st.header("Visão Geral dos Dados")

    st.write("Exemplo dos dados filtrados:")
    st.dataframe(df_filtered.head())

    # Gráfico 1: Screen time x Depressão
    st.subheader("Tempo de Tela e Depressão")
    fig1 = px.scatter(
        df_filtered,
        x="daily_screen_time_hours",
        y="weekly_depression_score",
        color="gender",
        hover_data=["age"],
        title="Screen Time x Depressão"
    )
    st.plotly_chart(fig1)

    # Gráfico 2: Screen time x Qualidade do Sono
    st.subheader("Tempo de Tela e Qualidade do Sono")
    fig2 = px.scatter(
        df_filtered,
        x="daily_screen_time_hours",
        y="sleep_quality",
        color="gender",
        hover_data=["age"],
        title="Screen Time x Sleep Quality"
    )
    st.plotly_chart(fig2)

# -----------------------------
# Página: Saúde Mental e Hábitos
# -----------------------------
elif page == "Saúde Mental e Hábitos":
    st.header("Saúde Mental e Hábitos de Vida")

    # Gráfico 3: Mindfulness x Stress
    st.subheader("Mindfulness e Nível de Stress")
    fig3 = px.scatter(
        df_filtered,
        x="mindfulness_minutes_per_day",
        y="stress_level",
        color="gender",
        hover_data=["age"],
        title="Mindfulness x Stress"
    )
    st.plotly_chart(fig3)

    # Gráfico 4: Cafeína x Ansiedade
    st.subheader("Cafeína e Ansiedade")
    fig4 = px.scatter(
        df_filtered,
        x="caffeine_intake_mg_per_day",
        y="weekly_anxiety_score",
        color="gender",
        hover_data=["age"],
        title="Cafeína x Ansiedade"
    )
    st.plotly_chart(fig4)

    # Gráfico 5: Atividade Física x Depressão
    st.subheader("Atividade Física e Depressão")
    fig5 = px.scatter(
        df_filtered,
        x="physical_activity_hours_per_week",
        y="weekly_depression_score",
        color="gender",
        hover_data=["age"],
        title="Atividade Física x Depressão"
    )
    st.plotly_chart(fig5)

    # Gráfico 6: Duração do Sono x Humor
    st.subheader("Sono e Humor")
    fig6 = px.scatter(
        df_filtered,
        x="sleep_duration_hours",
        y="mood_rating",
        color="gender",
        hover_data=["age"],
        title="Duração do Sono x Humor"
    )
    st.plotly_chart(fig6)
