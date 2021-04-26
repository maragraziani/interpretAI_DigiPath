import matplotlib.pyplot as plt
import numpy as np


def show_inline(image, title=''):
    f, ax = plt.subplots(1, 1, figsize=(10,10))
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(image)
    ax.set_title(title)
    plt.show()


def get_patches(out, k, patch_size=36, random=False):
    image = out['image']
    graph = out['graph']

    if random:
        importance_scores = np.random.uniform(size=out['importance_scores'].size)
    else:
        importance_scores = out['importance_scores']

    image = np.pad(image,
                   ((patch_size, patch_size), (patch_size, patch_size), (0, 0)),
                   mode="constant",
                   constant_values=255)
    important_indices = (-importance_scores).argsort()[:k]
    important_centroids = graph.ndata['centroid'][important_indices, :].cpu().numpy().astype(int)

    patches = []
    for i in range(k):
        x, y = important_centroids[i] + patch_size
        patch = image[y - int(patch_size / 2): y + int(patch_size / 2),
                x - int(patch_size / 2): x + int(patch_size / 2),
                :]
        patches.append(patch)
    return patches


def plot_patches(patches, ncol=5, patch_size=36):
    nrow = len(patches) // ncol
    patches = np.stack(patches, axis=0)
    patches = np.reshape(patches, newshape=(nrow, ncol, patch_size, patch_size, 3))

    for i in range(nrow):
        for j in range(ncol):
            if j == 0:
                grid_ = patches[i, j]
            else:
                grid_ = np.hstack((grid_, patches[i, j]))
        if i == 0:
            grid = grid_
        else:
            grid = np.vstack((grid, grid_))

    show_inline(grid)