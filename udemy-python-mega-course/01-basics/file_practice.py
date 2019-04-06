file = open("fruits.txt")
frutas = file.read()
file.close()
frutas = frutas.splitlines()
for i in frutas:
	print(len(i))
