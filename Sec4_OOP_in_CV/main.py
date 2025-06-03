from ImageProcessor import ImageProcossor, display_image


# ImageProcossor(filename="./class.png").load().resize(300,300).save("class_processed.png").display()

proccessor = ImageProcossor(filename="./class.png")

img = proccessor.load()

display_image(img)


# proccessor.load().resize(300,300).save("class_processed.png").display()

# proccessor.load().resize(300,300).reset().save("class_processed.png").display()
