import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.signal import convolve2d

fig, ax = plt.subplots()
grid = np.random.choice(a=[0.0, 1.0], size = (200,200), p = [0.8, 0.2]) # init
img = ax.imshow(grid, cmap = "Accent", interpolation = "none")
kernel2 = [[1,1,1], [1,10,1], [1,1,1]] # conway convolution idea

def conway_f(x): # boolean operations to decide if alive or dead
    return 12==x or x==13 or x==3

conway_vectorized = np.vectorize(conway_f)#to apply it to each element of a matrix

def anim_frame(i, kernel):
    global grid
    grid2 = convolve2d(grid,kernel, mode = "same", boundary = "wrap")#2d convolution for conway
    fig.suptitle(str(i))#show the timestep
    grid = conway_vectorized(grid2) # applying function for alive and deadcells
    img.set_data(grid) # setting visual data

animation = FuncAnimation(fig=fig, func=anim_frame, fargs = (kernel2,), frames=500, interval=30, blit = False)
plt.show()