# BIO-CEL INTERACTIVE: Sistema de Estudio de Biología Celular

## Descripción
BIO-CEL INTERACTIVE es un sistema de estudio interactivo en terminal para el aprendizaje de Biología Celular. El programa está basado en un temario completo de 20 temas que cubren los fundamentos de la biología celular, desde la estructura básica de células eucariotas y procariotas hasta procesos complejos como la mitosis, meiosis y señalización celular.

## SE ACEPTAN ADICION DE PREGUNTAS AL PROGRAMA Y ACTUALIZACIONES O CORRECCIONES QUE SE CONSIDEREN IMPORTANTES!!

## Características
- Temario completo: 20 temas organizados con conceptos clave
- Sistema de evaluación: Tests por tema con preguntas de opción múltiple
- Seguimiento de progreso: Registro de temas estudiados y resultados de tests
- Simulaciones interactivas: Modelos de procesos celulares como transporte activo y cadena respiratoria
- Interfaz de terminal: Navegación intuitiva mediante menús
- Persistencia de datos: Guardado automático del progreso del estudiante

## Requisitos
- Python 3.6 o superior
- Sistema operativo: Windows, Linux o macOS

## Instalación
1. Clona o descarga el archivo biocel_interactive.py
2. Asegúrate de tener Python instalado en tu sistema
3. Opcionalmente, haz el archivo ejecutable (en sistemas Unix/Linux):
   chmod +x biocel_interactive.py

## Uso
Ejecuta el programa desde la terminal:

python biocel_interactive.py

O si lo has hecho ejecutable:

./biocel_interactive.py

## Estructura del programa

## Temas incluidos
1. Eucariotas y Procariotas
2. Membrana Plasmática
3. Transporte de Moléculas a través de la Membrana
4. Matriz Extracelular y Pared Celular
5. Uniones y Adhesión Celular
6. Microfilamentos
7. Microtúbulos
8. Filamentos Intermedios
9. Compartimentos Intracelulares y Transporte de Proteínas
10. Núcleo
11. Citosol
12. Retículo Endoplasmático
13. Aparato de Golgi
14. Endosomas, Lisosomas, Vacuolas
15. Mitocondrias
16. Peroxisomas
17. Señalización Celular
18. Ciclo Celular
19. Mitosis
20. Meiosis

## Funcionalidades principales

## 1. Consultar temario completo
Muestra la lista de todos los temas con indicación de cuáles han sido estudiados.

## 2. Estudiar tema específico
Permite acceder a los conceptos clave de cada tema y sus preguntas de práctica.

## 3. Realizar test por tema
Evaluación con preguntas de opción múltiple sobre un tema específico, con retroalimentación inmediata.

## 4. Ver progreso de estudio
Muestra estadísticas de estudio: temas completados, tests realizados y calificaciones obtenidas.

## 5. Resumen de conceptos clave
Presenta un resumen organizado por categorías de todos los conceptos importantes.

## 6. Simulación de procesos celulares
Incluye tres simulaciones interactivas:
- Transporte activo Na+/K+
- Cadena respiratoria mitocondrial
- Ciclo celular y puntos de control

## 7. Salir del sistema
Guarda automáticamente el progreso antes de cerrar.

## Sistema de archivos
- biocel_interactive.py: Programa principal
- progreso_biocel.pkl: Archivo binario que guarda el progreso del usuario (se crea automáticamente)

## Navegación
El sistema utiliza una interfaz de menús jerárquica:
1. Menú principal con 7 opciones
2. Submenús específicos para cada funcionalidad
3. Navegación mediante números y tecla Enter
4. Retorno al menú anterior con opción 0 o específica

## Diseño técnico
- Programación orientada a objetos: Clases SistemaEstudio e InterfazEstudio
- Estructuras de datos: Dataclasses para temas y preguntas
- Persistencia: Serialización con pickle para guardar progreso
- Interfaz: Limpia y profesional, con encabezados y separadores visuales

## Autor
Miguel Martín Gil

## Licencia
Programa educativo para uso académico.

## Notas para el desarrollo
- El código está documentado en español con comentarios explicativos
- La estructura modular permite fácil expansión de temas y funcionalidades
- Las simulaciones pueden extenderse para incluir más procesos celulares
- El sistema de preguntas puede ampliarse con más temas y niveles de dificultad

## Sugerencias de uso académico
1. Estudio individual: Como herramienta de repaso y autoevaluación
2. Clases prácticas: Para demostraciones interactivas en laboratorio
3. Preparación de exámenes: Tests por tema para evaluar conocimiento
4. Complemento teórico: Resúmenes de conceptos clave organizados

El programa está diseñado para ser intuitivo y no requiere conocimientos previos de programación para su uso.
