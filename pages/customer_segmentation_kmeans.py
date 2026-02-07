import streamlit as st
import pandas as pd
from pathlib import Path

# =========================
# CONFIG APP
# =========================
st.set_page_config(
    page_title="Segmentation Clients",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================
st.sidebar.title(" Menu")
page = st.sidebar.radio(
    "Navigation",
    ["Accueil", "Customer Segmentation – KMeans"]
)

# =========================
# PATHS
# =========================
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "ml" / "customers_segmented.csv"

# =========================
# PAGE : ACCUEIL
# =========================
if page == "Accueil":
    st.title("Dashboard – Segmentation Clients")

    st.markdown("""
    ###  Objectif
    Segmenter les clients avec **KMeans** afin d’identifier
    des profils clients exploitables pour le marketing.

    ###  Pipeline
    - Préparation des données
    - Segmentation KMeans
    - Analyse des clusters
    """)

    st.info(" Utilisez le menu à gauche pour accéder à la segmentation")

# =========================
# PAGE : KMEANS
# =========================
elif page == "Customer Segmentation – KMeans":
    st.title(" Customer Segmentation – KMeans")

    # Vérification fichier
    if not DATA_PATH.exists():
        st.error(" Fichier customers_segmented.csv introuvable")
        st.stop()

    # Chargement données
    df = pd.read_csv(DATA_PATH)

    # Normalisation des noms de colonnes
    df.columns = df.columns.str.lower()

    # Détection automatique du cluster
    cluster_col = [c for c in df.columns if "cluster" in c]
    if not cluster_col:
        st.error(" Colonne cluster introuvable")
        st.stop()
    cluster_col = cluster_col[0]

    # Aperçu
    st.subheader(" Aperçu des données")
    st.dataframe(df.head())

    # Colonnes numériques
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if cluster_col in numeric_cols:
        numeric_cols.remove(cluster_col)

    # Profils moyens
    profiles = (
        df.groupby(cluster_col)[numeric_cols]
          .mean()
          .round(1)
    )

    st.subheader(" Profils moyens par cluster")
    st.dataframe(profiles)

    # Distribution
    st.subheader(" Distribution des clusters")
    st.bar_chart(df[cluster_col].value_counts().sort_index())
