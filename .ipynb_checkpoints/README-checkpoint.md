# Introducción

Durante muchos años he desarrollado mi carrera profesional usando R en casi un 90% en todas mis rutinas de trabajo. En los últimos años estoy viendo que Python se está convirtiendo en una herramienta complementaria muy potente en casi todas las áreas en las que se desarrolla R, pero con una visión más generalista. Python no está enfocado al campo de _Data Science_ pero tiene desarrolladas muy buenas herramientas.

![XKCD | A webcomic of romance, sarcasm, math, and language](https://imgs.xkcd.com/comics/python.png)

Por esa razón he empezado a investigar y descubrir el mundo de Python en _Data Science_ y aquí voy a ir dejando mis scripts de Python y mis _notebook_ de jupyter que voy a ir generando mientras pruebo diferentes paquetes y funciones.

Aunque tal vez me haya saltado un paso (afianzar mis conocimientos en Python), he empezado con dos libros de referencia en el análisis de datos con Python:

  * Python Data Science Handbook, Jake VanderPlas [amazon.es](https://www.amazon.es/Python-Data-Science-Handbook-Techniques/dp/1491912057/)
  
  * Python for data Analysis, Wes McKinney [amazon.es](https://www.amazon.es/Python-Data-Analysis-Wes-McKinney/dp/1491957662)
  
![Python Data Science Handbook](https://images-na.ssl-images-amazon.com/images/I/51MPp7yuZCL._SX389_BO1,204,203,200_.jpg "Python Data Science Handbook") ![Python for Data Analysis](https://images-na.ssl-images-amazon.com/images/I/515XdK-YtFL._SX379_BO1,204,203,200_.jpg "Python for Data Analysis")

No creo que estemos obligados a decidir entre R y Python, creo que son dos herramientas muy poderosas y que pueden encajar perfectamente en una rutina de trabajo robusta. En DataCamp hacen una buena comparación de los _pros_ y _contras_ de cada lenguaje, [Choosing R or Python for Data Analysis? An Infographic](https://www.datacamp.com/community/tutorials/r-or-python-for-data-analysis). 

Personalmente quiero centrarme en los siguientes paquetes de Python:

  * pandas
  * NumPy  
  * matplotlib/seaborn
  * Scikit-Learn
  * Otros paquetes y funciones interesantes con [SciPy](https://www.scipy.org/), [StatsModels](http://www.statsmodels.org/stable/), ...

Todo ello enfocando siempre los resultados a _Data Science_. **Pandas** y **NumPy** son las herramientas necesarias para trabajar con los datos, **matplotlib** y **seaborn** los paquetes para representar gráficamente los resultados y por último **Scikit-Learn** para el aprendizaje y modelización.

hay otros muchos paquetes interesantes en Python, como pueden ser [SciPy](https://www.scipy.org/ "SciPy is a Python-based ecosystem of open-source software for mathematics, science, and engineering") y [statsmodels](http://www.statsmodels.org/stable/ "statsmodels is a Python module that provides classes and functions for the estimation of many different statistical models")

También es interesante el proyecto [anaconda](https://www.anaconda.com/) que engloba todo un universo de software y paquetes en torno a Python y R. Gestiona los paquetes y las diferentes versiones así como GUIs para Python, [Spyder](https://spyder-ide.github.io/), y R, [RStudio](https://www.rstudio.com/).

## Pandas

![](https://github.com/pandas-dev/pandas/blob/master/web/pandas/static/img/pandas.svg)

Si estás interesado en trabajar con Pandas te sugiero leer los siguientes trabajos con Pandas y sus diferentes características y posibilidades (en inglés).

[Introduction to the Pandas](https://ai.plainenglish.io/introduction-to-the-pandas-library-a3a557c8d094?source=your_stories_page-------------------------------------)  
[Indexing-Selection-Filtering in Pandas](https://ai.plainenglish.io/indexing-selection-filtering-in-pandas-library-20d3fe4a6d71?source=your_stories_page-------------------------------------)  
[Important Methods in Pandas](https://ai.plainenglish.io/important-methods-in-pandas-2d4c774fcac9?source=your_stories_page-------------------------------------)  
[Arithmetic Operations in Pandas](https://ai.plainenglish.io/arithmetic-operations-in-pandas-7ef32226e41c?source=your_stories_page-------------------------------------)  
[Sorting and Ranking in Pandas](https://ai.plainenglish.io/sorting-and-ranking-in-pandas-701f99aa918e?source=your_stories_page-------------------------------------)  
[Summarizing And Computing Descriptive Statistics in Pandas](https://medium.com/nerd-for-tech/summarizing-and-computing-descriptive-statistics-in-pandas-7320a1fec371?source=your_stories_page-------------------------------------)  
[Reading and Writing Data in Pandas](https://ai.plainenglish.io/reading-and-writing-in-pandas-2d83dc538aff?source=your_stories_page-------------------------------------)  
[How to Fix Missing Data in Pandas](https://ai.plainenglish.io/missing-data-in-pandas-d41cbcec04e0?source=your_stories_page-------------------------------------)  
[Data Transformation in Pandas](https://ai.plainenglish.io/data-transformation-in-pandas-29b2b3c61b34?source=your_stories_page-------------------------------------)  
[Hierarchical Indexing in Pandas](https://levelup.gitconnected.com/hierarchical-indexing-in-pandas-94ff198b7f35?source=your_stories_page-------------------------------------)  
[Combining And Merging Datasets in Pandas](https://tirendazacademy.medium.com/combining-and-merging-datasets-in-pandas-8e71e11b76fa?source=your_stories_page-------------------------------------)  
[Reshaping And Pivoting in Pandas](https://tirendazacademy.medium.com/reshaping-and-pivoting-in-pandas-a41678e72d68?source=your_stories_page-------------------------------------)  
[Groupby in Pandas](https://medium.com/star-gazers/groupby-in-pandas-5df348e293f8?source=your_stories_page-------------------------------------)   
[Working With Groupby in Pandas](https://levelup.gitconnected.com/working-with-groupby-in-pandas-7e7823414537?source=your_stories_page-------------------------------------)  
[Pivot Tables in Pandas](https://levelup.gitconnected.com/pivot-tables-in-pandas-7b672e6d8f47?source=your_stories_page-------------------------------------)  
[Categorical Data in Pandas](https://tirendazacademy.medium.com/categorical-data-in-pandas-9eaaff71e6f3?source=your_stories_page-------------------------------------)  
[Working With Text Data in Pandas](https://tirendazacademy.medium.com/working-with-text-data-in-pandas-f78aa368e1a?source=your_stories_page-------------------------------------)  
[Practical Data Analysis with Pandas](https://levelup.gitconnected.com/practical-data-analysis-with-pandas-c40fbd2955fa?source=your_stories_page-------------------------------------)  
[Multiple Selecting-Filtering in Pandas](https://tirendazacademy.medium.com/multiple-selecting-filtering-in-pandas-68d710087a22?source=your_stories_page-------------------------------------)  




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

El módulo _pyplot_ proporciona una interfaz parecida a MATLAB, particularmente cuando se combina con IPython. Para el usuario avanzado, tiene un control total de los estilos de línea, propiedades de las fuentes, las propiedades de los ejes, etc., a través de una interfaz orientada a objetos o mediante un conjunto de funciones.

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

**NumPy** es una extensión de Python, que le agrega mayor soporte para vectores y matrices, constituyendo una biblioteca de funciones matemáticas de alto nivel para operar con esos vectores o matrices. El ancestro de **NumPy**, _Numeric_, fue creado originalmente por _Jim Hugunin_ con algunas contribuciones de otros desarrolladores. En 2005, _Travis Oliphant_ creó **NumPy** incorporando características de Numarray en **NumPy** con algunas modificaciones.

**NumPy** es el paquete fundamental para la informática científica con Python. Contiene, entre otras cosas:

  * Un poderoso objeto de matriz N-dimensional
  * Funciones sofisticadas (difusión)
  * Herramientas para integrar el código C / C ++ y Fortran
  * Álgebra lineal, transformada de Fourier y generación de números aleatorios

Además de sus múltiples usos científicos obvios, **NumPy** también se puede usar como un contenedor multidimensional eficiente de datos genéricos. Se pueden definir tipos de datos arbitrarios. Esto permite a **NumPy** integrarse de manera rápida y sin problemas con una amplia variedad de bases de datos.

**NumPy** está licenciado bajo la licencia BSD, lo que permite su reutilización con pocas restricciones.

## Scikit-Learn

![](http://i0.wp.com/blog.adeel.io/wp-content/uploads/2016/11/scikit-learn.png?fit=566%2C202)

**Scikit-Learn** (anteriormente scikits.learn) es una biblioteca de aprendizaje de máquina de software libre para el lenguaje de programación de Python. **Scikit-Learn** Cuenta con varios algoritmos de clasificación, regresión y agrupación, incluyendo máquinas de vectores de soporte (SVM), _random forest_, k-means y DBSCAN, ... y está diseñado para trabajar conjuntamente con las bibliotecas numéricas y científicas de Python, NumPy y SciPy.

El proyecto **Scikit-Learn** comenzó como _scikits.learn_, un proyecto _Google Summer of Code_ de _David Cournapeau_. Su nombre proviene de la idea de _SciKit_ (_SciPy Toolkit_), una extensión de terceros desarrollada por separado y distribuida para **SciPy**. La base de código original fue posteriormente reescrita por otros desarrolladores. En 2010, _Fabian Pedregosa_, _Gael Varoquaux_, _Alexandre Gramfort_ y _Vincent Michel_, todos de [INRIA](https://www.inria.fr/en/) tomaron el liderazgo del proyecto e hicieron su primer lanzamiento público el 1 de febrero de 2010. A partir de 2017, **Scikit-Learn** está en desarrollo activo.

## Otros paquetes y funciones interesantes
