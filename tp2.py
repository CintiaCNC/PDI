
**Cargar librerias**
import numpy as np
import imageio
import matplotlib.pyplot as plt

***Cargar imagen y Normalizar***
img = imageio.imread("image2.png")/255
plt.figure(1)
plt.imshow(img)


*** RGB a YIQ ***
yiq=np.zeros(img.shape) 
yiq[:,:,0]=0.229*img[:,:,0]+0.587*img[:,:,1]+0.114*img[:,:,2]
yiq[:,:,1]=0.595716*img[:,:,0]-0.274453*img[:,:,1]-0.321263*img[:,:,2]
yiq[:,:,2]=0.211456*img[:,:,0]-0.522591*img[:,:,1]+0.311135*img[:,:,2]
print(yiq)
plt.imshow(yiq)


***Y' = aY ***
*** a < 1   reduce la luminancia ***
a=0.9
yiq[:,:,0]=yiq[:,:,0]*a
plt.imshow(yiq)
print(yiq)


*** a > 1   aumenta la luminancia ***
a=1.5
yiq[:,:,0]=yiq[:,:,0]*a
plt.imshow(yiq)


*** I' = bI ***
*** Q' = bQ ***
*** b < 1  disminuye la saturacion ***
b=0.5
yiq[:,:,1]=yiq[:,:,1]*b
yiq[:,:,2]=yiq[:,:,2]*b
plt.imshow(yiq)

rgb1=np.zeros(yiq.shape)
rgb1[:,:,0]=yiq[:,:,0]+0.9663*yiq[:,:,1]+0.6210*yiq[:,:,2]
rgb1[:,:,1]=yiq[:,:,0]-0.2721*yiq[:,:,1]-0.6474*yiq[:,:,2]
rgb1[:,:,2]=yiq[:,:,0]-1.1070*yiq[:,:,1]+1.7046*yiq[:,:,2]
plt.imshow(rgb1)
print(rgb1)
