#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import cv2


# In[2]:


img = cv2.imread('index.jpg',cv2.IMREAD_GRAYSCALE)#reading an image


# In[3]:


#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1


# In[4]:


cv2.imshow('image',img) #showing the image
cv2.waitKey(0) #waiting for a keyboard interupt
cv2.destroyAllWindows() #closing all tabs


# In[5]:


# showing image and drawing a simple line in matplotlib
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()


# In[6]:


cv2.imwrite('watchgray.png',img)


# In[ ]:




