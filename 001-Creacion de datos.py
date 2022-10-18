
######################################################################
#      PROYECTO: DEFINIENDO ESTRATEGIAS DE ACCIÓN A PARTIR DEL
#                ANÁLISIS DE UN MODELO DE MACHINE LEARNING
#####################################################################

#######################################
# Autor: Nahuel Canelo
# Correo: nahuelcaneloaraya@gmail.com
#######################################

########################################
# IMPORTAMOS LAS LIBRERÍAS DE INTERÉS
########################################

# Activamos los gráficos
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.show()


import numpy as np
import pandas as pd
import uuid
import random
from scipy.stats import beta
from numpy.random import rand
import seaborn as sns
import matplotlib.pyplot as plt
from random import sample

seed=123
np.random.seed(seed) # fijamos la semilla
random.seed(seed)

#############################################
# CREAMOS LAS FUNCIONES QUE VAMOS A UTILIZAR
#############################################

# Construiremos una función que defina el comportamiento histórico del cliente según, si su marca de fuga es 0 o 1

# Rezagos: Número de meses anteriores al mes de referencia con información, 1 es el mes más cercano y 12 es el más lejano
# Valor_max: Es el valor máx alcanzado por la variable histórica que se desea construir

# Si el cliente se va a fugar, se construyen variables históricas a partir de una función beta decreciente
# Si el cliente no se va a fugar, se construyen variables históricas a partir de una función normal

# Creamos una función que defina la tendencia que tomará la variable histórica según si el cliente se fuga o no
def tendencia(x, rezagos,valor_max,ruido,ponderacion):
    ds=valor_max/10# ds
    azar=rand(1)
    if ruido==1:
        noise = np.random.uniform(-1, 1,rezagos)  # Se utilizará para agregar ruido
    else:
        noise =0
    if x==1: # Distribución beta (el cliente se fuga, "fuga" ==1)
        #a, b, inicio, fin = 10, 2, 0.1, 0.99  # párametros de la distribución beta
        a, b, inicio, fin = 5, 2, 0.1, 0.99  # párametros de la distribución beta
        x = np.linspace(beta.ppf(inicio, a, b), beta.ppf(fin, a, b), rezagos)
        x_valores = beta.pdf(x, a, b)
        x_valores = x_valores.copy() + (x_valores.copy() * noise)
        x_valores= (x_valores/np.max(x_valores)) * valor_max * azar
    else: # Distribución normal (el cliente NO se fuga, "fuga" ==0)
        x_valores = np.random.normal(valor_max*azar, ds * azar, rezagos)
        x_valores = x_valores + (x_valores * noise)
        x_valores = (x_valores/np.max(x_valores)) * valor_max * azar
        x_valores = x_valores.copy()*ponderacion
    return pd.Series(x_valores)

def registros_malos(porcentaje,n):
    n_ones=round((porcentaje/100)*n)
    ones = list(np.ones(n_ones))
    zeros=list(np.zeros(n-n_ones))
    vector=list(zeros + ones)
    return vector


###########################################################################
# CREAMOS LA BASE DE DATOS SEGÚN TENDENCIAS PLAUSIBLES ASOCIADAS A LA FUGA
###########################################################################

n=1000 # Número de clientes/registros que se van a crear
rezagos=12 # Número de meses anteriores al mes de referencia para los cuales se crearán variables

#Inicializamos un dataframe con los ID de cada cliente
#data=pd.DataFrame({"ID": [uuid.uuid4() for _ in range(n)]})
data=pd.DataFrame({"ID": list(range(n))})

# Agregamos una tasa de fuga del 15% (FUGA: 1: NO compra el siguiente mes, 0: SI lo hace)
vector=registros_malos(15,n)
data=data.assign(fuga=random.sample(vector,n))

# Monto mensual de compras de cada cliente
data_monto=data["fuga"].apply(tendencia,args=(rezagos, 500000,1,0.8))
data_monto.columns=np.array(["monto_"+str(i+1) for i in range(rezagos)])

