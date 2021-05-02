import matplotlib.pyplot as plt
import math


def euler(l, theta0, time, interval):
    cte = -(9.8/l)
    theta = theta0
    omega = 0
    valuesY = [theta]
    valuesX = [0]
    for i in range(math.ceil(time//interval)):
        omega = omega + interval * cte * math.sin(theta)
        theta = theta + interval * omega
        valuesX.append(valuesX[-1]+interval)
        valuesY.append(theta)
    return valuesX, valuesY


X, Y = euler(1.2, 20, 10, 0.1)
plt.plot(X, Y)
plt.xlabel("time Interval")
plt.ylabel("theta angle")
plt.title("time versus angle plot")
plt.show()
