# Diccionario de Variables – Dataset de Encuesta Universitaria

| Columna / Pregunta                                                   | Categoría               | Tipo de dato recomendado             | Observaciones |
|----------------------------------------------------------------------|------------------------|-------------------------------------|---------------|
| ¿En qué universidad estudias actualmente?                            | PERFIL                 | Categórico / Texto                  | Homogeneizar nombres |
| ¿En qué país estás cursando tus estudios?                             | PERFIL                 | Categórico / Texto                  |               |
| ¿A qué área principal pertenece tu carrera?                           | PERFIL                 | Categórico / Texto                  |               |
| Por favor, escribe el nombre de tu carrera o programa de estudios    | PERFIL                 | Categórico / Texto                  |               |
| ¿Qué semestre estás cursando actualmente?                             | PERFIL                 | Numérico                             | Convertir "9no Semestre" → 9 |
| ¿Cuál es tu edad?                                                     | PERFIL                 | Numérico                             | Validar valores plausibles |
| ¿Con qué género te identificas?                                       | PERFIL                 | Categórico                           |               |
| Análisis e interpretación de datos                                    | COMPETENCIAS_IA        | Entero (Likert 1–5)                 | Totalmente en desacuerdo = 1 ... Totalmente de acuerdo = 5 |
| Fundamentos de ciberseguridad                                         | COMPETENCIAS_IA        | Entero (Likert 1–5)                 |               |
| Conceptos básicos de programación y automatización                   | COMPETENCIAS_IA        | Entero (Likert 1–5)                 |               |
| Manejo de herramientas de IA (ej. ChatGPT, Copilot, Gemini, DALL-E)  | COMPETENCIAS_IA        | Entero (Likert 1–5)                 |               |
| Pensamiento crítico y resolución de problemas complejos              | COMPETENCIAS_IA        | Entero (Likert 1–5)                 |               |
| Comunicación efectiva en entornos digitales                           | COMPETENCIAS_IA        | Entero (Likert 1–5)                 |               |
| Adaptabilidad y aprendizaje continuo                                   | COMPETENCIAS_IA        | Entero (Likert 1–5)                 |               |
| Creatividad e innovación                                              | COMPETENCIAS_IA        | Entero (Likert 1–5)                 |               |
| Colaboración en equipos multidisciplinarios                           | COMPETENCIAS_IA        | Entero (Likert 1–5)                 |               |
| El currículo de mi carrera está alineado con las habilidades demandadas por el mercado laboral digital | PERTINENCIA_LABORAL | Entero (Likert 1–5) |               |
| Mi universidad promueve activamente el desarrollo de competencias digitales y blandas | PERTINENCIA_LABORAL | Entero (Likert 1–5) |               |
| Siento que la formación que he recibido me prepara para trabajos que aún no existen | PERTINENCIA_LABORAL | Entero (Likert 1–5) |               |
| El uso de la tecnología y la IA está bien integrado en las asignaturas de mi carrera | PERTINENCIA_LABORAL | Entero (Likert 1–5) |               |
| La metodología de enseñanza en mi carrera fomenta la adaptabilidad y el aprendizaje continuo | PERTINENCIA_LABORAL | Entero (Likert 1–5) |               |
| Me siento seguro(a) de que mi formación académica me prepara para conseguir un empleo relevante en mi área | CONFIANZA_LABORAL | Entero (Likert 1–5) |               |
| Mi perfil de egreso es competitivo en el mercado laboral actual       | CONFIANZA_LABORAL     | Entero (Likert 1–5)                 |               |
| Considero que mis habilidades blandas (ej. comunicación, creatividad) me dan una ventaja en el mercado laboral | CONFIANZA_LABORAL | Entero (Likert 1–5) |               |
| Creo que mi conocimiento sobre herramientas de IA mejorará mis oportunidades laborales | CONFIANZA_LABORAL | Entero (Likert 1–5) |               |
| Habilidades técnicas y digitales (ej. programación, análisis de datos) | CONFIANZA_LABORAL | Entero (Likert 1–5) |               |
| Habilidades blandas (ej. pensamiento crítico, adaptabilidad)         | CONFIANZA_LABORAL     | Entero (Likert 1–5)                 |               |
| Experiencia práctica o pasantías                                       | CONFIANZA_LABORAL     | Entero (Likert 1–5)                 |               |
| Red de contactos (networking)                                         | CONFIANZA_LABORAL     | Entero (Likert 1–5)                 |               |
| Título académico de la universidad                                    | CONFIANZA_LABORAL     | Entero (Likert 1–5)                 |               |
| El profesorado de mi carrera está capacitado para integrar herramientas de IA en la enseñanza | EVALUACION_DOCENTE | Entero (Likert 1–5) |               |
| Mi universidad fomenta la innovación en las metodologías de enseñanza para adaptarse a la era digital | EVALUACION_DOCENTE | Entero (Likert 1–5) |               |
| Mi universidad tiene los recursos adecuados (plataformas, software) para formar profesionales en la era digital | EVALUACION_DOCENTE | Entero (Likert 1–5) |               |
| En general, recomendaría mi universidad como una institución que prepara para los desafíos del mercado laboral digital | EVALUACION_DOCENTE | Entero (Likert 1–5) |               |
| El rol principal del profesorado será el de facilitador y guía del aprendizaje | EVALUACION_DOCENTE | Entero (Likert 1–5) |               |
| El profesorado deberá enfocarse más en enseñar habilidades humanas (pensamiento crítico, ética, creatividad) que en transmitir información | EVALUACION_DOCENTE | Entero (Likert 1–5) |               |
| El rol del profesorado se reducirá significativamente, siendo reemplazado en gran medida por la IA | EVALUACION_DOCENTE | Entero (Likert 1–5) |               |
| _id                                                                    | METADATOS              | Texto                               | Identificador único |
| _uuid                                                                  | METADATOS              | Texto                               | Identificador único universal |
| _submission_time                                                       | METADATOS              | Fecha/Hora                          | Momento de envío |
| _validation_status                                                     | METADATOS              | Texto / Categórico                  | Estado de validación |
| _notes                                                                 | METADATOS              | Texto                               | Comentarios internos |
| _status                                                                | METADATOS              | Texto / Categórico                  | Estado del registro |
| _submitted_by                                                          | METADATOS              | Texto                               | Usuario que envió |
| __version__                                                            | METADATOS              | Numérico                             | Versión del formulario |
| _tags                                                                  | METADATOS              | Texto                               | Etiquetas de seguimiento |
| _index                                                                 | METADATOS              | Numérico                             | Índice interno |

