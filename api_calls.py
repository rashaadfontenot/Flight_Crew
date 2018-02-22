import requests
from urllib.parse import quote, urlencode
import xml.etree.ElementTree as ET

#Zillow API ID
zws_id = 'X1-ZWz1fu1bkc2f4b_4aijl'

#Enter Street Address
address = input()
citystatezip = input()
house = urlencode({'address': address,
                   'citystatezip': citystatezip})

#Formated API Link
get_results = requests.get('http://www.zillow.com/webservice/GetSearchResults.htm?zws-id={}&{}'.format(zws_id, house))
#Parse XML
tree = ET.fromstring(get_results.content)

#Get Zillow Property ID
zpid = tree.find('response/results/result/zpid').text
zestimate = tree.find('response/results/result/zestimate/amount').text

print('The current Value for {} is ${}!'.format(address, zestimate))