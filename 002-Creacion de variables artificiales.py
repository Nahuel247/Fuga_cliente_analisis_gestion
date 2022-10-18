
######################################################################
#      PROYECTO: DEFINIENDO ESTRATEGIAS DE ACCIÓN A PARTIR DEL
#                ANÁLISIS DE UN MODELO DE MACHINE LEARNING
#####################################################################

#######################################
# Autor: Nahuel Canelo
# Correo: nahuelcaneloaraya@gmail.com
#######################################


########################################
# IMPORTAMOS LAS LIBRERIAS DE INTERÉS
########################################

import warnings
warnings.filterwarnings('once')


#######################################
# CREACIÓN DE VARIABLES ARTIFICIALES
#######################################

# Construimos una base de datos que entrará en el modelo
data_artificial=data[["fuga","antiguedad","grande","pequeno"]]


# Truquito para crear las variables de forma automática: A continuación se crean de forma automática la programación
# de múltiples variables, están quedan guardadas en el objeto "variables" y pueden ser ejecutadas con exec o impresas
# para dejarlas explicitas

list_var=["monto_","satisfaccion_","canasta_","espera_","descongelados_"]
meses=[12,6,3]
funciones=["sum","mean","max","min"]
variables=[("data_artificial=data_artificial.assign("+var+funcion+str(n_meses)+"=data[['"+var+
            "' +str(i+1) for i in range("+str(n_meses)+")]]."+funcion+"(axis=1))")
           for var in list_var for n_meses in meses for funcion in funciones]

# ejecutamos las funciones
#for var in variables:
#    exec(var)

# dejamos explicitas las funciones creadas
print(variables)

# Monto total, promedio, mínimo y máximo en los últimos 12, 6 y 3 meses
data_artificial=data_artificial.assign(monto_sum12=data[['monto_' +str(i+1) for i in range(12)]].sum(axis=1))
data_artificial=data_artificial.assign(monto_mean12=data[['monto_' +str(i+1) for i in range(12)]].mean(axis=1))
data_artificial=data_artificial.assign(monto_max12=data[['monto_' +str(i+1) for i in range(12)]].max(axis=1))
data_artificial=data_artificial.assign(monto_min12=data[['monto_' +str(i+1) for i in range(12)]].min(axis=1))
data_artificial=data_artificial.assign(monto_sum6=data[['monto_' +str(i+1) for i in range(6)]].sum(axis=1))
data_artificial=data_artificial.assign(monto_mean6=data[['monto_' +str(i+1) for i in range(6)]].mean(axis=1))
data_artificial=data_artificial.assign(monto_max6=data[['monto_' +str(i+1) for i in range(6)]].max(axis=1))
data_artificial=data_artificial.assign(monto_min6=data[['monto_' +str(i+1) for i in range(6)]].min(axis=1))
data_artificial=data_artificial.assign(monto_sum3=data[['monto_' +str(i+1) for i in range(3)]].sum(axis=1))
data_artificial=data_artificial.assign(monto_mean3=data[['monto_' +str(i+1) for i in range(3)]].mean(axis=1))
data_artificial=data_artificial.assign(monto_max3=data[['monto_' +str(i+1) for i in range(3)]].max(axis=1))
data_artificial=data_artificial.assign(monto_min3=data[['monto_' +str(i+1) for i in range(3)]].min(axis=1))

# Satisfacción total, promedio, mínimo y máximo en los últimos 12, 6 y 3 meses
data_artificial=data_artificial.assign(satisfaccion_sum12=data[['satisfaccion_' +str(i+1) for i in range(12)]].sum(axis=1))
data_artificial=data_artificial.assign(satisfaccion_mean12=data[['satisfaccion_' +str(i+1) for i in range(12)]].mean(axis=1))
data_artificial=data_artificial.assign(satisfaccion_max12=data[['satisfaccion_' +str(i+1) for i in range(12)]].max(axis=1))
data_artificial=data_artificial.assign(satisfaccion_min12=data[['satisfaccion_' +str(i+1) for i in range(12)]].min(axis=1))
data_artificial=data_artificial.assign(satisfaccion_sum6=data[['satisfaccion_' +str(i+1) for i in range(6)]].sum(axis=1))
data_artificial=data_artificial.assign(satisfaccion_mean6=data[['satisfaccion_' +str(i+1) for i in range(6)]].mean(axis=1))
data_artificial=data_artificial.assign(satisfaccion_max6=data[['satisfaccion_' +str(i+1) for i in range(6)]].max(axis=1))
data_artificial=data_artificial.assign(satisfaccion_min6=data[['satisfaccion_' +str(i+1) for i in range(6)]].min(axis=1))
data_artificial=data_artificial.assign(satisfaccion_sum3=data[['satisfaccion_' +str(i+1) for i in range(3)]].sum(axis=1))
data_artificial=data_artificial.assign(satisfaccion_mean3=data[['satisfaccion_' +str(i+1) for i in range(3)]].mean(axis=1))
data_artificial=data_artificial.assign(satisfaccion_max3=data[['satisfaccion_' +str(i+1) for i in range(3)]].max(axis=1))
data_artificial=data_artificial.assign(satisfaccion_min3=data[['satisfaccion_' +str(i+1) for i in range(3)]].min(axis=1))

