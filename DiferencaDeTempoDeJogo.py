x,dia1 = input().split()
dia1 = int(dia1)
hora1,minuto1,segundo1 = input().split(' : ')
hora1,minuto1,segundo1 = int(hora1),int(minuto1),int(segundo1)


palavra2,dia2= input().split()
dia2 = int(dia2)
hora2,minuto2,segundo2 = input().split(' : ')
hora2,minuto2,segundo2 = int(hora2),int(minuto2),int(segundo2)


if dia1 != dia2:
    tempo_dia1 = (hora1 * 3600) + (minuto1 * 60) + (segundo1)
    tempo_de_um_dia = 86400
    diferenca_1 = tempo_de_um_dia - tempo_dia1
    tempo_dia2 = (hora2 * 3600) + (minuto2 * 60) + (segundo2)
    diferenca_de_dias = (dia1 + 1) - (dia2)
    if diferenca_de_dias < 0:
        diferenca_de_dias = diferenca_de_dias * -1
    diferenca_total_em_segundos = (diferenca_de_dias * 86400) + (diferenca_1) + (tempo_dia2)
    quantidade_de_dias = diferenca_total_em_segundos // 86400
    diferenca_total_em_segundos = diferenca_total_em_segundos - (quantidade_de_dias * 86400)
    quantidade_de_horas = diferenca_total_em_segundos // 3600
    diferenca_total_em_segundos = diferenca_total_em_segundos - (quantidade_de_horas * 3600)
    quantidade_de_minutos = diferenca_total_em_segundos // 60
    diferenca_total_em_segundos = diferenca_total_em_segundos - (quantidade_de_minutos * 60)
    quantidade_de_segundos = diferenca_total_em_segundos
else:
    quantidade_de_dias = 0
    diferenca_inicio_fim = ((hora1 * 3600) + (minuto1 * 60) + (segundo1)) - ((hora2 * 3600) + (minuto2 * 60) + (segundo2))
    if diferenca_inicio_fim < 0:
        diferenca_inicio_fim = diferenca_inicio_fim * -1
    quantidade_de_horas = diferenca_inicio_fim // 3600
    diferenca_inicio_fim = diferenca_inicio_fim - (quantidade_de_horas * 3600)
    quantidade_de_minutos = diferenca_inicio_fim // 60
    diferenca_inicio_fim = diferenca_inicio_fim - (quantidade_de_minutos * 60)
    quantidade_de_segundos = diferenca_inicio_fim
    

print('{} dia(s)'.format(quantidade_de_dias))
print('{} hora(s)'.format(quantidade_de_horas))
print('{} minuto(s)'.format(quantidade_de_minutos))
print('{} segundo(s)'.format(quantidade_de_segundos))

