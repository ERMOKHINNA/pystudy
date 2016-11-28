
cities = {}

with open('temp.txt') as f_week_temperature:
	for city in f_week_temperature: 
		temperatures = f_week_temperature.readline()
		print(temperatures)
		a = temperatures.split()
		print (a)
	#	cities[city.strip()] = temperatures.split()
		cities[city] = temperatures.split()
	#	print(cities)

print(cities)

for city, temperatures in cities.items():
	avg = 0
	for t in temperatures:
		avg += int(t)
	avg = avg / len(temperatures)
	print (city, "%.2f" % avg)