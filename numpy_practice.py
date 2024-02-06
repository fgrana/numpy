import matplotlib.pyplot as plt
import numpy as np

# This is a test of the many ways I can use numpy

# we can create an empty array useing:

array_with_zeros = np.zeros(3)
# this indeed(how I love the word indeed) create an array full of zeros. 3 to be exact
# lets see it

print(array_with_zeros.shape)
# it prints (3,0) . Wonderful! What else can we do with this?

array_10_1 = np.zeros(10)

# But wait, this isn't correct! the variable is call array_10_1 but let's look at his shape
# and see if the name of the variable and the shape match :O

print(array_10_1)
# it prints "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]". Cool shape! But is not what we actually want :(
# lets change his shape to match the variable name! How? Using .shape

array_10_1.shape = (10, 1)
# did we do it? (LOL I know we did, im literally watching the tutorial in front of me but
# let's check it in the terminal as if we don't got a clue xd)

print(array_10_1)
# aaaaaand....
# [[0.]
# [0.]
# [0.]
# [0.]
# [0.]
# [0.]
# [0.]
# [0.]
# [0.]
# [0.]]

# cool, feels like I'm not writing an array in py by hand anymore. I have seen the sofisticated ways
# of numpy and can't go back to my old rudimentary ways. But if I'm not going back better know all
# of it. Lets make sure we dont hardcode an array never ever ever ever EVER! ò_ó again.
# what else we have?

z = np.ones(10)
print(z)
# that was obvious
# x = np.nine(10) this dont work, what a bumer u.u

x = np.empty(3)
print(x)
# [1. 1. 1.] men, what? I said empty, EMPTY! Why all thouse ones?
#
# "empty, unlike zeros, does not set the array values to zero, and
# may therefore be marginally faster. On the other hand, it requires
# the user to manually set all the values in the array, and should
# be used with caution."
#                                       -the documentation ;)
# "yea, i bet"
#           -angry python user

# okey so.... empty is not quite empty but is faster. Good to know.
# What else there is?
# Well, there is this cool trick...
y = np.linspace(2, 10, 5)
print(y)
# [ 2.  4.  6.  8. 10.]

# Do computer loop in an infinite array of sheep for sleep?
# *me: lit(literally) stoping work to make a meme about it but it was lit 🔥*

# also, here it is the hardcoded method if anyone was asking
a_list = [1, 2, 3, 4, 5, 6, 7]
zxy = np.array(a_list)
# boooorrring....
# What else is new?

# a py thingy is that we can check types
print(type(zxy[0]))
