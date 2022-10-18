# Fuga de cliente (II parte: Análisis de la gestión)

La fuga de clientes es una de las principales problemáticas que puede enfrentar una empresa, tema que debe ser tratado con suma atención ya que ganar un cliente es 7 veces más difícil que retenerlo.\
\
En este repositorio encontraran distintas herramientas para definir estrategias de gestión a partir de los resultados de un modelo de Machine Learning, particularmente se determinará la gestión que se debe realizar para evitar la fuga de clientes. 

Particularmente se trabajo de la siguiente manera:
* Se utilizó el modelo RandomForest, una metodología que se basa en árboles de decisiones.
* Se construyó una base de datos con 1000 registros y una tasa de fuga del 15%.
* Los datos se construyeron a partir de supuestos plausibles sobre el comportamiento de los clientes en los 12 meses anteriores al mes de referencia, condicionado sobre si se fugará (fuga=1) o no (fuga=0) el próximo mes.
* Las variables históricas para los clientes que se fugaban seguían una distribución beta decreciente y los que no una distribución normal, en ambos casos se agregó ruido a través de una distribución uniforme y mezclas de tendencias.
* Las variables que se construyeron fueron: total de la compra mensual, porcentage del pedido descongelado, nivel de satisfacción, tiempo de espera, diversidad de la canasta, antigüedad del cliente, tipo de cliente y aquellas relacionadas con su variacion temporal.
* El modelo fue construido a través de una muestra de construcción, validado mediante cross-validation y testeado en una muestra out of sample.
* El desempeño del modelo fue estimado a través de indicadores como el gini y accuracy.
* Luego del entrenamiento se determinaron las estrategias de retención más importantes en base a los resultados del modelo.

# Resultados
A continuación, se presentan aquellos resultados más relevantes relacionados a la gestión de clientes con el fin de evitar su fuga.

# Tabla de eficiencia
Una vez entrenado un modelo es sumamente importante identificar grupos de mayor riesgo ya que serán estos registros los que serán gestionados para evitar su fuga, en los resultados que se presentan a continuación se muestra que un grupo candidato podrían ser aquellos registros que tienen una probabilidad de fuga que va entre 0.9 y 1.

[![Modelo-3.png](https://i.postimg.cc/8zpJCsPt/Modelo-3.png)](https://postimg.cc/ppSXGWjF)

# Importancia de las variables
A partir del modelo es posible identificar aquellas variables más importantes ahora la hora de clasificar clientes entre los que se van a fugar o no, lo cual es muy relevante a la hora de decidir las gestiones que se deben realizar.

[![Figure-1.png](https://i.postimg.cc/Pqjnzv0k/Figure-1.png)](https://postimg.cc/18JdyX9W)

De los resultados es posible observar que el “tiempo de espera”, el “porcentaje de productos que llegan descongelados” y la “satisfacción del cliente” están entre las variables más importantes. Lo otro que se puede observar que desde una mirada temporal la espera y el porcentaje de productos descongelados se vuelven relevante a largo plazo, en cambio la satisfacción tiene un efecto más importante en los últimos 3 meses. Se usarán las variables presentadas para definir distintas estrategias de gestión.

# Distribución de las variables más importantes según categoría

[![Figure-2.png](https://i.postimg.cc/QCZrS66S/Figure-2.png)](https://postimg.cc/bDgMwRf2)

De los resultados es posible observar que el “porcentaje  de producto descongelado en los últimos 6 meses” (descongelados_mean6) y “El tiempo de espera total en los últimos 6 meses” (espera_sum6) alcanza valores más altos entre personas que se fugan, lo cual tiene bastante sentido. Por otro lado, es posible observar que “la satisfacción en los últimos 3 meses” (satisfaccion_mean3) es mayor entre personas que no se fugan. Por lo cual indicadores bajos de satisfacción en los últimos 3 meses podría ser considerado una alerta de probable fuga por lo cual habría que realizar gestiones de retención.

# Desviación porcentual de cada variable en relación con el promedio
	
[![Figure-3.png](https://i.postimg.cc/BQq62gj4/Figure-3.png)](https://postimg.cc/py6RHKQ6)

De los resultados presentados, es posible observar que las personas que se fugan tienen un 50% más “tiempo de espera” “porcentaje de productos descongelados” que el promedio. Por lo cual una estrategia de retención podría ser el disminuir el tiempo de espera y mejorar los sistemas de enfriamientos para evitar que los productos lleguen descongelados.

# Gráfico de radar

[![Figure-4.png](https://i.postimg.cc/2y884k0r/Figure-4.png)](https://postimg.cc/DJHThTVM)

De la figura anterior, es posible observar que las variables más importantes tienden a tomar valores muy altos entre las personas que se fugan por lo cual deberían ser temas de interés.

# Conclusión

En base a los resultados presentados es posible observar que se debe desarrollar mejores prácticas que estén enfocadas en la disminución del tiempo de espera, como lo podría ser el desarrollar mejores planes de distribución o el uso de modelos de predicción de la demanda y que permitan tener un stock suficiente para responder de forma inmediata a las necesidades del cliente. Por otro lado, se recomienda el utilizar mejores sistemas de congelamiento para evitar que los productos pierdan su calidad. Finalmente, en base a los resultados, se sugiere el utilizar la satisfacción del cliente como un indicador que gatille distintos tipos de acciones como el incorporar descuentos a la compra.
