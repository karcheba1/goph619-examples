import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay


def main():
    nx = 10
    ny = 15
    full_rand = False

    if full_rand:
        Xg = np.random.random((ny, nx))
        Yg = np.random.random((ny, nx))

    else:
        xmax = 1.0
        xg = np.linspace(0, xmax, nx)
        ymax = 1.0
        yg = np.linspace(0, ymax, ny)

        Xg, Yg = np.meshgrid(xg, yg)
        print(Xg.shape)

        Xg[1:-1, 1:-1] += np.random.normal(scale=0.01, size=(ny-2, nx-2))
        Yg[1:-1, 1:-1] += np.random.normal(scale=0.01, size=(ny-2, nx-2))

    Xg = Xg.flatten()
    Yg = Yg.flatten()
    print(Xg.shape)
    print(Yg.shape)

    points = np.vstack((Xg, Yg)).T
    print(points.shape)
    print()
    print(points[:10, :])
    print()

    tri = Delaunay(points)
    print(tri.simplices[:10, :])

    plt.figure(figsize=(6,6))
    plt.triplot(Xg, Yg, tri.simplices, label='simplices')
    hnod = plt.plot(Xg, Yg, 'ob', label='points')
    for k, (x, y) in enumerate(zip(Xg, Yg)):
        plt.text(x, y, k, fontsize=8)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.axis('equal')

    plt.show()


if __name__ == "__main__":
    main()
