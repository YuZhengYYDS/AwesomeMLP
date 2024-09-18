"""

Draw images based on the MNIST dataset.

"""

#### Libraries
# Standard library
import pickle
import sys

# My libraries

sys.path.insert(0, 'C:\GitHubProjects\AwesomeMLP\src')
import mnist_loader

# Third-party libraries
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def main():
    training_set, validation_set, test_set = mnist_loader.load_data()
    
    images = get_images(training_set)
    plot_mnist_digit(images[0])
    
 
def get_images(training_set):
    """ Return a list containing the images from the MNIST data
    set. Each image is represented as a 2-d numpy array."""
    flattened_images = training_set[0]
    return [np.reshape(f, (-1, 28)) for f in flattened_images]
 
    
def plot_mnist_digit(image):
    """ Plot a single MNIST image."""
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.matshow(image, cmap = matplotlib.cm.binary)
    plt.xticks(np.array([]))
    plt.yticks(np.array([]))
    plt.show()
    
#### Main
if __name__ == "__main__":
    main()