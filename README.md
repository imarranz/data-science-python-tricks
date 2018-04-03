# Introducción

Durante muchos años he desarrollado mi carrera profesional usando R en casi un 90% en todas mis rutinas de trabajo. En los últimos meses estoy viendo que Python se está convirtiendo en una herramienta complementaria muy potente en casi todas las áreas en las que se desarrolla R, pero con una visión más generalista. Python no está enfocado al campo de _Data Science_ pero tiene desarrolladas muy buenas herramientas.

![XKCD | A webcomic of romance, sarcasm, math, and language](https://imgs.xkcd.com/comics/python.png)

Por esa razón he empezado a investigar y descubrir el mundo de Python en _Data Science_ y aquí voy a ir dejando mis scripts de Python y mis _notebook_ de jupyter que voy a ir generando mientras pruebo diferentes paquetes y funciones.

Aunque tal vez me haya saltado un paso (afianzar mis conocimientos en Python), he empezado con dos libros de referencia en el análisis de datos con Python:

  * Python Data Science Handbook, Jake VanderPlas [amazon.es](https://www.amazon.es/Python-Data-Science-Handbook-Techniques/dp/1491912057/)
  
  * Python for data Analysis, Wes McKinney [amazon.es](https://www.amazon.es/Python-Data-Analysis-Wes-McKinney/dp/1491957662)
  
![Python Data Science Handbook](https://images-na.ssl-images-amazon.com/images/I/51MPp7yuZCL._SX389_BO1,204,203,200_.jpg "Python Data Science Handbook") ![Python for Data Analysis](https://images-na.ssl-images-amazon.com/images/I/515XdK-YtFL._SX379_BO1,204,203,200_.jpg "Python for Data Analysis")

No creo que estemos obligados a decidir entre R y Python, ni sea una guerra entre ambos lenguajes (en cualquier caso sólo beneficiaría a los _Data Scientists_), creo que son dos herramientas muy poderosas y que pueden encajar perfectamente en una rutina de trabajo robusta.

Personalmente quiero centrarme en los siguientes paquetes de Python:

  * pandas
  * NumPy  
  * matplotlib/seaborn
  * Scikit-Learn
  * Otros paquetes y funciones interesantes

Todo ello enfocando siempre los resultados a _Data Science_. **pandas** y **NumPy** son las herramientas necesarias para trabajar con los datos, **matplotlib** y **seaborn** los paquetes para representar gráficamente los resultados y por último **Scikit-Learn** para el aprendizaje y modelización.

hay otros muchos paquetes interesantes en Python, como pueden ser [SciPy](https://www.scipy.org/ "SciPy is a Python-based ecosystem of open-source software for mathematics, science, and engineering. In particular, these are some of the core packages") y [statsmodels](http://www.statsmodels.org/stable/ "statsmodels is a Python module that provides classes and functions for the estimation of many different statistical models")

## pandas

![](https://pandas.pydata.org/_static/pandas_logo.png)

### Python Data Analysis Library 

**pandas** es una biblioteca de código abierto con licencia BSD que proporciona estructuras de datos y herramientas de análisis de datos de alto rendimiento y fácil de usar para el lenguaje de programación Python que permite el análisis de datos a través de series y dataframes.

### Cheat Sheet

[pandas Cheat Sheet from DataCamp](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf)

### Otras fuentes

[A quick guide to the basics of the Python data analysis library Pandas, including code samples | DataCamp](https://www.datacamp.com/community/blog/python-pandas-cheat-sheet)  
[Rewrite your SQL queries in pandas](https://www.codementor.io/irinatruong/how-to-rewrite-your-sql-queries-in-pandas-and-more-hoa9l8z4k)

## matplotlib

![](https://matplotlib.org/_static/logo2.png)

**matplotlib** es una biblioteca de trazado 2D de Python que produce figuras de alta calidad de publicación en una gran variedad de formatos impresos y entornos interactivos en todas las plataformas. **matplotlib** se puede usar en scripts Python, shells Python e IPython, Jupyter notebook y servidores de aplicaciones web.

![](https://matplotlib.org/_images/sphx_glr_membrane_thumb.png) ![](https://matplotlib.org/_images/sphx_glr_histogram_thumb.png) ![](https://matplotlib.org/_images/sphx_glr_contour_thumb.png) ![](https://matplotlib.org/_images/sphx_glr_3D_thumb.png)

**matplotlib** intenta hacer que las cosas sean fáciles. Puede generar gráficos, histogramas, espectros de potencia, gráficos de barras, diagramas de errores, diagramas de dispersión, etc., con sólo unas pocas líneas de código. Para ver [algunos ejemplos](https://matplotlib.org/tutorials/introductory/sample_plots.html) y una amplia [galería](https://matplotlib.org/gallery/index.html).

El módulo _pyplot_ proporciona una interfaz parecida a MATLAB, particularmente cuando se combina con IPython. Para el usuario avanzado, tiene un control total de los estilos de línea, las propiedades de fuente, las propiedades de los ejes, etc., a través de una interfaz orientada a objetos o mediante un conjunto de funciones.

[matplotlib](https://matplotlib.org/)

### Cheat Sheet

[matplotlib Cheat Sheet from DataCamp](https://cdn-images-1.medium.com/max/2000/1*ykxp7OpgBXbRRHgjzSkeCA.png)

## seaborn

Según se definen ellos mismos, **seaborn** es una biblioteca de visualización de Python basada en **matplotlib**. Proporciona una interfaz de alto nivel para dibujar gráficos estadísticos atractivos.

[seaborn](https://seaborn.pydata.org/index.html)

### Otras fuentes y recursos

[Galería de ejemplos realizados con seaborn](https://seaborn.pydata.org/examples/index.html)

## NumPy

![](https://i1.wp.com/www.everythingai.co.in/wp-content/uploads/2018/03/285.jpg?resize=760%2C430)

**NumPy** es una extensión de Python, que le agrega mayor soporte para vectores y matrices, constituyendo una biblioteca de funciones matemáticas de alto nivel para operar con esos vectores o matrices. El ancestro de **NumPy**, Numeric, fue creado originalmente por _Jim Hugunin_ con algunas contribuciones de otros desarrolladores. En 2005, _Travis Oliphant_ creó **NumPy** incorporando características de Numarray en **NumPy** con algunas modificaciones.

**NumPy** es el paquete fundamental para la informática científica con Python. Contiene, entre otras cosas:

  * Un poderoso objeto de matriz N-dimensional
  * Funciones sofisticadas (difusión)
  * Herramientas para integrar el código C / C ++ y Fortran
  * Álgebra lineal, transformada de Fourier y generación de números aleatorios

Además de sus usos científicos obvios, **NumPy** también se puede usar como un contenedor multidimensional eficiente de datos genéricos. Se pueden definir tipos de datos arbitrarios. Esto permite a **NumPy** integrarse de manera rápida y sin problemas con una amplia variedad de bases de datos.

**NumPy** está licenciado bajo la licencia BSD, lo que permite su reutilización con pocas restricciones.

## Scikit-Learn

![](http://i0.wp.com/blog.adeel.io/wp-content/uploads/2016/11/scikit-learn.png?fit=566%2C202)

**Scikit-Learn** (anteriormente scikits.learn) es una biblioteca de aprendizaje de máquina de software libre para el lenguaje de programación de Python. **Scikit-Learn** Cuenta con varios algoritmos de clasificación, regresión y agrupación, incluyendo máquinas de vectores de soporte (SVM), _random forest_, k-means y DBSCAN, ... y está diseñado para trabajar conjuntamente con las bibliotecas numéricas y científicas de Python, NumPy y SciPy.

El proyecto **Scikit-Learn** comenzó como _scikits.learn_, un proyecto _Google Summer of Code_ de David Cournapeau. Su nombre proviene de la idea de "SciKit" (-SciPy Toolkit_), una extensión de terceros desarrollada por separado y distribuida para SciPy. La base de código original fue posteriormente reescrita por otros desarrolladores. En 2010, Fabian Pedregosa, Gael Varoquaux, Alexandre Gramfort y Vincent Michel, todos de [INRIA](https://www.inria.fr/en/) tomaron el liderazgo del proyecto e hicieron su primer lanzamiento público el 1 de febrero de 2010. A partir de 2017, **Scikit-Learn** está en desarrollo activo.

## Otras fuentes y recursos generales
