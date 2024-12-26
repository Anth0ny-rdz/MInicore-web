# MInicore-web

# Gestión de Gastos - Proyecto Django

Este proyecto es una aplicación web creada con **Django** para gestionar empleados, departamentos y sus gastos asociados. La funcionalidad principal permite filtrar y calcular los gastos en un rango de fechas específico.

## Funcionalidades

- Gestión de empleados y departamentos.
- Registro de gastos asociados a empleados.
- Filtrado de gastos en un rango de fechas.
- Cálculo del total de gastos en el rango filtrado.
- Interfaz de administración para gestionar datos.

## Requisitos

- **Python** 3.8 o superior.
- **Django** 4.0 o superior.
- Entorno virtual configurado (opcional pero recomendado).

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd gestion_gastos
2. Crear y activar un entorno virtual

Copy code
python -m venv venv
venv\Scripts\activate     ndows
3. Instalar dependencias
bash
Copy code
pip install django
4. Migrar la base de datos

Copy code
python manage.py makemigrations
python manage.py migrate
5. Crear un superusuario
bash
Copy code
python manage.py createsuperuser
6. Ejecutar el servidor de desarrollo
bash
Copy code
python manage.py runserver
Accede a la aplicación en tu navegador en http://127.0.0.1:8000/.


