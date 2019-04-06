def converter(c):
	return c*9/5 + 32
while(1  == 1):
	cel = float(input("Qual a temperatura em celsius?"))
	print(converter(cel))
	nov = input("Novamente? S/N")
	if nov == "N" or nov == "n":
		break
