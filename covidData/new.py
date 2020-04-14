import Cov
from urllib.request import Request, urlopen
import json

c = Cov.Cov()
country = 'south africa'

# print("1",c.getCountry(country),'\n')
# print('2',c.getNew(country),'\n')
# print('3',c.getCases(country), c.getTotal(country),'\n')
print('4',c.getByDate('20200414'),'\n')
# print('5',c.getAllProv(country),'\n')
print('6', c.getSouthy())

