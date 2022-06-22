import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(n, N_max, threshold):
    """ 
        constructs a mandelbrot fractal from an 'n x n' grid of points
        at 'N_max' iterations that cut off after evaluating beyond 'thershold'
    """
    
    # construct 'n x n' grid of points c
    x = np.linspace(-2,1,n)
    y = np.linspace(-1.5,1.5, n)
    xv, yv = np.meshgrid(x,y)
    c = xv + yv*1j
    
    # initialize mask with a default array of 1s i.e. "true"s
    mask = np.ones([n,n])
    
    # test each point c and return 0 i.e. "false"s to mask for points that diverge
    for row_index,line in enumerate(c):
        for column_index,ele in enumerate(line):
            z = complex(0,0)
            for j in range(N_max):
                z = z**2 + ele
                if abs(z) >= threshold:
                    mask[row_index,column_index] = 0
                    break
    
    # plot the mask
    plt.imshow(mask, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.show()
    return

mandelbrot(300,50,50)