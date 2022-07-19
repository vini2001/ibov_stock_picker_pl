from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
from re import search as re_search
import utils as utils
import constants as constants
import os

def download(driver, codigo):
  payload = "{"f" dataDe: '01/01/2019', dataAte: '31/12/2022' , empresa: ',{codigo}', setorAtividade: '-1', categoriaEmissor: '-1', situacaoEmissor: '-1', tipoParticipante: '1,2,8', dataReferencia: '', categoria: 'EST_4', periodo: '2', horaIni: '', horaFim: '', palavraChave:'',ultimaDtRef:'false', tipoEmpresa:'1', token: '', versaoCaptcha: ''""}"
  headers = {
    'Content-Type': 'application/json; charset=utf-8',
  }

  response = requests.request("POST", constants.listar_doc_url, headers=headers, data=payload)
  res = json.loads(response.text)
  res = res["d"]["dados"]
  res = res.split("DFP - Demonstrações Financeiras Padronizadas$&")
  res.pop(0)

  def scrap(url, date):
      driver.get(url)
      ticker = driver.find_element_by_id("lblNomeCompanhia").text.replace("/", "_*_")
      driver.switch_to.frame(driver.find_element_by_id("iFrameFormulariosFilho"))
      table = driver.find_element_by_tag_name("table")
      path = f"{constants.dre_dir}{codigo}/"
      
      if not os.path.exists(path):
        os.makedirs(path)
      
      name=f"{path}{ticker}-{date.replace('/', '-')}.csv"
      utils.table_to_csv(table, file_name=name)
      print(f"{ticker} saved")


  for r in res:
      if 'Ativo' in r:
          date = re_search(r'\d{2}/\d{2}/\d{4}', r).group()
          url_path = r.split("nclick=OpenPopUpVer('")[1].split("')")[0]
          url = f'https://www.rad.cvm.gov.br/ENET/{url_path}'
          print(f'Date: {date}, url: {url}')
          scrap(url, date)
          break
      