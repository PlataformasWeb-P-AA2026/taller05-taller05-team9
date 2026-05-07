
---

# Proyecto de Integración de Datos: Sistema de Estadísticas Mundial 2026

Este repositorio contiene la implementación de un sistema de gestión y visualización de datos para el Mundial 2026. El proyecto integra procesos de extracción, transformación y carga (ETL) sobre fuentes de datos heterogéneas y una interfaz web dinámica conectada a una base de datos NoSQL.

## Estructura del Proyecto

*   **/formato-json:** Scripts de Python para la unificación de datos (CSV, HTML, PDF) y carga masiva a la base de datos.
*   **/frontend:** Aplicación web desarrollada con Vite, JavaScript (ES6+) y DataTables.

---

## Requisitos Previos

Para la correcta ejecución del sistema, el entorno debe contar con:
1.  **CouchDB:** Instancia activa en el puerto `5985`.
2.  **Python 3.x:** Para la ejecución de los scripts de backend.
3.  **Node.js:** Versión 22 

---

## Instrucciones de Configuración y Ejecución

### 1. Preparación de la Base de Datos (ETL)
El primer paso consiste en unificar las fuentes de datos y enviarlas a CouchDB.

```bash
cd formato-json
# Unificación de archivos CSV, HTML y PDF en un único formato JSON estructurado
python3 unificar.py

# Carga de los documentos unificados a la base de datos 'jugadores'
python3 cargar.py
cd ..
```

### 2. Configuración de CouchDB y CORS
Para permitir la comunicación entre el servidor de desarrollo y la base de datos, es necesario habilitar CORS. Ejecute los siguientes comandos en su terminal o habilitarlos en el propio fauxton:

```bash
curl -X PUT http://admin:admin@localhost:5985/_node/couchdb@localhost/_config/httpd/enable_cors -d '"true"'
curl -X PUT http://admin:admin@localhost:5985/_node/couchdb@localhost/_config/cors/origins -d '"*"'
curl -X PUT http://admin:admin@localhost:5985/_node/couchdb@localhost/_config/cors/methods -d '"GET, POST, PUT, DELETE, OPTIONS"'
```

#### Definición de Vistas (MapReduce)
En la interfaz de administración (Fauxton), dentro del Design Document `_design/losjugadores`, se deben definir las siguientes vistas para el correcto funcionamiento de los filtros:

*   **por_club:** `function (doc) { if(doc.club_actual) emit(doc.club_actual, doc); }`
*   **por_goles:** `function (doc) { if(doc.goles !== undefined) emit(doc.goles, doc); }`
*   **por_partidos:** `function (doc) { if(doc.partidos !== undefined) emit(doc.partidos, doc); }`

### 3. Ejecución del Frontend
Acceda a la carpeta del frontend para instalar las dependencias e iniciar el servidor:

```bash
cd frontend
# Limpieza de dependencias previas
rm -rf node_modules package-lock.json
# Instalación de paquetes necesarios (Vite, DataTables)
npm install
# Ejecución del servidor de desarrollo
npm run dev
```

La aplicación será accesible a través de la dirección local: `http://localhost:5173`.

---

## Detalles de Implementación

*   **Estilo Visual:** Se han implementado los colores institucionales (Azul Marino y Amarillo Ocre) mediante variables CSS para mantener la identidad visual en la interfaz.
*   **Consumo de API:** El frontend realiza peticiones asíncronas (`fetch`) a los endpoints de las vistas de CouchDB, procesando la respuesta JSON para su renderizado dinámico.
*   **Componentes de Tabla:** Se utiliza DataTables para proporcionar funcionalidades de paginación, ordenamiento y búsqueda global sobre los registros obtenidos del servidor.

---

## Imagenes del correcto funcionamiento de la pagina, con las diferentes vistas funcionando



