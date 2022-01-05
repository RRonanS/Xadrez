def resizeimg(nome):
    from PIL import Image
    dic = 'arquivos/'
    imgage = Image.open(dic+nome)
    img2 = imgage.resize((60, 60))
    img2.save(nome)
resizeimg('blackking.png')