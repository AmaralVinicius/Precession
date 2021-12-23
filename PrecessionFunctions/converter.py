import numpy as np

# Função que converte um ângulo para graus
def degrees(angle):
    return angle * 180 / np.pi

# Função que converte um ângulo para radianos
def radians(angle):
    return angle * np.pi / 180

# Função que converte um tempo do tipo HH:MM:SS para graus
def time2degrees(time):
    M = np.array([1, 1/60, 1/3600])
    return np.sum(np.dot(M, time)) * 15

# Função que converte graus do tipo DD:MM:SS para graus
def degreeReduction(degrees):
    M = np.array([1, 1/60, 1/3600])
    return np.sum(np.dot(M, degrees))

# Função que converte horas ou graus no formato hh:mm:ss ou gg:mm:ss
def reformat(value):
    r, v0 = np.modf(value)
    r, v1 = np.modf(r * 60)
    v2 = r * 60
    return v0, v1, v2

# Função que converte uma data do tipo DD:MM:YYYY para data juliana
# A 1a função: Fliegel and Van Flandern (1968)
# A 2a função: Doggett (Calendars) - in Seidelmann 1992
def julianDate(day, month, year):
#    return 367 * year - (7 * (year + (month + 9) / 12)) / 4 - \
#           (3 * (year + (month - 9) / 7) / 100 + 1) / 4 + \
#           275 * month / 9 + day + 1721029
           
     return 367 * year - (7 * (year + 5001 + (month - 9) / 7)) / 4 + \
            (275 * month) / 9 + day + 1729777
