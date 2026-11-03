# Datos y recuperación

El paquete local incluye `senal_emg.csv`. Git lo ignora para evitar añadir 84,9 MB al historial. La licencia CC BY 4.0 permite el uso con atribución; esta decisión de almacenamiento responde al tamaño.

1. Acceder a https://data.mendeley.com/datasets/ckwc76xr2z/2.
2. Obtener `sEMG-dataset/raw/csv/1_raw.csv` de la versión 2, o usar el ZIP `señales_bruto.zip` ya descargado.
3. Desde la raíz del proyecto:

```powershell
python src/importar_datos.py "RUTA_AL_ARCHIVO/1_raw.csv"
# O desde el ZIP completo:
python src/importar_datos.py "RUTA_AL_ARCHIVO/señales_bruto.zip"
```

El importador lee solo el miembro necesario y comprueba dimensiones, finitud y huella numérica. Preserva un CSV existente que coincida y rechaza otro registro. No descarga cuestionarios personales.

`metadatos_fuente.md` detalla licencia, atribución y límites. `diccionario.csv` y `protocolo_gestos.csv` definen campos y tareas nominales. Las versiones procesadas se calculan en memoria y no reemplazan el original.
