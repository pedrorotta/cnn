# **CNN_Topics(Tópicos de CNN)**
## **Redes neuronales convolucionales**

<p> En este repositorio presento mi investigación en redes convoluciones profundas de manera matemática y a nivel de programación. Está diseñado para que puedas aprender sobre el tema de manera sencilla y eficaz.</p>

<p>Cuestiones de derechos: Es totalmente libre, agradecería si usas algo de este material, el que puedas citar el repositorio en tu investigación o video. Sin más preambulos. Descripción.</p>

## Descripción 

<p>En este repositorio hay documentos python y clases enlazadas con google colab. Me tomé el tiempo de hacer una librería completamente funcional de redes convolucionales profundas de manera autodidacta, para poder enseñar a mis alumnos y que entiendan un poco mejor el concepto de convolución.</p> 

<p>Las librerías contienen algunas funciones interesantes, que ayudan a visualizar como se pueden ver las convoluciones. Motivo al usuario a poder usurla y comprobar la potencialidad de esta librería, además de lo didácticas que pueden resultar ser. No olvides que si tienes dudas, puedes encontrarme en </p>

<p><img alt="Ig logo" height="45px" src="https://i.pinimg.com/736x/c8/95/2d/c8952d6e421a83d298a219edee783167.jpg" align="left" hspace="10px" vspace="0px"></img><a href="https://www.instagram.com/pedrorotta_ime/?hl=es"><h3>IG : pedrorotta_ime</h3></a></p>

<p><img alt = "Fb logo" height = "45" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/YouTube_social_white_square_%282017%29.svg/245px-YouTube_social_white_square_%282017%29.svg.png" align = "left" hspace = "10px"></img><a href = "https://www.youtube.com/channel/UCm4OyfZ5sd2-QWxYVtMI0SA"><h3>Youtube : Pedro Rotta</h3></a></p>

## **Instalación**

<p><h4>Clonar el repositorio: </h4>
Para clonar el repositorio desde<a href = "https://colab.research.google.com/notebooks/intro.ipynb?hl=es#scrollTo=5fCEDCU_qrC0"> Colab </a>debes escribir la siguiente línea de código</p>

```
!git clone https://github.com/pedrorotta/cnn
```

<p> Importar sys para enviar el path a la lista de paths</p>

```
import sys
path = "/content/cnn"
sys.path.append(path)
```
<p> Importar la librería convolution</p>

```
import convolution
```

## **Ejemplos**

<div>
  <h3> Ejemplo 1</h3>
  <p>Esta librería es educativa. Algunas funciones que acá se colocan representan las partes de la operación de convolución: </p>
  <p><strong> Multiplicación de kernel : </strong> Es la multiplicación que se da entre un array de 2D pero solo en el espacio de una matriz de convolución m*m. Demuestra
    lo que sucede en cada transición del kernel</p>
  
  <p> Librerías necesarias </p>
  
  ```
  import PIL
  form PIL import Image
  import numpy as np
  
  ```
  <p> Operación </p>

  ```
  a  = np.array([[10,5,10,2],
                    [2,9, 5,7],
                    [1,7,5,9],
                    [5,3,1,3]])

  b = np.array([[1,0,-1],
                    [1,0,-1],
                    [1,0,-1]])

  convolution.MultiplicacionMatriz2D(a,b)
  ```
  
  <p>respuesta</p>
  
  ```
  >>> -24
  ```
  
</div>




<div>
  <h3> Ejemplo 2</h3>
  <p><strong> Multiplicación de Fila : </strong> Es la multiplicación que se da entre un array de 2D y un kernel convolucional pero solo en una fila del array</p>
  
  <p> Librerías necesarias </p>
  
  ```
  import PIL
  form PIL import Image
  import numpy as np
  
  ```
  <p> Operación </p>

  ```
  a  = np.array([[10,5,10,2],
                    [2,9, 5,7],
                    [1,7,5,9],
                    [5,3,1,3]])

  b = np.array([[1,0,-1],
                    [1,0,-1],
                    [1,0,-1]])

  convolution.ConvolucionEnUnaFila(a,b)
  ```
  
  <p>respuesta</p>
  
  ```
  >>> array([-7,  3])
  ```
  
</div>


<div>
  <h3> Ejemplo 3</h3>
  <p><strong> Convolución total : </strong> Es la operación de convolución que se da entre un array de 2D y un kernel convolucional y que retorna un array entero de 8 bits
  que permite luego, graficar una imagen convolucionada. En este ejemplo se usan 3 funciones : <strong> Convolucion2D </strong> y <strong> MatrizConvolucion.</strong></p>
  
  <p> Librerías necesarias </p>
  
  ```
  import PIL
  form PIL import Image
  import numpy as np
  
  ```
  ejemplo_array = np.asarray(Image.open("/content/cnn/images/perro1.jpg"))
  convolution.
  
  ```
  
  <p>respuesta</p>
  
  ```
  >>> array([-7,  3])
  ```
  
</div>

<p><img src = "https://github.com/pedrorotta/cnn/blob/main/images/perro1.jpg"></img></p>













