from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from datetime import datetime
import pandas as pd
import requests
import threading
from bs4 import   BeautifulSoup
from time import sleep  
import PySimpleGUI as sg
import docx


options = Options()
options.headless = False # Visivel

def formata_mensagem(mensagem, Nome):
    mensagemform =  "Olá, " + str(Nome) + "! Tudo bem?" + "\n" + mensagem
    mensagemform = mensagemform.split("\n")
    return mensagemform

def envia_mensagem(mensagem, navegador, numContato):
    
        element2 = False
        while(element2 == False):
            element2 = WebDriverWait(navegador, 240, poll_frequency=0.1).until(
            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
            
        campo_msg = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
        for msg in mensagem:
            campo_msg.send_keys(msg)
            campo_msg.send_keys(Keys.SHIFT,'\n')
        campo_msg.send_keys("\n")
        sleep(5)

        btn_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")
        sleep(0.7)
        btn_contato.click()
        sleep(1.9)
        btn_contatos = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[5]/button/span")
        sleep(0.9)
        btn_contatos.click()
        sleep(0.4)
        procura_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]")
        sleep(0.8)
        procura_contato.send_keys(str(numContato))
        sleep(0.6)
        contato_oficial = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[2]/button/div[2]/div/div[2]/div[1]/div/span")
        sleep(0.6)
        contato_oficial.click()
        sleep(0.3)
        btn_envia_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/span/div/div/div")
        sleep(4.2)
        btn_envia_contato.click()
        sleep(2.2)
        btn = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div")
        sleep(0.5)
        btn.click()
        sleep(0.9) 
        btn_clip = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span") 
        btn_clip.click() 
        sleep(0.9)
   #     btn_img = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span") 
       # btn_img.click()
   #     input_box = navegador.find_element(by=By.TAG_NAME, value= 'input')
   #     file_path="C:/Users/Call-000/Desktop/Projetos/Asseba.png"

   #     input_box.send_keys(file_path)     
   #     sleep(1)   
   #     btn_img = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div") 
   #     btn_img.click()
   #     sleep(2)
      #  print("Erro do stale")
      #  sleep(0.2)
      #  btn = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div")
      #  sleep(0.5)
      #  btn.click()
      #  pass      

def num_primo(cont, navegador):

    try:
        if cont == 1:
            numero = "5571999617890"
            num_protocolo = "MAKTUB-ATENDIMENTO-23122022"
            navegador.get("https://web.whatsapp.com/send/?phone=" + str(numero) + "&text&type=phone_number&app_absent=0")

            element_inicia = False
            while(element_inicia == False):
                element_inicia = WebDriverWait(navegador, 240, poll_frequency=0.1).until(
                EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
            
        
            campo_msg = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
            sleep(1)
            campo_msg.send_keys("Olá, tudo bem? Teste numeros primos. " + "  Seu numero de protocolo é: " +str(num_protocolo))
            sleep(1)
            btn_enviar = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")
            sleep(1)
            btn_enviar.click()
            sleep(0.3)




        elif cont == 3:
            numero = "5571991471236"
            num_protocolo = "MAKTUB-ATENDIMENTO-23122022"
            navegador.get("https://web.whatsapp.com/send/?phone=" + str(numero) + "&text&type=phone_number&app_absent=0")

            element_inicia = False
            while(element_inicia == False):
                element_inicia = WebDriverWait(navegador, 240, poll_frequency=0.1).until(
                EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))

            campo_msg = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
            sleep(1)
            campo_msg.send_keys("Olá, tudo bem? Teste numeros. " + "  Seu numero de protocolo é: " +str(num_protocolo) + str(cont))
            sleep(1)
            btn_enviar = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")
            sleep(1)
            btn_enviar.click()
            sleep(0.3)
    except UnexpectedAlertPresentException:  
        print("Erro do num primo")
        pass        

