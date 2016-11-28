residence_limit = 90  # 45, 60
schengen_constraint = 180
visits = [[90, 100], [110, 180]]
planed_visit = 290

for visit in visits:
	if not isinstance(visit, list):
		raise Exception("Ошибка в типе поездки", visit)
		
#накладывающиеся визиты
#Что будет если в нашем списке будут накладывающиеся визиты?  [[1, 10], [5, 15]] 

total_time_in_es = 0

for visit in visits:
	for next_visit in visits:
		
		if ((next_visit > visit) and (visit[1] > next_visit[0])):
			
			raise Exception("Ошибка с датами в", visits.index(next_visit)+1, " поездке" )
			


days_in_eu = []

total_time_in_es = 0

for visit in visits:
	past_days = 0
	for past_visit in visits:
		if visit[0] - schengen_constraint < past_visit[0] <= visit[0]:
			past_days += past_visit[1] - past_visit[0] + 1
	days_in_eu.append(past_days)	

	total_time_in_es += visit[1] - visit[0] + 1

future_visits = visits + [[planed_visit, planed_visit]]

for visit in future_visits:
	past_days = 0
	for past_visit in future_visits:
		if visit[0] - schengen_constraint < past_visit[0] <= visit[0]:
			past_days += past_visit[1] - past_visit[0] + 1
	days_in_eu.append(past_days)
	days_in_es = residence_limit - days_in_eu[len(days_in_eu) - 1] + 1

print ('Если въедем %s числа, сможем провести в шенгене %s дней' % (planed_visit, days_in_es))

for visit, days in zip(visits, days_in_eu):
	if days > residence_limit:
		print('В течение поездки', visit, 'вы пребывали в ЕС слишком долго:', days)
		
#Что будет если дата выезда будет раньше даты въезда? 
#[[1, 10], [19, 2]]
	while visit[1] < visit [0]:
		raise Exception ("Машина времени в ", visits.index(visit)+1, 'поездеке')
		break
		
print ('Вы пробудете в ЕС дней:', total_time_in_es)


# Про планируемые поездки

#last_visit_in_eu = max(visits)	
#print (last_visit_in_eu)
#if last_visit_in_eu[1] > planed_visit[0]:
#	raise Exception ('опять машина времени')
#if last_visit_in_eu[1] < planed_visit[0] - schengen_constraint:
#	# если считать, что виза не на один год :) 
#	print('можете пробыть 90 дней')		
#else:
#	print ('сможете пробыть', planed_visit[0] - residence_limit - days_in_eu[-1], 'дней')		


		
	
