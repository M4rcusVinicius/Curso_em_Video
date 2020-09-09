s = input('Você é |H| Homem ou |M| Mulher : ').lower().strip()[0]
while s not in 'mh':
   s = input('Digite |H| para Homem ou |M| para Mulher : ').lower().strip()
if s == 'h':
    print('OK! Você foi registrado como um homem')
if s == 'm':
    print('OK! Você foi registrado como uma mulher')
