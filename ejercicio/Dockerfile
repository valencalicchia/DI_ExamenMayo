FROM mysql:8.0.33

# Configuración básica
ENV LANG C.UTF-8
ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_DATABASE EXAMEN2DI

# Copiar script de inicialización
COPY init.sql /docker-entrypoint-initdb.d/

# Establecer permisos
RUN chmod 644 /docker-entrypoint-initdb.d/init.sql

# Configuración MySQL directa en variables de entorno
ENV MYSQL_CHARACTER_SET_SERVER=utf8mb4
ENV MYSQL_COLLATION_SERVER=utf8mb4_spanish2_ci
ENV MYSQL_DEFAULT_AUTHENTICATION_PLUGIN=mysql_native_password
ENV MYSQL_MAX_ALLOWED_PACKET=64M
ENV MYSQL_SKIP_LOG_BIN=1