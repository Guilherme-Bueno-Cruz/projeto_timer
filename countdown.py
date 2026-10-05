import time


t = input('Digite o tempo em segundos: ')

if t.isdigit():
    t = int(t)
else:
    print('Por favor, digite um número válido.')
    quit()


while t > 0:
    minutes, seconds = divmod(t, 60)
    timer ="{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end='\r')
    time.sleep(1)
    t = t - 1

print('Tempo encerrado!')