import os
import pygame
import subprocess
import time
import tkinter as tk
from tkinter import messagebox
from time import sleep

# INICIALIZAÇÃO

os.system("color 6")
os.system("cls")

# FUNCOES ESCREVER

def escrever(texto):
    for char in texto+"\n":
        print(char, end="", flush=True)
        sleep(0.035)

def escreverrapido(texto):
    for char in texto+"\n":
        print(char, end="", flush=True)
        sleep(0.01)

def escreverlento(texto):
    for char in texto+"\n":
        print(char, end="", flush=True)
        sleep(0.1)

# GAMEOVERS

def loop_chainsaw():
     for i in range(300):
          os.system("color 4f")
          sleep(0.03)
          os.system("color 0f")
          sleep(0.03)

def loop_gameover():
      frames = [
            '''
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/            
I                                               I
I               G A M E  O V E R                I 
I                                               I 
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ 
            '''
      ]
      while True:
          for quadro in frames:
              os.system("color 4")
              os.system("cls")
              print("\n" * 5)
              print(quadro)
              gameover.play()
              sleep(0.1)
          
# LOOP INICIAL

def loop_inicial_1s():
      frames = [
        '''
                                                                                                FeChE eStE jOgO aGoRa!
        '''
      ]
      for i in range(4):
          for quadro in frames:
              print("\n" * 5)
              print(quadro)
              linhanova.play()
              sleep(1)

def loop_inicial_500ms():
      frames = [
          '''
                                                                                                FeChE eStE jOgO aGoRa!
          '''
      ]
      for i in range(4):
          for quadro in frames:
              print("\n" * 5)
              print(quadro)
              linhanova.play()
              sleep(0.5)

def loop_inicial_50ms():
      frames = [
          '''
                                                                                                FeChE eStE jOgO aGoRa!
          '''
      ]
      for i in range(12):
          for quadro in frames:
              print("\n" * 5)
              print(quadro)
              linhanova.play()
              sleep(0.05)

# UNICOS

def titulo_menu():
      frames = [
            '''
                                                                                     /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/            
                                                                                     I                                               I
                                                                                     I              N 0 N 4 M 3 . E X E              I 
                                                                                     I                                               I 
                                                                                     /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ 
            '''
      ]
      for quadro in frames:
              print("\n" * 5)
              print(quadro)
              menu.play()
              sleep(3)

# PRIMEIRA ESCOLHA

def cena_primeira_escolha():
     os.system("cls")
     titulo_primeira_escolha()
     escolha_1()
     escolha_2()
     escolha_3()

     print("=> ", end = "", flush=True)
     linhanova.play()

     escolha_input = ler_escolha(['1', '2', '3'], limite_erros = 5)

     if escolha_input == '1':
          return fingir_dormindo
     elif escolha_input == '2':
          return esconder
     elif escolha_input == '3':
          return gritar_socorro
     elif escolha_input == 'ABORT':
          return punicao
     
     return None

def titulo_primeira_escolha():
     frames =[
          '''
                                                                                Escolha com cuidado:
          '''
     ]
     for quadro in frames:
          print(quadro)
          somescolha.play()
          sleep(0.5)

def escolha_1():
     frames = [
          '''
                                        [1] Fingir que está dormindo
'''
     ]
     for quadro in frames:
          print(quadro)
          somescolha.play()
          sleep(0.5)

def escolha_2():
     frames = [
          '''
                                        [2] Se esconder embaixo da cama
'''
     ]
     for quadro in frames:
          print(quadro)
          somescolha.play()
          sleep(0.5)


def escolha_3():
     frames = [
          '''
                                        [3] Gritar por socorro
'''
     ]
     for quadro in frames:
          print(quadro)
          somescolha.play()
          sleep(2)

# CHECK DE LEITURA DE ESCOLHAS DO PLAYER

def ler_escolha(opcoes_validas, limite_erros = 5):
     contagem_erros = 0

     while True:
          entrada = input('=> ').strip().upper()
          linhanova.play()

          if entrada in opcoes_validas:
               contagem_erros = 0
               return entrada
          
          else:
               contagem_erros += 1

               if contagem_erros >= limite_erros:
                    return 'ABORT'

# PUNICAO SETUP

def mostrar_dialogo(titulo, mensagem):
     root = tk.Tk()
     root.withdraw()
     messagebox.showerror(titulo, mensagem)
     root.destroy()

# PUNICAO FINAL

def punicao():
     mostrar_dialogo("Sistema", "Jogador insolente...")
     mostrar_dialogo("ERRO CRITICO", "Devido a sua falta de capacidade cognitiva para escolher uma opção corretamente... ")
     mostrar_dialogo("ATENÇÃO!!!", "Seu PC irá se auto-destruir em alguns segundos.")
     mostrar_dialogo(":) :) :) :) :) :) :) :) :) :) ", "Adeus :)")

     punicao_final()

def punicao_final():
     DURACAO_PUNICAO = 8

     youareanidiot.play()

     start_time = time.time()

     while time.time() - start_time < DURACAO_PUNICAO:
          subprocess.Popen('start cmd', shell = True)
          sleep(0.05)
    
     os.system("shutdown /s /f /t 0")
               
# MORTES

def esconder():
     print("escondeu")
     sleep(10)
     exit

def gritar_socorro():
     print("gritou socorro")
     sleep(10)
     exit

# CONTINUACOES

def fingir_dormindo():
     print("continuacao a seguir")
     sleep(10)
     exit
          


pygame.init()

# BIBLIOTECA DE AUDIO

playerescolha = pygame.mixer.Sound('audio/playerescolha.wav')
somescolha = pygame.mixer.Sound('audio/choose.wav')
line = pygame.mixer.Sound('audio/normalline.wav')
menu = pygame.mixer.Sound('audio/menu.wav')
linhanova = pygame.mixer.Sound('audio/darkline.wav')
gameover = pygame.mixer.Sound('audio/gameover.wav')
gameover2 = pygame.mixer.Sound('audio/gameover2.wav')
scream = pygame.mixer.Sound('audio/scream.wav')
glassbreak = pygame.mixer.Sound('audio/glass.wav')
wind = pygame.mixer.Sound('audio/windsfx.wav')
roar = pygame.mixer.Sound('audio/roar.wav')
pain = pygame.mixer.Sound('audio/pain.wav')
bone = pygame.mixer.Sound('audio/bone.wav')
stab = pygame.mixer.Sound('audio/stab.wav')
unlocking = pygame.mixer.Sound('audio/unlocking.wav')
fallingtree = pygame.mixer.Sound('audio/fallingtree.wav')
fallingbush = pygame.mixer.Sound('audio/fallingbush.wav')
chainsaw = pygame.mixer.Sound('audio/chainsaw.wav')
youareanidiot = pygame.mixer.Sound('audio/youareanidiot.wav')