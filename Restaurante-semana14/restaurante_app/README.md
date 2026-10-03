# Restaurante App

**Autora:** Mariuxi Jessenia Tejada Mayorga

**Trabajo:** Semana 14

## Descripción

Restaurante App es una aplicación de escritorio desarrollada en Python y Tkinter para administrar un catálogo de productos y consultar los usuarios registrados. Esta versión amplía el trabajo de la Semana 13 con componentes y contenedores para organizar mejor la interfaz.

La aplicación conserva una separación clara entre datos, modelos, servicios, vistas y punto de entrada. En la sección de productos se pueden registrar, consultar, actualizar y eliminar registros, manteniendo los cambios en `productos.json`.

## Estructura

```text
restaurante_app/
├── .gitignore
├── main.py
├── README.md
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
└── ui/
	├── __init__.py
	├── login_view.py
	└── main_view.py
```

## Funcionamiento por componentes

- **Modelos:** representan la información de los productos y las cuentas de usuario.
- **Servicios:** gestionan la carga, persistencia y operaciones del catálogo, además de comprobar las credenciales.
- **Interfaz:** contiene el login y un panel principal organizado con `Frame`, `LabelFrame`, `Entry`, `Treeview`, `Scrollbar` y botones `ttk`.
- **Inicio:** `main.py` prepara la ventana, carga la información y enlaza los componentes.

## Archivos de datos

La información utilizada por el programa se encuentra en la carpeta `datos/`:

- `productos.json`: catálogo disponible.
- `usuarios.json`: usuarios habilitados para ingresar.

## Operaciones de productos

En la sección **Productos** se utiliza un formulario para capturar el ID, nombre, precio, categoría y stock. Las acciones disponibles son:

- **Registrar:** crea un producto nuevo.
- **Cargar / Consultar:** busca un producto mediante su ID y muestra sus datos en el formulario.
- **Actualizar:** reemplaza la información del producto seleccionado por su ID.
- **Eliminar:** retira el producto del catálogo.

Todas las acciones son solicitadas a `RestauranteServicio`. La interfaz no lee ni modifica directamente los archivos JSON; después de cada operación actualiza la tabla visible.

Las ventas no están implementadas; solo se muestran como una opción pendiente en la interfaz y no cuentan con modelo ni archivo de almacenamiento.

## Cómo iniciar la aplicación

Abre una terminal en la carpeta principal del proyecto y ejecuta:

```bash
python main.py
```

## Credenciales de demostración

```text
Usuario: admin
Contraseña: restaurante123
```

## Verificación de sintaxis

Para revisar que los archivos Python sean válidos, utiliza:

```bash
python -m compileall -q main.py modelos servicios ui
```

## Comprobación de la Semana 14

1. Ejecutar `python main.py` e ingresar con `admin` y `restaurante123`.
2. Abrir **Usuarios** para consultar la información registrada.
3. Abrir **Productos** y probar el registro, consulta, actualización y eliminación usando el formulario.
4. Cerrar y volver a ejecutar la aplicación para comprobar que los cambios permanecen en `datos/productos.json`.