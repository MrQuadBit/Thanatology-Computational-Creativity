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

En tiempos tan dificiles como el que nos tocó vivir gracias al SARS-COV2 y las cantidades tan grandes de defunsiones por día, creo que es importante poder hacerle sentir a una persona a la cual estimamos nuestro apoyo por medio de un mensaje, el problema es que casi nunca sabemos que decir y es normal, son temas que no nos enseñanor a manejar, pero gracias la creativdad computacional este puede ser un problema facilmente resuelto y creo este proyecto puede ser la primer piedrita para construir soluciones más complejas y completas.

Para que el sistema pueda generar una narrativa necesita 2 tipos de Datos:
1)Son los Datos con los que se llenan la plantilla, estos vienen de una "Base de Datos" que en realidad son archivos txt que contienen textos clasificados en 3 variantes (Negación, Ira y Negociación) de las palabras más populares dichas por las personas (actualmente extraidos y clasificados manualmente pero que podría obtenerse automáticamente con un modelo de machine learning clasificador de textos)
2)Son los Datos a los que se le aplican las reglas, estos se obtiene del usuario, el o ella los ingresa en la terminal (se podrían extraer de un archivo json, o incluirse como parametros al momento de la ejecución del sistema, cosa que en esta versión aún no se implementa).

La cantidad de textos que puede generar el sistemas va en función a la cantidad de líneas por archivo, conforme más grande sea la "Base de Datos" más diversos pueden ser las narrativas generadas (esto igual podría ser escalable creando 3 diferentes sistemas o uno sólo más complejo, donde dependiendo la etapa y la emoción se creara un texto alimentador de la "Base de Datos")

Las aplicaciones que le veo comercialmente a este proyecto sería sólo en la generación automática de textos para verder tarjetas de cumpleaños, bodas, saludos de correos o cartas (todos ellos basandonos en el principio de plantillas y el algoritmo "through the park"), en el aspecto cientifico creo podría ayudar a la misma rama de la psicología para poder ayudar a personas a sobre llevar la soledad, la depresión, las perdidas por medio de mensajes sonstantes y automáticos (respuesta sin fundamentos sólo basada en mis creencias), sin embargo podría tener un mayor alcance si se juntaran ambas ramas (psicología y computación) para hacer un sistema más complejo y que dejara de lado las creencias y se basara en hechos.

2.-Casos que contempla este programa
Para hablar de casos debemos de explicar como se están creando las narrativas:

Se usa una plantilla general:
[SALUDO], [MENSAJE_INICIAL], [NEGACIÓN || IRA || NEGOCIACIÓN], [MENSAJE_APOYO], [DESPEDIDA]

que es rellenada con listas:
SALUDO = ["", "Hola", "Buen@", "Querid@"]

estas listas son procesadas / elegidas dependiendo los "DATOS" de entrada ingresados por el usuario y es aquí donde tenemos los casos, se ingresa un nombre y el sexo de la persona que va a recibir el texto (se podría mejorar creando un modulo identificador de sexo en los nombres):
SER_QUERIDO_NOMBRE = "daniel"
SER_QUERIDO_GENERO = "m" 

y dependiendo el sexo se selecciona un elemento de la lista y se modifica para que la palabra u oración vaya acorde con el nombre, ejemplo:
"daniel" es "m" másculino y se ha seleccionamos la opción 4 de la lista "Querid@"; como daniel es hombre, entonces se cambia "@" por "o" quedando como resultado: "Querido Daniel"


3.-Uso de listas
Como mencionamos antes "La cantidad de textos que puede generar el sistema va en función a la cantidad de líneas por archivo", cada "archivo" es una lista de opciones, entonces cada [VARIABLE] en nuestra platilla será cambiada por una opción en la lista, a diferencia del algoritmo "Through the park" que es usado especificamente en las 3 etapas del duelo [NEGACIÓN || IRA || NEGOCIACIÓN] para hacer "elipsis", se usa un algoritmo parecido pero en vez de obviar u omitir una opción, se omiten todas menos una para así obtener un sólo condidato asignable a cada [VARIABLE], como todas las opciones no hacen referencia a otras opciones de otras listas y en identidad tienen coherencia por sí mismas, se genera un efecto parecido al algoritmo "Through the park" pero multiples veces por cada [VARIABLE] y en "elipsis" con las demás.

