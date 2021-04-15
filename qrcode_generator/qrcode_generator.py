import qrcode

url = input('Введите ссылку для генерации qrcode: ')
img = qrcode.make(url)
img.save('qrcode.png')
print('qrcode generate!')