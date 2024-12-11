import krpc
import matplotlib.pyplot as plt

# Подключение к серверу kRPC
conn = krpc.connect()

# Получение объекта космического корабля
vessel = conn.space_center.active_vessel

# Создание массивов для данных о времени и скорости
time_values = []
speed_values = []

# Получение скорости корабля на протяжении полета
while True:
    time = conn.space_center.ut
    speed = vessel.flight(vessel.orbit.body.reference_frame).speed
    time_values.append(time)
    speed_values.append(speed)
    print("Время: {}, Скорость корабля: {} м/с".format(time, speed))

    # Проверка условия завершения сбора данных
    altitude = vessel.flight().surface_altitude
    if altitude > 40000:  # Условие окончания программы
        break

# Построение графика скорости от времени
plt.plot(time_values, speed_values)
plt.title('Зависимость скорости от времени')
plt.xlabel('Время, s')
plt.ylabel('Скорость, m/s')
plt.show()
