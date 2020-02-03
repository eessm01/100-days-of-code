print ("Problema 3. Max factor primo")
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Función que determina si un número es primo
def esNumPrimo(n):
	esPrimo = True

	for i in range(2,n):
		n%i
		if ((n%i)==0):
			esPrimo=False
			break

	return esPrimo


print (esNumPrimo(16))
