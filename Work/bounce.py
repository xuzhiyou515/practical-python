# bounce.py
#
# Exercise 1.5
height = 100.0
for cnt in range(10):
    height *= 0.6
    print(cnt + 1, round(height, 4))