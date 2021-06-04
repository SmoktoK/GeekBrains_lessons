from pyModbusTCP.client import ModbusClient
import time

SERVER_HOST = "192.168.24.233"
SERVER_PORT = 502
r = int(input('Введите начальный регистр: '))
tot = int(input('Введите количество регистров: '))
c = ModbusClient()

# Разкоментировать для дебага
# c.debug(True)

# # Определил хост сервера Modbus, порт
c.host(SERVER_HOST)
c.port(SERVER_PORT)
start_time = time.time()
with open("registr.txt", "w", encoding="utf8") as reg:
    reg.writelines(f"ip - {SERVER_HOST} регистры с {r} по {r + tot}: ")

while True:
    # Открываем или переподключаемся к TCP
    if not c.is_open():
        if not c.open():
            print("unable to connect to "+SERVER_HOST+":"+str(SERVER_PORT))

    # Читаем регистры если все есть конект (modbus function 0x03)
    if c.is_open():
        # Читаем диапазон регистров и сохраняем в переменную(начальный регистр, количество)
        regs = c.read_holding_registers(r, tot)
        # выводим на экран
        if regs:
            print(f"Регистры с {r} по {r + tot}: "+str(regs))
            with open("registr.txt", "a", encoding="utf8") as reg:
                reg.writelines(f"\n{str(regs)}")
            # Разкоментировать, если нужен только 1 опрос
            break
    # Задержка между опросами
    # time.sleep(1)
print("--- %s seconds ---" % (time.time() - start_time))