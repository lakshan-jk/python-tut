x = [1, 2, 3, 4, 5]

y = [100, 200, 300, 400, 500]

x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)

numerator = sum((x[i]-x_mean)*(y[i]-y_mean) for i in range(len(x)))
denominator = sum((x[i]-x_mean)**2 for i in range(len(x)))
m = numerator/denominator
# here we can use for loop to calculate the numerator and denominator
# denominator = 0
# for i in range(len(x)):
#     deviation += (x[i]-x_mean)**2
#     squared= deviation**2
#     denominator += squared

# numerator = 0
# for i in range(len(x)):
#     numerator += (x[i]-x_mean)*(y[i]-y_mean)

b = y_mean - m*x_mean
print(m, b)

DAY_TO_PREDICT = 6

PREDICTED_SALES = m*DAY_TO_PREDICT+b
print(f"The predicted sales for day {DAY_TO_PREDICT} is {PREDICTED_SALES}")
