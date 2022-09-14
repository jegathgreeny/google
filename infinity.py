from math import pi


def infinity(a, b, c):
    r = a
    ans = r * r
    while r > 0:
        r *= b
        ans += r * r
        r /= c
        if int(r) == 0:
            return ans * pi
        ans += r * r
    return ans * pi

area = infinity(5, 2, 5)
print(area)
