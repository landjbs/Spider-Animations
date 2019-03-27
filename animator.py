import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg'
import matplotlib.animation as animation


def move(x,y,theta,v,dt):
  return x + np.cos(theta)*dt, y+np.sin(theta)*dt

fig, ax = plt.subplots()
ax = plt.axis([0,8,-4,4])
redDot, = plt.plot([], [], 'ro')
label = plt.xlabel("a")
plt.gca().set_aspect('equal', adjustable='box')

dt = .010
v = 1
t_tot = 10
theta = np.pi/2
x_0 = 0
y_0 = 0
x_t = [x_0]
y_t = [y_0]

steps = t_tot/dt

for i in range(int(steps)):
  new_x, new_y = move(x_t[-1],y_t[-1],theta,v,dt)
  x_t.append(new_x)
  y_t.append(new_y)
  v += -dt*y_t[-1]
  theta = np.arctan(v)

def animate(step):
    i = int(step)
    redDot.set_data(x_t[i],y_t[i])
    return redDot,

# create animation using the animate() function
anim = animation.FuncAnimation(fig, animate, frames=range(int(steps)),
                                      interval=1, blit=True, repeat=True)
FFwriter = animation.FFMpegWriter(fps=50)

# Set up formatting for the movie files
anim.save('animation.mp4', writer=FFwriter)
