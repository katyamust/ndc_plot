import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

interval_start = 5
interval_end = 30

def parabola_dataset(randomized=False):
    a = []
    b = []
    # y=0
    # x=-50
    np.random.seed(seed=3)


    r = np.random.rand(interval_end - interval_start)
    r -= 0.5
    print(r)

    for x in range(interval_start, interval_end, 1):
        #y = x ** 2 + 2 * x + 2

        y = x ** 2 + 40 + r[x-interval_start] * 250 * randomized
        a.append(x)
        b.append(y)

    return a, b


def linear(Q1,Q2):
    a = []
    b = []

    for x in range(interval_start, interval_end, 1):
        #y = x ** 2 + 2 * x + 2
        y = x * Q1 + Q2
        a.append(x)
        b.append(y)

    return a, b

def plot_linear(Q1,Q2):

    x,y = linear(Q1,Q2)

    plt.plot(x,y, color='red', linewidth=2)
    #plt.plot(np.arange(X_test.__len__()), Y_pred, color='blue', linewidth=2)

    plt.xticks(())
    plt.yticks(())

    plt.show()
    return

x, y = parabola_dataset(randomized=True)
xt, yt = parabola_dataset(randomized=False)
#plot_linear(5,4)

# fig = plt.figure()
# axes = fig.add_subplot(111)
plt.scatter(x, y)
x1,y1 = linear(15,10)
plt.plot(x1,y1, color='red', linewidth=2)
plt.plot(x,y, color='lightblue', linewidth=2)
plt.plot(xt,yt, color='green', linewidth=2)

plt.show()

print("Done")