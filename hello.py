#questo programma mi saluta e mi chiede il nome

print('Ciao mondo!')
print('Qual è il tuo nome?') #chiede il nome
mioNome = input()
print('E bello fare la tuA conoscenza', + mioNome)
print('La lunghezza del tuo nome è: ')
print(len(mioNome))
print('Quanti anni hai?') #chiede l'età
miaEta = input()
print('Avrai' + str(int(miaEta)+ 1) + 'anni fra un anno')