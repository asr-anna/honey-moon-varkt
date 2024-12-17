


import krpc
import matplotlib.pyplot as plt

# Подключение к серверу kRPC
conn = krpc.connect()

# Получение объекта космического корабля
vessel = conn.space_center.active_vessel



# Создание массивов для данных о времени и скорости
x_values = []
y_values = []
time_values = []
speed_values = []
# Получение скорости корабля на протяжении полета
while True:
    a = ('(%.1f, %.1f, %.1f)' % vessel.position(vessel.orbit.body.reference_frame))
    a = a[1:-1]
    a = a.split(', ')
    x_v = float(a[0])-159784.7
    y_v = float(a[1])- (-1017.3)
    x_values.append(float(a[0])-159784.7)
    y_values.append(float(a[1])-(-1017.3))
    time = conn.space_center.ut
    speed = vessel.flight(vessel.orbit.body.reference_frame).speed
    time_values.append(time)
    speed_values.append(speed)
    print("Время: {}, Скорость корабля: {} м/с".format(x_v, y_v))
    

    # Проверка условия завершения сбора данных
    altitude = vessel.flight().surface_altitude
    if altitude > 650000:  # Условие окончания программы
        break

# Построение графика скорости от времени
plt.plot(x_values, y_values)
plt.title('координаты по x, y')
plt.xlabel('oX')
plt.ylabel('oY')
plt.show()
plt.plot(time_values, speed_values)
plt.title('Зависимость скорости от времени')
plt.xlabel('Время, s')
plt.ylabel('Скорость, m/s')
plt.show()
