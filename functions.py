import numpy as np
import matplotlib.pyplot as pt

x=np.arange(0,19)
y=[(3*i*i)+4 for i in x]
pt.plot(x,y,color="red")