# PDSB - Guía 3: caracterización exploratoria de sEMG

**Autor único:** Benjamin Guzman Miranda. **Asignatura:** 92028, Procesamiento Digital de Señales Biológicas, Ingeniería Civil en Mecatrónica, Universidad de Santiago de Chile. **Docente:** Dr. Ing. Michael Miranda Sandoval.

**Periodo de trabajo indicado:** 22-10 al 03-11-2026. **Entrega oficial:** 04-11-2026. Las fechas por tarea son una reconstrucción de planificación; no se presentan como bitácora diaria ni como historial de commits de ese periodo.

El proyecto desarrolla control de calidad y características de una posible entrada para control mioeléctrico futuro. La matriz tactosensible de la tesis mide contacto/presión y requiere validación independiente.

## Productos de la guía

- [Informe técnico PDF](informe/informe_guia3.pdf) y [fuente editable Markdown](informe/informe_guia3.md).
- [Presentación PDF, 8 diapositivas](presentacion/presentacion_guia3.pdf) y [PowerPoint editable](presentacion/presentacion_guia3.pptx).
- [Gantt editable](planificacion/gantt.csv), [PDF](planificacion/gantt.pdf) y [PNG](planificacion/gantt.png).
- [Hitos](planificacion/hitos.csv), [materiales](planificacion/materiales.csv), [factibilidad](planificacion/factibilidad.md), [riesgos](planificacion/riesgos.md) y [seguimiento](planificacion/seguimiento.md).
- [Ficha del proyecto](datos/ficha_proyecto.md), [metadatos](datos/metadatos_fuente.md), [diccionario](datos/diccionario.csv) y [protocolo nominal](datos/protocolo_gestos.csv).
- [Notebook EDA](notebooks/01_eda.ipynb) y [notebook de características](notebooks/02_caracteristicas.ipynb), ejecutados secuencialmente.
- [Reflexión](planificacion/respuestas_reflexion.md) y [guion para vídeo auténtico de 3-5 minutos](presentacion/guion_video.md).

**Repositorio público:** https://github.com/benjaminguzmanm-web/pdsb-semg-guia3. **Publicación y clon remoto:** verificados; evidencia en [reproduccion_github.json](evidencias/reproduccion_github.json). **Vídeo:** pendiente de grabación real; aún no hay archivo ni enlace. [Estado de entrega](ESTADO_ENTREGA.md) identifica las acciones que faltan. El ZIP local no sustituye el repositorio solicitado.

## Datos y licencia

Fuente: Ozdemir et al., [Mendeley Data, versión 2](https://data.mendeley.com/datasets/ckwc76xr2z/2), DOI 10.17632/ckwc76xr2z.2, CC BY 4.0. [Atribución y cambios](ATRIBUCION_DATOS.md).

Se cotejó todo `senal_emg.csv` con `raw/csv/1_raw.csv` y `raw/mat/1_raw.mat`: coincidencia exacta de 1.280.000 x 4 muestras. El MAT confirma participante 1, fs=2.000 Hz, unidades mV e inicio 0. Duración N/fs=640 s. [Evidencia del cotejo](evidencias/procedencia_verificada.json). No se utiliza la versión filtrada ni se redistribuyen cuestionarios.

El CSV incluido en el paquete local se ignora en Git por su tamaño (84,9 MB). Para un clon sin datos, [recuperar exactamente el registro](datos/README.md), y desde la raíz ejecutar una de estas opciones:

```powershell
python src/importar_datos.py "RUTA_AL_ARCHIVO/1_raw.csv"
python src/importar_datos.py "RUTA_AL_ARCHIVO/señales_bruto.zip"
```

El importador verifica la huella numérica, no solo el nombre y las dimensiones. No sobrescribe otro registro.

## Ejecución reproducible

Usar el entorno de Python de la Guía 2. Se comprobó con Python 3.10.7, NumPy 2.2.6, Pandas 2.3.3, SciPy 1.15.3 y Matplotlib 3.10.8. Python 3.10 o 3.11 permite instalar las versiones fijadas. No se incorpora `.venv/` al repositorio.

Desde la raíz de esta carpeta (la que contiene README.md y src/):

```powershell
python -m pip install -r requirements.txt
python src/ejecutar_notebooks.py
```

El segundo comando inicia un kernel nuevo por notebook, ejecuta `01_eda.ipynb` y luego `02_caracteristicas.ipynb`, guarda salidas y escribe [el registro de ejecución](evidencias/ejecucion_notebooks.json). Requiere permitir la comunicación local de Jupyter. Como alternativa, abrir ambos notebooks en VS Code/Jupyter y usar reiniciar y ejecutar todo, en el mismo orden. Se admiten la raíz y notebooks/ como directorios de trabajo.

Para recalcular solamente tablas, figuras y pruebas sin interfaz Jupyter:

```powershell
python src/procesamiento.py
```

Resultados esperados: lectura 1.280.000 x 4; un tramo plano largo CH1 de 5.231 muestras; 1.280 filas de características, 1.277 aceptadas por las reglas; 200 filas de ventanas centrales del protocolo; FFT sintética 50 Hz con error 0 Hz; reducción temporal a 640.000 muestras y 1.000 Hz conservando 640 s. Los originales no se modifican. El vídeo debe mostrar ejecución real, no salidas simuladas.

## Decisiones e interpretación

Se preservan muestras originales, se marcan valores |x| >= 9,999 mV y rachas exactamente constantes de al menos 0,1 s. Se omiten las ventanas marcadas de los resúmenes de actividad, pero siguen en la tabla. `valida_calidad=True` significa que superó estas reglas, no que esté libre de todo artefacto.

RMS AC y MAV AC usan centrado local por ventana de 2 s. Welch usa Hann periódica, nperseg=2.000, noverlap=1.000, detrend constante, PSD unilateral en mV²/Hz e integración por trapecios entre 0 y 1.000 Hz. Los parámetros están en [evidencias](evidencias/parametros_analisis.json). La operación temporal compara 2.000 a 1.000 Hz con FIR de 161 coeficientes; no reemplaza los datos de las características.

Las etiquetas proceden del protocolo nominal y no de una comprobación independiente de movimiento. Reposo y agarre del ciclo 1 presentan RMS parecidos; no prueban separación útil. La señal constante tampoco identifica reposo muscular. Un participante y cinco ciclos no bastan para generalizar a personas nuevas. No se mide fuerza, diagnostica ni presenta clasificador.

## Uso de IA e historial

Codex/ChatGPT apoyó revisión, código, validación y redacción. Se adoptaron el cotejo completo, las banderas, la integración de PSD y las pruebas sintéticas. Se descartaron causas de hardware no demostradas y la interpretación de RMS cero como reposo. El estudiante debe revisar y comprender resultados y decisiones antes de entregar.

Los cambios Git se registran en sus fechas reales. La referencia de la Guía 2 queda preservada localmente en archivo_guia2/ y no forma parte del flujo de ejecución. [Corrección sobre centrado global/local](evidencias/correccion_interpretacion_centrado.md).
