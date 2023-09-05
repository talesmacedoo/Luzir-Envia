from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import*
from tkinter import messagebox
import os
import threading
import tkinter.messagebox
from tkinter import filedialog
import customtkinter
import pandas as pd
from tkinter.ttk import *
from bs4 import BeautifulSoup
from time import sleep  
from PIL import Image 
import requests
import json
from key_chatbot import *



customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"




class Janela(customtkinter.CTk):
    """
    Classe principal do aplicativo
    """
    def __init__(self):
        super().__init__()

        # configure window
        self.title("BotWPP V2 - LuzirSoftware.py")
        self.geometry(f"{1030}x{750}")
        self.resizable(False,False)

        # configure grid layout (4x4)
        #self.grid_columnconfigure(1, weight=0)
     #   self.grid_columnconfigure((2, 3), weight=0)
     #   self.grid_rowconfigure((0, 1, 2), weight=1)

        #Barra de configuração
        self.config_frame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.config_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.config_frame.grid_rowconfigure(4, weight=1)         
       # self.numConexoes_frame = customtkinter.CTkFrame(self)
       # self.numConexoes_frame.grid(row=0, column=0, padx=(20, 20), pady=(20, 0), sticky="n")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_conexoes = customtkinter.CTkLabel(master=self.config_frame, text="Selecione o número de conexões:", font=("Roboto", 14))
        self.label_conexoes.grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="n")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.config_frame, variable=self.radio_var, value=0, text= "1 conexão")
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20)
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.config_frame, variable=self.radio_var, value=1, text= "2 conexões")
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20)
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.config_frame, variable=self.radio_var, value=2, text= "3 conexões")
        self.radio_button_3.grid(row=3, column=0, pady=10, padx=0)

        self.navegador_label = customtkinter.CTkLabel(self.config_frame, text="Modo de Navegador:", anchor="w")
        self.navegador_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.navegador_wpp = customtkinter.CTkOptionMenu(self.config_frame, values=["Navegador 1", "Navegador 2", "Navegador 3", "Navegador 4"])
        self.navegador_wpp.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.var_switch_contato = customtkinter.StringVar(value="on")
        #def switch_event():
        #    print("switch toggled, current value:", switch_var.get())

        self.switch_contato = customtkinter.CTkSwitch(master=self.config_frame, text="Enviar contato",
                                        variable=self.var_switch_contato, onvalue="on", offvalue="off")
        self.switch_contato.grid(row=8, column=0, padx=47 , pady=10,sticky="nsew")
        self.var_switch_mensagens = customtkinter.StringVar(value="on")

        self.switch_mensagens = customtkinter.CTkSwitch(master=self.config_frame, text="Enviar mensagens",
                                        variable=self.var_switch_mensagens, onvalue="on", offvalue="off")
        self.switch_mensagens.grid(row=9, column=0, padx=0 , pady=10)        
        
        self.velocidade_label = customtkinter.CTkLabel(self.config_frame, text="Velocidade do Envio:", anchor="w")
        self.velocidade_label.grid(row=10, column=0, padx=20, pady=0)
        self.velocidade_mode_optionemenu = customtkinter.CTkOptionMenu(self.config_frame, values=["Lento", "Normal", "Rápido"])
        self.velocidade_mode_optionemenu.grid(row=11, column=0, padx=10, pady=10)        
        self.aparencia_label = customtkinter.CTkLabel(self.config_frame, text="Modo de Aparência:", anchor="w")
        self.aparencia_label.grid(row=12, column=0, padx=20, pady=(10, 0))
        self.aparencia_mode_optionemenu = customtkinter.CTkOptionMenu(self.config_frame, values=["Light", "Dark"],
                                                                       command=self.mudanca_aparencia)
        self.aparencia_mode_optionemenu.grid(row=13, column=0, padx=20, pady=(10, 10))

        # Caixa de texto
        self.tabview = customtkinter.CTkTabview(self, width=360, height=585 )
        self.tabview.grid(row=0, column=1, padx=(10, 0), pady=(0, 0), sticky="n")
        self.tabview.add("Mensagem 1")
        self.tabview.add("Mensagem 2") 
        self.tabview.tab("Mensagem 1").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Mensagem 2").grid_columnconfigure(0, weight=1)   
        self.textbox_msg1 = customtkinter.CTkTextbox(self.tabview.tab("Mensagem 1"), width=300, height=260)
        self.textbox_msg1.grid(row=0, column=0, padx=20, pady=20)
        self.check_var = tkinter.StringVar(value="off")
        self.checkbox_msg2 = customtkinter.CTkCheckBox(self.tabview.tab("Mensagem 2"),text="Ativar mensagem 2", command=self.ativa_msg2,
                                     variable=self.check_var, onvalue="on", offvalue="off")   
        self.checkbox_msg2.grid(row=0, column=0)                                  
        self.textbox_msg2 = customtkinter.CTkTextbox(self.tabview.tab("Mensagem 2"), width=300, height=260)
        self.textbox_msg2.grid(row=1, column=0, padx=20, pady=20)                                       
        self.check_var_img = tkinter.StringVar(value="off")
        self.checkbox_img = customtkinter.CTkCheckBox(self.tabview.tab("Mensagem 1"),text="Ativar imagem", command=self.ativa_img,
                                     variable=self.check_var_img, onvalue="on", offvalue="off")
        self.checkbox_img.grid(row=1, column=0)
        self.my_image = customtkinter.CTkImage(light_image=Image.open("enviarwpp.png"),
                                        size=(180, 180))

        self.envio_img = customtkinter.CTkButton(self.tabview.tab("Mensagem 1"), image=self.my_image, text="",fg_color="transparent")
        self.envio_img.grid(row=2, column=0)
        #self.img_selecionada = PhotoImage(file="enviarwpp.png")  
        #self.envio_img =  customtkinter.CTkLabel(self.tabview.tab("Mensagem 1"), image=self.img_selecionada, text=None)
        #self.envio_img.grid(row=2, column=0, pady=20)            



        #Campanha     
        self.campanha_frame = customtkinter.CTkFrame(self)
        self.campanha_frame.grid(row=0, column=2, padx=10, pady=17, sticky="nsew")
        self.label_campanha = customtkinter.CTkLabel(master=self.campanha_frame, text="Campanha:", font=("Roboto", 14))
        self.label_campanha.grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="n")         
        self.nomeCam = customtkinter.CTkEntry(master=self.campanha_frame, placeholder_text="Nome da Campanha", width=350)
        self.nomeCam.grid(row=1, column=0, padx=10, pady=20)
        self.numContato= customtkinter.CTkEntry(master=self.campanha_frame, placeholder_text="Contato Oficial", width=350)
        self.numContato.grid(row=2, column=0, padx=10, pady=20)      
        self.caminho_telefone = customtkinter.CTkLabel(master=self.campanha_frame, text="Arquivo Telefone")
        self.caminho_telefone.grid(row=3, column=0, padx=0, pady=0)
        self.browse_file = customtkinter.CTkButton(master=self.campanha_frame, command=self.browseFilesTel, text="Arquivo")
        self.browse_file.grid(row=4, column=0, padx=0, pady=0) 
        self.textbox_tel = customtkinter.CTkTextbox(master=self.campanha_frame, width=260, height=150)
        self.textbox_tel.grid(row=5, column=0, padx=20, pady=10)        
        self.numPrimos1 = customtkinter.CTkEntry(master=self.campanha_frame, placeholder_text="Número primo 1", width=350)
        self.numPrimos1.grid(row=6, column=0, padx=10, pady=20)
        self.numPrimos2 = customtkinter.CTkEntry(master=self.campanha_frame, placeholder_text="Número primo 2", width=350)
        self.numPrimos2.grid(row=7, column=0, padx=10, pady=20)                 

     #Envio
        #Frame de 
        self.envio_frame = customtkinter.CTkFrame(self)
        self.envio_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=0, sticky="nsew")
        self.btn_enviar = customtkinter.CTkButton(master=self.envio_frame, command=self.validador, text="Enviar")
        self.btn_enviar.grid(row=0, column=0, padx=300,pady=10, sticky="nsew")
        self.btn_verificar = customtkinter.CTkButton(master=self.envio_frame, command=self.verificar_wpp, text="Verificar WhatsAPP", fg_color="green")
        self.btn_verificar.grid(row=1, column=0, padx=300,pady=10, sticky="nsew")        
        self.btn_sair = customtkinter.CTkButton(master=self.envio_frame, command=self.destroy, text="Sair", fg_color="red")
        self.btn_sair.grid(row=2, column=0, padx=300,pady=10, sticky="nsew")

     #Configurações
        #Pré-configurações 
        self.textbox_msg2.configure(state="disabled")    
        self.textbox_tel.configure(state="disabled") 
        self.envio_img.configure(state="disabled")     

    def mudanca_aparencia(self, new_appearance_mode: str):
        """
        Método para alterar a aparência da tela de login  
        """        
        customtkinter.set_appearance_mode(new_appearance_mode)


    def lista_telefone(self, arquivo: str):
        pass    

    def ativa_img(self):
        """
        Método para buscar uma imagem no computador e habilitar o seu envio
        """

        if self.checkbox_img.get() == "on":
            self.img_filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select a File",
                                                filetypes = (("img files",
                                                                "*.png*"),
                                                            ("all files",
                                                                "*.*")))
            self.my_image.configure(light_image=Image.open(str(self.img_filename)),
                                        size=(180, 180))    
                                                           
    def updatee(self):
        self.update()
        print("oi")

    def ativa_msg2(self):
        """
        Método para ativar o segundo campo de mensagem 
        """
        print("checkbox toggled, current value:", self.check_var.get())  
        if self.check_var.get() == "on":
                self.textbox_msg2.configure(state="normal")
        else: 
                self.textbox_msg2.configure(state="disabled")

     #   def janela_2(self):
      #       self.retorno_frame = customtkinter.CTkFrame(self)
      #       self.retorno_frame.grid(row=0, column=0, columnspan=2, padx=100, pady=30, sticky="nsew")
      #       self.textbox_retorno = customtkinter.CTkTextbox(master=self.retorno_frame, width=500, height=460)
     #       self.textbox_retorno.grid(row=0, column=0, padx=20, pady=20)
     #       self.barra_progresso = customtkinter.CTkProgressBar(self.retorno_frame, width=500)
     #       self.barra_progresso.grid(row=1, column=0, rowspan=5, padx=(10, 20), pady=(15, 10), sticky="ns")        
    def verificar_wpp(self):
        """
        Método para verificar se o arquivo foi importado
        """
        if self.textbox_tel.get("1.0",'end-1c') == "":
             messagebox.showerror(title="Erro", message="Importe o arquivo de telefone")
        else:
            self.verificador(self.filename)     

    def validador(self):
        """
        Método para validar se os campos foram preenchidos 
        """
        if self.nomeCam.get() == "":
             messagebox.showerror(title="Erro", message="Preencha o nome da campanha")

        elif self.numContato.get() == "" and self.var_switch_contato.get()=="on":
             messagebox.showerror(title="Erro", message="Preencha o número de contato")

        elif self.numPrimos1.get() == "" or self.numPrimos2.get() == "" :
             messagebox.showerror(title="Erro", message="Preencha os dois números primos")  
        else:
            self.Luzir_wpp()
            pass    
    
    


    def bot_wpp(self):
        """
        Método para iniciar a tela de retorno do envio e o o bot de whatsapp 
        """          
        t1 = threading.Thread(target=self.tela_envio())
        t2 = threading.Thread(target=self.Luzir_wpp())

        t1.start()
        t1.join()
        sleep(2)
        t2.start()
        t2.join()


 #   def tela_envio(self):
 #       """
 #       Método para alterar a tela de login e transformar na tela de envio  
 #       """          
 #       self.config_frame.grid_remove()
 #       self.campanha_frame.grid_remove()
 #       self.tabview.grid_remove()
 #       self.envio_frame.grid_remove()
 #       self.geometry(f"{730}x{680}")
 #       self.retorno_frame = customtkinter.CTkFrame(self)
 #       self.retorno_frame.grid(row=0, column=0, columnspan=2, padx=100, pady=30, sticky="nsew")
 #       self.textbox_retorno = customtkinter.CTkTextbox(master=self.retorno_frame, width=500, height=460)
 #       self.textbox_retorno.grid(row=0, column=0, padx=20, pady=20)
 #       self.barra_progresso = customtkinter.CTkProgressBar(self.retorno_frame, width=500, mode="determinate")
 #       self.barra_progresso.grid(row=1, column=0, rowspan=5, padx=(10, 20), pady=(15, 10), sticky="ns")
        #self.update()

        

    def Luzir_wpp(self):

        """
        Método principal do bot whatsapp  
        """  


        #self.updatee
        if self.velocidade_mode_optionemenu.get() == "Lento":
            var_velocidade =  120
        elif self.velocidade_mode_optionemenu.get() == "Normal":
            var_velocidade =  90  
        elif self.velocidade_mode_optionemenu.get() == "Rápido":
            var_velocidade =  60                       
        btn_msg2 = self.check_var.get()
        mensagem1 = self.textbox_msg1.get("1.0",'end-1c')
        mensagem2 = self.textbox_msg2.get("1.0",'end-1c')        
        numContato =  self.numContato.get()
        telefones = self.filename
        numprimo1 = self.numPrimos1.get()
        numprimo2 = self.numPrimos2.get()
        nomeDaCampanha = self.nomeCam.get()
        var_contato = self.var_switch_contato.get()
        var_img = self.checkbox_img.get()
        tipo_navegador = self.navegador_wpp.get()

         

        def formata_mensagem(mensagem1, mensagem2, varDaMensagem, Nome):
            """
            Método para formatar a mensagem e alterar o campo @nome na mensagem pelo nome relacionado ao CPF
            """
           # self.update()
            if btn_msg2 == "off":
                mensagemform = mensagem1
                mensagemform = mensagemform.replace("@nome", str(Nome))
                mensagemform = mensagemform.split("\n")
                
            else:
                if (varDaMensagem%2) == 0:
                    mensagemform = mensagem1
                    mensagemform = mensagemform.replace("@nome", str(Nome))
                    mensagemform = mensagemform.split("\n")
                    
                else:
                    mensagemform = mensagem2
                    mensagemform = mensagemform.replace("@nome", str(Nome))
                    mensagemform = mensagemform.split("\n")
                    
            return mensagemform
        def envia_mensagem(mensagem, navegador, numContato):
                """
                Método que recebe a mensagem, o navegador, o contato a ser enviado e realiza o envio da mensagem através do XPATH 
                """
                #self.update()
            #try:
                #navegador.maximize_window()
                element2 = False
                while(element2 == False):
                    element2 = WebDriverWait(navegador, 240, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")))
                                                                       
                campo_msg = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
                for msg in mensagem:
                    campo_msg.send_keys(msg)
                    campo_msg.send_keys(Keys.SHIFT,'\n')
                campo_msg.send_keys("\n")
                sleep(5)
                if var_contato == "on":
                   # try:                                                        
                        btn_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")
                        sleep(0.6)
                        btn_contato.click()
                        sleep(0.7)                                                
                        btn_contatos = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[5]/button/span")
                        sleep(0.4)
                        btn_contatos.click()
                        sleep(1)
                        #procura_contato = navegador.find_element(by=By.CSS_SELECTOR, value="span[data-icon='chat-list-search']")   
                        #procura_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]")
                        procura_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p")

                        sleep(0.3)
                        procura_contato.send_keys(str(numContato))
                        sleep(0.6)
                        contato_oficial = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[2]/button/div[2]/div/div[2]/div[1]/div/span")
                        sleep(1.6)
                        contato_oficial.click()
                        sleep(0.3)
                        btn_envia_contato = navegador.find_element(by=By.CSS_SELECTOR, value="span[data-icon='send']")
                        sleep(4.0)
                        btn_envia_contato.click()
                        sleep(2.2)
                        btn = navegador.find_element(by=By.CSS_SELECTOR, value="span[data-icon='send']")
                        sleep(0.5)
                        btn.click()
                        sleep(0.9) 
                    #except:
                    #    print("Erro do stale")
                    #    btn_envia_contato = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/span/div/div/div")
                    #    sleep(2.2)
                    #    btn_envia_contato.click()
                    #    sleep(1.2)
                    #    btn = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div")
                    #    sleep(0.5)
                    #    btn.click()
                    #    sleep(0.9) 
                    #    pass        

                if var_img == "on":
                    sleep(1.9)
                    btn_clip = navegador.find_element(by=By.CSS_SELECTOR, value="span[data-icon='clip']") 
                    btn_clip.click() 
                    sleep(0.3)
                    #btn_img = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/span") 
                    # btn_img.click()
                    input_box = navegador.find_element(by=By.TAG_NAME, value= 'input')
                    file_path= str(self.img_filename)
                    file_path = file_path.replace("\ ", "/")
                    #print(file_path)
                    input_box.send_keys(file_path)     
                    sleep(2) 

                    #btn_img = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p") 
                    #btn_img.send_keys("\n")  
                    btn_envia_contato = navegador.find_element(by=By.CSS_SELECTOR, value="span[data-icon='send']")
                    sleep(4.0)                                     
                    btn_envia_contato.click()                                                        
                    sleep(2)   

        def num_primo(cont, navegador):
            """
            Método para enviar uma mensagem diferente da Copy que está sendo disparada, com o intuito de evitar bloqueios 
            """
            #self.update()
            try:
                if cont == 1:
                    numero = str(numprimo1)
                    num_protocolo = "MAKTUB-ATENDIMENTO-23122022"
                    navegador.get("https://web.whatsapp.com/send/?phone=" + str(numero) + "&text&type=phone_number&app_absent=0")

                    element_inicia = False
                    while(element_inicia == False):
                        element_inicia = WebDriverWait(navegador, 240, poll_frequency=0.1).until(
                        EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
                    
                
                    campo_msg = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
                    sleep(1)
                    campo_msg.send_keys("Olá, tudo bem? Teste numeros primos. " + "  Seu numero de protocolo é: " +str(num_protocolo))
                    sleep(1)
                    campo_msg.send_keys("\n")
                    #btn_enviar = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")
                    sleep(1)
                    #btn_enviar.click()
                    sleep(0.3)




                elif cont == 3:
                    numero = str(numprimo2)
                    num_protocolo = "MAKTUB-ATENDIMENTO-23122022"
                    navegador.get("https://web.whatsapp.com/send/?phone=" + str(numero) + "&text&type=phone_number&app_absent=0")

                    element_inicia = False
                    while(element_inicia == False):
                        element_inicia = WebDriverWait(navegador, 240, poll_frequency=0.1).until(
                        EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))

                    campo_msg = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
                    sleep(1)
                    campo_msg.send_keys("Olá, tudo bem? Teste numeros. " + "  Seu numero de protocolo é: " +str(num_protocolo) + str(cont))
                    sleep(1)
                    campo_msg.send_keys("\n")
                    #btn_enviar = navegador.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span")
                    sleep(1)
                    #btn_enviar.click()
                    #sleep(0.3)
            except:  
                print("Erro do num primo")
                pass        

        def wpp1conexao(mensagem1,mensagem2, telefones, nomeDaCampanha, numContato):
            """
            Método para a apenas um conexão de envio
            """
            #self.update()
         #  dados_mensagem = str(mensagem)     
            dados =  pd.read_excel(telefones)
            options = Options() 
            options.headless = False # Visivel
            print(dados)
            quantidade = len(dados) - 1

            dir_path = os.getcwd()
            profile = os.path.join(dir_path, "profile", str(tipo_navegador))
            options = webdriver.ChromeOptions()
            options.add_argument(
                r"user-data-dir={}".format(profile))

            navegador1 = webdriver.Chrome("./chromedriver.exe", chrome_options=options)

            #NAVEGADOR#
            #navegador1 = webdriver.Chrome(options=options)
            navegador1.get('https://web.whatsapp.com/')
            element = False
            
            while(element == False):
                #self.update()
                element = WebDriverWait(navegador1, 999, poll_frequency=0.1).until(
                EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]")))
                print("entrou0")
                
            #Variáveis 
            varDaMensagem = 1
            cont1 = 0
            #options.add_argument("--headless")
            for index,row in dados.iterrows():
                #self.update()
                Telefone = (row['TEL'])
                Nome = (row['NOME'])
                mens = formata_mensagem(mensagem1,mensagem2,varDaMensagem, Nome)

                TelWPP = Telefone
                sleep(1)
                print(Telefone)


                navegador1.get('https://web.whatsapp.com/send/?phone=' + str(row['TEL']) +'&text&type=phone_number&app_absent=0')
                sleep(1)
                try:
                    element_inicia = False
                    while(element_inicia == False):
                        element_inicia = WebDriverWait(navegador1, 20, poll_frequency=0.1).until(
                        EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")))

                except:

                    print("saiu")
                    sleep(2)
                    #resposta_consulta = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                    retorno ='Não enviado '
                    #btn_ok = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                    
                    #btn_ok.click()
                else:
                    Nome = (row['NOME'])
                    mens = formata_mensagem(mensagem1,mensagem2,varDaMensagem, Nome)
                    envia_mensagem(mens, navegador1, numContato)  
                    retorno ='Enviado '
                    varDaMensagem +=1
                    if cont1 == 1 or cont1 == 3:
                        num_primo(cont1, navegador1)
                        
                    elif cont1 == 5:
                        cont1 = -1

                    cont1 +=1
                with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                        retorno = retorno + ';'
                        TelWPP = str(Telefone) + ';'
                        Nome = Nome + ";"
                        
                        verificaWpp = retorno + TelWPP + Nome +  "\n"
                        #self.update()
                        #self.textbox_retorno.insert("0.0",str(verificaWpp))
                        #self.update()     
                        f.write(verificaWpp) 
                sleep(var_velocidade)



        def wpp2conexoes(mensagem1,mensagem2, telefones, nomeDaCampanha, numContato):
            """
            Método para envio de duas conexões simuntâneas 
            """
            
            dados =  pd.read_excel(telefones)
            #self.updatee
            def RetornaDados(dados):
                nome = []
                cpf = []
                num = []
                mrg = []
                for index,row in dados.iterrows():

                    Nome = (row['NOME'])
                    Cpf = (row['CPF'])
                    Num =  (row['TEL'])
                    Mrg = (row['MRG'])
                    cpf.append(Cpf)
                    nome.append(Nome)
                    num.append(Num)
                    mrg.append(Mrg)
                return cpf,nome,num, mrg
            Cpfs, Nomes, Nums, Mrgs  = RetornaDados(dados)

            options = Options()
            options.headless = False # Visivel
            def wpp1():
                quantidade = len(dados) - 1

                #NAVEGADOR 1#
                navegador1 = webdriver.Chrome(options=options)
                navegador1.get('https://web.whatsapp.com/')
                element = False

                print("teste 1")
                #self.update()
                while(element == False):
                                    
                    element = WebDriverWait(navegador1, 999, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]")))
                print("entrou0")
                #self.update()
                #Variáveis
                cont1 = 0
                vardonavegador1 = 0 
                varDaMensagem = 1
                for index,row in dados.iterrows():
                    #self.update()
                    if quantidade < vardonavegador1:
                        print("finalizou1")
                        break
                    Telefone = Nums[vardonavegador1]      
                    cpf1 =  Cpfs[vardonavegador1]    
                    nome1 = Nomes[vardonavegador1]
                    print("teste 2")
                    mens = formata_mensagem(mensagem1,mensagem2,varDaMensagem,nome1)
                    print("teste 3")
                    sleep(1)

                    navegador1.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                    sleep(1)
                    try:
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador1, 20, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")))

                    except:

                        print("Não enviado 1")
                        sleep(2)
                        #resposta_consulta = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ="Não enviado 1"
                        #btn_ok = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                        
                        #btn_ok.click()
                        vardonavegador1 += 2
                    else:
                            
                        envia_mensagem(mens, navegador1, numContato)    
                        retorno ='Enviado 1'
                        vardonavegador1 += 2
                        varDaMensagem +=1                        
                        print("enviado 1" )
                        if cont1 == 1 or cont1 == 3:
                            num_primo(cont1, navegador1)
                            
                        elif cont1 == 5:
                            cont1 = -1

                        cont1 +=1
                    with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                            verificaWpp = retorno +";" + str(Telefone) +";" + str(nome1) + ";" + str(cpf1) + "\n"
                            #self.update()
                            #self.textbox_retorno.insert("0.0",str(verificaWpp))
                            #self.update()            
                            f.write(verificaWpp)             
                    sleep(var_velocidade)

            def wpp2():  
                quantidade = len(dados) - 1      
                #NAVEGADOR 2#
                navegador2 = webdriver.Chrome(options=options)
                navegador2.get('https://web.whatsapp.com/')
                element2 = False
                #sleep(40)
                #self.update()
                while(element2 == False):
                    
                    element2 = WebDriverWait(navegador2, 999, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]")))
                print("entrou2")  
                #self.updatee
                #Variáveis
                cont2 = 0 
                vardonavegador2 = 1  
                varDaMensagem2 =1
                for index,row in dados.iterrows():
                    #self.updatee()
                    if quantidade < vardonavegador2:
                        print("finalizou2")
                        break
                    
                    sleep(1)
                    Telefone = Nums[vardonavegador2]              
                    cpf2 =  Cpfs[vardonavegador2]
                    nome2 = Nomes[vardonavegador2]
                    mens = formata_mensagem(mensagem1,mensagem2,varDaMensagem2, nome2)
                    navegador2.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text='+str(mens)+'&type=phone_number&app_absent=0')
                    sleep(1)

                    try:
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador2, 20, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")))

                    except:

                        print("nao enviado 2" )
                        sleep(2)
                        #resposta_consulta = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ='Nao enviado 2'
                        #btn_ok = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                        
                        #btn_ok.click()
                        vardonavegador2 += 2
                    else:
                        
                        
                        envia_mensagem(mens, navegador2, numContato)
                        retorno ='Enviado 2'
                        print("enviado 2")
                        vardonavegador2 += 2
                        varDaMensagem2 +=1                        


                        if cont2 == 1 or cont2 == 3:
                            num_primo(cont2, navegador2)
                            
                        elif cont2 == 5:
                            cont2 = -1

                        cont2 +=1
                    with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                            verificaWpp = retorno +";" + str(Telefone) +";" + str(cpf2) + "\n"
                            #self.updatee()
                            #self.textbox_retorno.insert("0.0",str(verificaWpp))
                            #self.updatee()                           
                            f.write(verificaWpp)    
                    sleep(var_velocidade)

            #t1 = threading.Thread(target=self.tela_envio)
            t2 = threading.Thread(target=wpp1)
            t3 = threading.Thread(target=wpp2)

           # t1.start()
            t2.start()
            t3.start()
           # self.updatee
           # t1.join()
            t2.join()
            t3.join()

        def wpp3conexoes(mensagem1,mensagem2, telefones, nomeDaCampanha, numContato):
            """
            Método de envio para três conexões simuntaneas 
            """
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
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]")))
                    print("entrou0")

                #Variáveis 
                cont1 = 0
                vardonavegador1 = 0 
                varDaMensagem = 1
                for index,row in dados.iterrows():
                    
                    if quantidade < vardonavegador1:
                        print("finalizou1")
                        break
                    Telefone = Nums[vardonavegador1]      
                    cpf1 =  Cpfs[vardonavegador1]    
                    nome1 = Nomes[vardonavegador1]
                    mens = formata_mensagem(mensagem1,mensagem2,varDaMensagem,nome1)
                    sleep(1)



                    navegador1.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                    sleep(1)
                    try:
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador1, 20, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")))

                    except:

                        print("Nao enviado 1" )
                        sleep(2)
                        #resposta_consulta = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ="Não enviado 1"
                        #btn_ok = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                        
                        #btn_ok.click()
                        vardonavegador1 += 3
                    else:
                            
                        envia_mensagem(mens, navegador1, numContato)
                        retorno ='Enviado 1'
                        vardonavegador1 += 3
                        varDaMensagem = 1
                        print("enviado 1" )
                        if cont1 == 1 or cont1 == 3:
                            num_primo(cont1, navegador1)
                            
                        elif cont1 == 5:
                            cont1 = -1
                        
                        cont1 +=1
                    with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                        verificaWpp = retorno +";" + str(Telefone) +";" + str(nome1) +";" + str(cpf1) + "\n"
                        
                        #self.textbox_retorno.insert("0.0",str(verificaWpp))
                                                        
                        f.write(verificaWpp)             
                    sleep(var_velocidade)

            def wpp2():  
                quantidade = len(dados) - 1      
                #NAVEGADOR 2#
                navegador2 = webdriver.Chrome(options=options)
                navegador2.get('https://web.whatsapp.com/')
                element = False
                while(element == False):
                    element = WebDriverWait(navegador2, 999, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]")))
                    print("entrou0")  

                #Variáveis
                cont2 = 0 
                vardonavegador2 = 1    
                varDaMensagem2 = 1
                print(vardonavegador2)
                for index,row in dados.iterrows():
                    if quantidade < vardonavegador2:
                        print("finalizou2")
                        break

                    sleep(1)
                    Telefone = Nums[vardonavegador2]              
                    cpf2 =  Cpfs[vardonavegador2]
                    nome2 = Nomes[vardonavegador2]
                    mens = formata_mensagem(mensagem1,mensagem2,varDaMensagem2, nome2)
                    navegador2.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                    sleep(1)

                    try:
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador2, 20, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")))

                    except:

                        print("nao enviado 2" )
                        sleep(2)
                        #resposta_consulta = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ='Nao enviado 2'
                        #btn_ok = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")
                        
                        #btn_ok.click()
                        vardonavegador2 += 3
                    else:
                        #cpf2 =  Cpfs[vardonavegador2]
                        #nome2 = Nomes[vardonavegador2]
                        #mens = formata_mensagem(mensagem1,mensagem2,varDaMensagem2, nome2)                        
                        envia_mensagem(mens, navegador2, numContato)
                        retorno ='Enviado 2'
                        print("enviado 2")                
                        vardonavegador2 += 3
                        varDaMensagem2 +=1

                        if cont2 == 1 or cont2 == 3:
                            num_primo(cont2, navegador2)
                            
                        elif cont2 == 5:
                            cont2 = -1

                        cont2 +=1
                    with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                            verificaWpp = retorno +";" + str(Telefone) +";" + str(cpf2) + "\n"
                            
                            #self.textbox_retorno.insert("0.0",str(verificaWpp))
                                                        
                            f.write(verificaWpp)    
                    sleep(var_velocidade)

            def wpp3():  
                quantidade = len(dados) - 1 

                     
                #NAVEGADOR 3#
                navegador3 = webdriver.Chrome(options=options)
                navegador3.get('https://web.whatsapp.com/')
                element = False
                while(element == False):
                    element = WebDriverWait(navegador3, 999, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]")))
                    print("entrou0")  

                #Variáveis
                cont3 = 0 
                vardonavegador3 = 2
                varDaMensagem3 = 1    
                for index,row in dados.iterrows():
                    
                    if quantidade < vardonavegador3:
                        print("finalizou2")
                        break
                    sleep(1)
                    Telefone = Nums[vardonavegador3]              
                    cpf3 =  Cpfs[vardonavegador3]
                    nome3 = Nomes[vardonavegador3]
                    mens = formata_mensagem(mensagem1,mensagem2,varDaMensagem3, nome3)
                    navegador3.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                    sleep(1)

                    try:
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador3, 20, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]")))

                    except:

                        print("nao enviado 3" )
                        sleep(2)
                        #resposta_consulta = navegador3.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ='Nao enviado 3'
                        #btn_ok = navegador3.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                        
                        #btn_ok.click()
                        vardonavegador3 += 3
                    else:
                        #cpf3 =  Cpfs[vardonavegador3]
                        #nome3 = Nomes[vardonavegador3]
                        #mens = formata_mensagem(mensagem1,mensagem2,varDaMensagem3, nome3)                        
                        envia_mensagem(mens, navegador3, numContato)
                        retorno ='Enviado 3'
                        print("enviado 3")
                        vardonavegador3 += 3
                        varDaMensagem3 +=1

                        if cont3 == 1 or cont3 == 3:
                            num_primo(cont3, navegador3)
                            
                        elif cont3 == 5:
                            cont3 = -1

                        cont3 +=1
                    with open (str(nomeDaCampanha)+".csv",'a',newline='', encoding='UTF-8') as f:        
                            verificaWpp = retorno +";" + str(Telefone) +";" + str(cpf3) + "\n"
                            
                            #self.textbox_retorno.insert("0.0",str(verificaWpp))
                                                        
                            f.write(verificaWpp)                 
                    sleep(var_velocidade)

            wt1 = threading.Thread(target=wpp1)
            wt2 = threading.Thread(target=wpp2)
            wt3 = threading.Thread(target=wpp3)      

            wt1.start()
            wt2.start()
            wt3.start()
            
            wt1.join()
            wt2.join()
            wt3.join()             

        #Chamando a função de acordo com o número de conexões
        if self.radio_var.get() == 0:
            wpp1conexao(mensagem1,mensagem2, telefones, nomeDaCampanha, numContato)
        elif self.radio_var.get() == 1:
            wpp2conexoes(mensagem1,mensagem2, telefones, nomeDaCampanha, numContato)
        elif self.radio_var.get() == 2:
            wpp3conexoes(mensagem1,mensagem2, telefones, nomeDaCampanha, numContato)   

    def verificador(self, telefones):
        """
        Método que recebe um arquivo com telefones e verifica se eles são WhastApp
        """
        SWpp = 0
        NWpp = 0
        dados =  pd.read_excel(telefones)
        nome_arquivo = telefones.split("/")
        nome_arquivo = nome_arquivo[-1]
        nome_arquivo = nome_arquivo.replace(".xlsx", "")
        options = Options()
        options.headless = False # Visivel
        #print(dados)
        quantidade = len(dados) - 1
        with open (str(nome_arquivo)+ "validados.csv",'a',newline='', encoding='UTF-8') as f:        
            
                      
            verificaWpp = "TEL" + ";" + "NOME" + ";" + "CPF"+ ";" + "MRG" + ";" + "MAT" + "\n"
                
            f.write(verificaWpp)

        with open (str(nome_arquivo)+ "invalidos.csv",'a',newline='', encoding='UTF-8') as f:        
            
                       
            verificaWpp = "TEL" + ";" + "NOME" + ";" + "CPF"  ";" + "MRG" + ";" + "MAT" + "\n"              
            f.write(verificaWpp)


        def verifi_1conexoes(telefones):
            """
            Verificação com apenas uma conexão 
            """
            #NAVEGADOR#
            navegador1 = webdriver.Chrome(options=options)
            navegador1.get('https://web.whatsapp.com/')
            element = False
            
            while(element == False):
                
                element = WebDriverWait(navegador1, 999, poll_frequency=0.1).until(
                EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/div/div[1]/span")))
                print("entrou0")
                


            cont1 = 0
            for index,row in dados.iterrows():
            
                Telefone = (row['TEL'])
                Nome = (row['NOME'])
                Cpf = (row['CPF'])
                Mrg = (row['MRG'])
                Mat = (row['MAT'])
                
                    
                TelWPP = Telefone
                sleep(0.2)
                print(Telefone)


                navegador1.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                sleep(0.5)
                element = False
                while (element==False):
                    try:
                        caixa_texto = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button")
                        caixa_texto.click()
                    except:                        
                        sleep(0.5) 
                        try:
                            pop_naoewpp = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]")
                        except:
                            sleep(0.3)
                        else:
                            break    
                    else:
                        element=True 

                try:
                        
                    element_inicia = False
                    while(element_inicia == False):
                        element_inicia = WebDriverWait(navegador1, 3, poll_frequency=0.1).until(
                        EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
                    
                except:
            
                    print("saiu")
                    sleep(0.1)
                    #resposta_consulta = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                    retorno ='Não é WhatsApp '
                    #btn_ok = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                    #NWpp += 1
                   #btn_ok.click()
                    with open (str(nome_arquivo)+ "invalidos.csv",'a',newline='', encoding='UTF-8') as f:        
                            retorno = retorno + ';'
                            TelWPP = str(Telefone)
                            #Nome = Nome + ";"
                            
                            verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                            
                            f.write(verificaWpp)             


                else:
                    #SWpp +=1
                    with open (str(nome_arquivo)+ "validados.csv",'a',newline='', encoding='UTF-8') as f:        
                            TelWPP = str(Telefone)
                            #Nome = Nome + ";"
                                
                            verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                            
                            f.write(verificaWpp)

        def verifi_2conexoes(telefones):
            """
            Verificação com duas conexões 
            """
            #tela_envio()
            SWpp = 0
            NWpp = 0
            dados =  pd.read_excel(telefones)
            #self.updatee
            def RetornaDados(dados):
                nome = []
                cpf = []
                num = []
                mrg = []
                mat = []
                for index,row in dados.iterrows():

                    Nome = (row['NOME'])
                    Cpf = (row['CPF'])
                    Num =  (row['TEL'])
                    Mrg = (row['MRG'])
                    Mat = (row['MAT'])
                    cpf.append(Cpf)
                    nome.append(Nome)
                    num.append(Num)
                    mrg.append(Mrg)
                    mat.append(Mat)
                return cpf,nome,num, mrg, mat
            Cpfs, Nomes, Nums, Mrgs, Mats  = RetornaDados(dados)

            options = Options()
            options.headless = False # Visivel
            def vrf1():
                quantidade = len(dados) - 1
                #NAVEGADOR#
                navegador1 = webdriver.Chrome(options=options)
                navegador1.get('https://web.whatsapp.com/')
                element = False
                
                while(element == False):
                    
                    element = WebDriverWait(navegador1, 999, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/div/div[1]/span")))
                    print("entrou0")
                    
                vardonavegador1 = 0 
                cont1 = 0
                for index,row in dados.iterrows():
                    if quantidade < vardonavegador1:
                        print("finalizou1")
                        break                
                    Telefone = Nums[vardonavegador1]
                    Nome = Nomes[vardonavegador1]
                    Cpf = Cpfs[vardonavegador1] 
                    Mrg = Mrgs[vardonavegador1]
                    Mat = Mats[vardonavegador1]
                    
                        
                    TelWPP = Telefone
                    sleep(0.2)
                    print(Telefone)


                    navegador1.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                    sleep(0.5)
                    element = False
                    while (element==False):
                        try:
                            caixa_texto = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button")
                            caixa_texto.click()
                        except:                        
                            sleep(0.5) 
                            try:
                                pop_naoewpp = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]")
                            except:
                                sleep(0.3)
                            else:
                                break    
                        else:
                            element=True 



                    try:
                            
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador1, 2, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
                        
                    except:
                
                        print("saiu")
                        sleep(0.1)
                        #resposta_consulta = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ='Não é WhatsApp '
                        #btn_ok = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                        #NWpp += 1
                        #btn_ok.click()
                        vardonavegador1 += 2
                        with open (str(nome_arquivo)+ "invalidos.csv",'a',newline='', encoding='UTF-8') as f:        
                                retorno = retorno + ';'
                                TelWPP = str(Telefone) 
                                #Nome = Nome + ";"
                                
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)             


                    else:
                        #SWpp +=1
                        vardonavegador1 += 2
                        with open (str(nome_arquivo)+ "validados.csv",'a',newline='', encoding='UTF-8') as f:        
                                TelWPP = str(Telefone) 
                                #Nome = Nome + ";"
                                    
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)


            def vrf2():  
                quantidade = len(dados) - 1
                #NAVEGADOR#
                navegador2 = webdriver.Chrome(options=options)
                navegador2.get('https://web.whatsapp.com/')
                element = False
                
                while(element == False):
                    
                    element = WebDriverWait(navegador2, 999, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/div/div[1]/span")))
                    print("entrou0")
                    
                vardonavegador2 = 1 
                cont1 = 0
                for index,row in dados.iterrows():
                    if quantidade < vardonavegador2:
                        print("finalizou1")
                        break                
                    Telefone = Nums[vardonavegador2]
                    Nome = Nomes[vardonavegador2]
                    Cpf = Cpfs[vardonavegador2] 
                    Mrg = Mrgs[vardonavegador2]
                    Mat = Mats[vardonavegador2]
                    
                        
                    TelWPP = Telefone
                    sleep(0.2)
                    print(Telefone)


                    navegador2.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                    sleep(0.5)
                    element = False
                    while (element==False):
                        try:
                            caixa_texto = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button")
                            caixa_texto.click()
                        except:                        
                            sleep(0.5) 
                            try:
                                pop_naoewpp = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]")
                            except:
                                sleep(0.3)
                            else:
                                break    
                        else:
                            element=True 
                    try:
                            
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador2, 3, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
                        
                    except:
                
                        print("saiu")
                        sleep(0.1)
                        #resposta_consulta = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ='Não é WhatsApp '
                        #btn_ok = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                        #NWpp += 1
                        #btn_ok.click()
                        vardonavegador2 += 2
                        with open (str(nome_arquivo)+ "invalidos.csv",'a',newline='', encoding='UTF-8') as f:        
                                retorno = retorno + ';'
                                TelWPP = str(Telefone) 
                                #Nome = Nome + ";"
                                
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)             


                    else:
                        #SWpp +=1
                        vardonavegador2 += 2
                        with open (str(nome_arquivo)+ "validados.csv",'a',newline='', encoding='UTF-8') as f:        
                                TelWPP = str(Telefone)
                                #Nome = Nome + ";"
                                    
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)


            t2 = threading.Thread(target=vrf1)
            t3 = threading.Thread(target=vrf2)


            t2.start()
            t3.start()

            t2.join()
            t3.join()

        def verifi_3conexoes(telefones):
            """
            Verificação com duas conexões 
            """
            #tela_envio()
            SWpp = 0
            NWpp = 0
            dados =  pd.read_excel(telefones)
            #self.updatee
            def RetornaDados(dados):
                nome = []
                cpf = []
                num = []
                mrg = []
                mat = []
                for index,row in dados.iterrows():

                    Nome = (row['NOME'])
                    Cpf = (row['CPF'])
                    Num =  (row['TEL'])
                    Mrg = (row['MRG'])
                    Mat = (row['MAT'])
                    cpf.append(Cpf)
                    nome.append(Nome)
                    num.append(Num)
                    mrg.append(Mrg)
                    mat.append(Mat)
                return cpf,nome,num, mrg, mat
            Cpfs, Nomes, Nums, Mrgs, Mats  = RetornaDados(dados)

            options = Options()
            options.headless = False # Visivel
            def vrf1():
                quantidade = len(dados) - 1
                #NAVEGADOR#
                navegador1 = webdriver.Chrome(options=options)
                navegador1.get('https://web.whatsapp.com/')
                element = False
                
                while(element == False):
                    
                    element = WebDriverWait(navegador1, 999, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/div/div[1]/span")))
                    print("entrou0")
                    
                vardonavegador1 = 0 
                cont1 = 0
                for index,row in dados.iterrows():
                    if quantidade < vardonavegador1:
                        print("finalizou1")
                        break                
                    Telefone = Nums[vardonavegador1]
                    Nome = Nomes[vardonavegador1]
                    Cpf = Cpfs[vardonavegador1] 
                    Mrg = Mrgs[vardonavegador1]
                    Mat = Mats[vardonavegador1]
                    
                        
                    TelWPP = Telefone
                    sleep(0.2)
                    print(Telefone)


                    navegador1.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                    sleep(0.5)
                    element = False
                    while (element==False):
                        try:
                            caixa_texto = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button")
                            caixa_texto.click()
                        except:                        
                            sleep(0.5) 
                            try:
                                pop_naoewpp = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]")
                            except:
                                sleep(0.3)
                            else:
                                break    
                        else:
                            element=True 
                    try:
                            
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador1, 3, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
                        
                    except:
                
                        print("saiu")
                        sleep(0.1)
                        #resposta_consulta = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ='Não é WhatsApp '
                        #btn_ok = navegador1.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                        #NWpp += 1
                        #btn_ok.click()
                        vardonavegador1 += 3
                        with open (str(nome_arquivo)+ "invalidos.csv",'a',newline='', encoding='UTF-8') as f:        
                                retorno = retorno + ';'
                                TelWPP = str(Telefone) 
                                #Nome = Nome + ";"
                                
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)             


                    else:
                        #SWpp +=1
                        vardonavegador1 += 3
                        with open (str(nome_arquivo)+ "validados.csv",'a',newline='', encoding='UTF-8') as f:        
                                TelWPP = str(Telefone)
                                #Nome = Nome + ";"
                                    
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)


            def vrf2():  
                quantidade = len(dados) - 1
                #NAVEGADOR#
                navegador2 = webdriver.Chrome(options=options)
                navegador2.get('https://web.whatsapp.com/')
                element = False
                
                while(element == False):
                    
                    element = WebDriverWait(navegador2, 999, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/div/div[1]/span")))
                    print("entrou0")
                    
                vardonavegador2 = 1 
                cont1 = 0
                for index,row in dados.iterrows():
                    if quantidade < vardonavegador2:
                        print("finalizou2")
                        break                
                    Telefone = Nums[vardonavegador2]
                    Nome = Nomes[vardonavegador2]
                    Cpf = Cpfs[vardonavegador2] 
                    Mrg = Mrgs[vardonavegador2]
                    Mat = Mats[vardonavegador2]
                    
                        
                    TelWPP = Telefone
                    sleep(0.2)
                    print(Telefone)


                    navegador2.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                    sleep(0.5)
                    element = False
                    while (element==False):
                        try:
                            caixa_texto = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button")
                            caixa_texto.click()
                        except:                        
                            sleep(0.5) 
                            try:
                                pop_naoewpp = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]")
                            except:
                                sleep(0.3)
                            else:
                                break    
                        else:
                            element=True 
                    try:
                            
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador2, 3, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
                        
                    except:
                
                        print("saiu")
                        sleep(0.1)
                        #resposta_consulta = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ='Não é WhatsApp '
                        #btn_ok = navegador2.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                        #NWpp += 1
                        #btn_ok.click()
                        vardonavegador2 += 3
                        with open (str(nome_arquivo)+ "invalidos.csv",'a',newline='', encoding='UTF-8') as f:        
                                retorno = retorno + ';'
                                TelWPP = str(Telefone)
                                #Nome = Nome + ";"
                                
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)             


                    else:
                        #SWpp +=1
                        vardonavegador2 += 3
                        with open (str(nome_arquivo)+ "validados.csv",'a',newline='', encoding='UTF-8') as f:        
                                TelWPP = str(Telefone) 
                                #Nome = Nome + ";"
                                    
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)

            def vrf3():  
                quantidade = len(dados) - 1
                #NAVEGADOR#
                navegador3 = webdriver.Chrome(options=options)
                navegador3.get('https://web.whatsapp.com/')
                element = False
                
                while(element == False):
                    
                    element = WebDriverWait(navegador3, 999, poll_frequency=0.1).until(
                    EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/div/div[1]/span")))
                    print("entrou0")
                    
                vardonavegador3 = 2 
                cont1 = 0
                for index,row in dados.iterrows():
                    if quantidade < vardonavegador3:
                        print("finalizou3")
                        break                
                    Telefone = Nums[vardonavegador3]
                    Nome = Nomes[vardonavegador3]
                    Cpf = Cpfs[vardonavegador3] 
                    Mrg = Mrgs[vardonavegador3]
                    Mat = Mats[vardonavegador3]
                    
                        
                    TelWPP = Telefone
                    sleep(0.2)
                    print(Telefone)


                    navegador3.get('https://web.whatsapp.com/send/?phone=' + str(Telefone) +'&text&type=phone_number&app_absent=0')
                    sleep(0.5)
                    element = False
                    while (element==False):
                        try:
                            caixa_texto = navegador3.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button")
                            caixa_texto.click()
                        except:                        
                            sleep(0.5) 
                            try:
                                pop_naoewpp = navegador3.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]")
                            except:
                                sleep(0.3)
                            else:
                                break    
                        else:
                            element=True 
                    try:
                            
                        element_inicia = False
                        while(element_inicia == False):
                            element_inicia = WebDriverWait(navegador3, 3, poll_frequency=0.1).until(
                            EC.presence_of_all_elements_located((By.XPATH , "/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div")))
                        
                    except:
                
                        print("saiu")
                        sleep(0.1)
                        #resposta_consulta = navegador3.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div").text
                        retorno ='Não é WhatsApp '
                        #btn_ok = navegador3.find_element(by=By.XPATH, value="/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div/div/div")
                        #NWpp += 1
                        #btn_ok.click()
                        vardonavegador3 += 3
                        with open (str(nome_arquivo)+ "invalidos.csv",'a',newline='', encoding='UTF-8') as f:        
                                retorno = retorno + ';'
                                TelWPP = str(Telefone)
                                #Nome = Nome + ";"
                                
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)             


                    else:
                        #SWpp +=1
                        vardonavegador3 += 3
                        with open (str(nome_arquivo)+ "validados.csv",'a',newline='', encoding='UTF-8') as f:        
                                TelWPP = str(Telefone) 
                                #Nome = Nome + ";"
                                    
                                verificaWpp = str(TelWPP)+ ";" + str(Nome) + ";" +str(Cpf)+ ";" +str(Mrg) + ";" + str(Mat) + "\n"
                                
                                f.write(verificaWpp)

            wt1 = threading.Thread(target=vrf1)
            wt2 = threading.Thread(target=vrf2)
            wt3 = threading.Thread(target=vrf3)      

            wt1.start()
            wt2.start()
            wt3.start()
            
            wt1.join()
            wt2.join()
            wt3.join()             

        #Chamando a função de acordo com o número de conexões
        if self.radio_var.get() == 0:
            verifi_1conexoes(telefones)
        elif self.radio_var.get() == 1:
            verifi_2conexoes(telefones)
        elif self.radio_var.get() == 2:
            verifi_3conexoes(telefones)   
 

        messagebox.showinfo(title="Validação de WhatsAPP", message="Total de números: " + str(SWpp + NWpp) +"\n" + "São WhatsAPP: " + str(SWpp) + "\n" + "Não são WhatsAPP: " + str(NWpp))


    def browseFilesTel(self):
        """
        Método para abrir o filebrowser e pesquisar pelo arquivo de telefones
        """        
        self.filename = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Text files",
                                                            "*.xlsx*"),
                                                        ("all files",
                                                            "*.*")))
        
        # Change label contents
        self.caminho_telefone.configure(text=self.filename)
        dados =  pd.read_excel(self.filename)
        self.textbox_tel.configure(state="normal")
        self.textbox_tel.delete("0.0",'end-1c')
        self.textbox_tel.insert("0.0",str(dados))


if __name__ == "__main__":
    janela = Janela()
    janela.mainloop()