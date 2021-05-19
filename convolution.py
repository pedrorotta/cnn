# -*- coding: utf-8 -*-
"""Convolution.ipynb
 Creado por PedroRotta. 
"""

from PIL import Image
import numpy as np

def MultiplicacionMatriz2D(a,b):
  """
  Esta función solo tiene fines educativos. 

  Esta función define la multiplicación entre una matriz a (nxn) y una matriz de 
  convolución que es de la forma mxm haciendo una multiplicación solo para la dimensión de mxm
  en la matriz a. Esto es lo que sucede en cada punto en donde se aplica el kernel. 

  Parámetros: 

  a : matriz : Normalmente es una matriz que pertenece a un canal de la imágen. Normalmente puede tener 
  cualquier dimensión nxm :

  >>> a = np.array([[10,5,10,2],
                    [2,9, 5,7],
                    [1,7,5,9],
                    [5,3,1,3]])
  >>> import PIL
  >>> from PIL import Image
  >>> import numpy as np
  >>> file = "https://cnnespanol.cnn.com/wp-content/uploads/2020/07/200703104728-labrador-retriever-stock-super-169.jpg"
  >>> a = np.asarray(Image.open(file))[:,:,0

  b : matriz : Representa a la matriz de convolución. Puede ser de varios tipos. Algunas matrices
  están en este link : "https://es.wikipedia.org/wiki/N%C3%BAcleo_(procesamiento_digital_de_im%C3%A1genes)"
  >>> b = np.array([[1,0,-1],
                    [1,0,-1],
                    [1,0,-1]])
  Ejemplo
  >>> a = np.array([[10,5,10,2],
                    [2,9, 5,7],
                    [1,7,5,9],
                    [5,3,1,3]])
  >>> b = np.array([[1,0,-1],
                    [1,0,-1],
                    [1,0,-1]])
  >>> -24
  Retorna un flotante. 

  """
  x = 0
  y = 0
  sum = 0  
  for i in a:
    for j in i: #cada columna
      m = b[x,y] 
      sum = sum + (j*m)
      if y>= len(b)-1:
        y = len(b)-1
      else: 
        y = y+1
    if x>= len(b)-1:
      x = len(b) -1
    else:
      x = x+1
    y = 0
  return sum

def ConvolucionEnUnaFila(array,mat_conv):
  """
  Esta función tiene solo fines educativos.

  Esta función muestra la convolución que existe en una columna de la matriz. 
  Devuelve un vector con los resultados de la convolución en toda una columna

  array: matriz (cualquier array n*m que desees conocer una fila de dicha matriz)

  >>> array = np.array([[10,5,10,2],
                    [2,9, 5,7],
                    [1,7,5,9],
                    [5,3,1,3]])

  mat_conv : La matriz de convolucion. 

  """
  size_conv = np.shape(mat_conv) #tamaño de la mat_conv (3,3)
  fil_conv = size_conv[0]
  col_conv = size_conv[1]
  #primera sub matriz
  iter_col = 0
  iter_fila = 0
  array_col = []
  array_fila = []
  while iter_col <= (len(array[0])-col_conv): #iter_col = 0
      pixel = MultiplicacionMatriz2D(array[iter_fila:(fil_conv+iter_fila),iter_col:(col_conv+iter_col)],mat_conv)
      array_fila.append(pixel)
      iter_col = iter_col+1
  array_fila = np.array(array_fila)      
  return array_fila

def Convolucion2D(array,mat_conv):
  size_conv = np.shape(mat_conv) #tamaño de la mat_conv (3,3)
  fil_conv = size_conv[0]
  col_conv = size_conv[1]
  respuesta = []
  iter_fila = 0
  while iter_fila <= (len(array)-fil_conv):
    array_de_respuesta = ConvolucionEnUnaFila(array[iter_fila:len(mat_conv)+iter_fila,:],mat_conv)
    respuesta.append(array_de_respuesta)
    iter_fila = iter_fila+1
  respuesta = np.array(respuesta)
  return respuesta

def MatrizConvolucion(A,mat_conv):
  """
  Ejemplo : 
  B = np.array([[1,3,4,2],
              [2,3,1,1],
              [0,1,0,2],
              [1,0,3,1]])
mat_conv = np.array([[1,0],
                     [0,-1]])
MatrizConvolucion(B,mat_conv)
array([[0, 2, 3],
       [1, 3, 0],
       [0, 0, 0]], dtype=uint8)
  """

  Matriz_Base = Convolucion2D(A,mat_conv)
  array_mod_col = []
  array_mod_fila =[]
  for i in Matriz_Base: 
    for j in i:
      if j>=255:
        j = 255
        array_mod_col.append(j)
      elif j<=0 :
        j = 0
        array_mod_col.append(j)
      else:
        array_mod_col.append(j)
  Matriz_Convolution = np.array(array_mod_col)
  Matriz_Convolution = Matriz_Convolution.reshape(np.shape(Matriz_Base))
  Matriz_Convolution = Matriz_Convolution.astype(np.uint8)
  return Matriz_Convolution

def DeVectoraImagen(MatrizConvolucion):
  """
  Transforma un array a una imagen usando la librería Image de la librería PIL.
  
  >>> MatrizConvolucion : array (que es una imagen convolucionada normalmente.)
  
  """
  imagen_conv = Image.fromarray(MatrizConvolucion)
  return imagen_conv