def wpp1conexao(mensagem, telefones, nomeDaCampanha, numContato):
  #    with open(mensagem, "r") as arqv:
  #        dados_mensagem = str(arqv.read()) 

  #  dados_mensagem = str(mensagem)     
    dados =  pd.read_excel(telefones)
    options = Options()
    options.headless = False # Visivel
    print(dados)
    quantidade = len(dados) - 1



    #NAVEGADOR#
    navegador1 = webdriver.Chrome(options=options)
    navegador1.get('https://web.whatsapp.com/')
    element = False

    while(element == False):
        element = WebDriverWait(navegador1, 999, poll_frequency=0.1).until(
        EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div/div[1]/span")))
        print("entrou0")


    cont1 = 0
    for index,row in dados.iterrows():

        Telefone = (row['TEL'])
        Nome = (row['NOME'])
        mens = formata_mensagem(mensagem, Nome)

        TelWPP = Telefone
        sleep(1)
        print(Telefone)


        navegador1.get('https://web.whatsapp.com/send/?phone=' + str(row['TEL']) +'&text&type=phone_number&app_absent=0')
        sleep(1)
        try:
            element_inicia = False
            while(element_inicia == False):
                element_inicia = WebDriverWait(navegador1, 20, poll_frequency=0.1).until(
                EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))

        except:

            print("saiu")
            sleep(2)
            resposta_consulta = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
            retorno ='N'
            btn_ok = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
            
            btn_ok.click()
        else:
            envia_mensagem(mens, navegador1, numContato)  
            retorno ='S'

            if cont1 == 1 or cont1 == 3:
                num_primo(cont1, navegador1)
                
            elif cont1 == 5:
                cont1 = -1

            cont1 +=1
        with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                retorno = retorno + ';'
                TelWPP = str(Telefone) + ';'
                
                verificaWpp = retorno + str(Telefone) +  "\n"
                
                f.write(verificaWpp) 
    
