'''
    ############################
    #                                                    # 
    #  Redução de Coordenadas        #
    #                                                    # 
    ############################ 

    - Alpha deve ser escrito no formato hh:mm:ss, por exemplo: 10:08:22.31099
    - Delta deve ser escrito no formato gg:mm:ss, por exemplo: 11º 58' 01.9516''
    - Date deve ser escrito no formato DD:MM:AA, por exemplo: 2/7/2021
'''

import numpy as np
from ReductionFunctions.calculus import coordReduction

def main():
    run = True

    while run:
        alpha = delta = date = np.array([])

        while alpha.size == 0:
            try:
                alpha = np.array([float(input('Alpha hora: ')), float(input('Alpha minuto: ')), float(input('Alpha segundo: '))])
            except ValueError:
                print('Tipo numérico inválido\n')

        print(f'\nAlpha: {alpha[0]}:{alpha[1]}:{alpha[2]}\n')

        while delta.size == 0:
            try:
                delta = np.array([float(input('Delta grau: ')), float(input('Delta minuto: ')), float(input('Delta segundo: '))])
            except ValueError:
                print('Tipo numérico inválido\n')

        print(f'\nDelta: {delta[0]}º {delta[1]}\' {delta[2]}\'\'\n')

        while date.size == 0:
            try:
                date  = np.array([int(input('Dia: ')), int(input('Mês: ')), int(input('Ano: '))])
            except ValueError:
                print('Tipo numérico inválido\n')

        print(f'\nData: {date[0]}/{date[1]}/{date[2]}\n')

        coordReduction(alpha, delta, date)

        if input('\nDeseja usar a aplicação novamente? [S/N] ').upper() not in ['S', 'SIM', 'Y', 'YES']:
            run = False
        else:
            print()

if __name__ == '__main__':
    main()
