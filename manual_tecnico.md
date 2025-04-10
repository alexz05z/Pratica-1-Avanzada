# Manual Técnico del Proyecto
## IES Abdera de Adra (Almería)
### CFGS Desarrollo de Aplicaciones Web (DAW)
#### Curso 2024-2025

---

## 1. Información General
- **Nombre del Proyecto:** Tienda Online
- **Autores:** Alejandro Rodriguez Sanchez
- **Fecha de creación:** Abril 2025  
- **Última actualización:** Abril 2025  
- **Profesor Responsable:** Jose Ramón Rivas Cano

---

## 2. Descripción del Proyecto

Este proyecto implementa un sistema básico de gestión de productos físicos y digitales, clientes, pedidos y reseñas, utilizando programación en Python con orientación a objetos. Permite realizar operaciones CRUD básicas, trabajar con productos digitales y físicos, asociar productos a pedidos, gestionar clientes y permitir reseñas de productos por parte de clientes.

El objetivo es reforzar conocimientos en:
- Programación orientada a objetos
- Manejo de estructuras de datos en Python
- Interacción entre diferentes entidades del sistema (modelo relacional básico)

---

## 3. Tecnologías Utilizadas
- **Frontend:** No aplicable (proyecto en consola)  
- **Backend:** Python (programación orientada a objetos)  
- **Base de Datos:** Simulada en memoria (listas y diccionarios)  
- **Control de Versiones:** Git y GitHub  
- **Despliegue:** Ejecutable local mediante intérprete de Python  

---

## 4. Requisitos Previos
- Python 3.10 o superior  
- Git instalado  
- Editor de código (Visual Studio Code recomendado)  
- Repositorio clonado desde GitHub  

---

## 5. Estructura del Proyecto
```plaintext
📂 tienda_online
 ├── producto.py
 ├── producto_digital.py
 ├── cliente.py
 ├── pedido.py
 ├── resena.py
 ├── main.py
 ├── manual_tecnico.md
 ├── manual_usuario.md
 ├── casodeuso_tiendaonline.png
 ├──diagramadeclase_tiendaonline.png
 ├── .gitignore

```

## 6. Instalación y Configuración
- Desde Git:
git clone https://github.com/alexz05z/Pratica-1-Avanzada
cd tienda_online
python main.py

- Desde Github:
Descargar el code de la página principal

---

## 7. Base de Datos
No tiene, simula con listas y diccionarios.

---

## 8. API y Endpoints
No tiene

---
## 9. Seguridad

Actualmente:
- Validación básica de entradas por consola.
- Comprobación de duplicados por ID para evitar conflictos.

—

## 10. Configuración del Servidor Web

Este proyecto se ejecuta de forma local.

—


## 11. Pruebas y Debugging

### Herramientas utilizadas:
- Salidas por consola (`print`) para verificar el flujo del programa.
- Menú interactivo con opciones para cada entidad.
- Pruebas manuales de inserción, modificación y visualización de datos.

### Casos de prueba realizados:
- Añadir productos (físicos y digitales) con validación de ID duplicado.
- Listar productos.
- Modificar stock de productos.
- Crear y listar clientes con verificación de duplicados.
- Crear pedidos y añadir productos a los pedidos.
- Calcular el total de un pedido.
- Crear reseñas y listarlas.

---

## 12. Uso de Inteligencia Artificial

En este proyecto no se ha utilizado la inteligencia artificial.

---

## 13. Despliegue en Producción

Este proyecto puede ser desplegado en un entorno virtual.

---

## 14. Conclusión

Este proyecto ha servido como base para aplicar conocimientos fundamentales de programación orientada a objetos, modularidad y diseño de sistemas básicos de gestión.

### Evaluación del desarrollo:
- Se ha estructurado el código en módulos bien definidos.
- La lógica de negocio se gestiona adecuadamente a través de clases como `Producto`, `Cliente`, `Pedido` y `Reseña`.
- La interacción por consola permite al usuario realizar operaciones CRUD de forma intuitiva.

---

## 15. Créditos y Referencias

- **IES Abdera** – Apuntes y recursos del módulo de Programación del CFGS DAW.  
- **Python.org** – [https://docs.python.org/es/3/](https://docs.python.org/es/3/)   
- **GitHub** – Plataforma utilizada para versionado y control del proyecto.  

---
Copyright (c) [2025] [alexz]

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y los archivos de documentación asociados (el "Software"), para tratar el
Software sin restricción, incluyendo sin limitación los derechos a usar, copiar, modificar,
fusionar, publicar, distribuir, sublicenciar y/o vender copias del Software, y a permitir a las
personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright y esta nota de permiso deberán incluirse en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES POR NINGUNA RECLAMACIÓN, DAÑO U OTRA RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, QUE SURJA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.
