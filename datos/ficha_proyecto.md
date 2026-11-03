# Ficha revisada del proyecto

**Autor y único integrante:** Benjamin Guzman Miranda.

**Nombre provisional:** Caracterización temporal y espectral de sEMG para un futuro sistema de control mioeléctrico de prótesis.

**Periodo de trabajo indicado por el autor:** 22 de octubre al 3 de noviembre de 2026. Las fechas por tarea del Gantt son una reconstrucción de planificación, no una bitácora observada. La entrega oficial de la Guía 3 es el 4 de noviembre de 2026.

## Problema y objetivo general

Antes de utilizar una señal muscular como entrada de un sistema mecatrónico se necesita conocer su procedencia, calidad y comportamiento temporal/espectral. Una característica numérica puede resultar engañosa si el registro presenta anomalías o si se le asigna un significado que los metadatos no respaldan.

El objetivo general es caracterizar un registro sEMG real mediante un flujo reproducible de control de calidad, análisis temporal y extracción de características, delimitando su posible utilidad como entrada de un futuro controlador mioeléctrico.

| ID | Objetivo específico observable | Evidencia prevista | Tareas |
|---|---|---|---|
| OE1 | Verificar fuente, modalidad y metadatos y justificar su relación con el proyecto. | Ficha y cotejo del archivo original. | T01, T02 |
| OE2 | Describir estructura y calidad, registrar anomalías y evaluar una operación temporal con comparación explícita. | EDA, tabla de calidad, banderas y comparación antes/después. | T03, T04 |
| OE3 | Calcular e interpretar al menos dos características por ventana real, incluyendo una espectral, y comprobar el código con una señal sintética separada. | Tabla, PSD/FFT, parámetros y prueba sintética. | T05 |
| OE4 | Planificar recursos y comunicar un flujo reproducible con límites claros. | Gantt, BOM, factibilidad, ejecución, informe, presentación y repositorio. | T06-T11 |

## Señal y variables

Se utiliza `1_raw.csv`, participante 1 de Mendeley Data v2, coincidente exactamente con `senal_emg.csv`. El MAT confirma 1.280.000 muestras por canal, cuatro canales, 2.000 Hz y mV. La duración nominal es 640 s. Se conserva el original y se derivan versiones de trabajo. El tiempo se construye desde el índice y la frecuencia documentada y no representa timestamps independientes.

La variable medida es voltaje diferencial superficial asociado a actividad muscular, con posibles contribuciones de ruido y artefactos. Se estudian amplitud y distribución espectral por ventana. RMS o MAV no equivalen directamente a fuerza. Los canales se mantienen neutrales cuando el archivo no aporta un mapa anatómico verificable.

## Propuesta y productos

El flujo conserva muestras, verifica calidad, marca intervalos problemáticos, compara una transformación temporal y resume ventanas mediante atributos temporales y espectrales. La segmentación sigue el guion del conjunto cuando se comprueba la sincronización. Los productos locales incluyen dos notebooks corregidos ejecutados con kernels Jupyter nuevos y cero errores, tablas y figuras, ficha de datos, planificación, informe y presentación. Se obtuvieron 1.280 ventanas globales, de las cuales 1.277 pasan la máscara de calidad y tres de CH1 están marcadas. Las 200 filas del protocolo nominal pasan la máscara. Publicación GitHub, clon remoto y demostración auténtica siguen pendientes.

## Proximidad al futuro prototipo

La sEMG aproxima la modalidad de entrada de un controlador mioeléctrico, pero las condiciones de un usuario real, sus electrodos y protocolo exigirán validación posterior. Un solo participante no acredita generalización. No se implementa un clasificador ni se prueba una prótesis física en esta guía.

La matriz tactosensible de la tesis es un subsistema de contacto y posible presión/fuerza. Complementaría la realimentación de una prótesis, mientras que la sEMG se relaciona con actividad/intención motora. Esta guía estudia procesamiento sEMG y no valida el sensor táctil, su calibración ni su capacidad de medir fuerza.

## Supuestos y restricciones

La fuente declara muestreo uniforme y el MAT confirma `fs=2000`; el CSV no contiene timestamps independientes para reconstruir posibles pérdidas. El tramo plano de CH1 en [533,3845; 536) s debe marcarse y no interpretarse como reposo fisiológico. Las etiquetas de gesto se apoyan en el protocolo temporal, sin asegurar que cada participante ejecutara cada instrucción exactamente como se esperaba.

El estudiante informó que aún no había hecho trabajo en GitHub. Su publicación, historial, clon limpio y vídeo auténtico deben completarse y comprobarse. La continuidad del proyecto se ajustará a la siguiente pauta y al calendario docente confirmado, sin fechas futuras inventadas.
