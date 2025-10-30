# README – Dataset de Encuesta Universitaria

Este documento describe la estructura, categorías de preguntas y tipos de datos del CSV de resultados de la encuesta. El dataset está listo para análisis tras aplicar ajustes mínimos de limpieza y codificación.

---

## 1. Estructura general del CSV

- Cada fila representa las respuestas de un participante.
- Cada columna representa una pregunta o un metadato de seguimiento.
- Columnas de separación de categorías (`PERFIL`, `COMPETENCIAS_IA`, etc.) **solo indican el inicio de una categoría** y no contienen datos.
- Columnas de metadatos (`_id`, `_uuid`, `_submission_time`, `_validation_status`, `_notes`, `_status`, `_submitted_by`, `__version__`, `_tags`, `_index`) pueden conservarse para seguimiento o eliminarse para análisis de contenido.

---

## 2. Categorías de preguntas y ejemplos

| Categoría                | Ejemplos de preguntas                                                                                     | Tipo de dato sugerido |
|---------------------------|----------------------------------------------------------------------------------------------------------|---------------------|
| **PERFIL**                | ¿En qué universidad estudias actualmente? <br> ¿Cuál es tu edad? <br> ¿Con qué género te identificas? | Texto / Numérico / Categórico |
| **COMPETENCIAS_IA**       | Análisis e interpretación de datos <br> Manejo de herramientas de IA <br> Creatividad e innovación      | Escala Likert (1–5) |
| **PERTINENCIA_LABORAL**   | El currículo de mi carrera está alineado con las habilidades demandadas por el mercado laboral digital | Escala Likert (1–5) |
| **CONFIANZA_LABORAL**     | Me siento seguro(a) de que mi formación académica me prepara para conseguir empleo relevante            | Escala Likert (1–5) |
| **EVALUACION_DOCENTE**    | El profesorado de mi carrera está capacitado para integrar herramientas de IA en la enseñanza          | Escala Likert (1–5) |

> Nota: Las respuestas tipo Likert deben codificarse numéricamente para análisis (ej.: Totalmente en desacuerdo = 1, ..., Totalmente de acuerdo = 5).

---

## 3. Tipos de datos sugeridos por columna

| Columna / Pregunta        | Tipo de dato recomendado |
|---------------------------|-------------------------|
| Universidad, País, Área, Carrera, Género | Categórico / Texto |
| Semestre                  | Numérico (convertir "9no Semestre" a 9) |
| Edad                      | Numérico |
| Respuestas Likert          | Entero (1–5) |
| Metadatos (_id, _uuid, ...) | Texto o Fecha según corresponda |
| Fecha de nacimiento       | Fecha (para cálculo de edad) |
| _submission_time          | Fecha/Hora |

---

## 4. Recomendaciones de limpieza

1. **Eliminar o ignorar** columnas de separación de categorías vacías.
2. **Homogeneizar** nombres de universidades, carreras y áreas de estudio.
3. **Codificar Likert** a valores numéricos.
4. **Convertir fechas** a formato datetime para análisis de edad o tiempo de envío.
5. **Verificar valores atípicos** en edad y semestre.

---

## 5. Preparación para análisis

Tras estos pasos, el dataset estará listo para:

- Análisis estadístico descriptivo.
- Agrupaciones y comparaciones por categoría.
- Visualizaciones (gráficos de barras, boxplots, heatmaps, etc.).
- Modelos predictivos o correlaciones entre competencias, confianza y evaluación docente.

---

