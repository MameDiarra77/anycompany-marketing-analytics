import streamlit as st
import pandas as pd
import snowflake.connector

st.title("Marketing ROI Dashboard")
st.write("Analyse globale des performances financières marketing")

# Connexion Snowflake
try:
    conn = snowflake.connector.connect(
        account=st.secrets["snowflake"]["account"],
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        role=st.secrets["snowflake"]["role"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"],
    )
    st.success(" Connexion Snowflake réussie")
except Exception as e:
    st.error(f" Connexion Snowflake échouée : {e}")
    st.stop()

# Requête SQL
query = """
SELECT 
    SUM(CASE WHEN TRANSACTION_TYPE = 'Revenue' THEN AMOUNT ELSE 0 END) AS TOTAL_REVENUE,
    SUM(CASE WHEN TRANSACTION_TYPE = 'Expense' THEN AMOUNT ELSE 0 END) AS TOTAL_COST
FROM ANYCOMPANY_LAB.SILVER.FINANCIAL_TRANSACTIONS_CLEAN
"""

try:
    df = pd.read_sql(query, conn)
except Exception as e:
    st.error(f" Erreur SQL : {e}")
    st.stop()

# Récupération des valeurs
revenue = df["TOTAL_REVENUE"][0]
cost = df["TOTAL_COST"][0]

# Calcul ROI sécurisé
if cost and cost != 0:
    roi = ((revenue - cost) / cost) * 100
else:
    roi = 0

# KPIs
st.subheader("KPIs Globaux")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Revenu total", f"{revenue:,.0f} €")

with col2:
    st.metric("Coût total", f"{cost:,.0f} €")

with col3:
    st.metric("ROI Global", f"{roi:.1f}%")

# Fermeture connexion
conn.close()
