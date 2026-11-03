# Guion para demostración auténtica de la Guía 3

**Autor:** Benjamin Guzman Miranda  
**Duración prevista:** 4 minutos, ajustable entre 3 y 5 minutos.  
**Estado:** guion preparado. El video todavía debe grabarse a partir de una ejecución real.
**Repositorio público creado:** https://github.com/benjaminguzmanm-web/pdsb-semg-guia3. Falta completar la publicación de archivos y comprobar el clon remoto. El repositorio existe pero todavía está vacío. La ejecución desde un clon local sí está verificada.

## Preparación

1. Abrir la carpeta del proyecto y el README. Mantener visibles solamente archivos académicos y datos públicos autorizados.
2. Abrir el Gantt exportado y `planificacion/materiales.csv`.
3. Abrir `notebooks/01_eda.ipynb` y `notebooks/02_caracteristicas.ipynb` con el intérprete del entorno del proyecto.
4. Reiniciar el kernel y ejecutar las celdas en orden durante la grabación. Si la ejecución tarda, explicar la espera o recortar únicamente el tiempo de espera, conservando la secuencia y declarando ese recorte.
5. Preparar la figura EDA, la comparación temporal, la PSD y la tabla de características producidas por esa misma ejecución.

## 0:00 a 0:30 - Problema y alcance

Mostrar la portada y el README.

> Soy Benjamin Guzman Miranda. Este proyecto caracteriza señales de electromiografía de superficie como una base para estudiar futuras entradas de control mioeléctrico de una prótesis. La señal mide variaciones eléctricas registradas en el antebrazo. La matriz tactosensible de mi tesis corresponde a otro subsistema, relacionado con el contacto. En esta guía analizo datos públicos y no pruebo todavía una prótesis ni un sensor táctil.

## 0:30 a 1:00 - Planificación y recursos

Mostrar el Gantt y la lista de materiales.

> El periodo de trabajo considerado es del 22 de octubre al 3 de noviembre de 2026. El cronograma reúne revisión de datos, control de calidad, características y documentación. La entrega oficial corresponde al 4 de noviembre. Para esta etapa dispongo del computador y de los registros públicos. El análisis usa Python y bibliotecas científicas. No requiere comprar un sistema de adquisición ni realizar mediciones con participantes. Las fechas específicas de las tareas del cronograma son una reconstrucción de la planificación y el avance se comprueba con archivos.

## 1:00 a 1:40 - Ejecución y procedencia

Reiniciar y ejecutar las celdas de carga y comprobación del notebook.

> El archivo de trabajo coincide muestra por muestra con el registro `1_raw.csv` de la versión 2 del conjunto de Mendeley. Los metadatos del archivo MATLAB confirman el participante 1, cuatro canales, unidades en milivoltios y una frecuencia de muestreo de dos mil hertz. La matriz contiene un millón doscientas ochenta mil muestras por canal. Su duración es de seiscientos cuarenta segundos. El original se conserva y las transformaciones se realizan sobre copias.

## 1:40 a 2:20 - Calidad y decisión

Mostrar la figura global y el tramo constante del canal 1.

> El control de calidad revisa valores ausentes, valores no finitos, estadísticos y tramos constantes. El canal 1 tiene una meseta de cinco mil doscientas treinta y una muestras, entre los segundos 533,3845 y 536. Es un indicio compatible con recorte en el límite superior. Lo marco como anomalía. Si centro una ventana completamente plana, su RMS queda en cero, pero eso no demuestra reposo muscular. Por ese motivo las características deben conservar sus banderas de calidad.

## 2:20 a 2:55 - Prueba temporal

Ejecutar la celda correspondiente y mostrar la comparación antes y después.

> Esta prueba reduce la tasa de dos mil a mil muestras por segundo y aplica antes un filtro antialiasing. La tabla informa el número de muestras, la duración y los cambios observados. Reducir la tasa limita el contenido representable por debajo de la nueva frecuencia de Nyquist. Por eso no equivale a descartar filas sin filtrar, y esta demostración se mantiene separada del cálculo principal de características.

## 2:55 a 3:35 - Características y espectro

Mostrar la PSD real, la tabla por ventanas y la prueba sintética de FFT.

> Calculo características de amplitud y características espectrales en ventanas definidas. Cada fila conserva su canal, intervalo y estado de calidad. En el canal cuatro, el reposo programado entre los segundos seis y ocho entrega un RMS de 0,006439 milivoltios y una frecuencia mediana de 109,33 hertz. El agarre programado entre los segundos cincuenta y seis y cincuenta y ocho entrega 0,006524 milivoltios y 130,41 hertz. Estos resultados comparan dos ventanas y no demuestran clasificación de movimientos. La prueba sintética comprueba que el código identifica una frecuencia conocida. Esa señal de prueba no forma parte de los resultados biológicos.

## 3:35 a 4:00 - Límites y cierre

Mostrar las instrucciones de reproducción y los pendientes de entrega.

> Los resultados describen un registro de un participante. No estiman fuerza en newtons, no validan un clasificador y no prueban la matriz táctil. El código y los documentos están verificados desde un clon local. El repositorio público existe y aún está vacío. Falta completar la publicación de archivos y comprobar el clon remoto, enlazar esta grabación auténtica desde el README y revisar la entrega. Declaro el apoyo de inteligencia artificial en la organización, el código y la revisión, junto con las comprobaciones realizadas.

## Comprobación antes de entregar el video

- La grabación dura entre 3 y 5 minutos.
- Se ven Gantt y materiales.
- Se observa la ejecución real del notebook.
- Se muestran una figura EDA, una PSD/FFT y una tabla de características reales.
- El video corresponde a la misma versión del informe y de los notebooks.
- No aparecen credenciales, archivos personales ni información ajena al trabajo.
- El README contiene el enlace definitivo al video, o su ruta si se incorpora al repositorio.

Este guion no sustituye la grabación. La existencia de este archivo no demuestra que el video haya sido realizado o publicado.
