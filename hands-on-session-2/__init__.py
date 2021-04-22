import matplotlib.pyplot as plt
%matplotlib inline
import mpld3
mpld3.enable_notebook()

def show_inline(image):
    f, ax = plt.subplots(1, 1, figsize=(10,10))
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(image)
    plt.show()