print("\tTEXTO A BINARIO XD\n")
binario = []

texto = input("Ingresa texto: ")
for letra in texto:
	codigo_ascii = ord(letra)

	codigo_ascii -= 128
	if codigo_ascii < 0:
		codigo_ascii+=128
		binario.append("0")
	else:
		binario.append("1")

	codigo_ascii -=64
	if codigo_ascii < 0:
		binario.append("0")
		codigo_ascii+=64
	else:
		binario.append("1")

	codigo_ascii -= 32
	if codigo_ascii < 0:
		binario.append("0")
		codigo_ascii+=32
	else:
		binario.append("1")

	codigo_ascii -= 16
	if codigo_ascii < 0:
		binario.append("0")
		codigo_ascii+=16
	else:
		binario.append("1")

	codigo_ascii -= 8
	if codigo_ascii < 0:
		binario.append("0")
		codigo_ascii+=8
	else:
		binario.append("1")

	codigo_ascii -= 4
	if codigo_ascii < 0:
		binario.append("0")
		codigo_ascii+=4
	else:
		binario.append("1")

	codigo_ascii -= 2
	if codigo_ascii < 0:
		binario.append("0")
		codigo_ascii+=2
	else:
		binario.append("1")

	codigo_ascii -= 1
	if codigo_ascii < 0:
		binario.append("0")
		codigo_ascii += 1	
	else:
		binario.append("1")

	#print(letra, codigo_ascii, "".join(binario))
	
print("".join(binario))