import numpy as np
import matplotlib.pyplot as plt
import os

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def draw_mandelbrot(xmin,xmax,ymin,ymax,width,height,max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1,r2,np.array([[mandelbrot(complex(r, i),max_iter) for r in r1] for i in r2]))

img_width = 800
img_height = 800
max_iter = 256

# Ensure the 'output' directory exists
os.makedirs('output', exist_ok=True)

for frame in range(50):
    zoom = 0.05 * frame
    xmin, xmax = -0.74877 + zoom, -0.74872 - zoom
    ymin, ymax = 0.065053 + zoom, 0.065103 - zoom
    dpi = 80
    fig = plt.figure(frame, dpi = dpi, figsize = (img_width/dpi, img_height/dpi), frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.], )
    ax.set_axis_off()
    fig.add_axes(ax)
    r1, r2, mandelbrot_image = draw_mandelbrot(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)
    ticks = np.arange(0,img_width,3*dpi)
    x_ticks = r1[ticks]
    plt.xticks(ticks, x_ticks)
    y_ticks = r2[ticks]
    plt.yticks(ticks, y_ticks)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(mandelbrot_image, origin='lower', cmap='nipy_spectral', extent=(xmin, xmax, ymin, ymax))
    plt.savefig(f'./output/frame_{frame}.jpg')
    plt.close()
