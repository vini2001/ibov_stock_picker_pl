# 

import os
import constants as c
import requests
from bs4 import BeautifulSoup

# mapcvmtoticker.py => For every CVM code, map it to a ticker and save it in a file called cvm_to_ticker.csv


dir = c.dre_dir
with open('cvm_to_ticker.csv', "w") as f:
    f.write(",".join(['CVM', 'Ticker']) + "\n")

    codigos_cvm = [f for f in os.listdir(dir) if os.path.isdir(os.path.join(dir, f))]
    
    i = 0
    for codigo_cvm in codigos_cvm:
        i += 1
        response = requests.request("GET", f'https://bvmf.bmfbovespa.com.br/pt-br/mercados/acoes/empresas/ExecutaAcaoConsultaInfoEmp.asp?CodCVM={codigo_cvm}&ViewDoc=0', headers={})
        print(codigo_cvm)
        # print(response.text)
        soup = BeautifulSoup(response.text)
        els = soup.select_one('.LinkCodNeg')
        if els != None and len(els.text) > 2:
            print(els.text)
            f.write(",".join([codigo_cvm, els.text]) + "\n")
        print(f'\n{i}')
