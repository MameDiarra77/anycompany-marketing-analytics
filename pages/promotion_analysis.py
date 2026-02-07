import streamlit as st
import pandas as pd
from pathlib import Path

# =====================
# CONFIG
# =====================
st.title(" Dashboard des Avis / Propension à l’achat")

BASE_PATH = Path(__file__).resolve().parents[1]

# =====================
# CHARGEMENT DES DONNÉES
# =====================
df_propensity = pd.read_csv(
    BASE_PATH / "customers_propensity_scores.csv"
)

# Normalisation
df_propensity.columns = df_propensity.columns.str.lower()

# =====================
# CONTENU DASHBOARD
# =====================
if len(df_propensity) > 0:

    st.subheader(" Distribution du score de propension")
    st.bar_chart(df_propensity["propensity_score"])

    high_prop = (df_propensity["propensity_score"] > 0.7).mean() * 100
    st.metric(" Clients à forte propension (> 0.7)", f"{high_prop:.1f}%")

    st.subheader(" Répartition par segment")
    segment_counts = df_propensity["propensity_segment"].value_counts()
    st.bar_chart(segment_counts)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Score moyen", f"{df_propensity['propensity_score'].mean():.2f}")
    with col2:
        st.metric("Score minimum", f"{df_propensity['propensity_score'].min():.2f}")
    with col3:
        st.metric("Score maximum", f"{df_propensity['propensity_score'].max():.2f}")

    st.subheader(" Aperçu des données")
    st.dataframe(df_propensity.head(20), use_container_width=True)

else:
    st.error(" Aucune donnée disponible")
