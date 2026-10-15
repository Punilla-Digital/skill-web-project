# Estructura sugerida

Adaptar a lo que ya exista. Mantener nombres estables y rutas relativas.

- docs/brief.md: objetivo, audiencia, propuesta, CTA y restricciones.
- docs/scope.md: páginas, entregables, exclusiones y aceptación.
- docs/decisions.md: fecha, decisión, fundamento y aprobación.
- docs/feedback.md: ronda, página, observación, acción y estado.
- docs/pending.md: página, contenido, responsable y decisión pendiente.
- docs/content-inventory.md: recurso, origen, derechos, selección, ubicación y estado.
- docs/roadmap.md: etapas, tareas, validación, estado y commit real.
- docs/release.md: origen, destino, procedimiento, URL y comprobaciones.
- research/references/: análisis y enlaces de referentes.
- research/screenshots/: capturas reales identificadas.
- assets/source/: originales conservados sin edición destructiva.
- assets/approved/: materiales aprobados para el sitio.
- prototypes/option-01/, option-02/, option-03/: muestras visuales comparables.
- prototypes/synthesis/: implementación de la dirección seleccionada.
- reviews/: capturas e informes de revisión.
- deploy/: copia publicable por versión; excluir de Git si es un resultado generado y el mecanismo existente lo permite.

En frameworks utilizar src/, public/ y build según su convención; evitar duplicar el código fuente dentro de esta estructura. No modificar .gitignore existente automáticamente. Nunca guardar contraseñas en estos documentos.
