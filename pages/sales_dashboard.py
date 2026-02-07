"""
AnyCompany Food & Beverage - Sales Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from snowflake.snowpark import Session

st.set_page_config(page_title="AnyCompany - Sales", page_icon="", layout="wide")

@st.cache_resource
def create_snowflake_session():
    try:
        return Session.builder.configs({
            "account": st.secrets["snowflake"]["account"],
            "user": st.secrets["snowflake"]["user"],
            "password": st.secrets["snowflake"]["password"],
            "role": st.secrets["snowflake"]["role"],
            "warehouse": st.secrets["snowflake"]["warehouse"],
            "database": st.secrets["snowflake"]["database"],
            "schema": st.secrets["snowflake"]["schema"]
        }).create()
    except Exception as e:
        st.error(f"Erreur connexion : {str(e)}")
        return None

@st.cache_data(ttl=600)
def load_sales_data(_session):
    if _session is None:
        return None
    try:
        query = """
        SELECT 
            transaction_year,
            transaction_quarter,
            region,
            COUNT(*) as nb_transactions,
            SUM(amount) as total_revenue
        FROM SILVER.FINANCIAL_TRANSACTIONS_CLEAN
        WHERE transaction_type = 'Sale'
        GROUP BY transaction_year, transaction_quarter, region
        """
        return _session.sql(query).to_pandas()
    except Exception as e:
        st.error(f"Erreur chargement : {str(e)}")
        return None

st.title(" AnyCompany - Sales Dashboard")
st.markdown("---")

session = create_snowflake_session()
if session is None:
    st.error(" Connexion Snowflake échouée")
    st.info("""
    Vérifiez .streamlit/secrets.toml :
    - account doit être au format: DSB06387.us-west-2
    - Vérifiez user, password, role
    """)
    st.stop()

st.success(" Connecté à Snowflake")

df = load_sales_data(session)
if df is None or df.empty:
    st.warning(" Aucune donnée disponible")
    st.stop()

df['TOTAL_REVENUE'] = pd.to_numeric(df['TOTAL_REVENUE'])
df['NB_TRANSACTIONS'] = pd.to_numeric(df['NB_TRANSACTIONS'])

st.header(" Métriques Clés")
col1, col2, col3 = st.columns(3)

with col1:
    total_revenue = df['TOTAL_REVENUE'].sum()
    st.metric("CA Total", f"${total_revenue:,.0f}")

with col2:
    total_transactions = df['NB_TRANSACTIONS'].sum()
    st.metric("Transactions", f"{total_transactions:,.0f}")

with col3:
    nb_regions = len(df['REGION'].unique())
    st.metric("Régions", nb_regions)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader(" CA par Année")
    yearly = df.groupby('TRANSACTION_YEAR')['TOTAL_REVENUE'].sum().reset_index()
    fig = px.bar(yearly, x='TRANSACTION_YEAR', y='TOTAL_REVENUE', 
                 color='TOTAL_REVENUE', color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader(" CA par Région")
    regional = df.groupby('REGION')['TOTAL_REVENUE'].sum().reset_index()
    fig = px.pie(regional, values='TOTAL_REVENUE', names='REGION')
    st.plotly_chart(fig, use_container_width=True)

with st.expander(" Données détaillées"):
    st.dataframe(df)
    