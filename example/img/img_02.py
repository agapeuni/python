import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as pimg

img1 = pimg.open("lib/img/logo.png")

pixel1 = np.array(img1)
pixel1 = (1/255) * pixel1
pixelSize = np.array(pixel1.shape)
pixel2 = np.empty(pixelSize)

for i in range(pixelSize[0]):
    for j in range(pixelSize[1]):
        graypixel = (pixel1[i][j][0] + pixel1[i][j][1] + pixel1[i][j][2]) / 3
        pixel2[i, j] = (graypixel, graypixel, graypixel)

plt.subplot(141)
plt.imshow(pixel1)
plt.axis("off")
plt.title("Nagano Mei", fontsize=9)

plt.subplot(142)
plt.imshow(pixel2)
plt.axis("off")
plt.title("Gray Mei", fontsize=9)

plt.show()
