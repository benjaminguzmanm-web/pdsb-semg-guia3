# Factibilidad del avance de la Guía 3

Responsable: Benjamin Guzman Miranda. Revisión: 3 de noviembre de 2026.

El avance utiliza un registro público de sEMG y el equipo computacional existente. No requiere nuevas mediciones, sensores ni compras para cumplir el análisis de esta guía. La adquisición propia y la matriz tactosensible quedan fuera del ensayo actual.

| Dimensión | Evidencia disponible | Limitación | Decisión y contingencia |
|---|---|---|---|
| Técnica | El CSV coincide exactamente con `1_raw.csv`, participante 1. El MAT confirma cuatro canales, 2.000 Hz y mV. Hay código, datos locales y resultados corregidos. | No hay timestamps independientes para auditar pérdidas de adquisición. El MAT no asigna músculos anatómicos. Existe un tramo plano en CH1. | Conservar original, construir tiempo nominal desde `fs`, usar canales neutrales y documentar banderas. La versión corregida se ejecutó sin errores; conservar banderas y metadatos. |
| Temporal | La pauta fija entrega el 4 de noviembre de 2026. El estudiante indicó trabajo entre 22 de octubre y 3 de noviembre. | La asignación diaria por tarea es una reconstrucción de planificación, no un registro observado. La publicación y el vídeo aún requieren cierre. | Priorizar reproducción, informe, presentación y demostración. No atribuir al calendario docente fechas posteriores no confirmadas. |
| Económica | Datos públicos con CC BY 4.0, computador y almacenamiento existentes, bibliotecas abiertas. | No hay valorización consultada de equipo, conectividad o tiempo, ni presupuesto institucional confirmado. No se cotizaron sensores. | No afirmar coste total cero ni asignar precios. Registrar recursos existentes y gestiones pendientes en BOM. No proponer compras para esta entrega. |
| Ética y seguridad | Registro publicado, identificado solo por su ID dentro del conjunto. No se realizan ensayos personales ni recopilan datos nuevos. | Un participante no representa usuarios de prótesis. La licencia requiere atribución y declaración de cambios. | Citar autores, versión y DOI, declarar transformaciones y prescindir de encuestas o metadatos personales no necesarios. Limitar conclusiones a caracterización. |
| Reproducibilidad | Estructura local, procedencia cotejada, dependencias fijadas y dos notebooks corregidos ejecutados en kernels nuevos sin errores. | Archivos locales no prueban publicación, historial Git, clon limpio ni vídeo auténtico. El estudiante informó que aún no había hecho trabajo en GitHub. | El flujo local está verificado. Completar publicación, clon remoto limpio y grabación auténtica; mantener esas tareas pendientes hasta comprobarlas. |

## Alternativa ejecutable

La falta de hardware se resuelve manteniendo la modalidad basada en datos públicos de sEMG, coherente con el futuro control mioeléctrico. Si falta memoria, se lee por bloques sin cambiar índices ni el registro. Si un canal o segmento no supera el control de calidad, se conserva su evidencia y se comparan ventanas válidas, informando criterio y cantidad excluida.

Una señal sintética comprueba código y no sustituye resultados del registro real. Una simulación de presión tampoco valida la matriz táctil ni convierte este estudio en medición de fuerza.

## Actividades excluidas

No hay adquisición piloto propia: el objetivo de esta etapa puede demostrarse con muestras temporales públicas de modalidad sEMG. No se seleccionan ni compran DAQ, electrodos o microcontrolador. No se implementa un clasificador ni se prueba una prótesis física. Esas decisiones requieren una pregunta, recursos, protocolo y validación posteriores.
