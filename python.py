def calculadorIMC(peso, altura):
    imc = peso / (altura*altura)
    return imc

peso = input('Insira seu peso: \t\n')
altura = input('Insira sua altura: \t\n ')
print("\n")
if peso != '' and altura != '':
    peso = float(peso)
    altura = float(altura)
    
    result = float(calculadorIMC(peso, altura))
    
    print(f"Seu iMC é de: {result:.2f}")
    
    if result < 18.5:
        print('Voce esta abaixo do peso ideal \n')
    elif result < 24.9:
        print('Voce esta no peso ideal \n ')
    if result < 18.5:
        print('Voce esta acima do peso ideal \n')
    if result < 18.5:
        print('Voce esta com obesidade nivel 1 \n')
    if result < 18.5:
        print('Voce esta com obesidade nivel 2 \n')
    if result < 18.5:
        print('Voce esta com obesidade nivel 3 \n')
        
else:
    print('Por favor insira os valores de peso e altura corretamente!!!')