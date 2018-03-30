
# coding: utf-8

# In[9]:


import numpy as np
from numpy import array
#pillow file import
from PIL import Image


# In[15]:


#load image
file = Image.open("test1.jpg")
#load image as multidimentional array
arr = array(file)
print ("image dimensions",file.size)
dim=file.size


# In[24]:


#WRITE YOUR CODE HERE

#part 1 crop image


col, row = [int(x) for x in input("enter pivot point coodinates as:col row").split()]
ratio=dim[0]/dim[1]
#print ("x/y col/row",ratio)
#print ("entered values  col",col,"row",row)

#edge case pivot point     
if col == 0 or row == 0 or col == dim[0] or row == dim[1]:
  #how much zoom?
  print("")
  
  
#general case pivot point  
else:  
  if dim[0]-col <= col:
    colmin = dim[0] - col
  else:
    colmin = col
  if dim[1]-row <= row:
    rowmin = dim[1] - row
  else: 
    rowmin = row
  #print ("colmin",colmin,"rowmin",rowmin)


if (colmin < rowmin):
  #print("case1")
  if ratio>1:
    #print("case11")
    q1 =row-int(colmin*ratio)
    q2 =row+int(colmin*ratio)
    if  q1 < 0:
      q2 = q2-q1 
      q1 = 0
    elif q2 > dim[1]:
      q1 =q1 + q2-dim[1]
      q2 =dim[1]
      newimg = arr[q1:q2,col-colmin:col+colmin,:]
  else:
    #print("case12")
    p1 =row-int(colmin/ratio)
    p2 =row+int(colmin/ratio)
    if  p1 < 0:
      p2 = p2-p1 
      p1 = 0
    elif p2 > dim[1]:
      p1 =p1 + p2-dim[1]
      p2 =dim[1]
    newimg = arr[p1:p2,col-colmin:col+colmin,:]
      
else:
  #print("case2")
  if ratio < 1:
    #print("case21")
    r1 = col-int(rowmin/ratio)
    r2 = col+int(rowmin/ratio)
    if  r1 < 0:
      r2 = r2 - r1
      r1 = 0
    elif r2 > dim[0]:
      r1 = r1 + r2-dim[0]
      r2 = dim[0]
    newimg = arr[row-rowmin:row+rowmin,r1:r2,:]
    
      
  else:
    #print("case22")
    s1 = col-int(rowmin/ratio)
    s2 = col+int(rowmin/ratio)
    if  s1 < 0:
      s2 = s2- s1
      s = 0
    elif s2 > dim[0]:
      s1 = s1 + s2-dim[0]
      s2 = dim[0]
    newimg = arr[row-rowmin:row+rowmin,col-int(rowmin*ratio):col+int(rowmin*ratio),:]
    
#print (newimg.shape)
#print (p1,p2)
#print(row+int(colmin/ratio))


# In[27]:


from matplotlib import pyplot as plt
print("cropped image with pivot point as centre and maintaining aspect ratio")
plt.imshow(newimg, interpolation='nearest')
plt.show()
print("original image")
plt.imshow(arr, interpolation='nearest')
plt.show()

# part 2 zoom cropped image