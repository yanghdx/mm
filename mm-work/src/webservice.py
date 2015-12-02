import suds
from suds.client import Client
url = 'http://192.168.54.137:8080/webservice/?wsdl'

cli = Client(url)

print(cli)


print(cli.service.getServerAttackTopN(10))