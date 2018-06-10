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


def parabola_different():
    a = []
    b = []

    for x in range(interval_start, interval_end, 1):
        #y = x ** 2 + 2 * x + 2

        y = x ** 1.8 + 40

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
xd, yd = parabola_different()
#plot_linear(5,4)

# fig = plt.figure()
# axes = fig.add_subplot(111)
plt.scatter(x, y)
x1,y1 = linear(10,-100)
#plt.plot((x1, x), (y1, y), 'r-', color='lightblue')
#plt.plot(x1,y1, color='red', linewidth=2)

#x2,y2 =  linear(33,-200) #fits well
#plt.plot(x2,y2, color='red', linewidth=2)

#plt.plot(x,y, color='lightblue', linewidth=2)
plt.plot(xt,yt, color='red', linewidth=2)
plt.plot(xd,yd, color='red', linewidth=2)

plt.show()

#linear that does not fit (10,-100)
#(33,-200) #fits well

print("Done")