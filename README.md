# EntIntermediaRosenman
La página, programada en Python y Django para la parte lógica, usa HTML para los templates y código Jinja para aquellos que requieren código en Python en los mismos.
Se trata de una página en la que se pueden ingresar rashguards, kimonos y bermudas de Brazilian Jiu Jitsu, como así también buscar kimonos por criterio de marca. En la
función buscar kimonos, se ingresaron marcas como Atama, Maeda, Shoyoroll. Maeda tiene más de un modelo ingresado en la DB con el fin de demostrar funcionalidad a la 
hora de buscar (al buscar por marca Maeda, el buscador traerá todos los modelos Maeda existentes en la DB).
Las URLS del cada template se encuentran dentro de la App, y la URL de la App dentro del proyecto, por cuestiones de practicidad y prolijidad.
Las clases de los productos (bermudas, kimonos y rashguards) se encuentran en models, y toda la parte lógica de búsqueda y de agregar productos se encuentra en las views 
del proyecto. Las clases de todos los formularios se encuentran dentro del archivo forms.py, mientras que la lógica de los mismos podemos encontrarlas en las views.
Los templates de las funcionalidades buscar e ingresar heredan de un template padre a través de extends en cada uno de ellos.
Se creó un superuser con el fin de poder acceder a la DB pero sin la posibilidad de manipular el código.

