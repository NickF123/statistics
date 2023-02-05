# Nicholas Finney 2023
# Free to use with attribution, not for production use

from math import sqrt
import matplotlib.pyplot as plt
from decimal import Decimal


def mean(data):
    return sum(data) / len(data)


def variance_s(data):  # s^2
    this_mean = mean(data)
    sum_differences = Decimal(0)
    for item in data:
        sum_differences += ((item - this_mean) ** 2)

    return sum_differences / (len(data) - 1)


def std_deviation_s(data):  # s^1/2
    return Decimal(sqrt(variance_s(data)))


def covariance_s(x, y):  # Sxy
    mean_x = mean(x)
    mean_y = mean(y)
    n = len(x)
    sums = Decimal(0)

    for i in range(n):
        sums += (x[i] - mean_x) * (y[i] - mean_y)

    return sums / (n - 1)


def covariance_coefficient_s(x, y):  # Rxy
    cov = covariance_s(x, y)
    dev_x = std_deviation_s(x)
    dev_y = std_deviation_s(y)

    return cov / (dev_x * dev_y)


def b_s(r, sx, sy): # b
    return r * (sy / sx)

def f(x, a, b): # returns y for y = bx + a
    return b * x + a


#Sample data
x1 = [Decimal(2.00), Decimal(3.00), Decimal(4.00), Decimal(5.00),
        Decimal(6.00), Decimal(7.00)]
y1 = [Decimal(8.00), Decimal(9.50), Decimal(10.00), Decimal(14.00),
        Decimal(15.00), Decimal(17.50)]


#print values
mean_x = mean(x1)
mean_y = mean(y1)
print(f"The mean of x is: {round(mean_x, 3)}")
print(f"The mean of y is: {round(mean_y, 3)}")

std_d_x = std_deviation_s(x1)
std_d_y = std_deviation_s(y1)
print(f"\nThe standard deviation of x is: {round(std_d_x, 3)}")
print(f"The standard deviation of y is: {round(std_d_y, 3)}")

cocof = covariance_coefficient_s(x1, y1)  # r
print(f"\nThe covariance coefficient (r) of x, y is: {round(cocof, 3)}")


#linear regression
b = b_s(cocof, std_d_x, std_d_y)
a = mean_y - (b * mean_x)

print(f"\nThe best fit line is \u0177 = {round(b, 3)}x + {round(a, 3)}")

plt.scatter(x1, y1) #show scatter plot

y2 = [f(x, a, b) for x in x1] #making a trendline for all values in the list x1
plt.plot(x1, y2) #add trendline to plot

plt.show()