4.-Uso de reglas y cálculos
Aparte del algoritmo "Through the park", la multi "elipsis" entre [VARIABLES], nos enfocamos mucho en la sexualización de frases, oraciones o palabras, este proceso es relativamente simple, dentro de las opciones de las listas hay ciertas palabras u oraciones que cambian dependiendo si nos referimos a un hombre o a una mujer, para ello la opciones tienen un "@" cada vez que no se sabe el sexo de la persona, entonces en el momento entre la selección de de opción en una lista y la integración a la platilla, pasa por un sexualizador de palabras que cambia ese "@" por la conjugación que vaya acuerdo al sexo de la persona, sin embargo no siempre es tan fácil por ejemplo:
Supongamos que de nuestra "Lista" de "SALUDOS":
SALUDO = ["", "Hola", "Buen@", "Querid@"]

escogemos la opción 3 "Buen@", esta opción hace referencia al momento de día en el que se pide el mensaje, para crearlo correctamente se hace:
1)Se obtiene la hora actual
2)Se evalua (si es antes de las 12 es mañana, si es después de las 12 pero antes de las 7 es tarde, de lo contrario es noche)
3)Dependiendo el momento del día se cambia el "@" por:
mañana = "os días"
tarde = "as tardes"
noche = "as noches"
4) Se forma la frase
	Buen@ = "Buenos días Daniel" || "Buenas noches Daniel" || "Buenas tardes Daniel"

Otro cálculo que hacemos para darle dinamismo / variedad  a las opciones y a la plantilla es ante poner el saludo al nombre o vice versa, por ejemplo:

Supongamos que ahora escogemos de la "Lista" de "SALUDOS" la opción 2 "Hola", lanzamos una moneda (un número aleatorio entre 1 y 2) y dependiendo el resultado escogemos si va antes o después
Si sale 1 ponemos el saludo antes:
	"Hola Daniel"
Si sale 2 ponemos el saludo después:
	"Daniel hola"
	(nota: si va después el [SALUDO] del nombre pasa por un conversor a minusculas)

Esta dinámica o regla no sólo se ocupa para la opción "Hola", se aplica a todas las opciones de saludos quedando una plantilla con OPCIONES_SALUDOS X 2(ante poner el saludo o no) X RESTO_DE_VARIABLES = CANTIDAD_DE_NARRATIVAS_QUE_SE_PUEDEN_GENERAR, la cual podría ocuparse para otras situaciones (opción aún no implementada).

Por último debemos de hablar del tan mencionado algortimo "Through the park" implementado a las etapas del duelo.
Ya entendemos como funciona el algoritmo para darle "elipsis" a las narrativas, entendemos que de una lista se puede obtener opciones y que tenemos 3 etapas del duelo, entonces juntemos todas las variables.
Supongamos que ya asignamos el [SALUDO] con las reglas y calculos antes mencionados, hicimos la multi "elipsis" con el [MENSAJE_INICIAL], [MENSAJE_APOYO] Y [DESPEDIDA], sólo nos queda la parte extraña de la plantilla [NEGACIÓN || IRA || NEGOCIACIÓN], le haremos el algoritmo "Through the park" a la "Lista" de "Listas" (NEGACIÓN || IRA || NEGOCIACIÓN) (si una lista puede tener otras listas como opciones)  para así eliminar una lista y después hacerle multi "elipsis" a cada "Lista", dandonos como resultado las siguientes tuplas de opciones disponibles:
[Negación + Ira]
[Ira + Negociación]
[Negación + Negociación]

Esto se hace con el fin darle "elipsis" pero porque al momento de envíar el mensaje no sabemos en que etapa del duelo se encuentra la persona recepetora del mensaje, lo que sí sabemos es que sí o sí deberá pasar por cada etapa por un menor o mayor tiempo en cada una de las etapas (Segun la tanatología) y como dice el algoritmo "si se omite una o varias de ellas no debe de interferir en el entendiemento general de la suma de todas las opciones" así dando un mensaje diferente pero siempre "adecuado" indiferentemente la etapa en la que se cuentre la persona.

5.-Formularios empleados
Para este punto ya entendimos mejor como se crean las diferentes narrativas, si pudieramos listar las plantillas totales que se general serían:
[SALUDO] [NOMBRE], [MENSAJE_INICIAL], [NEGACIÓN + IRA], [MENSAJE_APOYO], [DESPEDIDA]

[SALUDO] [NOMBRE], [MENSAJE_INICIAL], [IRA + NEGOCIACIÓN], [MENSAJE_APOYO], [DESPEDIDA]

[SALUDO] [NOMBRE], [MENSAJE_INICIAL], [NEGACIÓN + NEGOCIACIÓN], [MENSAJE_APOYO], [DESPEDIDA]

[NOMBRE] [SALUDO], [MENSAJE_INICIAL], [NEGACIÓN + IRA], [MENSAJE_APOYO], [DESPEDIDA]

[NOMBRE] [SALUDO], [MENSAJE_INICIAL], [IRA + NEGOCIACIÓN], [MENSAJE_APOYO], [DESPEDIDA]

