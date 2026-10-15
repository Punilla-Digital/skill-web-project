# Web Project

Habilidad completa de Punilla Digital para organizar y desarrollar proyectos web desde el brief hasta la publicación. Reemplaza la versión básica de este repositorio.

## Qué incluye

- Relevamiento comercial, alcance y criterios de aceptación.
- Investigación de mercado y referencias.
- Tres direcciones visuales comparables y registro de la elección.
- Arquitectura, contenido e inventario de fotos y videos.
- Implementación por etapas, feedback y documentación de decisiones.
- Revisión responsive, accesibilidad y SEO básico.
- Preparación de demos, revisión del cliente y publicación autorizada.
- Script para crear carpetas y documentación sin sobrescribir archivos.
- Icono y metadatos para agentes compatibles.

## Archivos

- [SKILL.md](SKILL.md): procedimiento completo.
- [references/project-structure.md](references/project-structure.md): estructura adaptable.
- [scripts/init_project.py](scripts/init_project.py): inicializador.
- [agents/openai.yaml](agents/openai.yaml): nombre, prompt e icono.
- [assets/icon.svg](assets/icon.svg): icono de la habilidad.

## Uso

En un agente compatible, copiar la carpeta completa con el nombre `web-project` a su directorio de habilidades. Conservar scripts, referencias e iconos junto a SKILL.md. Subir el repositorio a GitHub no instala automáticamente la habilidad en ChatGPT.

Ejemplo de pedido:

> Usá Web Project para organizar una web de un hotel. Investigá referencias, proponé tres estilos y registrá el proceso por etapas.

Inicializar un proyecto con Python 3:

```bash
python scripts/init_project.py /ruta/al/proyecto --name "Mi proyecto"
```

Ejecutar desde la carpeta de esta habilidad o usar la ruta completa del script. Se crean ocho documentos en docs/ y carpetas para investigación, recursos, tres propuestas, síntesis, revisiones y despliegue. El script conserva archivos existentes; no instala dependencias, inicia Git ni publica.

## Requisitos y alcance

El inicializador usa únicamente la biblioteca estándar de Python. La implementación del sitio requiere las herramientas del stack elegido. Investigación, capturas, informes PDF y QR necesitan herramientas equivalentes disponibles en el agente; no se incluyen habilidades de terceros.

El método toma como referencia una experiencia previa con PGB, pero no impone su sector, estética ni número de páginas. No incluye archivos privados ni recursos del cliente. Adaptar identidad, alcance y estructura a cada proyecto.

## Origen

Copia de la habilidad instalada en Complementos, publicada el 15/10/2026. Esta publicación no modifica la habilidad instalada.

[Punilla Digital](https://punilladigital.com.ar/) · [Licencia](LICENSE)
