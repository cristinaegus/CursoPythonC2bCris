import psycopg2
# Crear conexión y cursor para ejecutar las sentencias de creación de tablas
connection = None
try:
    connection = psycopg2.connect('postgresql://Biblioteca_owner:npg_6c8nezqiMwCL@ep-frosty-cherry-a8f9w9k6-pooler.eastus2.azure.neon.tech/Biblioteca?sslmode=require')
    cursor = connection.cursor()

    # 1. Tabla de usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario SERIAL PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL
    );
    """)

    # 2. Tabla de materiales
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materiales (
        codigo_inventario VARCHAR(20) PRIMARY KEY,
        titulo VARCHAR(100) NOT NULL,
        tipo VARCHAR(10) NOT NULL CHECK (tipo IN ('libro', 'revista', 'dvd')),
        ubicacion VARCHAR(100),
        disponible BOOLEAN NOT NULL DEFAULT TRUE
    );
    """)

    # 3. Tabla de libros
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        codigo_inventario VARCHAR(20) PRIMARY KEY REFERENCES materiales(codigo_inventario) ON DELETE CASCADE,
        autor VARCHAR(100) NOT NULL,
        isbn VARCHAR(20),
        numero_paginas INT
    );
    """)

    # 4. Tabla de revistas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS revistas (
        codigo_inventario VARCHAR(20) PRIMARY KEY REFERENCES materiales(codigo_inventario) ON DELETE CASCADE,
        fecha_publicacion DATE,
        numero_edicion INT
    );
    """)

    # 5. Tabla de dvds
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dvds (
        codigo_inventario VARCHAR(20) PRIMARY KEY REFERENCES materiales(codigo_inventario) ON DELETE CASCADE,
        duracion INT,
        director VARCHAR(100)
    );
    """)

    # 6. Tabla de préstamos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prestamos (
        id_prestamo VARCHAR(8) PRIMARY KEY,
        id_usuario VARCHAR(8) REFERENCES usuarios(id_usuario) ON DELETE CASCADE,
        codigo_inventario VARCHAR(20) REFERENCES materiales(codigo_inventario) ON DELETE CASCADE,
        fecha_prestamo TIMESTAMP NOT NULL,
        fecha_devolucion TIMESTAMP NOT NULL
    );
    """)

    connection.commit()
    print("✅ Tablas creadas correctamente")
except psycopg2.Error as e:
    print(f"❌ Error al crear tablas: {e}")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("🔗 Conexión cerrada tras crear tablas")

