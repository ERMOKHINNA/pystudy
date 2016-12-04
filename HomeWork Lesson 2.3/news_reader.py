
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
def find_repeated_words(word_list, word_len, word_exception, word_exception_1):
	repeated_words = {}
	for article in word_list:
		for word in article:
			count = 0
			if len(word) >= word_len and word[len(word_exception)] != word_exception and word[len(word_exception_1)] != word_exception_1:
				for next_article in word_list:
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
def write_result_in_file(filename, result):
	with open ('outpput.txt', 'a') as out_file:
		out_file.write('ТОП-10 из файла  %s \n \n' % (filename))
		for i in range (10):
			out_file.write ('%s \n' % (result[i]))

write_result_in_file('newscy.xml',range_repeated_words(find_repeated_words(get_content_from_tag('description', 'newscy.xml', 'KOI8_r'),6, 'href', '<br')))
write_result_in_file('newsafr.xml',range_repeated_words(find_repeated_words(get_content_from_tag('description', 'newsafr.xml', 'utf-8'),6, 'href', '<br')))
write_result_in_file('newsfr.xml',range_repeated_words(find_repeated_words(get_content_from_tag('description', 'newsfr.xml', 'iso8859_5'),6, 'href', '<br')))
write_result_in_file('newsit.xml',range_repeated_words(find_repeated_words(get_content_from_tag('description', 'newsit.xml', 'cp1251'),6, 'href', '<br')))