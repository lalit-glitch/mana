from captcha.image import ImageCaptcha

#Captcha box resizing
img=ImageCaptcha(width=280,height=90)

# Inside words in captcha
data=img.generate("hello1956world")

# Captcha creation in png file
img.write("hello1956world",'demo.png')