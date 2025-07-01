import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Carregar dados
# -----------------------------
df = pd.read_csv("digital_diet_mental_health.csv")

# Renomear colunas

column_translation = {
    "user_id": "id_usuario",
    "age": "idade",
    "gender": "genero",
    "daily_screen_time_hours": "horas_tela_diaria",
    "phone_usage_hours": "horas_celular",
    "laptop_usage_hours": "horas_laptop",
    "tablet_usage_hours": "horas_tablet",
    "tv_usage_hours": "horas_tv",
    "social_media_hours": "horas_redes_sociais",
    "work_related_hours": "horas_trabalho",
    "entertainment_hours": "horas_entretenimento",
    "gaming_hours": "horas_jogos",
    "sleep_duration_hours": "horas_sono",
    "sleep_quality": "qualidade_sono",
    "mood_rating": "nivel_humor",
    "stress_level": "nivel_estresse",
    "physical_activity_hours_per_week": "horas_atividade_fisica_semanal",
    "location_type": "tipo_localizacao",
    "mental_health_score": "pontuacao_saude_mental",
    "uses_wellness_apps": "usa_apps_bem_estar",
    "eats_healthy": "alimentacao_saudavel",
    "caffeine_intake_mg_per_day": "consumo_cafeina_mg_dia",
    "weekly_anxiety_score": "pontuacao_ansiedade_semanal",
    "weekly_depression_score": "pontuacao_depressao_semanal",
    "mindfulness_minutes_per_day": "minutos_mindfulness_dia"
}
df = df.rename(columns=column_translation)

# -----------------------------
# Sidebar: Navegação e Filtros
# -----------------------------
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", ["Visão Geral", "Saúde Mental e Hábitos"])

st.sidebar.header("Filtros Globais")
gender_filter = st.sidebar.multiselect(
    "Gênero",
    options=df["genero"].unique(),
    default=df["genero"].unique()
)

location_filter = st.sidebar.multiselect(
    "Localização",
    options=df["tipo_localizacao"].unique(),
    default=df["tipo_localizacao"].unique()
)

age_min = int(df["idade"].min())
age_max = int(df["idade"].max())

age_filter = st.sidebar.slider(
    "Idade",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max)
)

# Aplicar filtros
df_filtered = df[
    (df["genero"].isin(gender_filter)) &
    (df["tipo_localizacao"].isin(location_filter)) &
    (df["idade"] >= age_filter[0]) &
    (df["idade"] <= age_filter[1])
]

# -----------------------------
# Documentação e Explicação
# -----------------------------
st.title("Dashboard Hábitos Digitais & Saúde Mental")

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

    # Gráfico 1: Tempo de Tela x Ansiedade
    st.subheader("Tempo de Tela e Ansiedade")
    fig1 = px.scatter(
        df_filtered,
        x="horas_tela_diaria",
        y="pontuacao_ansiedade_semanal",
        color="genero",
        hover_data=["idade"],
        title="Tempo de Tela x Ansiedade"
    )
    st.plotly_chart(fig1)

    # Gráfico 2: Tempo de Tela x Qualidade do Sono
    st.subheader("Tempo de Tela e Qualidade do Sono")
    fig2 = px.scatter(
        df_filtered,
        x="horas_tela_diaria",
        y="qualidade_sono",
        color="genero",
        hover_data=["idade"],
        title="Tempo de Tela x Qualidade do Sono"
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
        x="minutos_mindfulness_dia",
        y="nivel_estresse",
        color="genero",
        hover_data=["idade"],
        title="Mindfulness x Stress"
    )
    st.plotly_chart(fig3)

    # Gráfico 4: Cafeína x Ansiedade
    st.subheader("Cafeína e Ansiedade")
    fig4 = px.scatter(
        df_filtered,
        x="consumo_cafeina_mg_dia",
        y="pontuacao_ansiedade_semanal",
        color="genero",
        hover_data=["idade"],
        title="Cafeína x Ansiedade"
    )
    st.plotly_chart(fig4)

    # Gráfico 5: Atividade Física x Depressão
    st.subheader("Atividade Física e Depressão")
    fig5 = px.scatter(
        df_filtered,
        x="horas_atividade_fisica_semanal",
        y="pontuacao_depressao_semanal",
        color="genero",
        hover_data=["idade"],
        title="Atividade Física x Depressão"
    )
    st.plotly_chart(fig5)

    # Gráfico 6: Duração do Sono x Humor
    st.subheader("Sono e Humor")
    fig6 = px.scatter(
        df_filtered,
        x="horas_sono",
        y="nivel_humor",
        color="genero",
        hover_data=["idade"],
        title="Duração do Sono x Humor"
    )
    st.plotly_chart(fig6)
