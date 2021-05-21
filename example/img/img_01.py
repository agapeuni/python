import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as pimg

img1 = pimg.open("lib/img/logo.png")

pixel = np.array(img1)
plt.subplot(141)
plt.imshow(pixel)
plt.axis("off")
plt.title("RGB")

# Red
pixel_R = pixel.copy()
pixel_R[:, :, (1, 2)] = 0
plt.subplot(142)
plt.imshow(pixel_R)
plt.axis("off")
plt.title("R(Red)")

# Green
pixel_G = pixel.copy()
pixel_G[:, :, (0, 2)] = 0
plt.subplot(143)
plt.imshow(pixel_G)
plt.axis("off")
plt.title("G(Green)")

# Blue
pixel_B = pixel.copy()
pixel_B[:, :, (0, 1)] = 0
plt.subplot(144)
plt.imshow(pixel_B)
plt.axis("off")
plt.title("B(Blue)")
plt.show()