[NOMBRE] [SALUDO], [MENSAJE_INICIAL], [NEGACIÓN + NEGOCIACIÓN], [MENSAJE_APOYO], [DESPEDIDA]

y el total estimado de narrativas como antes habíamos mencionado es igual a "La cantidad de textos ... que va en función a la cantidad de líneas por archivo" por el número de plantillas, conforme más grandes sean los archivos, más narrativas se pueden generar.

6.-Pruebas del sistema
A continuación les dejaremos unos de mejores reultados según mi opinión y la de seres queridos cercanos:

(Los datos de entreda fueron "Daniel" y "m"):

"Daniel, no existen palabras para describir lo mucho que lamento tu perdida, aún no me creo que sea verdad, aunque no queramos así es el ciclo de la vida, te deseo sanación y paz, un gran y fuerte abrazo"

"Daniel, no puedo imaginarme el dolor que estás sintiendo ahorita, aún no me creo que sea verdad, no podemos cambiar lo que sucedió, estoy a tu disposición, cuidate mucho."

"Querido Daniel, me entristece mucho escuchar tu perdida, quisiera cerrar los ojos y despertar de esta pesadilla, aunque no queramos así es el ciclo de la vida, siempre has estado para mi y quería hacerte saber que yo lo estaré para ti también, estoy a tu disposición, cuidate mucho."


7.-Resultados y Conclusiones
Creo la primer obervación que puedo hacer es la oportunidad de crecimiento del proyecto, creo que tiene (aparte de que mencioné durante el desarrollo de este documento) muchas oportunidas para mejorar, como automatizar ciertos procesos (recolección de mensajes o generación de los mismos) o identificadores (sexualizador de palabras u oraciones más complejos o clasificador de mensajes dependiendo la etapa del duelo).

Lo segundo es que noté que los mensajes que más noté que son aceptados por las personas son aquellos que no contienen la etapa del duelo [IRA], creen que es muy agresivo.

Otra observación es que mis seres queridos gente cree prudente agregar mensajes o frases con tildes religiosas como "Díos te bendiga", "Díos te de paz", "Esa personas se encuentra en un lugar mejor", "Ya está en el cielo", reservo mis comentarios pero probablemente sería un sesgo cultural y regional.

Por último también observé que hacen faltas más mensajes de apoyo o más humanizados, las narrativas que más gustaron fueron las que tenía frases como "cuidate mucho", "estoy a tu disposición" o "Te deso sanación y paz", todas referntes a que la persona que envía el mensaje apoya a la persona recpetora en este momento de luto.

sigo creyendo que tiene potencial el proyecto pero sí y sólo sí se acompaña con especialistas en el tema.

Apéndice 1.-Diagrama de bloques

Apéndice 2.-Código fuente
A continuación debería de aparecer el código completo pero es muy verboso por la cantidad de archivos o listas que se usan, así que dejaré la liga a mi "Git-hub", una descripción de los archivos, para qué sirven y que contienen, y un trozo del código del archivo pincipal que llama a los demás pero que muestra los cálculos y reglas:

Repositorio donde se encuentra el código completo:
https://github.com/MrQuadBit/Thanatology-Computational-Creativity

Descripción de los archivos:

README.md
Este mismo documento más las instrucciones de como ejecutar el programa

anger.txt
Etapa de Ira, la segunda etapa del duelo, contiene mensajes clasificados con este sentimiento.

bargaining.txt
Etapa de Negociación, la tercer etapa del duelo, contiene mensajes clasificados con este sentimiento.

denial.txt
Etapa de Negación, la primer etapa del duelo, contiene mensajes clasificados con este sentimiento.

farewells_messages.txt
Contiene mensajes de despedida y se usa como "Lista" para asignación de la variable [DESPEDIDA]

starting_messages.txt.txt
Contiene textos clasicos de apertura de mensajes de duelo y se usa como "Lista" para asignación de la variable [MENSAJE_INICAL]

support_messages.txt
Contiene mensajes de apoyo y se usa como "Lista" para asignación de la variable [APOYO]

main.py
Es el archivo principal que se ejecuta para obtener una narrativa usando todos los arcvivos anteriores y que contiene las reglas y cálculos para su generación:


def main():
	thanatology_message = ""
	thanatology_message += makeGreeting(input_data)
	thanatology_message += ", " + getRandomLineFromFile(FILE_STARTING)

	result = throughThePark([FILE_DENIAL, FILE_ANGER, FILE_BARGAINING])
	thanatology_message += ", " + result[0] + ", " + result[1]

	thanatology_message += ", " + getRandomLineFromFile(FILE_SUPPORT)
	thanatology_message += ", " + getRandomLineFromFile(FILE_FAREWELLS) + "."

	print(thanatology_message)