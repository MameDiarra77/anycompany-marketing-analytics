import streamlit as st
import snowflake.connector
import pandas as pd

# =====================
# CONFIG PAGE
# =====================
st.set_page_config(
    page_title="AnyCompany - Sales Dashboard",
    layout="wide"
)

st.title(" App")

# =====================
# CONNEXION SNOWFLAKE
# =====================
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
    st.error(" Connexion Snowflake échouée")
    st.stop()

# =====================
# REQUÊTE EXEMPLE
# =====================
query = """
SELECT *
FROM ANYCOMPANY_LAB.ANALYTICS.SALES_ENRICHED
LIMIT 100
"""


df = pd.read_sql(query, conn)

# =====================
# AFFICHAGE
# =====================
st.subheader(" Aperçu des ventes")
st.dataframe(df)

