import csv
import io
from urllib.request import Request, urlopen
import json
from urllib.error import HTTPError
from cachetools import cached, TTLCache
import time

class Cov():

	global entries
	entries=[]

	global recovered
	recovered = 'recovered'
	global cases
	cases = 'cases'
	global deaths
	deaths = 'deaths'	

	global prov_data
	prov_data = []

	global prov_tmp
	prov_tmp = prov_data

	global data_dict
	data_dict = {}
	
	global headers
	headers = []

	global dict1
	dict1 = {}

	global list1
	list1 = []

	cache = TTLCache(maxsize=100, ttl=3600)

	#Default source is specified below, feel free to change this using the provided method
	#not wise to hard code the source? Feel free to advise on this.
	#Source can be changed using changeSrc() but the fromat of the new data may be an issue
	# cache = TTLCache(maxsize=100, ttl=14400)  # 2 - let's create the cache object.
	#makes available multiple type of data types that may be used by other methods. 
	@cached(cache)
	def __init__(self, src='https://interactive-static.scmp.com/sheet/wuhan/viruscases.jsonasd'):
		self.src = src
		self.getData(src)

	#doesn't work
	def changeSrc(self, src):
		self.src=src
		return self.getData(src)

	@cached(cache)
	def getData(self, src):	
		

		req = Request(src, headers={'User-Agent': 'Mozilla/5.0'})
		src = 'https://api.covid19api.com/summary'
		req = Request(src, headers={'User-Agent': 'Mozilla/5.0'})
		with urlopen(req) as response:
			if response.getcode() == 200:
				source = response.read()
				data = json.loads(source)
			else:
				print("Default source are unavailable. Please specify a source by using the changeSrc() method")

		global entries 
		entries = data['Countries']
		for i in range(len(entries)-1):

			entries[i] = {k.lower(): v for k, v in entries[i].items()}

		global recovered
		recovered = 'totalrecovered'
		global cases
		cases = 'totalconfirmed'
		global deaths
		deaths = 'totaldeaths'	

		url = "https://raw.githubusercontent.com/dsfsi/covid19za/master/data/covid19za_provincial_cumulative_timeline_confirmed.csv"
		webpage = urlopen(url)
		datareader = csv.reader(io.TextIOWrapper(webpage))
		
		global prov_data
		prov_data = list(datareader)
		del prov_data[prov_data.index([])]
		
		global prov_tmp
		prov_tmp = prov_data
		
		global headers
		headers = prov_tmp.pop(0)
		
		global dict1

		global list1

		for row in prov_tmp:
			dict1 = {}
			for i in headers:
				dict1[i] = row[headers.index(i)]
			list1.append(dict1)

		return entries, prov_data, prov_tmp,


	# This method returns a dict containing all the 
	# available data about any country that is parsed 
	# Returns zero if country is not found
	# @cached(cache)
	def getCountry(self,country):	
		for i in range(len(entries)-1):
			if entries[i]['country'].lower()==country.lower():
				return entries[i]
		return 0



	# This method returns a dict containing all the 
	# available data about any continet that is parsed 
	@cached(cache)
	def getContinent(self,continent):
		continent_data = []
		for i in range(len(entries)):
			if entries[i]['continent'].lower()==continent.lower():
				continent_data.append(entries[i])
		return continent_data



	#Returns number of cases, 
	# t=0 returns all confimed cases, t=1 returns number recovered,t=2 returns number of deaths
	@cached(cache)
	def getCases(self,country,t=cases):
		global cases
		global recovered
		global deaths
		
		if country == 'south africa' and t == cases:	
			return self.getSouthy()
		elif t == 'totalrecovered':# and t==cases:
		# elif t == recovered:
			return self.getCountry(country)[recovered]
		elif t == 'totaldeaths':
			return self.getCountry(country)[deaths]
		else:
			return self.getCountry(country)[cases]




	#Returns active number of cases. 
	#ie: total tested positive minus number recovered minus number of deaths
	@cached(cache)
	def getActCases(self,country):

		return int(self.getTotal(country)) - int(self.getCases(country, recovered)) - int(self.getCases(country,deaths))



	#Returns list [Date of changes, num new cases, num new recoveries, num new deaths]
	@cached(cache)
	def getNew(self, country):

		cntry = self.getCountry(country)
		return [cntry['date'], cntry['newconfirmed'], cntry['newrecovered'], cntry['newdeaths']]
  


	#Returns all recorded cases, same as calling getCases(country, t=0)
	@cached(cache)
	def getTotal(self, country):
		if country.lower() == 'south africa':
			return self.getSouthy()
		try:	
			return self.getCases(country)['totalconfirmed']
		except KeyError:
			return self.getCases(country)['total']


	@cached(cache)
	def getAllProv(self, country):

		ret_dict= {}
		headers = prov_data[0]
		for i in range(len(headers)-1):
			ret_dict[headers[i+1].lower()] = prov_data[len(prov_data)-1][i+1]
		return ret_dict


	@cached(cache)
	def getByDate(self, date):
		global data_dict
		last_row = list1[len(list1)-1]
		prev = list1[0]
		try:
			for i in list1:
				# print('date',date,'i[date]')
				if (date == i['date'] or date == i['YYYYMMDD']):
					return i

				elif (date < i['date'] or date < i['YYYYMMDD']):

					return prev
				elif date > last_row['YYYYMMDD']:
					return last_row
				prev = i
		except KeyError:
			return "wtf"

	#returns value of total confirmed cases for south africa.
	def getSouthy(self):
		a = list(prov_tmp)[len(list(prov_tmp))-1][len(list(prov_tmp)[len(list(prov_tmp))-1])-1]
		return a





# start = time.time()
# c = Cov()
# end = time.time()
# country = 'south africa'
# print(c.getCountry(country))
# print(c.getActCases(country))
# print(c.getSouthy())
# print(c.getTotal('south africa'))
# print(c.getAllProv(country))
# print('20200305'<'20200414')
# # print(c.getNew(country))
# print(c.getCases(country))#, c.getTotal(country))
# print(c.getByDate('20200305'))
# print(c.getByDate('20200414'))
# print(c.getByDate('20200304'))

# print(end - start)