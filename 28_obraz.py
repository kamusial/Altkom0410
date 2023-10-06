import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('C:\\Users\\musiakam\\Desktop\\Firma\\6. Altkom\\4. Python analiza danych\\Altkom0410\\pliki\\images.jpg')

plt.imshow(image)
plt.show()
plt.imsave('zapisany.png', image, format = 'png')




