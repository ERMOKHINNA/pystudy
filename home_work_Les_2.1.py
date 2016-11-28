                                                                              
# -*- coding: utf-8 -*-
def date_difference (leave, arrive):
	difference = leave - arrive + 1
	return difference
	
def visit_length (visit):
	return date_difference(visit[1], visit[0])
	
def visit_not_in_future(visits, date_in_future):
	visits = visits + [[date_in_future, date_in_future]]
	future = False
	for visit in visits:
		for next_visit in visits:
			
			if ((next_visit > visit) and (visit[1] > next_visit[0])):
				future = True
				
	return future

def print_days_future_visit(visits, date_in_future):
	visits_for_future = visits + [[date_in_future, date_in_future]]
	days_for_future_visits = get_days_for_visits(visits_for_future)
	days_in_es = residence_limit - days_for_future_visits[len(days_for_future_visits) - 1] + 1
	print ('Если въедем %s числа, сможем провести в шенгене %s дней' % (date_in_future, days_in_es))
	visits.append([date_in_future, date_in_future + days_in_es])
	
def print_residence_limit_violation(visits):
	days_for_visits = get_days_for_visits(visits)
	for visit, total_days in zip(visits, days_for_visits):
		if total_days > residence_limit:
		  overstay_time = total_days - residence_limit
		  print('Во время визита', visit, 'количество время пребывания превышено на', overstay_time, 'дней')
	    
				
def get_days_for_visits(visits):
	days_for_visits = []
	for visit in visits:
	    days_for_visit = 0
	    for past_visit in visits:
	        if visit[0] - schengen_constraint < past_visit[0] < visit[0]:
	            days_for_visit += visit_length(past_visit)
	    days_for_visit += visit_length(visit)
	    days_for_visits.append(days_for_visit)
	    
	return days_for_visits
	
#def get_date(b_date, e_date):
#	b_date = int(input('Введите дату начала'))
#	e_date = int(input('Введите дату конца'))
#	return (b_date, e_date)

def get_date_from_file():
	visits_bank = []
	with open ('visits.txt') as visit_bank:
		for visit in visit_bank:
			visits_bank.append(list(map(int, visit.split())))
	return visits_bank

def new_visit(visits_bank):
	print(('Пробудете в шенгене %s дней\n') % (sum(get_days_for_visits(visits_bank))))
	print_residence_limit_violation(visits_bank)

def future_visit(visits_bank):
  next_date = int(input('введите дату визита '))
  if visit_not_in_future(visits_bank, next_date) == True:
  	print ('Вы хотите вернуться в прошлое?')
  else:
    print_days_future_visit(visits_bank, next_date)
  
def remove_visits(visits_bank):
  print('Ваши поездки:', visits_bank)
 
  visits_bank.remove(visits_bank[int(input('введите номер поездки которую нужно удалить ' ))-1])
  
def handle(action):
	
	if action == 'v':
	  new_visit(visits_bank)
		
	elif action == 'p':
	  future_visit(visits_bank)

	elif action == 'r':
	  remove_visits(visits_bank)
		
	elif action == 'e':
		with open ('visits.txt', 'w') as visit_bank:
			for v in visits_bank:
				visit_bank.write('%2s %2s \n' % (v[0], v[1]))
		exit()
		
	else:
	  print ('Некорректный ввод')
	
visits_bank = get_date_from_file()
while True:
	print (' Введите действие:\n v - получить текущий список поездок \n p - дата следующего визита, чтобы узнать сколько дней можно будет провести в шенгене \n e - для выхода из приложения \n r - для удаления поездки')
	schengen_constraint = 180
	residence_limit = 90
#	action = input()
	handle(input())
