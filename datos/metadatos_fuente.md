# Procedencia verificada del registro

Benjamin Guzman Miranda. Verificación: 03-11-2026.

Fuente: Ozdemir, M. A., Kisa, D. H., Guren, O. y Akan, A. Dataset for multi-channel surface electromyography (sEMG) signals of hand gestures. Mendeley Data, versión 2 (22-12-2021). https://doi.org/10.17632/ckwc76xr2z.2. Página: https://data.mendeley.com/datasets/ckwc76xr2z/2.

Licencia CC BY 4.0 comprobada en la página de la versión 2 el 03-11-2026. Atribuir autores, versión, enlace y modificaciones al redistribuir. No se incluye el cuestionario demográfico ni se intenta reidentificar participantes.

## Cotejo de todas las muestras

Se compararon numéricamente las 1.280.000 filas y cuatro columnas de `senal_emg.csv` con `ckwc76xr2z-2/sEMG-dataset/raw/csv/1_raw.csv` del ZIP original del usuario. Diferencia absoluta máxima: 0. La matriz `data` de `raw/mat/1_raw.mat` también coincidió exactamente. No se utilizó la versión filtrada.

El CSV del trabajo permanece sin cambios. SHA256 de sus bytes: `f0ab451b295030d2207ef75d1cb8d0079edc06597ceb34c61137ba025091791b`. Huella numérica canónica float64 little endian por filas: `0bf791c1d2d55f93b755f2f9566809cb4d36ba9888a25a26bf5c925294f926e6`. Esta última reconoce el mismo registro cuando cambia únicamente el formato decimal. Evidencia: `evidencias/procedencia_verificada.json`.

| Campo del MAT | Valor verificado |
|---|---|
| `iD` | 1 |
| `data` | 1.280.000 x 4 |
| `fs` | 2.000 Hz |
| `isi`, `isi_units` | 0,5 ms |
| `start_sample` | 0 |
| `units` | mV en los cuatro canales |
| `labels` | EMG_Raw_CH1, EMG_RAW_CH2, EMG_RAW_CH3, EMG_RAW_CH4 |
| Duración N/fs | 640 s |
| Última muestra | 639,9995 s |

El [artículo original](https://doi.org/10.1016/j.dib.2022.107921) describe BIOPAC MP36, electrodos superficiales bipolares Ag/AgCl del antebrazo y rango de señal +/-10 mV. No se comprobó una asignación anatómica individual de las columnas. No hay timestamps independientes para verificar pérdidas anteriores a la exportación.

## Protocolo nominal

El script original se conserva sin editar en `datos/EMG_gesture_segmentation.m` y fija ciclos que comienzan con reposo en 4, 138, 272, 406 y 540 s. Cada ciclo tiene diez tareas de seis segundos, con inicios separados diez segundos. Orden: reposo, extensión, flexión, desviación cubital, desviación radial, agarre, abducción, aducción, supinación y pronación. Se toma la ventana central de dos segundos de cada tarea. Tabla: `datos/protocolo_gestos.csv`.

El índice MATLAB `a*fs+1:b*fs` se traduce a Python `[a*fs:b*fs]`. Las etiquetas representan tareas programadas. El cotejo exacto sustenta aplicar la temporización, pero no confirma independientemente el movimiento realizado ni su fuerza.

## Pertinencia y límites

La sEMG caracteriza actividad eléctrica para una entrada futura de control mioeléctrico. La matriz tactosensible mide contacto/presión y requiere validación independiente. Este registro no valida esa matriz ni estima fuerza en newtons. Se estudia un participante y no se presenta un clasificador.