def wpp2conexoes(mensagem, telefones, nomeDaCampanha, numContato):

    dados =  pd.read_excel(telefones)
    def RetornaDados(dados):
        nome = []
        cpf = []
        num = []
        for index,row in dados.iterrows():

           Nome = (row['NOME'])
           Cpf = (row['CPF'])
           Num =  (row['TEL'])
           cpf.append(Cpf)
           nome.append(Nome)
           num.append(Num)
        return cpf,nome,num
    Cpfs, Nomes, Nums  = RetornaDados(dados)
    #    print(Nomes)
    #    print(Cpfs)
    #    print(Nums)

    options = Options()
    options.headless = False # Visivel
    def wpp1():
        quantidade = len(dados) - 1



        #NAVEGADOR 1#
        navegador1 = webdriver.Chrome(options=options)
        navegador1.get('https://web.whatsapp.com/')
        element = False


        while(element == False):
            element = WebDriverWait(navegador1, 999, poll_frequency=0.1).until(
            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div/div[1]/span")))
            print("entrou0")


        cont1 = 0
        vardonavegador1 = 0 

        for index,row in dados.iterrows():

            if quantidade < vardonavegador1:
                print("finalizou1")
                break
            Telefone = Nums[vardonavegador1]      
            cpf1 =  Cpfs[vardonavegador1]    
            nome1 = Nomes[vardonavegador1]
            mens = formata_mensagem(mensagem,nome1)
            sleep(1)



            navegador1.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
            sleep(1)
            try:
                element_inicia = False
                while(element_inicia == False):
                    element_inicia = WebDriverWait(navegador1, 20, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))

            except:

                print("nao enviado 1" )
                sleep(2)
                resposta_consulta = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                retorno ='N'
                btn_ok = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                
                btn_ok.click()
                vardonavegador1 += 2
            else:
                    
                envia_mensagem(mens, navegador1, numContato)    
                retorno ='S'
                vardonavegador1 += 2
                print("enviado 1" )
                if cont1 == 1 or cont1 == 3:
                    num_primo(cont1, navegador1)
                    
                elif cont1 == 5:
                    cont1 = -1

                cont1 +=1
            with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                    verificaWpp = retorno +";" + str(Telefone) +";" + str(cpf1) + "\n"
                    
                    f.write(verificaWpp)             


    def wpp2():  
        quantidade = len(dados) - 1      
        #NAVEGADOR 2#
        navegador2 = webdriver.Chrome(options=options)
        navegador2.get('https://web.whatsapp.com/')
        element = False
        while(element == False):
            element = WebDriverWait(navegador2, 999, poll_frequency=0.1).until(
            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div/div[1]/span")))
            print("entrou0")  
        cont2 = 0 
        vardonavegador2 = 1    
        for index,row in dados.iterrows():
            if quantidade < vardonavegador2:
                print("finalizou2")
                break
            
            sleep(1)
            Telefone = Nums[vardonavegador2]              
            cpf2 =  Cpfs[vardonavegador2]
            nome2 = Nomes[vardonavegador2]
            mens = formata_mensagem(mensagem, nome2)
            navegador2.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
            sleep(1)

            try:
                element_inicia = False
                while(element_inicia == False):
                    element_inicia = WebDriverWait(navegador2, 20, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))

            except:

                print("nao enviado 2" )
                sleep(2)
                resposta_consulta = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                retorno ='N'
                btn_ok = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                
                btn_ok.click()
                vardonavegador2 += 2
            else:
                
                
                envia_mensagem(mens, navegador2, numContato)
                retorno ='S'
                print("enviado 2")
                vardonavegador2 += 2
                if cont2 == 1 or cont2 == 3:
                    num_primo(cont2, navegador2)
                    
                elif cont2 == 5:
                    cont2 = -1

                cont2 +=1
            with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                    verificaWpp = retorno +";" + str(Telefone) +";" + str(cpf2) + "\n"
                    
                    f.write(verificaWpp)    
    
    t1 = threading.Thread(target=wpp1)
    t2 = threading.Thread(target=wpp2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

def wpp3conexoes(mensagem, telefones, nomeDaCampanha, numContato):

    dados =  pd.read_excel(telefones)
    def RetornaDados(dados):
        nome = []
        cpf = []
        num = []
        for index,row in dados.iterrows():

           Nome = (row['NOME'])
           Cpf = (row['CPF'])
           Num =  (row['TEL'])
           cpf.append(Cpf)
           nome.append(Nome)
           num.append(Num)
        return cpf,nome,num
    Cpfs, Nomes, Nums  = RetornaDados(dados)
 

    options = Options()
    options.headless = False # Visivel
    def wpp1():
        quantidade = len(dados) - 1



        #NAVEGADOR 1#
        navegador1 = webdriver.Chrome(options=options)
        navegador1.get('https://web.whatsapp.com/')
        element = False


        while(element == False):
            element = WebDriverWait(navegador1, 999, poll_frequency=0.1).until(
            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div/div[1]/span")))
            print("entrou0")


        cont1 = 0
        vardonavegador1 = 0 

        for index,row in dados.iterrows():

            if quantidade < vardonavegador1:
                print("finalizou1")
                break
            Telefone = Nums[vardonavegador1]      
            cpf1 =  Cpfs[vardonavegador1]    
            nome1 = Nomes[vardonavegador1]
            mens = formata_mensagem(mensagem,nome1)
            sleep(1)



            navegador1.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
            sleep(1)
            try:
                element_inicia = False
                while(element_inicia == False):
                    element_inicia = WebDriverWait(navegador1, 20, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))

            except:

                print("nao enviado 1" )
                sleep(2)
                resposta_consulta = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                retorno ='N'
                btn_ok = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                
                btn_ok.click()
                vardonavegador1 += 3
            else:
                    
                envia_mensagem(mens, navegador1, numContato)
                retorno ='S'
                vardonavegador1 += 3
                print("enviado 1" )
                if cont1 == 1 or cont1 == 3:
                    num_primo(cont1, navegador1)
                    
                elif cont1 == 5:
                    cont1 = -1
                
                cont1 +=1
                with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                    verificaWpp = retorno +";" + str(Telefone) +";" + str(cpf1) + "\n"
                    
                    f.write(verificaWpp)             


    def wpp2():  
        quantidade = len(dados) - 1      
        #NAVEGADOR 2#
        navegador2 = webdriver.Chrome(options=options)
        navegador2.get('https://web.whatsapp.com/')
        element = False
        while(element == False):
            element = WebDriverWait(navegador2, 999, poll_frequency=0.1).until(
            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div/div[1]/span")))
            print("entrou0")  
        cont2 = 0 
        vardonavegador2 = 1    
        for index,row in dados.iterrows():
            if quantidade < vardonavegador2:
                print("finalizou2")
                break

            sleep(1)
            Telefone = Nums[vardonavegador2]              
            cpf2 =  Cpfs[vardonavegador2]
            nome2 = Nomes[vardonavegador2]
            mens = formata_mensagem(mensagem, nome2)
            navegador2.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
            sleep(1)

            try:
                element_inicia = False
                while(element_inicia == False):
                    element_inicia = WebDriverWait(navegador2, 20, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))

            except:

                print("nao enviado 2" )
                sleep(2)
                resposta_consulta = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                retorno ='N'
                btn_ok = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                
                btn_ok.click()
                vardonavegador2 += 3
            else:
                
                envia_mensagem(mens, navegador2, numContato)
                retorno ='S'
                print("enviado 2")                
                vardonavegador2 += 3

                if cont2 == 1 or cont2 == 3:
                    num_primo(cont2, navegador2)
                    
                elif cont2 == 5:
                    cont2 = -1

                cont2 +=1
            with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                    verificaWpp = retorno +";" + str(Telefone) +";" + str(cpf2) + "\n"
                    
                    f.write(verificaWpp)   

    def wpp3():  

        quantidade = len(dados) - 1      
        #NAVEGADOR 2#
        navegador3 = webdriver.Chrome(options=options)
        navegador3.get('https://web.whatsapp.com/')
        element = False
        while(element == False):
            element = WebDriverWait(navegador3, 999, poll_frequency=0.1).until(
            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div/div[1]/span")))
            print("entrou0")  
        cont3 = 0 
        vardonavegador3 = 2    
        for index,row in dados.iterrows():
            if quantidade < vardonavegador3:
                print("finalizou2")
                break
            sleep(1)
            Telefone = Nums[vardonavegador3]              
            cpf3 =  Cpfs[vardonavegador3]
            nome3 = Nomes[vardonavegador3]
            mens = formata_mensagem(mensagem, nome3)
            navegador3.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
            sleep(1)

            try:
                element_inicia = False
                while(element_inicia == False):
                    element_inicia = WebDriverWait(navegador3, 20, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))

            except:

                print("nao enviado 3" )
                sleep(2)
                resposta_consulta = navegador3.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                retorno ='N'
                btn_ok = navegador3.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                
                btn_ok.click()
                vardonavegador3 += 3
            else:
                
                envia_mensagem(mens, navegador3, numContato)
                retorno ='S'
                print("enviado 3")
                vardonavegador3 += 3

                if cont3 == 1 or cont3 == 3:
                    num_primo(cont3, navegador3)
                    
                elif cont3 == 5:
                    cont3 = -1

                cont3 +=1
            with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                    verificaWpp = retorno +";" + str(Telefone) +";" + str(cpf3) + "\n"
                    
                    f.write(verificaWpp)                    
    
    t1 = threading.Thread(target=wpp1)
    t2 = threading.Thread(target=wpp2)
    t3 = threading.Thread(target=wpp3)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t2.join()

'''
def botwpp(telefones, mensagem, nomeDaCampanha):
  #Bot de whatsapp para três conexoes 

  #(telefones, mensagem, nomeDaCampanha, numConexoes) = janela()
  options = Options()
  options.headless = False # Visivel
  dados =  pd.read_excel(telefones)
 #  dados_mensagem = docx.Document(mensagem)

  data = datetime.now()
  data = data.strftime('%d/%m/%Y %H:%M:%S')
  data = data.replace("/","").replace(":","").replace(" ","")

  with open(mensagem, "r") as arqv:
    dados_mensagem = arqv.read()
  #NAVEGADOR 1#
  dados_mensagem = dados_mensagem +"\n"+ "Seu protocolo de atendimento é: " + data
  dados_mensagem = str(dados_mensagem)
  print(dados_mensagem)
  navegador = webdriver.Chrome(options=options)
  navegador.get('https://web.whatsapp.com/')
  element = False



  while(element == False):
    element = WebDriverWait(navegador, 120, poll_frequency=0.1).until(
    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div/div[1]/span")))
    print("entrou0")

  cont = 0
  for index,row in dados.iterrows():
    
    Telefone = (row['TEL'])
    
    sleep(0.8)
    navegador.get('https://wa.me/' + str(row['TEL']))
    sleep(2)
    element_inicia = False
    while(element_inicia == False):
        element_inicia = WebDriverWait(navegador, 120, poll_frequency=0.1).until(
        EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a/span")))
    iniciar_conversa = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a/span") 
    sleep(0.5)
    iniciar_conversa.click()
    sleep(4)
    whats_web = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a/span")
    sleep(4)
    whats_web.click()
    sleep(4)
    try:
        sleep(2)
        resposta_consulta = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
        retorno ='Nao enviada, verifique o numero!'
    except:
        
        
        element2 = False
        while(element2 == False):
            element2 = WebDriverWait(navegador, 120, poll_frequency=0.1).until(
            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
        
        campo_msg = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
        sleep(1)
 #        campo_msg.send_keys("Saque do FGTS sem complicações, somente na MAKTUB.")
        campo_msg.send_keys(str(dados_mensagem))
        sleep(0.5)
        btn_enviar = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")
        sleep(1)
        btn_enviar.click()
        btn_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")
        sleep(0.5)
        btn_contato.click()
        btn_contatos = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[5]/button/span")
        sleep(0.2)
        btn_contatos.click()
        sleep(0.3)
        procura_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]")
        sleep(0.2)
        procura_contato.send_keys("557130215455")
        sleep(0.2)
        contato_oficial = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[2]/button/div[2]/div/div[2]")
        sleep(0.2)
        contato_oficial.click()
        sleep(0.2)
        btn_envia_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/span/div/div/div")
        sleep(0.2)
        btn_envia_contato.click()
        sleep(0.2)
        btn = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div")
        btn.click()
        sleep(0.5)

        retorno ='Mensagem enviada com sucesso'


        if cont == 1:
            numero1 = "5571999617890"
            numero2 = "5571991471236"
            num_protocolo = "MAKTUB-ATENDIMENTO-23122022"
            navegador.get("https://wa.me/" + str(numero1))

            element_inicia = False
            while(element_inicia == False):
                element_inicia = WebDriverWait(navegador, 120, poll_frequency=0.1).until(
                EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a/span")))
            iniciar_conversa = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a/span") 
            sleep(0.5)
            iniciar_conversa.click()
            sleep(2.9)
            whats_web = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a/span")
            sleep(0.5)
            whats_web.click()
            
            element2 = False
            while(element2 == False):
                element2 = WebDriverWait(navegador, 120, poll_frequency=0.1).until(
                EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")))
             
            campo_msg = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
            sleep(1)
            campo_msg.send_keys("Olá, tudo bem? Teste numeros primos. " + "  Seu numero de protocolo é: " +str(num_protocolo) + str(cont))
            sleep(1)
            btn_enviar = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")
            sleep(1)
            btn_enviar.click()
        
        if cont == 2:
            numero2 = "5571991471236"
            navegador.get("https://wa.me/" + str(numero2))
        
            element_inicia = False
            while(element_inicia == False):
                element_inicia = WebDriverWait(navegador, 120, poll_frequency=0.1).until(
                EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a/span")))
            #iniciar_conversa = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a/span") 
            iniciar_conversa = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a/span") 
            sleep(0.5)
            iniciar_conversa.click()
            sleep(2.9)
            whats_web = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a/span")
            sleep(0.5)
            whats_web.click()
            
            element2 = False
            while(element2 == False):
                element2 = WebDriverWait(navegador, 120, poll_frequency=0.1).until(
                EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")))
             
            campo_msg = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
            sleep(1)
            campo_msg.send_keys("Olá, tudo bem? Teste numeros primos. " + "  Seu numero de protocolo é: " +str(num_protocolo) + str(cont))
            sleep(1)
            btn_enviar = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")
            sleep(1)
            btn_enviar.click()
        
        if cont ==5:
            cont = 0

        cont +=1
      
    with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:
 #        for retorno_whatsapp in retorno:
    
        retorno = retorno + ';'
        TelWPP = str(Telefone) + ';'
            
        verificaWpp = retorno + str(Telefone) +  "\n"
            
        f.write(verificaWpp)
        return str(verificaWpp)
'''


#------------------------------------------------------ janelas----------------------------------------



# Layouts

def janela_principal():
    sg.theme('LightBrown3')
    global telefones, mensagem, nomeDaCampanha, numContato

#    layout_l = [
#        [sg.Image(r'../BotWPP/Img/numconexoes.png', size=(250, 25), pad=(0, 0))], 
#        [sg.Radio('', "conex",key="1conexao", default=True, size=(0,0)), sg.Image(r'../BotWPP/Img/1conexao.png', size=(88, 25), pad=(0, 0))],
#        [sg.Radio('', "conex",key="2conexoes"), sg.Image(r'../BotWPP/Img/2conexoes.png', size=(95, 25), pad=(0, 0))],
#        [sg.Radio('', "conex", key="3conexoes"), sg.Image(r'../BotWPP/Img/3conexoes.png', size=(95, 25), pad=(0, 0))],        
#        [sg.Slider(range=(0,2),disable_number_display=True, s=(10,15), key='velocidade')],        
#    ]

#    layout_r = [
#        [sg.Image(r'../BotWPP/Img/numContato.png', size=(160, 25), pad=(0, 0))],
#        [sg.InputText(key ='num_contato')], 
#        [sg.In(key='TEL'), sg.FileBrowse(button_text='Arquivo',file_types=(("Text Files", "*.xlsx"),))],        
#        [sg.InputText(key ='nome_cam')],        
#        [sg.Image(r'../BotWPP/Img/msgwpp.png', size=(95, 25), pad=(0, 0))],
#		[sg.Multiline(size=(70, 10), enter_submits=False, write_only=False, key='MSG')],        
#
#    ]

    layout = [
        [sg.Image(r'../BotWPP/Img/numconexoes.png', size=(250, 25), pad=(0, 0))], 
        [sg.Radio('', "conex",key="1conexao", default=True, size=(0,0)), sg.Image(r'../BotWPP/Img/1conexao.png', size=(88, 25), pad=(0, 0))],
        [sg.Radio('', "conex",key="2conexoes"), sg.Image(r'../BotWPP/Img/2conexoes.png', size=(95, 25), pad=(0, 0))],
        [sg.Radio('', "conex", key="3conexoes"), sg.Image(r'../BotWPP/Img/3conexoes.png', size=(95, 25), pad=(0, 0))],        
        [sg.Image(r'../BotWPP/Img/numContato.png', size=(160, 25), pad=(0, 0))],
        [sg.InputText(key ='num_contato')], 
        [sg.Image(r'../BotWPP/Img/nomewpp.png', size=(160, 25), pad=(0, 0))],
        [sg.InputText(key ='nome_cam')],        
        [sg.Image(r'../BotWPP/Img/msgwpp.png', size=(95, 25), pad=(0, 0))],
		[sg.Multiline(size=(70, 10), enter_submits=False, write_only=False, key='MSG')],
 #      [sg.InputText(key ='MSG')],
  #      [sg.In(key='MSG'), sg.FileBrowse(button_text='Arquivo',file_types=(("Text Files", "*.txt"),))],
        [sg.Image(r'../BotWPP/Img/telwpp.png', size=(93, 25), pad=(0, 0))],
        [sg.In(key='TEL'), sg.FileBrowse(button_text='Arquivo',file_types=(("Text Files", "*.xlsx"),))],
        [sg.Button('',key='Enviar',pad=(140,0), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='../BotWPP/Img/enviarwpp.png', image_size=(210, 0), image_subsample=1, border_width=0)],
        [sg.Button('',key='Sair',pad=(140,0), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='../BotWPP/Img/sairwpp.png', image_size=(210, 0), image_subsample=1, border_width=0)],
        [sg.Image(r'../BotWPP/Img/logowpp.png', size=(500, 110))], 
    ]                                                                   
    return sg.Window('Bot Luzir Software', layout=layout, finalize=True) 

'''
def janela_1conexao():
    sg.theme('LightBrown3')
    layout = [
        [sg.Image(r'logo1conexao.png', size=(220, 40), pad=(120, 0))],         
        [sg.Multiline(size=(70, 10), enter_submits=False, write_only=False, key='textMen')],
        [sg.Multiline(size=(70, 10), enter_submits=False, write_only=False, key='textNum')],
        [sg.Image(r'logowpp.png', size=(500, 110))],              
    ]
    return sg.Window('Conexões', layout=layout, finalize=True,element_justification='center')


def janela_conexao2():
    sg.theme('LightBrown3')
    global telefones1, telefones2, mensagem1, mensagem2,  nomeDaCampanha 

    layout = [
        [sg.Image(r'logo1conexao.png', size=(220, 40), pad=(120, 0))], 
        [sg.Image(r'nomewpp.png', size=(160, 25), pad=(0, 0))],
        [sg.InputText(key ='nome_cam')],        
        [sg.Table(values='',headings=["Mensagem"],key="-TABLE-",size=(500,10),auto_size_columns=False,col_widths=[40,9,30],vertical_scroll_only=True,justification="l",font="None 15")],      
        [sg.Image(r'tel1wpp.png', size=(93, 25), pad=(0, 0))],
        [sg.In(key='TEL1'), sg.FileBrowse(file_types=(("Text Files", "*.xlsx"),))],
        [sg.Image(r'tel2wpp.png', size=(93, 25), pad=(0, 0))],
        [sg.In(key='TEL2'), sg.FileBrowse(file_types=(("Text Files", "*.xlsx"),))],        
        [sg.Button('',key='Enviar',pad=(140,0), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='enviarwpp.png', image_size=(210, 0), image_subsample=1, border_width=0)],
        [sg.Button('',key='Voltar',pad=(140,0), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='voltarwpp.png', image_size=(210, 0), image_subsample=1, border_width=0)],
        [sg.Button('',key='Sair',pad=(140,0), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='sairwpp.png', image_size=(210, 0), image_subsample=1, border_width=0)],

    ]
    return sg.Window('2 Conexões', layout=layout, finalize=True)

def janela_conexao3():
    sg.theme('LightBrown3')
    global telefones1, telefones2, telefones3, mensagem1, mensagem2, mensagem3, nomeDaCampanha

    layout = [
        [sg.Image(r'logo1conexao.png', size=(220, 50), pad=(120, 0))], 
        [sg.Image(r'nomewpp.png', size=(160, 25), pad=(0, 0))],
        [sg.InputText(key ='nome_cam')],        
        [sg.Image(r'msg1wpp.png', size=(95, 25), pad=(0, 0))],
        [sg.In(key='MSG1'), sg.FileBrowse(file_types=(("Text Files", "*.txt"),))],
        [sg.Image(r'msg2wpp.png', size=(95, 25), pad=(0, 0))],
        [sg.In(key='MSG2'), sg.FileBrowse(file_types=(("Text Files", "*.txt"),))], 
        [sg.Image(r'msg3wpp.png', size=(95, 25), pad=(0, 0))],
        [sg.In(key='MSG3'), sg.FileBrowse(file_types=(("Text Files", "*.txt"),))],                
        [sg.Image(r'tel1wpp.png', size=(93, 25), pad=(0, 0))],
        [sg.In(key='TEL1'), sg.FileBrowse(file_types=(("Text Files", "*.xlsx"),))],
        [sg.Image(r'tel2wpp.png', size=(93, 25), pad=(0, 0))],
        [sg.In(key='TEL2'), sg.FileBrowse(file_types=(("Text Files", "*.xlsx"),))],
        [sg.Image(r'tel3wpp.png', size=(93, 25), pad=(0, 0))],
        [sg.In(key='TEL3'), sg.FileBrowse(file_types=(("Text Files", "*.xlsx"),))],                  
        [sg.Button('',key='Enviar',pad=(140,0), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='enviarwpp.png', image_size=(210, 0), image_subsample=1, border_width=0)],
        [sg.Button('',key='Voltar',pad=(140,0), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='voltarwpp.png', image_size=(210, 0), image_subsample=1, border_width=0)],
        [sg.Button('',key='Sair',pad=(140,0), button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename='sairwpp.png', image_size=(210, 0), image_subsample=1, border_width=0)],

    ]
    return sg.Window('3 Conexões', layout=layout, finalize=True)
'''
# Janelas iniciais
janela0, janela1, janela2, janela3 = janela_principal(), None, None, None

#loop de eventos
while True:
    window, event, values = sg.read_all_windows()

  #--------------------- Janela principal -------------------- 
    if window == janela0:
    #Quando a janela for fechada
      if event == sg.WIN_CLOSED:
         window.close()
         break
    #Quando o botao Enviar for selecionado         
      if event == 'Enviar':
            #Quando a janela de 1 conexão for selecionada 
            if values["1conexao"] == True:
                telefones = values['TEL']
                mensagem = values['MSG']
                nomeDaCampanha = values['nome_cam']
                numContato =  values['num_contato']
                try:
                    wpp1conexao(mensagem, telefones, nomeDaCampanha, numContato)
                except  FileNotFoundError:
                    sg.popup_error('Arquivo .xlsx não encontrado ou inválido: :(', title='Erro', font='Courier 12')                       
                else:
                    window.close() 


            #Quando a janela de 2 conexão for selecionada 
            elif values["2conexoes"] == True:
                telefones = values['TEL']
                mensagem = values['MSG']
                nomeDaCampanha = values['nome_cam']
                numContato =  values['num_contato']                
                try:
                    wpp2conexoes(mensagem, telefones, nomeDaCampanha, numContato)
                except  FileNotFoundError:
                    sg.popup_error('Arquivo .xlsx não encontrado ou inválido: :(', title='Erro', font='Courier 12')                       
                else:
                    window.close() 

            #Quando a janela de 3 conexão for selecionada 
            elif values["3conexoes"] == True:
                telefones = values['TEL']
                mensagem = values['MSG']
                nomeDaCampanha = values['nome_cam']
                numContato =  values['num_contato']                
                try:
                    wpp3conexoes(mensagem, telefones, nomeDaCampanha, numContato)
                except  FileNotFoundError:
                    sg.popup_error('Arquivo .xlsx não encontrado ou inválido: :(', title='Erro', font='Courier 12')                       
                else:
                    window.close() 

      if event == 'Sair':
         telefones = ''
         mensagem = ''
         nomeDaCampanha = ''
         window.close()         

  #--------------------- Janela 1 conexao ---------------------------------------------       
'''
    if window == janela1:
      sleep(1)
      msg=lermensagem(mensagem)
      print(msg)
      window['textMen'].update(msg) 
      window.Refresh()
    
      #Quando a janela for fechada
      if event == sg.WIN_CLOSED:
         window.close()
         break

      #Quando o botao Voltar for selecionado 
      if event == 'Voltar':
         janela0.un_hide()
         janela1.hide()            
      #Quando o botao Sair for selecionado
      if event == 'Sair':
         telefones = ''
         mensagem = ''
         nomeDaCampanha = ''
         conexoes = ''
         window.close()
      #Quando o botao Enviar for selecionado
      if event == 'Enviar':

         telefones = values['TEL']
         mensagem = values['MSG']
         nomeDaCampanha = values['nome_cam']
         botwpp(telefones, mensagem, nomeDaCampanha)
         window.close()


  #--------------------- Janela conexao 2--------------------------------------------      
    if window == janela2:
      #Quando a janela for fechada
      if event == sg.WIN_CLOSED:
         window.close()
         break

      #Quando o botao Voltar for selecionado 
      if event == 'Voltar':
         janela0.un_hide()
         janela2.hide()            
      #Quando o botao Sair for selecionado
      if event == 'Sair':
         telefones = ''
         mensagem = ''
         nomeDaCampanha = ''
         window.close() 
      #Quando o botao Enviar for selecionado         
      if event == 'Enviar':
         telefones1 = values['TEL1']
         telefones2 = values['TEL2']         
         mensagem1 = values['MSG1']
         mensagem2 = values['MSG2']         
         nomeDaCampanha = values['nome_cam']
         botwpp2(telefones1, telefones2,  mensagem1, mensagem2, nomeDaCampanha)
         window.close()             

  #--------------------- Janela conexao 3--------------------------------------------       
    if window ==  janela3:
    #Quando a janela for fechada
      if  event == sg.WIN_CLOSED:
         window.close()
         break

      #Quando o botao Voltar for selecionado 
      if event == 'Voltar':
         janela0.un_hide()
         janela3.hide()            
      #Quando o botao Sair for selecionado
      if event == 'Sair':
         telefones = ''
         mensagem = ''
         nomeDaCampanha = ''
         conexoes = ''
         window.close()
      #Quando o botao Enviar for selecionado         
      if event == 'Enviar':
         telefones1 = values['TEL1']
         telefones2 = values['TEL2']
         telefones3 = values['TEL3']         
         mensagem1 = values['MSG1']
         mensagem2 = values['MSG2'] 
         mensagem3 = values['MSG3']        
         nomeDaCampanha = values['nome_cam']
         botwpp3(telefones1, telefones2, telefones3,  mensagem1, mensagem2, mensagem3, nomeDaCampanha)
         window.close()          
'''
    



 




#janela()
#botwpp()
#print(nomeDaCampanha)
#print(telefones)
#print(mensagem)
#print(numConexoes)
sleep(1000)