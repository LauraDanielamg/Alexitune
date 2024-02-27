# Alexitune

## Descripción General del Trabajo

Nuestro proyecto, Alexitune, se centra en el desarrollo de un modelo de análisis de lenguaje natural para clasificar emociones en base a sentimientos presentes en la letra de canciones. Este proyecto fue un viaje de  3 semanas que nos permitió explorar la complejidad de la mente humana y la importancia de la música como vehículo para el bienestar.

## Descripción de las Fuentes de Datos y Tecnologías

Para este proyecto, utilizamos el conjunto de datos go_emotions, que se basa en  58K comentarios seleccionados de Reddit, etiquetados en  27 categorías. A partir de un modelo preentrenado de RoBERTa, realizamos pruebas iniciales y decidimos reentrenarlo, dejando solo categorías relevantes para nuestro propósito. Aplicamos este modelo sobre conjuntos de datos extraídos de genius.com, utilizando su API.

El proceso de desarrollo se apoyó en PyTorch y la biblioteca Transformers para el manejo y entrenamiento del modelo, ofreciendo una integración eficiente para el procesamiento del lenguaje natural y la clasificación de texto. También exploramos la versión ONNX del modelo para mejorar la velocidad de inferencia y reducir el tamaño de los archivos requeridos.

## Descripción de los Resultados Más Relevantes

Hemos construido un modelo capaz de clasificar en  10 categorías sentimentales cualquier texto, seleccionadas de las  27 categorías originales. Aunque las métricas de evaluación del modelo no son óptimas debido a limitaciones temporales, representan un buen rendimiento para nuestros propósitos.

## Comentario de los Retos y Que Se Han Presentado

Durante el desarrollo, enfrentamos varios retos, desde la extracción de datos hasta la limpieza y el tratamiento de los mismos, hasta la necesidad de reentrenar el modelo para mejorar su precisión. La subjetividad inherente a las emociones y su representación en la música también nos llevó a reflexionar sobre cómo mejorar aún más nuestro modelo.

## Conclusiones y Comentarios

Alexitune ha sido una incursión fascinante en el análisis de emociones a través de la música, utilizando inteligencia artificial y procesamiento del lenguaje natural. A pesar de las limitaciones temporales, hemos logrado un modelo funcional y una aplicación que puede proporcionar una valiosa herramienta de autoconciencia emocional para los usuarios.

## Cómo Contribuir

Si estás interesado en contribuir a este proyecto, por favor revisa nuestra guía de contribución y no dudes en abrir un issue o pull request.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto

Para más información, por favor contacta a:
- Laura: [https://www.linkedin.com/in/lauradaniela-moralesgutierrez/]