# Canasta total, promedio, mínimo y máximo en los últimos 12, 6 y 3 meses
data_artificial=data_artificial.assign(canasta_sum12=data[['canasta_' +str(i+1) for i in range(12)]].sum(axis=1))
data_artificial=data_artificial.assign(canasta_mean12=data[['canasta_' +str(i+1) for i in range(12)]].mean(axis=1))
data_artificial=data_artificial.assign(canasta_max12=data[['canasta_' +str(i+1) for i in range(12)]].max(axis=1))
data_artificial=data_artificial.assign(canasta_min12=data[['canasta_' +str(i+1) for i in range(12)]].min(axis=1))
data_artificial=data_artificial.assign(canasta_sum6=data[['canasta_' +str(i+1) for i in range(6)]].sum(axis=1))
data_artificial=data_artificial.assign(canasta_mean6=data[['canasta_' +str(i+1) for i in range(6)]].mean(axis=1))
data_artificial=data_artificial.assign(canasta_max6=data[['canasta_' +str(i+1) for i in range(6)]].max(axis=1))
data_artificial=data_artificial.assign(canasta_min6=data[['canasta_' +str(i+1) for i in range(6)]].min(axis=1))
data_artificial=data_artificial.assign(canasta_sum3=data[['canasta_' +str(i+1) for i in range(3)]].sum(axis=1))
data_artificial=data_artificial.assign(canasta_mean3=data[['canasta_' +str(i+1) for i in range(3)]].mean(axis=1))
data_artificial=data_artificial.assign(canasta_max3=data[['canasta_' +str(i+1) for i in range(3)]].max(axis=1))
data_artificial=data_artificial.assign(canasta_min3=data[['canasta_' +str(i+1) for i in range(3)]].min(axis=1))

# Tiempo de espera total, promedio, mínimo y máximo en los últimos 12, 6 y 3 meses
data_artificial=data_artificial.assign(espera_sum12=data[['espera_' +str(i+1) for i in range(12)]].sum(axis=1))
data_artificial=data_artificial.assign(espera_mean12=data[['espera_' +str(i+1) for i in range(12)]].mean(axis=1))
data_artificial=data_artificial.assign(espera_max12=data[['espera_' +str(i+1) for i in range(12)]].max(axis=1))
data_artificial=data_artificial.assign(espera_min12=data[['espera_' +str(i+1) for i in range(12)]].min(axis=1))
data_artificial=data_artificial.assign(espera_sum6=data[['espera_' +str(i+1) for i in range(6)]].sum(axis=1))
data_artificial=data_artificial.assign(espera_mean6=data[['espera_' +str(i+1) for i in range(6)]].mean(axis=1))
data_artificial=data_artificial.assign(espera_max6=data[['espera_' +str(i+1) for i in range(6)]].max(axis=1))
data_artificial=data_artificial.assign(espera_min6=data[['espera_' +str(i+1) for i in range(6)]].min(axis=1))
data_artificial=data_artificial.assign(espera_sum3=data[['espera_' +str(i+1) for i in range(3)]].sum(axis=1))
data_artificial=data_artificial.assign(espera_mean3=data[['espera_' +str(i+1) for i in range(3)]].mean(axis=1))
data_artificial=data_artificial.assign(espera_max3=data[['espera_' +str(i+1) for i in range(3)]].max(axis=1))
data_artificial=data_artificial.assign(espera_min3=data[['espera_' +str(i+1) for i in range(3)]].min(axis=1))

# Porcentaje total, promedio, mínimo y máximo en los últimos 12, 6 y 3 meses
data_artificial=data_artificial.assign(descongelados_sum12=data[['descongelados_' +str(i+1) for i in range(12)]].sum(axis=1))
data_artificial=data_artificial.assign(descongelados_mean12=data[['descongelados_' +str(i+1) for i in range(12)]].mean(axis=1))
data_artificial=data_artificial.assign(descongelados_max12=data[['descongelados_' +str(i+1) for i in range(12)]].max(axis=1))
data_artificial=data_artificial.assign(descongelados_min12=data[['descongelados_' +str(i+1) for i in range(12)]].min(axis=1))
data_artificial=data_artificial.assign(descongelados_sum6=data[['descongelados_' +str(i+1) for i in range(6)]].sum(axis=1))
data_artificial=data_artificial.assign(descongelados_mean6=data[['descongelados_' +str(i+1) for i in range(6)]].mean(axis=1))
data_artificial=data_artificial.assign(descongelados_max6=data[['descongelados_' +str(i+1) for i in range(6)]].max(axis=1))
data_artificial=data_artificial.assign(descongelados_min6=data[['descongelados_' +str(i+1) for i in range(6)]].min(axis=1))
data_artificial=data_artificial.assign(descongelados_sum3=data[['descongelados_' +str(i+1) for i in range(3)]].sum(axis=1))
data_artificial=data_artificial.assign(descongelados_mean3=data[['descongelados_' +str(i+1) for i in range(3)]].mean(axis=1))
data_artificial=data_artificial.assign(descongelados_max3=data[['descongelados_' +str(i+1) for i in range(3)]].max(axis=1))
data_artificial=data_artificial.assign(descongelados_min3=data[['descongelados_' +str(i+1) for i in range(3)]].min(axis=1))


# Dimensiones de data_artificial
data_artificial.shape

# Nombre de las columnas
data_artificial.columns


# Se observa que se han creado 51 variables artificiales