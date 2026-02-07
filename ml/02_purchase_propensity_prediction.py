# Prédiction de Propension d'Achat
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report
import warnings
warnings.filterwarnings('ignore')

print("="*60)
print("PRÉDICTION DE PROPENSION D'ACHAT")
print("="*60)

# 1. Charger les données
print("\n1. Chargement des données...")
df = pd.read_csv('ml/customer_ml_data.csv')
print(f"✅ {df.shape[0]} clients chargés")

# 2. Créer une variable cible (exemple)
# IMPORTANT: Remplacez par votre vraie colonne cible !
if 'total_transactions' in df.columns:
    df['will_purchase'] = (df['total_transactions'] > 0).astype(int)
else:
    # Cible synthétique pour démo
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df['purchase_score'] = df[numeric_cols].fillna(0).mean(axis=1)
    df['will_purchase'] = (df['purchase_score'] > df['purchase_score'].median()).astype(int)
    df.drop('purchase_score', axis=1, inplace=True)

print(f"\n2. Variable cible créée")
print(df['will_purchase'].value_counts())

# 3. Préparer les features
target = 'will_purchase'
X = df.drop([target], axis=1)

# Retirer IDs
for col in ['customer_id', 'CUSTOMER_ID', 'id', 'ID']:
    if col in X.columns:
        X = X.drop(col, axis=1)

# Seulement numériques
numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
X = X[numeric_features].fillna(X[numeric_features].median())
y = df[target]

print(f"\n3. {len(numeric_features)} features préparées")

# 4. Split Train/Test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\n4. Train: {len(X_train)}, Test: {len(X_test)}")

# 5. Standardiser
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. Entraîner Random Forest
print("\n5. Entraînement Random Forest...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train_scaled, y_train)
print("✅ Modèle entraîné !")

# 7. Évaluer
y_proba = model.predict_proba(X_test_scaled)[:, 1]
y_pred = model.predict(X_test_scaled)

print("\n6. Performance du modèle :")
print(classification_report(y_test, y_pred, target_names=['Non-acheteur', 'Acheteur']))
print(f"ROC-AUC Score: {roc_auc_score(y_test, y_proba):.4f}")

# 8. Scorer tous les clients
X_all_scaled = scaler.transform(X)
df['propensity_score'] = model.predict_proba(X_all_scaled)[:, 1]
df['propensity_segment'] = pd.cut(
    df['propensity_score'],
    bins=[0, 0.3, 0.7, 1.0],
    labels=['Faible', 'Moyenne', 'Forte']
)

print("\n7. Distribution propension :")
print(df['propensity_segment'].value_counts())

# 9. Sauvegarder
df[['propensity_score', 'propensity_segment']].to_csv(
    'customers_propensity_scores.csv', index=False
)
print("\n✅ Scores sauvegardés : customers_propensity_scores.csv")

# 10. Top features
feature_importance = pd.DataFrame({
    'Feature': numeric_features,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

print("\n8. Top 10 Features :")
print(feature_importance.head(10).to_string(index=False))

print("\n"+"="*60)
print("✅ PRÉDICTION TERMINÉE !")
print("="*60)