# Auditoría de la versión anterior

Revisión del archivo `PDSB_Guia3_paquete_revision.zip` de Descargas. Las copias con sufijos `(1)` a `(5)` son idénticas por SHA-256: `3aedd2ec32b81b759342060f1318e75d1b78842e4439b184746381989f4dd093`.

## Resultados comprobados

- El CSV contiene 1.280.000 filas y cuatro columnas. Las medias, mínimos, máximos y desviaciones estándar informados coinciden con el cálculo independiente desde el CSV.
- El Canal 1 contiene 5.393 muestras exactamente iguales al máximo, `9,99969482421875`, y 5.398 muestras mayores o iguales a `9,999`.
- La mayor meseta constante del Canal 1 comprende los índices de base cero `[1.066.769, 1.072.000)`: 5.231 muestras. Si la frecuencia es 2.000 Hz, corresponde a `[533,3845; 536)` segundos y dura 2,6155 s.
- La ventana de 534 a 536 s del Canal 1 es completamente constante. Al restarle su media, RMS y MAV son cero, y las frecuencias mediana y media son indefinidas. El CSV anterior contiene una frecuencia mediana y una frecuencia media vacías por esta razón.
- Los notebooks anteriores guardan ejecuciones completas y no contienen salidas de error. Esto no sustituye una nueva ejecución en el entorno de entrega.

## Correcciones necesarias o recomendadas

| Aspecto | Problema observado | Corrección |
|---|---|---|
| Calidad por ventanas | La meseta constante produce RMS cero y puede parecer reposo si se pierde su contexto. | Añadir banderas de calidad, fracción de muestras en el máximo y duración de mesetas; informar resúmenes con y sin ventanas afectadas. No inferir reposo muscular a partir de esa ventana. |
| Frecuencias indefinidas | Las frecuencias de una ventana sin potencia son `NaN`; el resumen por canal las omite automáticamente. | Conservar los `NaN`, explicar su causa y reportar el número de ventanas válidas y excluidas. |
| Fuente y unidades | Frecuencia de 2.000 Hz y unidades mV heredadas del notebook de Guía 2. | Cotejar el archivo exacto con los datos originales y documentar sujeto, ensayo, canal, muestreo y unidades. Hasta entonces, identificar esas magnitudes como provisionales. |
| Afirmaciones de Guía 2 | El notebook de referencia afirma causas de hardware, clipping confirmado y nombres anatómicos sin evidencia suficiente en el CSV. | Archivarlo explícitamente como antecedente y no reutilizar esas conclusiones; distinguir observaciones numéricas de causas propuestas. |
| Rutas | `ROOT=Path("..")` depende de iniciar cada notebook desde su carpeta. | Detectar la raíz por la existencia de `datos/senal_emg.csv` o indicar y verificar el directorio de ejecución. |
| Carpetas de salida | `01_eda.ipynb` guarda figuras sin crear previamente la carpeta `figuras`. | Crear `figuras` y `evidencias` al inicio, con `parents=True, exist_ok=True`. |
| Decimación | Reducir de 2.000 a 500 Hz impone un límite de Nyquist de 250 Hz; la comparación anterior usa solo número de muestras, duración y desviación estándar. | Explicar qué banda elimina el antialiasing y comparar PSD, potencia por banda y características antes/después. No tratar el cambio de desviación estándar como prueba de eliminación exclusiva de ruido. |
| Validación espectral | Una sinusoide de 50 Hz comprueba un caso controlado mediante Welch. | Identificarla como prueba sintética, declarar resolución espectral y mantener separados sus resultados de las inferencias sobre sEMG real. |
| Visualización global | La figura usa una de cada varias muestras para reducir puntos. | Etiquetar esa reducción como recurso de visualización; para investigar picos o mesetas, usar datos completos, zoom o envolventes mínimo/máximo. |
| Cronograma | El Gantt anterior contiene fechas anteriores a la revisión actual. | Distinguir actividades efectivamente realizadas de tareas planificadas; no presentar fechas pasadas como evidencia de ejecución. |

La presencia de una meseta exacta al máximo es evidencia de un problema de calidad que requiere investigación. Su causa física debe determinarse con el rango y protocolo del equipo, sin asignarla exclusivamente al ADC a partir del CSV.
