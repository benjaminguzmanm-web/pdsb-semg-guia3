# Aclaración respecto de la Guía 2

El informe anterior sugería que una ventana con media distinta de cero podía contradecir un centrado global correcto. Esa inferencia no es válida: al restar la media global, solo queda en cero la media del registro completo. Una ventana particular puede conservar un nivel local positivo o negativo por deriva o cambios de nivel.

La Guía 3 distingue el centrado global usado en la comparación temporal del canal 4 y el centrado local por ventana usado para RMS AC y MAV AC. Ninguno prueba una falla de calibración ni repara un recorte.
