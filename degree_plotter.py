import matplotlib.pyplot as plot

def farenheit(celsius):
    return (celsius * 1.8) + 32

xs = range(0, 30)
ys = []

for x in xs:
    ys.append(farenheit(x))

plot.plot(xs, ys)
plot.show()
