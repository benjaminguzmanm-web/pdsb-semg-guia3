# Calendario, dependencias y seguimiento

## Horizonte solicitado y carácter reconstruido

Benjamin Guzman Miranda indicó como periodo de trabajo el **22 de octubre al 3 de noviembre de 2026**. Ese es el horizonte del Gantt. La guía oficial fija la entrega para el **4 de noviembre de 2026**, como fecha externa al periodo representado.

La distribución de actividades dentro del horizonte es una **reconstrucción de planificación propuesta**, no una bitácora diaria verificada ni evidencia de que cada tarea se ejecutó exactamente en las fechas asignadas. Los estados y porcentajes describen la evidencia actual al 3 de noviembre. Una tarea pendiente puede conservar una fecha planificada dentro de ese intervalo, señalando trabajo por cerrar y sin afirmar ejecución histórica.

La unidad de duración es el día calendario, contando inicio y fin. No representa horas de esfuerzo ni días exclusivos. Las tareas se solapan cuando son compatibles y el orden dentro de una misma fecha no está documentado. No se asignan fechas a clases o hitos posteriores, porque ese calendario no está confirmado.

## Dependencias y prioridad

T02 confirma procedencia para EDA T03. El control de calidad condiciona tanto T04 como T05, que pueden avanzar en paralelo. T07 requiere ambas ramas. La factibilidad T06 puede elaborarse mientras se revisa el análisis. T08 usa resultados validados. La grabación T09 debe demostrar la versión final. T10 incluye publicación y reproducción; T11 verifica todos los productos antes de la entrega institucional.

La cadena con mayor riesgo de bloquear el cierre es **T02, T03, T04/T05, T07, T08, T10, T11**. El vídeo T09 es otra condición necesaria de T11. Esta es una ruta crítica potencial identificada cualitativamente: no se ha calculado CPM ni holgura numérica porque no hay estimaciones de esfuerzo ni disponibilidad diaria verificadas.

T06 tiene margen relativo mientras finaliza T07 siempre que no retrase T08. Las figuras adicionales y la ampliación a otros participantes son actividades posponibles. La contingencia temporal es reducir esas ampliaciones y concentrar el cierre en los requisitos de esta guía.

## Porcentajes y evidencia

Los porcentajes describen cierre de criterios verificables, no tiempo transcurrido ni comprensión personal. Se marca 100 % cuando el producto y su criterio documental o computacional están comprobados, aunque su revisión y comprensión por el autor se mantengan como tarea separada. Una tarea pendiente de evidencia real permanece en 0 %.

T01 y T06 disponen de ficha, BOM, factibilidad y planificación completas. T02 conserva el cotejo completo y metadatos. T03-T05 cuentan con las tablas corregidas, banderas y comparación temporal. T07 está verificada en `evidencias/ejecucion_notebooks.json`: dos notebooks ejecutados secuencialmente con kernels Jupyter nuevos y cero errores.

El resultado actual contiene 1.280 ventanas de dos segundos: 1.277 aceptadas por la máscara de calidad y tres marcadas en CH1. La tabla del protocolo nominal tiene 200 filas y todas pasan esa máscara. La prueba temporal convierte 2.000 a 1.000 Hz con FIR de 161 coeficientes, ventana Kaiser beta=8,6 y corte de 450 Hz. No se utiliza la reducción anterior a 500 Hz para el resultado final.

T08 tiene informe y presentación revisados visualmente; el Gantt está exportado desde su CSV actualizado. H06 permanece incompleto mientras no exista vídeo auténtico, aun cuando los PDFs estén terminados.

El repositorio público ya fue creado. T10 está al 50 %: hay repositorio e historial local verificables, pero faltan la carga y el clon remoto. GitHub rechaza la escritura de la conexión (403). El clon local limpio se verificó; no se presenta como clon remoto. Vídeo y entrega siguen pendientes. T09 y T11 no cambian por la mera existencia de archivos locales. Benjamin debe revisar y comprender los resultados antes de presentarlos, sin que esa revisión personal se confunda con el estado de los archivos.

## Rutina de revisión

1. Abrir el criterio del hito y comprobar el archivo o ejecución asociado.
2. Registrar versión y evidencia disponible.
3. Actualizar estado, porcentaje y ruta en Gantt e hitos.
4. Verificar que cada dependencia apunta a un ID existente.
5. Actualizar la exportación PNG o PDF desde el CSV final.
6. Revisar enlaces y productos antes de publicar y de entregar.

La continuación del proyecto se planificará cuando el docente confirme las clases y el siguiente alcance. No se presentan fechas futuras ni compromisos no informados.
