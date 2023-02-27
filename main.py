from vpython import *
#GlowScript 2.9 VPython
#display(width=600,height=600,center=vector(6,0,0),background=color.white)
Mass=box(pos=vector(3,0,0),velocity=vector(0,0,0),size=vector(1,1,1),mass=1.0,color=color.blue)
caixa=box(pos=vector(0,3,0),velocity=Mass.velocity,size=vector(0.3,0.3,0.3),mass=2.0,color=color.green)
pivot=vector(-9,0,0)
spring=helix(pos=pivot,axis=Mass.pos-pivot,radius=0.4,constant=20,thickness=0.1,coils=30,color=color.red)
eq=vector(0,0,0)
Posi = text(pos=vector(3.5,0,0),text="|Alcance")

t=0
dt=0.01
di = vector(0,0.6,0)
while (True):
  if (t >= 3.99 and t <= 4.00):
    Mass.mass = Mass.mass + caixa.mass 
    Mass.velocity = Mass.mass*Mass.velocity/(Mass.mass + caixa.mass)
  rate(100)
  acc=(eq-Mass.pos)*(spring.constant/Mass.mass)
  Mass.velocity=Mass.velocity+acc*dt
  Mass.pos=Mass.pos+Mass.velocity*dt
  if (t > 5.00):
    caixa.velocity=Mass.velocity
    caixa.pos=Mass.pos+di
  spring.axis=Mass.pos-spring.pos
  t=t+dt
  print(t)