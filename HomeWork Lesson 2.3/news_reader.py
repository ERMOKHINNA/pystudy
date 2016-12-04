
import json 
import csv
import codecs

from pprint import pprint
import xml.etree.ElementTree as etree

# берем данные из xml
def get_data_from_xml(filename, code):
	parser = etree.XMLParser(encoding = code) #iso8859_5 )#koi8_r')
	
	tree = etree.parse(filename, parser=parser)
	return tree
# берем все значения из указанного тега
def get_content_from_tag(tag, filename, code):
	words_list = []
	for MainCharacter in get_data_from_xml(filename, code).iter(tag):
		words_list.append(MainCharacter.text.split())
	return (words_list)
# ищем повторяющиеся слова, заданной длины и исключая слова разметки
def find_repeated_words(tag, filename, code, word_len, word_exception):
	repeated_words = {}
	for article in get_content_from_tag(tag, filename, code):
		for word in article:
			count = 0
			if len(word) >= word_len and word[len(word_exception)] != word_exception:
				for next_article in get_content_from_tag(tag, filename, code):
					for next_word in next_article:
						if word == next_word:
							count += 1
				repeated_words[word] = count
	return (repeated_words)
# ранжируем слова по частоте использованиея
def range_repeated_words(repeated_words):
	ranged_repeated_words = []
	for v in sorted(repeated_words.values(), reverse = True):
		for k in list(repeated_words.keys()):
			if repeated_words[k] == v:
				ranged_repeated_words.append([k, v])
				repeated_words.pop(k)
	return (ranged_repeated_words)
# выводим ТОП 10
def write_result_in_file(tag, filename, code, word_len, word_exception):
	with open ('outpput.txt', 'a') as out_file:
		out_file.write('\n ТОП-10 из файла  %s \n' % (filename))
		for i in range (10):
			out_file.write ('%s \n' % (range_repeated_words(find_repeated_words(tag, filename, code, word_len, word_exception))[i]))


write_result_in_file('description', 'newscy.xml', 'KOI8_r',6,'<br>')
write_result_in_file('description', 'newsafr.xml', 'utf-8',6, 'href', '<br')
write_result_in_file('description', 'newsfr.xml', 'iso8859_5',6, 'href', '<br')
write_result_in_file('description', 'newsit.xml', 'cp1251',6, 'href', '<br')