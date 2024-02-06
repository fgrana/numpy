import matplotlib.pyplot as plt
from skimage import io
import numpy as np

# here im checking what spells 🧙‍♂️ I can use with skimage
photo = io.imread('picture_sunset.jpg')
# print(type(photo))
# print(photo.shape)
# plt.imshow(photo)
# plt.show()  # shows normal
# why I got to use 8 AND 9 line to get the image? IDK, but works.
# plt.imshow(photo[::-1])
# plt.show()  # shows upside down
# plt.imshow(photo[:, ::-1])
# plt.show()  # horizontal flip! The sun now is in the right changing
# the hole composition of the picture. Now it feels like the picture is
# making us go backwards.

# Using the classic method for selecting a slice of an array we can
# get only the image of our star
# plt.imshow(photo[50:150, 150:280])
# plt.show()  # not quite the sun. Actually not at all. If you are
# disappointed about this you can email me at federico******@gmail.com
# I let you figure out the missing parts ;)

# we got this func call sin. Im not quite the sheep of god but
# im hesitant to "call" that func xd

print(np.sin(photo))
# "The sine of each element of x. This is a scalar if x is a scalar." -The docu
# No idea, cool, lets keep moving

# Okay, we got a BUNCH of funcs some look cool and some do not so much. Should we check
# them one by one. ...yeh? or only the cool ones...? let's just get on with it...
# np. [sum, prod, mean, std, var, min, max, argmin, argmax]

# Okay, this looks a bit boring but let's just go through it, it will be finished in no time.
# 加油!

# np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32)
# returns: 1
# it just sums everything in the array

# a = np.array([[1., 2.], [3., 4.]])
# np.prod(a)
# 24.0
# yea, prod does prod. Mistery solved.

# "The arithmetic mean is the sum of the elements along the axis divided by the number of elements."
# -the Docs
# a = np.array([[1, 2], [3, 4]])
# np.mean(a)
# 2.5

# std
# I know a guy Freddy who hated this func.
#
# The standard deviation is the square root of the average of the squared deviations from the mean,
# i.e., std = sqrt(mean(x)), where x = abs(a - a.mean())**2.
# So... math. I can confidently say it does some kind of mathematical thingy.
# Good to know I will have to google this... ...in duckduckgo ;).(just kidding! I use Google services for every-thing)
#
# var
# Okay, var. What's var?
# "Returns the variance of the array elements, a measure of the spread of a distribution.
# The variance is computed for the flattened array by default, otherwise over the specified axis."
#                       - the Docs
# So, is this suppose to explain something?
# https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var
#
# min, max
# This guys return the lower and higher number in the array
#
# argmin Returns the indices of the minimum values along an axis.
# a = np.arange(6).reshape(2,3) + 10
# a
# array([[10, 11, 12],
#        [13, 14, 15]])
# np.argmin(a)
# returns: 0
# argmax Returns the indices of the maximum values along an axis.
#
# z = np,array([1, 2, 3, 4, 5])
# and
# z < 3
# returns an array
# array([True, True, False, False, False])
#
# z[z > 3]
# returns:
# array([4, 5])

# photo_masked = np.where(photo > 100, 255, 0)
# plt.imshow(photo_masked)
# plt.show()
#
# nice saturated image. I don't know quite why it did that. This also should have further investigations
#
# a_array = np.array([1,2,3,4,5])
# a_array = np.array([6,7,8,9,10])
# okey, as we all know we can do this tricks when we have 2 arrays with the same shape
# a_array + b_array
# a_array + 30
# a_array * b_array
# a_array * 10
#
# Now comes the cursed ones
# a_array @ b_array
# plt.imshow(photo[:, :, 0].T)
# plt.show()
# Yep, that was cool.
#
# And finally. np.sort(np.array([3, 2, 1]) returns: [1, 2, 3]
