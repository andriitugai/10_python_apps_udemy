temperatures = [10, -0, -289, 100]

def c2f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        return c * 9/5 + 32

with open("converted.txt", "w") as results:
    for t in temperatures:
        results.write(str(c2f(t))+'\n')
