
import matplotlib.pyplot as plt

def show_img(img, cmap='Greys_r'):
    fig, ax = plt.subplots(1, 1, dpi=200)
    ax.imshow(img, cmap=cmap)
    plt.axis('off')
    plt.show()


