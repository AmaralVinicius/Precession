'''
    ############################
    #                                                    # 
    #  Redução de Coordenadas        #
    #                                                    # 
    ############################ 

    - Alpha deve ser escrito no formato hh:mm:ss, por exemplo: 10:08:22.31099
    - Delta deve ser escrito no formato gg:mm:ss, por exemplo: 11º 58' 01.9516"
    - Date deve ser escrito no formato DD:MM:AA, por exemplo: 2/7/2021
'''

import os
import platform
import numpy as np
from ReductionFunctions.calculus import coordReduction

def main():
    run = True

    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')

    print('''- Alpha deve ser escrito no formato hh:mm:ss, por exemplo: 10:08:22.31099
- Delta deve ser escrito no formato gg:mm:ss, por exemplo: 11º 58\' 01.9516"
- Date deve ser escrito no formato DD:MM:AA, por exemplo: 2/7/2021\n''')

    while run:
        alpha =  list()
        delta = list()
        date = list()

        while len(alpha) != 3:
            alphaInput = str(input('Alpha: ')).replace(' ', '')

            if alphaInput.count(':') == 2:
                try:
                    alpha.append(float(alphaInput[:alphaInput.find(':')]))
                    alphaInput = alphaInput[alphaInput.find(':') + 1:]
                    alpha.append(float(alphaInput[:alphaInput.find(':')]))
                    alpha.append(float(alphaInput[alphaInput.find(':') + 1:]))
                except ValueError:
                    print('Tipos numéricos inválidos\n')
                    alpha.clear()
            else:
                print('Formato inválido\n')

        print(f'\nAlpha: {alpha[0]}:{alpha[1]}:{alpha[2]}\n')

        while len(delta) != 3:
            deltaInput = str(input('Delta: ')).replace(' ', '').replace(':', '').replace('º', ':').replace('\'', ':').replace('"', ':')

            if deltaInput.count(':') == 3:
                try:
                    delta.append(float(deltaInput[:deltaInput.find(':')]))
                    deltaInput = deltaInput[deltaInput.find(':') + 1:]
                    delta.append(float(deltaInput[:deltaInput.find(':')]))
                    delta.append(float(deltaInput[deltaInput.find(':') + 1:-1]))
                except ValueError:
                    print('Tipos numéricos inválidos\n')
                    delta.clear()
            else:
                print('Formato inválido\n')

        print(f'\nDelta: {delta[0]}º {delta[1]}\' {delta[2]}"\n')

        while len(date) != 3:
            dateInput = str(input('Date: ')).replace(' ', '')

            if dateInput.count('/') == 2:
                try:
                    date.append(int(dateInput[:dateInput.find('/')]))
                    dateInput = dateInput[dateInput.find('/') + 1:]
                    date.append(int(dateInput[:dateInput.find('/')]))
                    date.append(int(dateInput[dateInput.find('/') + 1:]))
                except ValueError:
                    print('Tipos numéricos inválidos\n')
                    date.clear()
            else:
                print('Formato inválido\n')

        print(f'\nData: {date[0]}/{date[1]}/{date[2]}\n')

        coordReduction(alpha, delta, date)

        if input('\nDeseja usar a aplicação novamente? [S/N] ').upper() not in ['S', 'SIM', 'Y', 'YES']:
            run = False
        else:
            print()

if __name__ == '__main__':
    main()
