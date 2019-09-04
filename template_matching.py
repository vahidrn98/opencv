#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import cv2


# In[21]:


img = cv2.imread('main.jpg')
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('template.jpg')
#template = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,w,h = template.shape[::-1]
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.7
location = np.where(res>threshold)
for point in zip(*location[::-1]):
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(0,255,255),2)
cv2.imshow('image',img)


# In[ ]:




