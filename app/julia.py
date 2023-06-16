import numpy as np
import matplotlib.pyplot as plt


def julia_set(c, xlim, ylim, res, max_iter):
    x = np.linspace(xlim[0], xlim[1], res[0])
    y = np.linspace(ylim[0], ylim[1], res[1])
    X, Y = np.meshgrid(x, y)
    img = np.zeros(X.shape, dtype=float)
    Z = X + 1j * Y
    for i in range(max_iter):
        Z = Z**2 + c
        mask = np.abs(Z) < 1000
        img += mask
    img = img / img.max()
    return img


def main():
    c_values = [-0.7, -0.8j, -0.7+0.3j, 0.27, -0.4+0.6j, 0.37-0.1j]

    fig, axes = plt.subplots(2, 3, figsize=(12, 8))

    axes = axes.flatten()

    for ax, c in zip(axes, c_values):
        img = julia_set(c, xlim=(-1.5, 1.5), ylim=(-1.5, 1.5),
                        res=(500, 500), max_iter=200)
        ax.imshow(img, extent=(-1.5, 1.5, -1.5, 1.5), cmap='nipy_spectral')
        ax.axis('off')
        ax.set_facecolor('black')

    fig.patch.set_facecolor('black')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
