temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That's not a valid temperature"
    else:
        return c*9/5 + 32

with open('temperatures.txt', 'w') as file:
    for t in temperatures:
            temp = c_to_f(t)
            if type(temp) is not str:
                file.write(str(temp) + '\n')
print('Finalizado!')
