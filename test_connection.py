from snowflake.connector import connect

print("=" * 60)
print("TEST DE CONNEXION SNOWFLAKE")
print("=" * 60)

# Configurations à tester
configs = [
    "DSB06387",
    "DSB06387.us-west-2",
    "dsb06387",
    "dsb06387.us-west-2"
]

user = "MAMEDIARRA144"
password = "AissatouNgom1994@"

for account in configs:
    print(f"\n🔄 Test: {account}")
    
    try:
        conn = connect(
            account=account,
            user=user,
            password=password
        )
        
        print(f"   ✅ CONNEXION RÉUSSIE !")
        
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_ACCOUNT(), CURRENT_USER()")
        result = cursor.fetchone()
        
        print(f"   Account: {result[0]}")
        print(f"   User: {result[1]}")
        
        cursor.close()
        conn.close()
        
        print(f"\n🎉 FORMAT CORRECT: {account}")
        break
        
    except Exception as e:
        if "Incorrect username or password" in str(e):
            print(f"   ❌ Identifiants incorrects")
        else:
            print(f"   ❌ {str(e)[:60]}")

print("\n" + "=" * 60)