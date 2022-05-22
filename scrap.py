import requests
from bs4 import BeautifulSoup

url = 'https://verify.iebc.or.ke/index.php/webapi/submit_voter'

def makeRequest(payload):
    return requests.post(url,data=payload)
    

def scrap(html_content):
    soup = BeautifulSoup(html_content,'html.parser')
    # finding elements
    h2 = soup.find('h2')
    if h2.text != 'Voter found! Details as below:':
        return {'msg':'Voter Not Found'}
    # getting details

    table = soup.select('table.table-striped > tr > td > b')

    return {'data':[x.text for x in table],'msg':'Success'}

   


def execute(payload):
    req = makeRequest(payload)
    if req.status_code == 200:
        scrapped = scrap(req.content.decode('utf-8'))
        if scrapped['msg'] == 'Success':
            print('Voter Found')
            print(scrapped['data'])
        else:
            print(scrapped['msg'])
    else:
        print('Result Not Found')