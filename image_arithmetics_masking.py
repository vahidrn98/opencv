#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np


# In[4]:


img1 = cv2.imread('esarmayeh.jpg')
img2 = cv2.imread('watchgray.png')


# In[5]:


rows,cols,channels = img1.shape
roi = img2[0:rows,0:cols]


# In[7]:


img1gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img1gray,220,255,cv2.THRESH_BINARY_INV)
#cv2.imshow('mask',mask)


# In[8]:


mask_inv = cv2.bitwise_not(mask)
#cv2.imshow('mask_inv',mask_inv)


# In[9]:


img2_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img1_fg = cv2.bitwise_and(img1,img1,mask=mask)
#cv2.imshow('pic_bg',img2_bg)
#cv2.imshow('logo_fg',img1_fg)


# In[10]:


dst = cv2.add(img2_bg,img1_fg)
img2[0:rows,0:cols] = dst
#cv2.imshow('dst',dst)

cv2.imshow('img2',img2)
# In[11]:


cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




