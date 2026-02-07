import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Marketing ROI")

# Base du projet
BASE_DIR = Path(__file__).resolve().parents[1]

#  UTILISE UN FICHIER QUI EXISTE
DATA_PATH = BASE_DIR / "ml" / "customers_segmented.csv"

# Vérification
if not DATA_PATH.exists():
    st.error("Fichier customers_segmented.csv introuvable")
    st.stop()

# Chargement
df = pd.read_csv(DATA_PATH)
df.columns = df.columns.str.lower()

st.subheader(" Aperçu des données")
st.dataframe(df.head())

# Détection automatique du cluster
cluster_col = [c for c in df.columns if "cluster" in c]
if not cluster_col:
    st.error(" Colonne cluster introuvable")
    st.stop()

cluster_col = cluster_col[0]

# Exemple simple de KPI ROI par cluster
st.subheader(" Répartition des clients par cluster")
st.bar_chart(df[cluster_col].value_counts().sort_index())
