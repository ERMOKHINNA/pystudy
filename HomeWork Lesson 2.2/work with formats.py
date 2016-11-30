#coding: utf8
import json 
import csv

from pprint import pprint
import xml.etree.ElementTree as etree


#смотрим что есть в нашем файле, по тегам и по значению
tree = etree.parse('countries.xml')
#root = tree.getroot()
print ('File tags:\n')
for MainCharacter in tree.iter():
	if MainCharacter.text == 0 or MainCharacter.attrib != {}:
		print (MainCharacter.tag, ':', MainCharacter.attrib)
	if MainCharacter.attrib == {}:
		print (MainCharacter.tag, ':', MainCharacter.text)

schengen_countries = set()
sea_countries = set()
	
#преобразуем полученное в словарь словарей, чтобы работыли те же циклы, что и в лекции
country_list = {}	
for MainCharacter in tree.iter('country'):
	country_list[MainCharacter.attrib['name']] =  MainCharacter.attrib
for country_name, properties in country_list.items():
	del properties['name']
#	properties['sea'] = bool(properties['sea'])
#	properties['schengen'] = bool(properties['schengen'])
#смотрим что получилось
print ('\nNew view from xml')
pprint (country_list)

# работаем со словарем, как нам угодно
for country_name, properties in country_list.items():
	if properties['schengen'] == 'True':
		schengen_countries.add(country_name)
	if properties['sea'] == 'True':
		sea_countries.add(country_name)
		
print (sea_countries)
print (schengen_countries)

#готовим структуру для выводы в json
out_date = {} 
out_date[u'Входные данные'] = country_list

out_date[u'Страны с Морем'] = list(sea_countries)
out_date[u'Страны в Шенгене'] = list(sea_countries)


#выводим в json
with open('countriesW.json', 'w') as json_output:
	json.dump(out_date, json_output, indent = 2 )
