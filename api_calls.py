import requests
from urllib.parse import urlencode
import xml.etree.ElementTree as ET

#Zillow API ID
zws_id = 'X1-ZWz1fu1bkc2f4b_4aijl'

#Enter Street Address
address = '1311 S. L. St'
citystatezip = 'Tacoma, WA'
house = urlencode({'address': address,
                   'citystatezip': citystatezip})

#Formated API Link
get_results = requests.get('http://www.zillow.com/webservice/GetDeepSearchResults.htm?zws-id={}&{}'.format(zws_id, house))
#Parse XML
tree = ET.fromstring(get_results.content)

#Get Zillow Property ID
zpid = tree.find('response/results/result/zpid').text
zestimate = tree.find('response/results/result/zestimate/amount').text
bathrooms = tree.find('response/results/result/bathrooms').text
bedrooms = tree.find('response/results/result/bedrooms').text
lastSoldDate =  tree.find('response/results/result/lastSoldDate').text
lastSoldPrice =  tree.find('response/results/result/lastSoldPrice').text
yearBuilt =  tree.find('response/results/result/yearBuilt').text
useCode =  tree.find('response/results/result/useCode').text

print('The current value for {} is ${}!'.format(address, zestimate))
print('This house has {} bathrooms'.format(bathrooms))
print('This house has {} bedrooms'.format(bedrooms))
print('This house was last sold on {} for a price of ${}'.format(lastSoldDate, lastSoldPrice))
print('This house was built in {}'.format(yearBuilt))
print('This house is zoned for {}'.format(useCode))
