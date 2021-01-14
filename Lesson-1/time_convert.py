
sec = int(input('Введите количество секунд: '))

hour = str(sec // 3600)
min = (sec // 60) % 60
sec_out = sec % 60
if min < 10:
    min = '0' + str(min)
else:
    min = str(min)
if sec_out < 10:
    sec_out = '0' + str(sec_out)
else:
    sec_out = str(sec_out)
print(hour+':'+min+':'+sec_out)