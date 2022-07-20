from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
from re import search as re_search
import dre as dre
import bpa as bpa
import bpp as bpp
import constants as c
import sys
import os


DRIVER_PATH = './chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)


args = sys.argv
fromI = int(args[1])
toI = int(args[2])


# DRE
for i in range(fromI, toI):
  codigo = c.codigos[i]
  path = f"{c.dre_dir}{codigo}/"
  print(path)
  if os.path.exists(path): continue
  
  while True:
    # try catch
    try:
      print(f"Baixando o código {codigo}")
      dre.download(driver, codigo)
      break
    except:
      print(f"Erro ao baixar o codigo: {codigo}")
      continue
    
#BPA
for i in range(fromI, toI):
  codigo = c.codigos[i]
  path = f"{c.bpa_dir}{codigo}/"
  print(path)
  if os.path.exists(path): continue
  
  while True:
    # try catch
    try:
      print(f"Baixando o código {codigo}")
      bpa.download(driver, codigo)
      break
    except:
      print(f"Erro ao baixar o codigo: {codigo}")
      continue

#BPP
for i in range(fromI, toI):
  codigo = c.codigos[i]
  path = f"{c.bpp_dir}{codigo}/"
  print(path)
  if os.path.exists(path): continue
  
  while True:
    # try catch
    try:
      print(f"Baixando o código {codigo}")
      bpp.download(driver, codigo)
      break
    except:
      print(f"Erro ao baixar o codigo: {codigo}")
      continue


# https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/ResultBuscaParticCiaAb.aspx?CNPJNome=AMBEV&TipoConsult=C


# https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=H
# var trs = document.querySelectorAll('tr')
# var codigos = []
# for(const tr of trs) {
#     if(!tr.innerHTML.includes("Concedido")) continue;
#     codigo = tr.querySelector("td:nth-child(4)").innerText
#     codigos.push(codigo)
# }
# console.log(codigos.join(","))

# https://bvmf.bmfbovespa.com.br/pt-br/mercados/acoes/empresas/ExecutaAcaoConsultaInfoEmp.asp?CodCVM=24406&ViewDoc=0

driver.close()