


def c_to_f(c):
    if c < -273.15:
        return "Non sense"
    else:
        f = c*(9/5) + 32
        return f

temperatures = [10, -20, -289, 100]
a = []
for t in temperatures:
    if t < -273.15:
        pass
    else:
        a.append(c_to_f(t))

for num in a:
    with open('Temp.txt', 'a') as f:
        f.write(str(num) + '\n')
