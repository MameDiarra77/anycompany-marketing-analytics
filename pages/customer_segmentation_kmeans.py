import streamlit as st
import pandas as pd
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import plotly.express as px

# ==============================
# CONFIG PAGE
# ==============================
st.set_page_config(
    page_title="Customer Segmentation – KMeans",
    layout="wide"
)

st.title(" Customer Segmentation – KMeans")
st.markdown("Segmentation clients basée sur AGE et ANNUAL_INCOME")

# ==============================
# PATH DU FICHIER
# ==============================
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "ml" / "customers_segmented.csv"

# ==============================
# VERIFICATION FICHIER
# ==============================
if not DATA_PATH.exists():
    st.error(" Fichier customers_segmented.csv introuvable dans le dossier ml/")
    st.stop()

df = pd.read_csv(DATA_PATH)
st.success(" Fichier chargé avec succès")

# Nettoyage colonnes
df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_")

st.write("Colonnes détectées :", df.columns.tolist())

# ==============================
# VERIFICATION COLONNES
# ==============================
required_cols = ["AGE", "ANNUAL_INCOME"]

if not all(col in df.columns for col in required_cols):
    st.error(" Colonnes requises manquantes")
    st.stop()

# ==============================
# PREPARATION DONNEES
# ==============================
X = df[required_cols]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==============================
# CHOIX DU NOMBRE DE CLUSTERS
# ==============================
k = st.slider("Nombre de clusters", 2, 8, 4)

kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

df["KMEANS_CLUSTER"] = clusters

# ==============================
# METRIQUE SILHOUETTE
# ==============================
score = silhouette_score(X_scaled, clusters)
st.metric("Silhouette Score", round(score, 3))

# ==============================
# DISTRIBUTION DES CLUSTERS
# ==============================
st.subheader(" Distribution des clusters")
cluster_counts = df["KMEANS_CLUSTER"].value_counts().sort_index()
st.bar_chart(cluster_counts)

# ==============================
# PROFILS MOYENS
# ==============================
st.subheader(" Profils moyens par cluster")

profiles = (
    df.groupby("KMEANS_CLUSTER")[required_cols]
    .mean()
    .round(1)
)

st.dataframe(profiles)

# ==============================
# VISUALISATION
# ==============================
st.subheader(" Visualisation des clusters")

fig = px.scatter(
    df,
    x="ANNUAL_INCOME",
    y="AGE",
    color="KMEANS_CLUSTER",
    title="Segmentation Clients KMeans",
    width=800,
    height=600
)

st.plotly_chart(fig)

st.success(" Segmentation terminée avec succès")
