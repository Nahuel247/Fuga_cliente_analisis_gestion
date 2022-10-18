# Fuga de cliente (II parte: Análisis de la gestión)

La fuga de clientes es una de las principales problemáticas que puede enfrentar una empresa, tema que debe ser tratado con suma atención ya que ganar un cliente es 7 veces más difícil que retenerlo.\
\
En este repositorio encontraran todos los análisis correspondientes para la el desarrollo metodológico para identificar, a través de Machine Learning, aquellos clientes más propensos a fugarse en el próximo mes (información relevante para realizar retención),
Ademásen particular:

* Se utilizó el modelo RandomForest, una metodología que se basa en árboles de decisiones.
* Se construyó una base de datos con 1000 registros y una tasa de fuga del 15%.
* Los datos se construyeron a partir de supuestos plausibles sobre el comportamiento de los clientes en los 12 meses anteriores al mes de referencia, condicionado sobre si se fugará o no el próximo mes.
* Las variables históricas para los clientes que se fugaban seguían una distribución beta decreciente y los que no una distribución normal, en ambos casos se agregó ruido a través de una distribución uniforme.
* Las variables que se construyeron fueron: total de la compra mensual, porcentage del pedido descongelado, nivel de satisfacción, tiempo de espera, diversidad de la canasta, antigüedad del cliente, tipo de cliente y aquellas relacionadas con su variacion temporal.
* El modelo fue construido a través de una muestra de construcción, validado mediante cross-validation y testeado en una muestra out of sample.
* El desempeño del modelo fue estimado a través de indicadores como el gini y accuracy.

# Resultados
A continuación, se presentan aquellos resultados más relevantes relacionados al desarrollo metodológico

# Distribución beta decreciente (tendencia para clientes que se fugan)
Para construir las variables históricas de los clientes que se fugan, se utilizó una distribución beta decreciente, a la cual se le ajustó el valor máximo según la variable que se quería simular, para generar variabilidad se agregó ruido a la tendencia a través de una distribución uniforme. 

En la imagen que se muestra a continuación, es posible observar en la parte superior distintas series obtenidas de una distribución betas, y en la parte inferior, las mismas series una vez que se le ha agregado ruido.

[![Distribuci-n-beta.png](https://i.postimg.cc/QCLXTzCt/Distribuci-n-beta.png)](https://postimg.cc/LYTKdNzK)

# Distribución normal (tendencia para clientes que no se fugan)
Para construir las variables históricas de los clientes que NO se fugan, se utilizó una distribución normal, a la cual se le ajustó el valor máximo según la variable que se quería construir, para generar variabilidad se agregó ruido a la tendencia a través de una distribución uniforme. 

En la imagen que se muestra a continuación, es posible observar en la parte superior distintas series obtenidas de una distribución normal, y en la parte inferior, las mismas series una vez que se le ha agregado ruido.

[![Distribuci-n-normal.png](https://i.postimg.cc/m2sLZKKp/Distribuci-n-normal.png)](https://postimg.cc/14vhJ7mD)

# Comportamiento de compra de los clientes que se fugan 
A modo de ejemplo, a continuación, se muestra el comportamiento de compra de aquellos clientes que se fugan

[![Monto-total-de-la-compra-clientes-que-se-fugan.png](https://i.postimg.cc/ZRNm4LHh/Monto-total-de-la-compra-clientes-que-se-fugan.png)](https://postimg.cc/HcTRtXFS)

# Comportamiento de compra de los clientes que no se fugan
A modo de ejemplo, a continuación, se muestra el comportamiento de compra de aquellos clientes que NO se fugan

[![Monto-total-de-la-compra-clientes-que-NO-se-fugan.png](https://i.postimg.cc/Gm3bGGLk/Monto-total-de-la-compra-clientes-que-NO-se-fugan.png)](https://postimg.cc/BXyWG816)

# Cross validation
Para asegurar la robustez del modelo y su correcta parametrización, se optó por utilizar la metodología de croos-validation, que consiste en utilizar cierto porcentaje de la muestra de desarrollo para entrenar el modelo y el resto para probar el efecto que tiene los parámetros sobre el desempeño del modelo ante datos nuevos. Para este proyecto se dejaron fijos valores como la profundidad del árbol, el porcentaje de variables que se van a utilizar, etc. y se hizo variar el número de árboles del modelo (n_estimators), con el fin de obtener el conjunto de parámetros que asegurasen la robustez del modelo ante un conjunto de datos nuevos.

[![cross-validation.png](https://i.postimg.cc/4yrXpS3y/cross-validation.png)](https://postimg.cc/QKJL3S1Z)

# Accuracy Cross-validation vs Train
Del proceso anterior, se graficó el desempeño del modelo durante su construcción y durante cross validation, a lo largo de distintos números de árboles (n_estimators). En rojo se encuentra marcado el número de árboles óptimos para lograr el mejor desempeño durante cross-validation.

[![Accuracy-CV.png](https://i.postimg.cc/gJ2cph5z/Accuracy-CV.png)](https://postimg.cc/GB6nJ4dV)

# Tabla de eficiencia
[![Tabla-de-eficiencia.png](https://i.postimg.cc/RCQrdhbG/Tabla-de-eficiencia.png)](https://postimg.cc/DmZYyvhb)
# SIGUIENTES ETAPAS
* Desarrollo de un análisis al modelo y definición de gestiones
* Desarrollo de un Dashbord para su ejecución mensual
