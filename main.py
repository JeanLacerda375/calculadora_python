from operacao import somar, subtrair ,multiplicar,dividir
def main():
        numero1= float(input("digite o primeiro numero: "))
        numero2= float(input("digite seu segundo numero: "))
        op = input("operação '+','-','*','/': ")
        resultado = None
        if op == '+':
            resultado = somar(numero1,numero2)
        elif op == '-' :
            resultado = subtrair(numero1,numero2)
        elif op == '*':
            resultado = multiplicar(numero1,numero2)
        elif op == '/':
            resultado = dividir(numero1,numero2)
        if not None:
            print("escolha não aceita")
        print(f"o resultado de {numero1} {op} {numero2} = {resultado}")

if __name__ == "__main__":
    main()
   
