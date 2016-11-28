def get_date_from_file():
	visits_bank = []
	with open ('visits.txt') as visit_bank:
		for visit in visit_bank:
			visits_bank.append(list(map(int, visit.split())))
	return visits_bank

def visit_not_in_future(visits, date_in_future):
	visits = visits + [[date_in_future, date_in_future]]
	future = False
	print (visits)
	for visit in visits:
		print ('iter1:', visit)
		for next_visit in visits:
			print ('iter2:', visit)

			
			#if ((next_visit > visit) and (visit[1] > next_visit[0])):
			#	future = True
				
	


visit_bank = [[1, 2], [3, 4], [7, 8]]
print (visit_bank[1])
visit_bank.remove(visit_bank[1])
print (visit_bank)
