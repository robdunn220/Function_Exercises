import matplotlib.pyplot as plot

def farenheit(celsius):
    return float((celsius * 1.8) + 32)

usr_celsius = float(raw_input("Enter a degree in celsius to convert: "))

xs = usr_celsius
ys = farenheit(usr_celsius)

plot.plot(xs, ys)
plot.show()
