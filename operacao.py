try:
    def somar(numero1, numero2):
        return numero1 + numero2
    
    def subtrair(numero1, numero2):    
        return numero1- numero2
    
    def multiplicar(numero1, numero2):
        return numero1 * numero2
    
    def dividir(numero1, numero2):
        if numero2 == 0:

            raise ValueError("Não é possível dividir por zero.")
        return numero1 / numero2

except:
    print("operação não aceita")
