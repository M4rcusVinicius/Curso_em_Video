from time import sleep
print('Contagem regressiva : ', end='\n\n')
sleep(1)

for n in range(10, 0, -1):
    print('=' * 15, f' {n} ', '='*15)
    sleep(1)

print('\n======== Feliz ano novo !!! =======')