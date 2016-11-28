# Создание нового словаря
# new_dict = dict() # {}

#country_1 = {'name': 'Thailand, 'sea': True}
#country_2 = {'name': 'Hungary', 'sea': False}

# Подход 1 - списки
#countries = [
	#{'name': 'Thailand', 'sea': True, 'schengen': False, 'average_temperature': 30, 'currency_rate': 1.8},
	#{'name': 'Hungary', 'sea': False, 'schengen': True, 'average_temperature': 10, 'currency_rate': 0.3},
	#{'name': 'Germany', 'sea': True, 'schengen': True, 'average_temperature': 5, 'currency_rate': 80},
	#{'name': 'Japan', 'sea': True, 'schengen': False, 'average_temperature': 15, 'currency_rate': 0.61}
	#]
	
	
# Подход 2 - словарь
countries = {
	#'Cuba': data_about_Cuba,
	'Thailand': {'sea': True, 
				'schengen': False, 
				'average_temperature': 30, 
				'currency_rate': 1.8},
	'Hungary': {'sea': False, 
				'schengen': True, 
				'average_temperature': 10, 
				'currency_rate': 0.3},
	'Germany': {'sea': True, 
				'schengen': True, 
				'average_temperature': 5, 
				'currency_rate': 80},
	'Japan': {'sea': True, 
				'schengen': False, 
				'average_temperature': 15, 
				'currency_rate': 0.61},
	}
# Как заполнить словарь
# d = dict()
# d['name'] = 'Thailand'
	
# Множества - удобная структура для операций пересечения и объединения, поддерживает уникальность элементов	
# В отличие от списков, элементы множества не упорядочены
schengen_countries = set()
sea_countries = set()
	
for country_name, properties in countries.items():
	if properties['schengen']:
		schengen_countries.add(country_name)
	if properties['sea']:
		sea_countries.add(country_name)
		
		
print (sea_countries)
print (schengen_countries)
#print ('Страны в шенгене и с морем: ', schengen_countries & sea_countries)


# Форматирование вывода
#money_amount = 10000
#for country in countries:
#	currency_amount = money_amount / country['currency_rate']
#	print('У нас будет %.3f денег в местной валюте' % currency_amount)


sea_schengen_countries = schengen_countries & sea_countries

# Подход со списками словарей
#for country_name in sea_schengen_countries:
#	for country in countries:
#		if country['name'] == country_name:
#			print(country)
#			break

# Подход со словарем словарей
for country_name in sea_schengen_countries:
	print("Страны с морем", country_name, countries[country_name])


