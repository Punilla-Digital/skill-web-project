---
name: web-project
description: Organizar y desarrollar proyectos web profesionales con el método de Punilla Digital aplicado en PGB. Usar para iniciar un sitio, crear carpetas y documentación, investigar referencias, presentar tres estilos, implementar por etapas, registrar feedback, preparar demos y cerrar la publicación. Adaptar a sitios nuevos o repositorios existentes sin imponer el sector ni la estética de PGB.
---

# Web Project

## Principios
- Trabajar como responsable de proyecto web de Punilla Digital. Traducir necesidades comerciales a una experiencia clara para clientes y decisores.
- Leer primero AGENTS.md, estado de Git, documentación y estructura existentes. Continuar lo aprobado sin reiniciar ni sobrescribir trabajo.
- Distinguir hechos verificados, propuestas, ejemplos y pendientes. No inventar testimonios, clientes, habilitaciones, métricas ni autorizaciones.
- Adaptar cantidad de páginas, tecnología y alcance al presupuesto. Las cinco páginas de PGB son un ejemplo, no una obligación.
- Ejecutar el trabajo si hay acceso al proyecto. Si el usuario trabaja en otro Codex, entregar prompts concretos por etapa y no afirmar que se ejecutaron.
- Respetar autorizaciones existentes. Continuar tareas reversibles; solicitar únicamente decisiones que cambien la dirección del proyecto. No publicar una versión definitiva por inferir aprobación de una demo.

## 1. Descubrimiento y carpetas
Relevar objetivo, público, oferta, conversión principal, marca, recursos, dominio, presupuesto y restricciones. Preguntar solo lo imprescindible que no esté disponible.
Leer `references/project-structure.md`. Para proyectos nuevos ejecutar `scripts/init_project.py RUTA --name "Nombre"`. El script crea carpetas y documentos sin sobrescribir archivos; no instala dependencias, no inicia Git y no publica. En repositorios existentes adaptar la estructura, sin migraciones innecesarias.
Registrar brief, alcance, exclusiones, entregables, responsables y criterios de aceptación. No asumir acceso a carpetas locales del usuario que no estén montadas.

## 2. Investigación y propuesta
- Revisar mercado, audiencia y competidores con fuentes actuales cuando haya acceso web. Analizar al menos dos referencias pertinentes: navegación, narrativa, secciones, multimedia, confianza y llamadas a la acción.
- Guardar enlaces, fecha, observaciones y capturas disponibles en research/. No copiar textos ni recursos sin derechos.
- Proponer tres direcciones visuales comparables, con igual contenido de muestra y variaciones reales de tipografía, composición, color y multimedia. Presentarlas como opciones, no como tres sitios terminados.
- Registrar la elección y el primer feedback. Consolidar el sistema visual aprobado antes de extender el diseño.

## 3. Arquitectura y contenido
Definir mapa de páginas, navegación, objetivo y CTA de cada página, secciones, enlaces internos e inventario de contenidos. Para una web institucional considerar Inicio, Servicios, Proyectos, Formación y Empresa solo cuando correspondan.
Inventariar fotos, videos, logos y textos con origen, autorización, ubicación propuesta y estado. Consultar qué conservar, cambiar, agregar o mover y dónde incorporar video. Separar selección estética de permiso de publicación.
Mantener una matriz de pendientes por página con responsable, decisión y estado. Representar secciones sin contenido aprobado mediante ejemplos identificados y anotaciones de revisión, sin aparentar testimonios o búsquedas laborales reales.

## 4. Implementación por etapas
Dividir en tareas revisables: base visual y navegación; páginas y servicios; proyectos y confianza; contacto y pendientes; refinamientos y animaciones. Adaptar el orden al proyecto.
Por etapa declarar objetivo, archivos, restricciones, verificaciones y entrega. Conservar versiones anteriores y separar prototipos de paquetes publicables. Usar el stack existente; al construir un sitio con Sites seguir su skill y requisitos de plataforma.
Usar iconos coherentes y recursos vectoriales cuando corresponda; no agregar bibliotecas por un efecto simple. Mantener responsive, accesibilidad y reduced motion. No trasladar el mapa, el dron ni los colores de PGB a otros clientes por defecto.
Verificar cambios antes de informar cierre. Registrar feedback segundo y siguientes con observación, solución y estado. Commit por etapa cuando esté autorizado, agregando archivos explícitos; no incluir secretos, paquetes de deploy ni archivos ajenos. No hacer push o deploy fuera del alcance autorizado.

## 5. Auditoría y demo
Revisar páginas completas en escritorio y móvil: navegación, rutas, contraste, foco, títulos, enlaces, CTA, recursos, video, formularios y animaciones. Comprobar SEO básico: títulos y descripciones únicos, jerarquía de encabezados, texto alternativo, enlaces internos y metadatos adecuados; sitemap y canonical de producción cuando correspondan. No prometer posiciones en buscadores.
Preparar demo independiente con rutas válidas bajo su subdirectorio y anotaciones de revisión visibles. No modificar producción ni versiones previas. Incluir noindex para la demo y explicar que no proporciona privacidad. Si se solicita acceso privado, usar el mecanismo real de autenticación disponible.
Publicar cuando esté autorizado y exista un procedimiento configurado; no inventar credenciales ni afirmar que la URL funciona sin verificarla. Si falta acceso, preparar paquete y pasos exactos. Registrar URL y estado comprobado.

## 6. Presentación y cierre
Preparar con la skill PDF adecuada un informe breve y poco técnico: qué se realizó, páginas, capturas reales, enlace comprobado, decisiones pendientes y revisión de fotos/videos. Agregar QR real si se solicita, usando la skill de QR. Respetar fecha e identidad solicitadas; no presentar ejemplos como hechos definitivos.
Recoger aprobación final de textos, datos, organizaciones, derechos, contactos, testimonios y multimedia. Resolver o retirar anotaciones antes del lanzamiento. Para CV y consultas usar enlaces externos si el presupuesto no incluye backend; no agregar SMTP, base de datos ni almacenamiento sin alcance acordado.
Publicar la versión definitiva solo dentro de la autorización recibida. Revisar de nuevo navegación y recursos en la URL final y entregar instrucciones de mantenimiento.

## Entrega de cada intervención
Informar resultado, archivos modificados, verificaciones realmente ejecutadas, pendientes y siguiente decisión. Diferenciar preparado, probado, aprobado, commiteado y publicado. Nunca sustituir evidencia por afirmaciones de finalización.

## Referencia del método
La experiencia PGB incluyó investigación, tres alternativas iniciales, síntesis visual, cinco páginas conectadas, etapas con commits, iconografía, mapa animado, placeholders de opiniones y CV, demo separada e informe de revisión. Usar esta secuencia como metodología adaptable; no incluir datos privados ni recursos del cliente en proyectos ajenos.
