# Thanatology-Computational-Creativity
This proyect was made it with python
Trying to use the technique "Through The Park" by Montfort 
Described in the book "Creatividad Computacional" by Rafael Pérez y Pérez 
to create a system that can write grief messages

To run it you need:
Python 3.6 or higher
Dependecies:
  random, time, re
  
How to run it:
Just execute "python3 main.py"


Sistema generador de textos automaticos de condolencia (Tanatología)
Seminario de Sistemas Inteligentes I
Dr. Rafael Pérez y Pérez
Ayala De La Rosa José Daniel
2173071015

Indice:
1.-Introducción
-Generación de narrativas usando plantillas
-Algoritmo "Through The Park"
-Temática del proyecto
-Importancia
-Obtención de los datos
-Aplicaciones (comerciales y cientificas)

2.-Casos que contempla este programa
3.-Uso de listas
4.-Uso de reglas y cálculos
5.-Formularuios empleados
6.-Pruebas del sistema
7.-Resultados y Conclusiones

Apéndice 1.-Diagrama de bloques
Apéndice 2.-Código fuente

1.-Introducción
La generación de narrativas usando plantillas es una de las multiples implementaciones de la creatividad computacional, siendo esta una de las más conocidas y comerciales, el objetivo principal de esta forma es crear textos diferentes unos de otros, que parezcan creados por un humano y que se puedan conciderae como "Creativos" o "Nuevos" o "Inovadores" usando la Formula:
D + F + C + R = texto "nuevo"
donde:

D = Datos:
Se refiere a al información de entrada, es la que se analizará para crear diferentes narrativas en base a su propia naturaleza o identidad (diferencia entre otros Datos)

F = Formulario o Platilla
La plantilla como sabemos es un esquema base del cual se parte para crear nuevas cosas, en este caso es lo mismo: es una estructura básica de la cual se parte para crear las diferentes narrativas

C = Cálculos
Como su nombre se indica es la parte donde se hacen operaciones (regularmente aritmeticas) para obtener información no explicita en base a los Datos

R = Reglas
Son las normas que se estabablecen para saber como actuar cuando se tiene un caso concreto, como por ejemplo modificar un saludo dependiendo si la persona a la que nos referimos es hombre o mujer:
si es hombre "Hola amigo" de lo contrario "Hola amiga"

Algoritmo Through The Park:
Este algortimo descrito por Montfort en el 2008, trata de explicar la importancia de la "Elipsis" en la generación de narrativas y aún más en la generación de narrativas por medio de plantillas en la creativdad computacional.

Este algoritmo lo que dice es: de una lista de opciones (frases, oraciones o palabras) que van una detrás de otra de forma secuencial, si se omite una o varias de ellas no debe de interferir en el entendiemento general de la suma de todas las opciones y además debe o puede generar dinamismo y repitiendo este proceso varias veces sobre la misma lista, genra resultados diferentes en el entendimiento de la suma.

El objetivo de este proyecto es generar narrativas que ayuden a las personas que no saben que decir cuando un ser querido afronta una perdida en base a las tres primeras etapas del duelo descritas por la tanatología (Negación, Ira y Negociación) y que suenen o que la persona que la quiere envíar sienta empatía o mínimo se sienta agusto con ella (la narrativa generada)

La tanatología es una rama de la psicología que trata de ayudar a las personas con sus perdidas, en ella se describe el duelo la cual es una etapa por la que todos pasamos despúes de sufrir la perdida de cualquier objeto al cual le teníamos apego, esta fase se divide en 5 etapas (o más, eso dependerá el autor):

La negación:
Es regularmente la reacción inmediata después de una perdida, se tiene la sensación de irrealidad con la situación.

La ira:
Tras la negación regularmente lo que presigue son sentimientos de frustración e impotencia.

La negociación:
Es el primer paso cuando tenemos contacto con la realidad de laperdida, afrontamos que eso que perdimos ya no volverá pero empezamo a exlplorar que cosas se pudieron haber hecho para revertir la situación:

La depresión:
La persona conforme sale de la etapa anterior empieza tener sentimientos de "pena", "tristeza", "nostalgia" y "ausencia", lo cual lleva a el aislamiento social y perdida del interés cotidiano, esta etapa no es clinicamente una depresión, es más el camino para empezar a seguir viviendo a pesar de la perdida, sin embargo se le llama así por la gran similitud con una depresión patologica (sin embargo si no se trata a tiempo y en forma sí puede desembocar en una)

La aceptación:
Es la llegada de un estado de calma y compresión de que la muerte y otras perdidad son fenómenos inherentes a la vidad humana y sus acciones.

En tiempos tan dificiles como el que nos tocó vivir gracias al SARS-COV2 y las cantidades tan grandes de defunsiones por día, creo que es importante poder hacerle sentir a una persona a la cual estimamos nuestro apoyo por medio de un mensaje, el problema es que casi nunca sabemos que decir y es normal, son temas que no nos enseñanor a llevar, pero gracias la creativdad computacional este puede ser un problema facilmente resuelto y creo este proyecto puede ser la primer piedrita para construir soluciones más complejas y completas.

Para que el sistema pueda generar una narrativa necesita 2 tipos de Datos:
1)Son los Datos con los que se llenan la plantilla, estos vienen de una "Base de datos" que en realidad son archivos txt que contienen textos clasificados en 3 variantes (Negación, Ira y Negociación) de las palabras más populares dichas por las personas (actualmente extraidos y clasificados manualmente pero que podría obtenerse autamticamente con un modelo de machine learning clasificador de textos)
2)Son los Datos a los que se le aplican las reglas, estos se obtiene del usuario, el o ella los ingresa en la terminal (se podrían extraer de un archivo json, o incluirse como parametros al momento de la ejecución del sistema, cosa que en esta versión aún no se implementa).

La cantidad de textos que puede generar el sistemas va en función a la cantidad de líneas por archivo, conforme más grande sea la "Base de Datos" más diversos pueden ser las narrativas generadas (esto igual podría ser escalable creando 3 diferentes sistemas o uno más complejo, donde dependiendo la etapa y la emoción se creara un texto alimentador de la "Base de Datos")

Las aplicaciones que le veo comercialmente a este proyecto sería sólo en la generación automática de textos para verder tarjetas de cumpleaños, bodas, saludos de correos o cartas (todos ellos basandonos en el rpincipio de plantillas y el algoritmo "through the park"), en el aspecto cientifico creo podría ayudar a la misma rama de la psicología para poder ayudar a personas a sobre llevar la soledad, la depresión, las perdidas por medio de mensajes sonstantes y automáticos (respuesta sin fundamentos sólo basada en mis creencias), sin embargo podría tener un mayor alcance si se juntaran ambas ramas (psicología y computación) para hacer un sistema más complejo y que dejara de lado las creencias y se basara en hechos.

2.-Casos que contempla este programa
Los casos que contempla este sistema (de momento en esta versión) son 2
3.-Uso de listas
4.-Uso de reglas y cálculos
5.-Formularuios empleados
6.-Pruebas del sistema
7.-Resultados y Conclusiones

Apéndice 1.-Diagrama de bloques
Apéndice 2.-Código fuente