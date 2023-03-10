# С постоением графиков будет сложнее.Для начала чтобы пользоваться библеотекой matplotlib, нужно её установить
# для установки matplotlib октрываешь консоли window и пишешь pip install matplotlib
# затем в самом начале своего кода пишешь from matplotlib import pyplot, важно чтобы прописал эту строку до того, как
# ты будешь писать код, который будет строить графики, так как если ты сделаешь наоборот, то вылезет ошибка
# импортируешь pyplot, через него будешь строить графики
from matplotlib import pyplot

# чтобы построить линейный график используй pyplot.plot(x, y), где x - лист с координатами x,
# y - лист с координатами y, а после этого пишешь pyplot.show() для того, чтобы отобразить график.
# Этот график синего цвета
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]
pyplot.plot(x, y)


# Можно не указывать лист с x, тогда просто указываешь лист с y, а исксы будут в диапозоне от 0 до размера листа 
# этот график оранжевого цвета
pyplot.plot([-1, -2, -3, -4])


# Чтобы нарисовать точку на графике надо использовать pyplot.scatter, с координатами также как и с линеный графиком
pyplot.scatter([1, 2, 3, 4], [1, 3, 4, 5])


#А вот пример, как создать параболу
y = []
for i in range(-9, 10):
    y.append(i**2)
pyplot.plot(y)
pyplot.show()
