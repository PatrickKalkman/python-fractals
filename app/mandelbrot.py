import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def draw_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2])

def update(frame):
    ax.clear()
    ax.axis('off')

    # Focusing on the Seahorse Valley
    zoom = 0.05 * frame
    xmin, xmax = -0.74877 + zoom, -0.74872 - zoom
    ymin, ymax = 0.065053 + zoom, 0.065103 - zoom
    
    mandelbrot_image = draw_mandelbrot(xmin, xmax, ymin, ymax, img_width, img_height, max_iter)
    ax.imshow(mandelbrot_image, origin='lower', cmap='nipy_spectral', extent=(xmin, xmax, ymin, ymax))
    plt.savefig(f",/output/frame_{frame}.jpg", bbox_inches='tight')  # save each frame as a jpg

dpi = 80
img_width = dpi * 5
img_height = dpi * 5
max_iter = 256

fig, ax = plt.subplots(figsize=(img_width/dpi, img_height/dpi), dpi=dpi)
ani = FuncAnimation(fig, update, frames=range(50), interval=200)
ani.save('./output/mandelbrot_zoom.mp4', writer='ffmpeg')  # save animation as mp4
plt.axis('off')
plt.show()
