nome = str(input('Qual o seu nome ?'))
print(f'Olá {nome}')

nm = nome.lower()

if nm == 'marcus':
    print('Que nome bonito')
elif nm == 'maria' or nm == 'fabiano' or nm == 'erica':
    print('O seu nome é bem normal')
elif nm in 'ana jorge eduardo irineu luiza gorge':
    print('Hora de por café')
else :
    print('Hora de porca fé')



