# Presentación de la Guía 3

**Autor:** Benjamin Guzman Miranda  
**Versión:** cierre local al 3 de noviembre de 2026  
**Archivos:** `presentacion_guia3.pdf` y `presentacion_guia3.pptx`.

1. **Caracterización de señales sEMG.** Objetivo, autor, periodo de trabajo y entrega oficial.
2. **Planificación y recursos.** Etapas del 22 de octubre al 3 de noviembre, recursos disponibles y pendientes de publicación, clon remoto, video y revisión. La distribución por tarea reconstruye la planificación.
3. **Procedencia verificada del registro.** Igualdad exacta con `1_raw.csv` y `1_raw.mat`, participante 1, cuatro canales, 2.000 Hz, mV y 640 s.
4. **Calidad: meseta en el canal 1.** 5.231 muestras constantes entre 533,3845 y 536 s, decisión de marcado y conservación. Se aceptan 1.277 de las 1.280 filas de características bajo las reglas utilizadas.
5. **Reducción de tasa con filtro antialiasing.** Canal 4 de 2.000 a 1.000 Hz, 1.280.000 a 640.000 muestras, 640 s. FIR de 161 coeficientes y corte de 450 Hz. Las características principales usan la tasa original.
6. **Características por tarea programada.** Canal 4, ciclo 1, reposo nominal 6-8 s y agarre nominal 56-58 s. RMS AC de 0,006439 y 0,006524 mV, frecuencia mediana de 109,33 y 130,41 Hz.
7. **PSD real y comprobación de la FFT.** PSD de las dos ventanas reales mediante Welch. Prueba sintética separada: 50 Hz conocido, 50 Hz estimado, error 0 Hz.
8. **Alcance y cierre.** Un participante y tareas nominales, sin fuerza, clasificación ni validación de la matriz táctil. Repositorio público creado: https://github.com/benjaminguzmanm-web/pdsb-semg-guia3. Pendientes: completar publicación de archivos y comprobar clon remoto, video auténtico y revisión de entrega. El repositorio existe pero todavía está vacío. La ejecución desde un clon local sí está verificada.

El PPTX conserva texto, tablas y gráficos editables. Las fuentes y parámetros ampliados están en las notas de cada diapositiva. Los valores de los gráficos editables se redondean a 12 cifras significativas para compatibilidad con las hojas de datos de Office, sin alterar las tablas analíticas del proyecto.

Para la grabación auténtica de 3 a 5 minutos, utilizar `guion_video.md` y mostrar la ejecución real del notebook. La presentación no sustituye esa evidencia.
