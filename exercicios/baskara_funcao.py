import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input("Digite o primeiro valor:"))
    b = float(input("Digite o segundo valor:"))
    c = float(input("Digite o terceiro valor:"))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):

    resDelta = delta(a, b, c)
    
    if resDelta < 0:
	    print("esta equação não possui raízes reais")
    else: 
        if resDelta == 0:
	        x = -b / 2*a
	        print("a raiz desta equação é", x)
        else: 
	        x1 = (-b + math.sqrt(delta(a, b, c))) // (2*a)
	        x2 = (-b - math.sqrt(delta(a, b, c))) // (2*a)
	
	        if(x1 < x2):
		        print("as raízes da equação são",x1, "e", x2)
	        else:
		        print("as raízes da equação são",x2, "e", x1)
	