# Agregamos ruido en tendencia
casos=sample(range(data[data["fuga"]==0].shape[0]),200)
indice=data[data["fuga"]==0].index[casos]
for i in indice:
    print(i)
    data_monto.iloc[i]=tendencia(1,12, 500000,1,1)

data=pd.concat([data,data_monto],axis=1)

# Indicador mensual de satisfacción de cada cliente
data_satisfaccion=data["fuga"].apply(tendencia,args=(rezagos, 6.6,1,1.5))
data_satisfaccion.columns=np.array(["satisfaccion_"+str(i+1) for i in range(rezagos)])
data=pd.concat([data,data_satisfaccion],axis=1)

# Número de productos distintos en la canasta mensual de cada cliente
data_canasta = data["fuga"].apply(tendencia, args=(rezagos, 12,1,1))
data_canasta.columns = np.array(["canasta_" + str(i + 1) for i in range(rezagos)])
data = pd.concat([data, data_canasta], axis=1)

# Horas entre la solicitud del pedido y la entrega para cada cliente
data_espera = data["fuga"].apply(tendencia, args=(rezagos,500,1,0.5))
data_espera.columns = np.array(["espera_" + str(i+1) for i in reversed(range(rezagos))])
data = pd.concat([data, data_espera], axis=1)

# Porcentaje del pedido que ha llegado descongelado
data_descongelados = data["fuga"].apply(tendencia, args=(rezagos, 30,1,0.5))
data_descongelados.columns = np.array(["descongelados_" + str(i+1) for i in reversed(range(rezagos))])
data = pd.concat([data, data_descongelados], axis=1)

# Antiguedad del cliente (meses)
data=data.assign(antiguedad= np.random.uniform(15,300,len(data)))

# Tipo de cliente
data=data.assign(grande=random.choices([1,0], cum_weights=(40,60),k = n))
data=data.assign(pequeno= lambda x: (x.grande==0) * 1)


##############################
# VISUALIZAMOS ALGUNOS CASOS
##############################

def visualizamos(variable, fuga, valor_max,seed):
    salida = []
    for i in [1, 0]:  # noise o no
        n = 0
        np.random.seed(seed)
        for j in [fuga]:  # se fuga==1, o no fuga==0
            for k in range(5):  # registros
                print(i, j, k)
                y = tendencia(j, rezagos, valor_max, i,1)
                ID = [str(n)] * rezagos
                x = np.array(["Rezago" + str(i + 1) for i in range(rezagos)])
                ruido = [i] * rezagos
                data = pd.DataFrame({"ID": ID, "variable": x, "valor": y, "fuga": j, "ruido": ruido})
                salida.append(data)
                n += 1

    salida = pd.concat(salida)
    salida = salida.reset_index()

    fig, axes = plt.subplots(2, 1)
    fig1=sns.lineplot(data=salida.query("ruido==0"), x="variable", y="valor", hue="ID", ax=axes[0])
    fig1.legend(loc='upper right')
    fig2=sns.lineplot(data=salida.query("ruido==1"), x="variable", y="valor", hue="ID", ax=axes[1])
    fig2.legend(loc='upper right')
    fig1.set_xlabel(""),fig1.set_ylabel(variable+" sin ruido"),fig2.set_xlabel(""),fig2.set_ylabel(variable+" con ruido")
    plt.suptitle("Variación histórica: "+ variable)
    axes[0].invert_xaxis()
    axes[1].invert_xaxis()
    plt.show()

#Distribución beta decreciente
visualizamos("Distribución beta", 1, 1,123)

#Distribución normal
visualizamos("Distribución normal", 0, 1,123)

# Consumo
visualizamos("Consumo", 1, 50000,123)
visualizamos("Consumo", 0, 50000,123)

# Satisfacción
visualizamos("satisfacción", 1, 100,124)
visualizamos("satisfacción", 0, 100,124)

# Canasta
visualizamos("canasta", 1,200,125)
visualizamos("canasta", 0,200,125)

# Tiempo de espera
visualizamos("espera", 1, 20,126)
visualizamos("espera", 0, 20,126)
