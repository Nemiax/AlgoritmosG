#El problema es... tengo una base de datos de vinos, y hay que hacer una red que clasifique.
#Para ello considero hacer una red con 14 entradas, 6 neuronas en la capa escondida y tres salidas, pues hay tres tipos de 
#vino a clasificar.
#Entonces cada neurona va a tener la forma x1w1+..+x12w13, wi pesos, xi atributos. Esto nos da un número, después ese número
#lo pasamos por la función de activación. 
#Hay que hacer eso con los 162 renglones. 
#Luego hay que medir la distancia de la clasificación que da la red con la clasificación que tienen los datos.
#Se seleccionan los de mejor rendimiento y esos pasan al genético....

#Creamos cromosomas en binario y encontrar una manera de convertirlos en flotantese.
#Un cormosoma es algo de la forma x1w1+...+x14w14 con wi los pesos y xi cada uno de los atributos.
#Crar valores de inicio en un rango muy pequeños.
#Evaluar la red, eso devuelve una clasificación.
#medir la distancia de la clasitidication que da la red con la clasificacin de los datos
#dependiendo del rendimiento del fitness selecciona los mejores cromosomas para la reproducción del genético
#vuelves a evaluar la red para que te de una clasificacion.""



import random
import csv
#imprime el renglón uno, no sirve ese renglón.
#with open('mlptrain.csv') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print("F1: {0},F2: {1}, F3: {2}, F4: {3},F5: {4},F6: {5},F7: {6}, F8: {7},F9: {8}, F10: {9}, F11: {10}, F12: {11}, F13: {12}".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))


for i in range(1000):
    print(random.random())

#hay que hacer los cromosomas. Un cromosoma es algo de la forma x1w1+...+x16w16 donde x1=x2=x3=1 por ser el umbral de x4 a x16
# son las características del vino. Voy a hacer eso a modo de lista (sugerencia del profesor). Entonces quiero
# una lista, con tres umbrales y 13 pesos
#Quiero l1 = [1,1,1,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13] con pi valores aleatorios chiquitos
lu=[1,1,1]
#print(lu1)
lpe1 = []
for i in range(0,12):
    x = random.random()
    lpe1.append(x)

#print(lpe1)
mergedlist = lu+lpe1
print(mergedlist) #Y esto saca el primer cromosoma :D ... pero necesito tantos cromosomas como renglones del cvs, i.e. 162
#Supongo que se crean con un ciclo

lpe2 = []
for i in range(0,12):
    x = random.random()
    lpe2.append(x)

#print(lpe1)
mergedlist = lu+lpe2
print(mergedlist)

lpe3 = []
for i in range(0,12):
    x = random.random()
    lpe3.append(x)

#print(lpe1)
mergedlist = lu+lpe3
print(mergedlist)

#pero ahora quiero muchas de esas... tantas como renglones. Son 162 renglones, así que imagino que debe haber un modo de hacer un ciclo que
#pueda generar este tipo de listas en vez de hacer 162 manualmente

#otro detalle que eventualmente saldrá es que el genético recibe cosas en binario, así que lo mejor sería que las listas estuvieran creadas
#en binario y operar en binario x.x

#Ahora la población... La población va a ser una lista conformada por todas estas listas
#Población=[[1,1,1,p1,....,p13],[],[],....,[]] con pi ya convertidos a binario.

#Los trece pesos se multiplican con los datos de la base, para tener algo "de la forma" x1w1+...+x16w16.

#
