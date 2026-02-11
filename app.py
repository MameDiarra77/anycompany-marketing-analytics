import streamlit as st

# ===============================
# CONFIGURATION PAGE
# ===============================

st.set_page_config(
    page_title="AnyCompany Marketing Analytics",
    page_icon="",
    layout="wide"
)

# ===============================
# PAGE D'ACCUEIL
# ===============================

st.title(" AnyCompany Marketing Analytics Dashboard")
st.markdown("### Plateforme d’analyse Marketing & Business Intelligence")

st.markdown("---")

st.markdown("""
Bienvenue sur le dashboard analytique d’AnyCompany.

Ce projet comprend :

-  Marketing ROI Dashboard  
-  Promotion Analysis  
-  Customer Segmentation (KMeans)  
-  Sales Performance  

Utilisez le menu à gauche pour naviguer entre les différentes analyses.
""")

st.markdown("---")

# ===============================
# KPIs DESCRIPTION
# ===============================

st.subheader(" Objectifs du Projet")

st.markdown("""
Ce dashboard permet :

-  Suivi des performances marketing  
-  Analyse du retour sur investissement (ROI)  
-  Analyse des promotions  
-  Segmentation clients via Machine Learning  
-  Support à la prise de décision stratégique  
""")

st.markdown("---")

# ===============================
# INFORMATIONS TECHNIQUES
# ===============================

st.subheader(" Stack Technique")

st.markdown("""
- **Base de données :** Snowflake  
- **Transformation :** SQL (Bronze / Silver / Gold)  
- **Visualisation :** Streamlit  
- **Machine Learning :** Scikit-learn (KMeans)  
""")

st.markdown("---")

st.success("Projet prêt pour démonstration ")
