from time import sleep

time = 5
while time > 0.00000001:
    print('-------=------=-------=--------')
    sleep(time)
    print('=-=========-======-==========-=')
    sleep(time)
    if time > 1:
        time = time / 1.2
    elif time > 0.01:
        time = time / 1.02
    else:
        time = time / 1.001


