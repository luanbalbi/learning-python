segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dia = segundos // 86400
seg_sobra_dia = segundos % 86400

hora = seg_sobra_dia // 3600
seg_sobra_hora = seg_sobra_dia % 3600

minuto = seg_sobra_hora // 60
seg_final = seg_sobra_hora % 60

print(dia, "dias,", hora, "horas,", minuto, "minutos e", seg_final, "segundos.")
