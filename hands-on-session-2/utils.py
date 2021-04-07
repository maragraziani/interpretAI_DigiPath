import matplotlib.pyplot as plt

def show_inline(image, title=''):
    f, ax = plt.subplots(1, 1, figsize=(10,10))
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(image)
    ax.set_title(title)
    plt.show()