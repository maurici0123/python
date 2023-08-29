times = ( 'Botafogo','Flamengo','Palmeiras','Grêmio','Fluminense','RedBullBragantino','AthleticoPR','SãoPaulo','Cuiabá','Cruzeiro','Fortaleza','Internacional','Atlético-MG','Corinthians','Santos','Goiás','Bahia','Coritiba','América-MG','Vasco')

print(times[0:5])

print('\n', times[-4:len(times)])

print('\n', sorted(times))

for pos, time in enumerate(times):
    if time=='Corinthians':
        print(f'\na posição da Corinthians é a {pos+1}º')