# import os
# if os.path.exists('demofile.txt'):
#     os.remove('demofile.txt')
# else:
#     print("File doesn't exist")

# from scipy import constants
import scipy
# print(constants.liter)
# print(scipy.__version__)
# print(constants.pi)
# print(dir(constants))
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# yplots = np.array([1, 2, 4, 5, 2, 8])
# yplot2 = np.array([2, 3, 0, 1, 0, 1])
#
# plt.plot(yplots)
# plt.plot(yplot2)
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# x1 = np.array([1,2,3,1,2])
# y1 = np.array([4,4,6,7,1])
# x2 = np.array([7,8,1,23,4])
# y2 = np.array([1,0,2,2,2])
#
#
# plt.plot(x1, y1, x2, y2)
#
#
# plt.title("X AND Y DATA COMPARISON")
# plt.xlabel("X AXIS ")
# plt.ylabel('Y AXIS')
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# x  = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# font1 = {'family':'serif','color':'blue','size':15}
# font2 = {'family':'serif','color':'darkred', 'size':15}
#
# plt.title("Sports watch data", fontdict=font1, loc = 'left')
# plt.xlabel("Average Pulse", fontdict=font2)
# plt.ylabel("Calorie Burnage", fontdict=font2)
#
# plt.plot(x, y)
# plt.grid()
# plt.show()
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.plot(x, y)
# plt.title('Sports Watch data')
# plt.xlabel("X LABEL")
# plt.ylabel("Y LABEL")
# plt.grid()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# #plot 1
# x1 = np.array([0, 1, 2, 3, 5])
# y1 = np.array([3, 4, 5, 1, 3])
# plt.subplot(1, 2, 1)
# plt.plot(x1, y1)
#
# #plot 2
# x2 = np.array([3, 1, 7, 4, 2])
# y2 = np.array([3, 6, 3, 1, 3])
#
# plt.subplot(1, 2, 2)
# plt.plot(x2, y2)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# #day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)
#
# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)

# plt.show()
import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

m = np.mean(speed)
print(m)

#NUMBER SHOULD BE SORTED BEFORE CALCULATING MEAN
Med = np.median(speed)
print(Med)

#mode
M = stats.mode(speed)
print("Mode of series of number is: ", M)

#standard deviation
std = np.std(speed)
print("Standard Deviation: ", std)




