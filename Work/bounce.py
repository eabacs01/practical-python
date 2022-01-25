# bounce.py
#
# Exercise 1.5

height =100.0 #meters

for i in range(10):
    height = height * 0.6
    print(i+1, round(height, 4))
    