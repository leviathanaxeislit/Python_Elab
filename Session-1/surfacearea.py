"""
Selvan was playing with the a object of random size for stress relief. 
Selvan knows that the Length, Width, and Height of the object.  
But he would like to know the surface area of the object he is playing with. 
Can you help him in finding it?
Functional Description
Surface area of the Object = 2 x [width x length + length x height + height x width]
"""
l = int(input(''))
w = int(input(''))
h = int(input(''))
sa = (2*((w*l)+(l*h)+(h*w)))
print(sa)
