from snowflake.connector import connect

print("🔄 Test de connexion avec le bon account...")

try:
    conn = connect(
        account="IQB68372.us-west-2",
        user="MAMEDIARRA144",
        password="AissatouNgom1994@",
        warehouse="ANYCOMPANY_WH",
        database="ANYCOMPANY_LAB",
        schema="SILVER"
    )
    
    print("✅ CONNEXION RÉUSSIE !")
    
    cursor = conn.cursor()
    
    # Test 1 : Vérifier la connexion
    cursor.execute("SELECT CURRENT_ACCOUNT(), CURRENT_DATABASE(), CURRENT_SCHEMA()")
    result = cursor.fetchone()
    print(f"📊 Account: {result[0]}")
    print(f"📊 Database: {result[1]}")
    print(f"📊 Schema: {result[2]}")
    
    # Test 2 : Vérifier les tables
    cursor.execute("SHOW TABLES IN SCHEMA SILVER")
    tables = cursor.fetchall()
    print(f"\n✅ {len(tables)} tables trouvées dans SILVER")
    
    # Test 3 : Compter les données
    cursor.execute("SELECT COUNT(*) FROM CUSTOMER_DEMOGRAPHICS_CLEAN")
    count = cursor.fetchone()[0]
    print(f"✅ CUSTOMER_DEMOGRAPHICS_CLEAN : {count} lignes")
    
    cursor.close()
    conn.close()
    
    print("\n🎉 Tout fonctionne parfaitement !")
    
except Exception as e:
    print(f"❌ Erreur : {e}")