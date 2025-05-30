import psycopg2

# Configuración de la conexión a Neon PostgreSQL
config = {
    'dbname': 'neon',      # Cambia por el nombre de tu base de datos
    'user': 'Biblioteca_owner',            # Cambia por tu usuario de Neon
    'password': 'npg_6c8nezqiMwCL',     # Cambia por tu contraseña de Neon
    'host': 'ep-tuendpoint.us-east-2.aws.neon.tech',  # Cambia por tu endpoint de Neon
    'port': 5432                     # Puerto estándar de PostgreSQL
}

def ejecutor_sql(codigo_sql):
    connection = None
    try:
        connection = psycopg2.connect('postgresql://Biblioteca_owner:npg_6c8nezqiMwCL@ep-frosty-cherry-a8f9w9k6-pooler.eastus2.azure.neon.tech/Biblioteca?sslmode=require')
        cursor = connection.cursor()
        cursor.execute(codigo_sql)
        connection.commit()
        print("✅ Ejecución correcta de SQL")
    except psycopg2.Error as e:
        print(f"❌ Error de PostgreSQL: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("🔗 Conexión cerrada")

def get_connection():
    """Establece una conexión a la base de datos PostgreSQL."""
    try:
        connection = psycopg2.connect('postgresql://Biblioteca_owner:npg_6c8nezqiMwCL@ep-frosty-cherry-a8f9w9k6-pooler.eastus2.azure.neon.tech/Biblioteca?sslmode=require')
        print("🔗 Conexión exitosa a la base de datos")
        return connection
    except psycopg2.Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        connection.close()
        print("🔗 Conexión cerrada")
        return None

    
    