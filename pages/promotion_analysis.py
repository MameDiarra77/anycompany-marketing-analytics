import streamlit as st
import pandas as pd
import snowflake.connector

st.title(" Promotion Analysis Dashboard")
st.markdown("Analyse des performances des promotions")

# =============================
# CONNEXION SNOWFLAKE
# =============================

try:
    conn = snowflake.connector.connect(
        account="IQB68372.us-west-2",
        user="MAMEDIARRA144",
        password="AissatouNgom1994@",
        warehouse="ANYCOMPANY_WH",
        database="ANYCOMPANY_LAB",
        schema="SILVER"
    )
    st.success(" Connexion Snowflake réussie")

except Exception as e:
    st.error(f" Connexion échouée : {e}")
    st.stop()

# =============================
# REQUÊTE SQL
# =============================

query = """
SELECT *
FROM ANYCOMPANY_LAB.SILVER.PROMOTIONS_CLEAN
"""

try:
    df = pd.read_sql(query, conn)
    st.success(" Données chargées avec succès")

except Exception as e:
    st.error(f" Erreur SQL : {e}")
    st.stop()

# =============================
# NETTOYAGE COLONNES
# =============================

df.columns = df.columns.str.upper()

st.write("Colonnes disponibles :", df.columns.tolist())

# =============================
# KPI
# =============================

st.subheader(" KPIs Promotions")

col1, col2, col3 = st.columns(3)

if "REVENUE" in df.columns:
    col1.metric("Total Revenue", f"{df['REVENUE'].sum():,.0f}")

if "DISCOUNT_PERCENT" in df.columns:
    col2.metric("Average Discount (%)", round(df["DISCOUNT_PERCENT"].mean(), 2))

if "CONVERSION_RATE" in df.columns:
    col3.metric("Average Conversion Rate", round(df["CONVERSION_RATE"].mean(), 3))

# =============================
# TABLEAU
# =============================

st.subheader(" Détail des promotions")
st.dataframe(df)

# =============================
# VISUALISATION
# =============================

if "DISCOUNT_PERCENT" in df.columns and "REVENUE" in df.columns:
    st.subheader(" Revenue vs Discount")
    st.scatter_chart(df, x="DISCOUNT_PERCENT", y="REVENUE")
