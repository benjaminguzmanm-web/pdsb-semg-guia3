# Riesgos y respuestas

Responsable de todos los riesgos: Benjamin Guzman Miranda. Revisión al 3 de noviembre de 2026. Probabilidad e impacto son estimaciones cualitativas para priorizar acciones, no mediciones estadísticas.

| ID | Riesgo | Probabilidad | Impacto | Señal temprana | Respuesta principal | Alternativa ejecutable | Evidencia de cierre |
|---|---|---|---|---|---|---|---|
| Q1 | Interpretar tramo plano como reposo | Alta si no se marca | Alto | RMS/MAV=0 en 534-536 s al centrar | Marcar CH1 en [533,3845; 536) s y ventanas afectadas | Comparar ventanas válidas y conservar la anomalía por separado | Tabla de anomalías y banderas de características |
| Q2 | Atribuir músculo o gesto sin trazabilidad | Media | Alto | Etiquetas anatómicas sin respaldo o ventanas arbitrarias llamadas gestos | Usar CH1-CH4 y contrastar intervalos con guion oficial | Reportar solo ventanas temporales si falta sincronización fiable | Ficha y tabla de segmentación |
| Q3 | Rutas o dependencias impiden reproducir | Media | Alto | El flujo depende de carpeta particular o kernel distinto | Rutas relativas, creación de directorios y versiones registradas | Ejecutar el mismo flujo desde terminal con datos locales autorizados | Ejecución de versión actual y prueba limpia |
| Q4 | Datos agotan memoria o almacenamiento | Media | Medio | Fallo de lectura o espacio escaso | Extraer solo el registro seleccionado | Lectura por bloques y archivo fuente preservado externamente | Ejecución completa e integridad del registro |
| Q5 | GitHub o autenticación demoran cierre | Media | Alto | Cuenta/repositorio no configurados o errores de subida | Configurar repositorio con margen y verificar acceso | Preparar copia local íntegra mientras se resuelve conexión | URL, historial y clon limpio |
| Q6 | Falta vídeo auténtico o ejecución legible | Media | Alto | Solo hay guion o diapositivas | Grabar 3-5 minutos con ejecución real, Gantt, BOM, EDA, PSD y tabla | Ensayar un segmento corto y repetir si no es legible | Vídeo/enlace probado desde README |
| Q7 | Extrapolar sEMG a fuerza o desempeño de prótesis | Media | Alto | RMS interpretado en newtons o validación táctil | Limitar afirmaciones a amplitud y distribución espectral | Separar ensayo futuro de fuerza/contacto con calibración | Alcance explícito en informe y presentación |
| Q8 | Falta tiempo para cerrar entrega | Alta por proximidad al plazo | Alto | Documentos antes de validar código o pendientes sin evidencia | Priorizar T07-T11 y detener ampliaciones fuera de pauta | Reducir figuras adicionales preservando requisitos | Lista final con evidencias reales |
| Q9 | Confundir cronograma reconstruido con bitácora | Media | Medio | Fechas por tarea presentadas como observadas | Declarar origen del horizonte y carácter reconstruido | Sustituir fechas por bitácora real si el estudiante la aporta | Nota metodológica junto a Gantt |
| Q10 | Datos sin atribución o metadatos innecesarios | Baja si se documenta | Alto | Falta DOI o se incluyen encuestas no usadas | Atribuir CC BY 4.0 y declarar cambios; incluir solo lo necesario | Publicar recuperación autorizada y resultados permitidos | Ficha, cita y revisión de repositorio |

Cada riesgo se cierra al revisar su evidencia. La meseta es compatible con recorte y justifica una decisión de calidad, pero no identifica por sí sola una causa electrónica concreta.
