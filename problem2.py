def problem2(x1,y1,x2,y2,x3,y3):
 import numpy as np
 import math
 DEF=np.array([[x1,y1,1],[x2,y2,1],[x3,y3,1]])
 X=np.array([((-x1**2)+(-y1**2)),((-x2**2)+(-y2**2)),((-x3**2)+(-y3**2))])
 Unknowndef = np.linalg.solve(DEF,X)
 D=Unknowndef[0]
 E=Unknowndef[1]
 F=Unknowndef[2]
 h=-D/2
 k=-E/2
 r=math.sqrt(-F+((D**2/4))+((E**2))/4)
 print(Unknowndef)
 print(h)
 print(k)
 print(r)                    