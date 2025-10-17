import pymysql
import time
import sys
import os

# Pega variáveis de ambiente
host = os.getenv("DB_HOST", "db")
user = os.getenv("DB_USER", "work")
password = os.getenv("DB_PASSWORD", "work")
database = os.getenv("DB_NAME", "workout")

print("⏳ Aguardando MySQL ficar pronto...")

while True:
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3306,
            connect_timeout=2
        )
        print("✅ MySQL está pronto!")
        conn.close()
        break
    except pymysql.MySQLError as e:
        print(f"⏳ Ainda aguardando MySQL... ({e})")
        time.sleep(3)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        time.sleep(3)
