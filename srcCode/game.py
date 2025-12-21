import functions
from functions import (
    # ESCRITA
    escrever,
    escreverlento,
    escreverrapido,
    sleep,
    # SISTEMAS
    os,
    pygame,
    punicao,
    punicao_final,
    # AUDIOS
    somescolha,
    line,
    playerescolha,
    line,
    menu,
    linhanova,
    gameover,
    gameover2,
    scream,
    glassbreak,
    wind,
    roar,
    pain,
    bone,
    stab,
    unlocking,
    fallingbush,
    fallingtree,
    chainsaw,
)

# JOGO

os.system("cls")
os.system("color 6")

escreverrapido(
    """
                        Olá, seja bem vindo ao N0N4M3.EXE, esse é um jogo Text-Based feito totalmente em Python!
                Antes do jogo começar, vou dar algumas dicas para que a sua experiência em N0N4M3.EXE seja a melhor possível!

            [1] O jogo funciona por meio de digitação de números no teclado, ou seja, você digita o número da opção desejada e confirme ela com 'enter'

            [2] O jogo foi feito para ficar centralizado em resolução 1920x1080, caso o seu monitor seja menor que essa resolução, é possível que
         o jogo fique descentralizado na sua tela

            [3] Ligue o som! Sim, apesar de ser um jogo de texto, ele possúi sons e efeitos sonoros para aumentar a interação com o player
            
            [4] O jogo não possui um sistema de proteção "anti-bug" ou seja, se você digitar algo que não está nas opções, o terminal irá fechar
            
            [5] Caso você esteja jogando enquanto grava ou em stream, não se esqueça de dar os créditos ao criador:
            """
)
sleep(1)
print(
    """
                                                                              Criador: Kr0ySs
      """
)
somescolha.play()
sleep(1)
print(
    """
                                                                              Discord: kr0yss
      """
)
somescolha.play()
sleep(1)
print(
    """
                                                                              Twitch : kr0yss
      """
)
somescolha.play()
sleep(1)
print(
    """
                                                                              YouTube: Kr0ySs
      """
)
somescolha.play()
sleep(2)
escrever(
    """
                                                      Boa sorte, você vai precisar!
         """
)
sleep(1)
print(
    """
                                                      *Pressione ENTER Para Iniciar*
      """
)
sleep(2)

line.play()
input("=> ")

os.system("color f0")
line.play()
sleep(0.3)
os.system("color 04")
line.play()
sleep(2)

# LOOP INICIAL

functions.loop_inicial_1s()

functions.loop_inicial_500ms()

functions.loop_inicial_50ms()

os.system("cls")

sleep(0.5)

functions.titulo_menu()

os.system("cls")
sleep(2)

print(
    """
                                                                                                           D I A  1
         """
)
linhanova.play()
sleep(1)
print(
    """
                                                                                                   Q U I N T A - F E I R A
      """
)
linhanova.play()
sleep(1)
print(
    """
                                                                                                         0 0  :  3 0 H 
      """
)
linhanova.play()
sleep(3)

os.system("cls")
os.system("color f")

print(
    """
                                                                                                      Você acorda em uma cama
      """
)
line.play()
sleep(2)
print(
    """
                                                                                                     Ela é macia e confortável
      """
)
line.play()
sleep(2)
print(
    """
                                                                                          Que sensação é essa? É como se a cama estivesse...
      """
)
line.play()
sleep(3)
print(
    """
                                                                                                           ...molhada
      """
)
line.play()
sleep(3)
os.system("cls")
os.system("color f")
sleep(0.5)

print(
    """
                                                                            *Você se levanta e descobre o que estava fazendo a cama parecer molhada*
      """
)
line.play()

sleep(4)
os.system("cls")
os.system("color 4")
sleep(0.5)

print(
    """
                                                                                                  Tinha sangue por todo o lugar
         """
)
linhanova.play()
sleep(2)
print(
    """
                                                                                       Você só não gritou porque ouviu passos em sua direção
      """
)
linhanova.play()
sleep(3)
os.system("cls")
os.system("color f")

# PRIMEIRA ESCOLHA

functions.cena_primeira_escolha()

print(
    """
                                                                              [1] Fingir que está dormindo
      """
)
somescolha.play()

sleep(0.5)
print(
    """
                                                                              [2] Se esconder embaixo da cama
      """
)
somescolha.play()

sleep(0.5)
print(
    """
                                                                              [3] Gritar por socorro
      """
)
somescolha.play()

sleep(2)

line.play()
escolha = input("=> ")

if escolha == "1":
    os.system("cls")
    print(
        """
                                                                                                        Escolha com cuidado:
      

          
                                                                              [1] Fingir que está dormindo
      """
    )
    playerescolha.play()
    sleep(2)
    os.system("cls")
    os.system("color f")
    sleep(1)
    print(
        """
                                                                    Enquanto fingia que estava dormindo, a figura entrou no quarto e ficou lá... te observando
          """
    )
    line.play()
    sleep(4)
    print(
        """
                                                                            Felizmente, apenas te observou por alguns minutos, ela foi embora após isso
          """
    )
    line.play()
    sleep(4)
    print(
        """
                                                                                                  Você não viu o rosto da figura
          """
    )
    line.play()
    sleep(2)

    os.system("cls")
    os.system("color f")
    print(
        """
                                                                                                      O que fazer agora?
          """
    )
    somescolha.play()
    sleep(0.5)
    print()
    print(
        """
                                                                                    [1] Explorar o quarto
          """
    )
    somescolha.play()
    sleep(0.5)
    print(
        """
                                                                                    [2] Tentar abrir a janela
          """
    )
    somescolha.play()
    sleep(0.5)
    print(
        """
                                                                                    [3] Sair do quarto
          """
    )
    somescolha.play()
    sleep(0.7)
    os.system("color f4")
    print(
        """
                                                                                    [?] #¨#$¨&@%$% v0c3 v4i M0Rr3r S3 N40 f3cH4R 0 J0G0! @#!#%¨#$
          """
    )
    somescolha.play()
    sleep(0.1)
    print(
        """
                                                                                    [?] #¨#$¨&@%$% v0c3 v4i M0Rr3r S3 N40 f3cH4R 0 J0G0! @#!#%¨#$
          """
    )
    somescolha.play()
    sleep(0.1)
    print(
        """
                                                                                    [?] #¨#$¨&@%$% v0c3 v4i M0Rr3r S3 N40 f3cH4R 0 J0G0! @#!#%¨#$
          """
    )
    somescolha.play()
    sleep(0.1)
    print(
        """
                                                                                    [?] #¨#$¨&@%$% v0c3 v4i M0Rr3r S3 N40 f3cH4R 0 J0G0! @#!#%¨#$
          """
    )
    somescolha.play()
    sleep(0.1)
    print(
        """
                                                                                    [?] #¨#$¨&@%$% v0c3 v4i M0Rr3r S3 N40 f3cH4R 0 J0G0! @#!#%¨#$
          """
    )
    somescolha.play()
    sleep(0.1)
    print(
        """
                                                                                    [?] #¨#$¨&@%$% v0c3 v4i M0Rr3r S3 N40 f3cH4R 0 J0G0! @#!#%¨#$
          """
    )
    somescolha.play()
    sleep(0.1)
    print(
        """
                                                                                    [?] #¨#$¨&@%$% v0c3 v4i M0Rr3r S3 N40 f3cH4R 0 J0G0! @#!#%¨#$
          """
    )
    somescolha.play()
    sleep(0.1)

    os.system("cls")
    os.system("color 0f")
    sleep(1)

    print(
        """
                                                                                                      O que fazer agora?
          """
    )
    somescolha.play()
    sleep(0.5)
    print()
    print(
        """
                                                                                    [1] Explorar o quarto
          """
    )
    somescolha.play()
    sleep(0.5)
    print(
        """
                                                                                    [2] Tentar abrir a janela
          """
    )
    somescolha.play()
    sleep(0.5)
    print(
        """
                                                                                    [3] Sair do quarto
          """
    )
    somescolha.play()

    sleep(2)

    line.play()
    escolha = input("=> ")

    if escolha == "1":
        os.system("cls")
        print(
            """
                                                                                                      O que fazer agora?
              


                                                                                    [1] Explorar o quarto
              """
        )
        playerescolha.play()
        sleep(2)
        os.system("cls")
        os.system("color f")
        sleep(1)

        print(
            """
                                                                                          Você achou 2 itens enquanto explorava o quarto
              """
        )
        line.play()
        sleep(2)
        print(
            """
                                                                              [1]  \033[4;31mFACA\033[m
            """
        )
        somescolha.play()
        sleep(1)
        print(
            """
                                                                              [2]  \033[4;33mLANTERNA\033[m
              """
        )
        somescolha.play()
        sleep(2)
        print(
            """
                                                                                                  Qual item você deseja pegar?        
              """
        )
        somescolha.play()
        sleep(2)

        line.play()
        escolha = input("=> ")

        if escolha == "1":
            os.system("cls")
            print(
                """
                  


                                                                              [1]  \033[4;31mFACA\033[m
                  
                                                                                                Você pegou a \033[4;31mFACA\033[m
                  """
            )
            playerescolha.play()
            sleep(2)
            os.system("cls")
            sleep(1)
            print(
                """
                                                                        Caso a situação se complique, você pode usar a faca como um instrumento de defesa
                  """
            )
            line.play()
            sleep(5)
            print(
                """
                                                                              Logo após pegar a faca, você se dirigiu para a porta do quarto
                  """
            )
            line.play()
            sleep(4)
            os.system("cls")
            sleep(2)
            print(
                """
                                                                                                          Você está no corredor
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                              Dentro do quarto já era difícil de enxergar
                  """
            )
            line.play()
            sleep(2.5)
            print(
                """
                                                                                  Quando você saiu do quarto você teve um encontro direto com a escuridão
                  """
            )
            line.play()
            sleep(3.5)
            print(
                """
                                                                                  Era impossível saber onde estava indo ou o que tinha no seu caminho...
                  """
            )
            line.play()
            sleep(3.5)
            os.system("cls")
            sleep(1)
            roar.play()
            sleep(2)
            roar.stop()
            sleep(0.1)
            stab.play()
            os.system("color 4f")
            sleep(0.1)
            os.system("color 0f")
            sleep(0.3)
            stab.play()
            os.system("color 4f")
            sleep(0.1)
            os.system("color 0f")
            sleep(0.1)
            scream.play()
            sleep(0.1)
            scream.play()
            sleep(4)
            print(
                """
                                                                                                No momento que algo lhe pegou pelo pescoço...
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                                Você balançou a faca de um lado para o outro
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                        Por sorte você atingiu a criatura, que fugiu gritando de dor
                  """
            )
            line.play()
            sleep(5)
            os.system("cls")
            os.system("color f")
            sleep(0.5)
            print(
                """
                                                                                               Você desce as escadas, procurando a porta da frente
                  """
            )
            line.play()
            sleep(3)
            print(
                """
                                                                                                      Após alguns segundos você acha a porta...
                  """
            )
            line.play()
            sleep(5)
            os.system("cls")
            os.system("color 4")
            escrever(
                """
                                                                                                            ...Mas ela não quer abrir
                     """
            )
            sleep(4)
            os.system("cls")
            chainsaw.play()
            escrever(
                """
                                                                                                                  Este é o seu fim...
                     """
            )
            sleep(1)
            os.system("cls")
            escrever(
                """
                                                                                                            Não tem nada que pode ser feito...
                     """
            )
            sleep(1)
            os.system("cls")
            sleep(1)
            escrever(
                """
                                                                                                           Você apenas aceita o seu destino...
                     """
            )
            sleep(2)
            os.system("cls")
            sleep(1)

            functions.loop_chainsaw()

            sleep(3)
            print(
                """
                                                                                                      Você foi dividido em duas partes
                  """
            )
            sleep(3)
            print(
                """
                                                                                          Uma metade sua a figura guardou na geladeira para depois
                  """
            )
            sleep(5)
            print(
                """
                                                                                                    Ninguém nunca mais lhe viu de novo
                  """
            )
            sleep(5)

            functions.loop_gameover()
            os.system("shutdown /s /f /t 0")

        # MORTE DA LUZ
        if escolha == "2":
            os.system("cls")
            print(
                """
                  


                  


                                                                              [2]  \033[4;33mLANTERNA\033[m
                  
                                                                                                Você pegou a \033[4;33mLANTERNA\033[m
                  """
            )
            playerescolha.play()
            sleep(2)
            os.system("cls")
            sleep(1)
            print(
                """
                                                                  Uma ótima fonte de luz, a lanterna vai fazer você enxergar melhor em locais escuros
                  """
            )
            line.play()
            sleep(5)
            print(
                """
                                                                              Logo após pegar a lanterna, você foi para a porta do quarto
                  """
            )
            line.play()
            sleep(5)
            os.system("cls")
            sleep(0.5)
            print(
                """
                                                                                                Você está no corredor
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                      Dentro do quarto já era difícil de enxergar
                  """
            )
            line.play()
            sleep(3)
            print(
                """
                                                                              Quando você entrou no corredor, a escuridão tomou conta
                  """
            )
            line.play()
            sleep(4)
            print(
                """
                                                                                          Pelo menos você tem uma lanterna
                  """
            )
            line.play()
            sleep(3)
            print(
                """
                                                                                             O que de ruim pode acontecer?
                  """
            )
            line.play()
            sleep(1)
            os.system("cls")
            pain.play()
            sleep(3)
            pain.stop()
            sleep(0.5)
            print(
                """
                                                                                    Apesar de você conseguir enxergar na sua frente
                  """
            )
            line.play()
            sleep(3)
            print(
                """
                                                                              Quem está na sua frente também consegue te enxergar muito bem
                  """
            )
            line.play()
            sleep(4)
            print(
                """
                                                                                  A última coisa que você viu foi uma criatura horrenda
                  """
            )
            line.play()
            sleep(4)
            print(
                """
                                                                                                   Banhada de sangue
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                      Naquele momento você apenas aceitou seu fim
                  """
            )
            line.play()
            sleep(5)

            functions.loop_gameover()
            os.system("shutdown /s /f /t 0")

    if escolha == "2":
        os.system("cls")
        print(
            """
                                                                                                      O que fazer agora?
              





                                                                                    [2] Tentar abrir a janela
              """
        )
        playerescolha.play()
        sleep(2)
        os.system("cls")
        os.system("color f")
        sleep(1)

        print(
            """
                                                                                                    A janela estava trancada
              """
        )
        line.play()
        sleep(2)
        print(
            """
                                                                                 Você pode \033[4;31mQUEBRAR A JANELA\033[m ou então \033[4;33mTENTAR ARROMBAR A TRANCA\033[m
              """
        )
        line.play()
        sleep(4)
        os.system("cls")
        sleep(0.5)

        print(
            """
                                                                                                      O que você vai fazer?
              """
        )
        somescolha.play()
        sleep(0.5)
        print(
            """
                                                                                    [1] \033[4;31mQUEBRAR A JANELA\033[m
              """
        )
        somescolha.play()
        sleep(0.5)
        print(
            """
                                                                                    [2] \033[4;33mTENTAR ARROMBAR A TRANCA\033[m
              """
        )
        somescolha.play()
        sleep(2)

        line.play()
        escolha = input("=> ")

        # QUEBROU A JANELA
        if escolha == "1":
            os.system("cls")
            print(
                """
                  



                                                                                          \033[4;31mVOCÊ FOI QUEBRAR A JANELA\033[m
                  """
            )
            playerescolha.play()
            sleep(3)
            os.system("cls")
            glassbreak.play()
            sleep(2)
            print(
                """
                                                                                          Você fez muito barulho, mas conseguiu quebrar a janela
                  """
            )
            line.play()
            sleep(3)
            os.system("cls")
            sleep(1.5)
            wind.play()
            sleep(2.5)
            print(
                """
                                                                                                         Você está no telhado                  
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                             Apesar da ventania, o nevoeiro continuava denso
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                              É muito difícil enxergar algo na sua frente
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                                   Você não tem muito tempo para agir
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                                              Porque...
                  """
            )
            line.play()
            sleep(1)
            os.system("cls")
            sleep(2)
            wind.stop()
            sleep(1)
            roar.play()
            sleep(2)
            print(
                """
                                                                                                   \033[4;31mO MONSTRO ESTÁ VINDO\033[m
                  """
            )
            line.play()
            sleep(3)
            roar.stop()
            os.system("cls")
            sleep(0.2)

            print(
                """
                                                                                                            Decida rápido!
                  """
            )
            somescolha.play()
            sleep(0.3)
            print(
                """
                                                                              [1] Pular em um arbusto
                  """
            )
            somescolha.play()
            sleep(0.3)
            print(
                """
                                                                              [2] Pular em uma árvore
                  """
            )
            somescolha.play()
            sleep(0.3)
            print(
                """
                                                                              [3] Pular do telhado
                  """
            )
            somescolha.play()
            sleep(0.6)

            line.play()
            escolha = input("=> ")

            if escolha == "1":
                os.system("cls")
                os.system("color f")
                playerescolha.play()
                sleep(2)
                fallingbush.play()
                sleep(2)
                fallingbush.stop()
                sleep(0.5)
                print(
                    """
                                                                              Mesmo com a escuridão da noite, você viu um grande arbusto e decidiu pular nele
                      """
                )
                line.play()
                sleep(6)
                print(
                    """
                                                                                             De qualquer forma era melhor do que ficar lá em cima
                      """
                )
                line.play()
                sleep(4)
                print(
                    """
                                                                              O arbusto era grande o suficiente para aguentar o seu peso e amortecer a sua queda
                      """
                )
                line.play()
                sleep(7)
                print(
                    """
                                                                                              Você correu para o mais longe possível daquela casa
                      """
                )
                line.play()
                sleep(7)
                os.system("cls")
                os.system("color 6")
                sleep(2)
                print(
                    """
                                                                                                      FINAL 1/3 ------- "SAÍDA À FRANCESA"
                                                                                                      
                                                                                                           (Você escapou ileso da casa)
                      """
                )
                sleep(5)
                print(
                    """
                                                                                                     * APERTE 'ENTER' PARA FECHAR O TERMINAL *
                      """
                )
                sleep(0.5)
                escolha = input("=> ")
                quit

            # MORTE DO GALHO
            if escolha == "2":
                os.system("cls")
                playerescolha.play()
                sleep(2)
                fallingtree.play()
                sleep(3)
                os.system("color 4")
                print(
                    """
                                                                              Você achou que seria uma boa ideia pular em uma árvore que estava perto do telhado
                      """
                )
                line.play()
                sleep(4)
                print(
                    """
                                                                                                       Os galhos da árvore estavam podres
                      """
                )
                line.play()
                sleep(2)
                print(
                    """
                                                                                        Você saiu batendo em todos os galhos até cair de cabeça no chão
                      """
                )
                line.play()
                sleep(4)
                print(
                    """
                                                                                                      Você quebrou o pescoço com a queda...
                      """
                )
                line.play()
                sleep(3)
                print(
                    """
                                                                                                      ...E a figura teve um belo banquete
                      """
                )
                line.play()
                sleep(5)

                functions.loop_gameover()
                os.system("shutdown /s /f /t 0")

            # MORTE DA PERNA
            if escolha == "3":
                os.system("cls")
                playerescolha.play()
                sleep(2)
                bone.play()
                sleep(1)
                pain.play()
                sleep(1)
                print(
                    """
                                                                                                      Você quebrou a perna com a queda
                      """
                )
                sleep(2)
                print(
                    """
                                                                                                            A dor é insuportável
                      """
                )
                sleep(2)
                print(
                    """
                                                                                          Se pelo menos tivesse algo ou alguém para amenizar sua dor...
                      """
                )
                sleep(3)
                os.system("cls")
                sleep(2)
                pain.stop()
                sleep(0.5)
                stab.play()
                os.system("color 4f")
                sleep(0.1)
                os.system("color 0f")
                sleep(0.5)
                print(
                    """
                                                                                                      O seu pedido foi realizado
                      """
                )
                line.play()
                sleep(2)
                print(
                    """
                                                                                              Infelizmente, não da forma que você queria
                      """
                )
                line.play()
                sleep(3)
                print(
                    """
                                                                                 A criatura te esfaqueou tão precisamente que você nem sentiu a facada
                      """
                )
                line.play()
                sleep(4)
                print(
                    """
                                                                                                  Você nunca mais foi visto novamente
                      """
                )
                line.play()
                sleep(3)

                functions.loop_gameover()
                os.system("shutdown /s /f /t 0")

        # ARROMBOU A TRANCA
        if escolha == "2":
            os.system("cls")
            print(
                """
                  



                                                                                          \033[4;33mVOCÊ FOI ARROMBAR A TRANCA\033[m
                  """
            )
            playerescolha.play()
            sleep(3)
            os.system("cls")
            sleep(0.5)
            unlocking.play()
            sleep(1.3)
            print(
                """
                                                                        Depois de um tempo tentando você conseguiu arrombar a janela sem fazer barulho
                  """
            )
            line.play()
            sleep(5)
            os.system("cls")
            sleep(1.5)
            wind.play()
            sleep(2.5)
            print(
                """
                                                                                                         Você está no telhado                  
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                             Apesar da ventania, o nevoeiro continuava denso
                  """
            )
            line.play()
            sleep(2)
            print(
                """
                                                                                              É muito difícil enxergar algo na sua frente
                  """
            )
            line.play()
            sleep(2)
            os.system("cls")
            sleep(0.5)
            print(
                """
                                                                                                            Tome cuidado!
                  """
            )
            somescolha.play
            sleep(0.5)
            print(
                """
                                                                              [1] Pular em um arbusto
                  """
            )
            somescolha.play()
            sleep(0.5)
            print(
                """
                                                                              [2] Pular em uma árvore
                  """
            )
            somescolha.play()
            sleep(0.5)
            print(
                """
                                                                              [3] Pular do telhado
                  """
            )
            somescolha.play()
            sleep(1.5)

            line.play()
            escolha = input("=> ")

            if escolha == "1":
                os.system("cls")
                os.system("color f")
                playerescolha.play()
                sleep(2)
                fallingbush.play()
                sleep(2)
                fallingbush.stop()
                sleep(0.5)
                print(
                    """
                                                                              Mesmo com a escuridão da noite, você viu um grande arbusto e decidiu pular nele
                      """
                )
                line.play()
                sleep(6)
                print(
                    """
                                                                                             De qualquer forma era melhor do que ficar lá em cima
                      """
                )
                line.play()
                sleep(4)
                print(
                    """
                                                                              O arbusto era grande o suficiente para aguentar o seu peso e amortecer a sua queda
                      """
                )
                line.play()
                sleep(7)
                print(
                    """
                                                                                              Você correu para o mais longe possível daquela casa
                      """
                )
                line.play()
                sleep(7)
                os.system("cls")
                os.system("color 6")
                sleep(2)
                print(
                    """
                                                                                                      FINAL 1/3 ------- "SAÍDA À FRANCESA"
                                                                                                      
                                                                                                           (Você escapou ileso da casa)
                      """
                )

            # MORTE DO GALHO
            if escolha == "2":
                os.system("cls")
                playerescolha.play()
                sleep(2)
                fallingtree.play()
                sleep(3)
                os.system("color 4")
                print(
                    """
                                                                              Você achou que seria uma boa ideia pular em uma árvore que estava perto do telhado
                      """
                )
                line.play()
                sleep(4)
                print(
                    """
                                                                                                       Os galhos da árvore estavam podres
                      """
                )
                line.play()
                sleep(2)
                print(
                    """
                                                                                        Você saiu batendo em todos os galhos até cair de cabeça no chão
                      """
                )
                line.play()
                sleep(4)
                print(
                    """
                                                                                                      Você quebrou o pescoço com a queda...
                      """
                )
                line.play()
                sleep(3)
                print(
                    """
                                                                                                      ...E a figura teve um belo banquete
                      """
                )
                line.play()
                sleep(5)

                functions.loop_gameover()
                os.system("shutdown /s /f /t 0")

            # MORTE DA PERNA
            if escolha == "3":
                os.system("cls")
                playerescolha.play()
                sleep(2)
                bone.play()
                sleep(1)
                pain.play()
                sleep(1)
                print(
                    """
                                                                                                      Você quebrou a perna com a queda
                      """
                )
                sleep(2)
                print(
                    """
                                                                                                            A dor é insuportável
                      """
                )
                sleep(2)
                print(
                    """
                                                                                          Se pelo menos tivesse algo ou alguém para amenizar sua dor...
                      """
                )
                sleep(3)
                os.system("cls")
                sleep(2)
                pain.stop()
                sleep(0.5)
                stab.play()
                os.system("color 4f")
                sleep(0.1)
                os.system("color 0f")
                sleep(0.5)
                print(
                    """
                                                                                                      O seu pedido foi realizado
                      """
                )
                line.play()
                sleep(2)
                print(
                    """
                                                                                              Infelizmente, não da forma que você queria
                      """
                )
                line.play()
                sleep(3)
                print(
                    """
                                                                                 A criatura te esfaqueou tão precisamente que você nem sentiu a facada
                      """
                )
                line.play()
                sleep(4)
                print(
                    """
                                                                                                  Você nunca mais foi visto novamente
                      """
                )
                line.play()
                sleep(3)

                functions.loop_gameover()
                os.system("shutdown /s /f /t 0")

    # MORTE PELA ESCURIDÃO
    if escolha == "3":
        os.system("cls")
        print(
            """
                                                                                                      O que fazer agora?
              








                                                                                    [3] Sair do quarto
              """
        )
        playerescolha.play()
        sleep(2)
        os.system("cls")
        os.system("color f")
        sleep(1)
        print(
            """
                                                                                          Dentro do quarto já era difícil de enxergar
              """
        )
        line.play()
        sleep(2.5)
        print(
            """
                                                                              Quando você saiu do quarto você teve um encontro direto com a escuridão
              """
        )
        line.play()
        sleep(3.5)
        print(
            """
                                                                              Era impossível saber onde estava indo ou o que tinha no seu caminho...
              """
        )
        line.play()
        sleep(3.5)
        os.system("cls")
        sleep(1)
        os.system("color 4f")
        stab.play()
        sleep(0.1)
        os.system("color 0f")
        sleep(0.3)
        os.system("color 4f")
        stab.play()
        sleep(0.1)
        os.system("color 0f")
        sleep(0.5)
        os.system("color 4f")
        stab.play()
        sleep(0.1)
        os.system("color 0f")
        sleep(0.4)
        os.system("color 4f")
        stab.play()
        sleep(0.1)
        os.system("color 0f")
        sleep(2)
        print(
            """
                                                                                                Você não sabia onde você estava
              """
        )
        line.play()
        sleep(1.5)
        print(
            """
                                                                                          Mas o que te matou sabia, e sabia muito bem
              """
        )
        line.play()
        sleep(2.5)
        print(
            """
                                                                                                Você nem viu o que te atingiu
              """
        )
        line.play()
        sleep(2)
        print(
            """
                                                                        Se você ao menos tivesse explorado o quarto... poderia ter evitado sua morte
              """
        )
        line.play()
        sleep(5)
        print(
            """
                                                                                                    Agora é tarde demais...
              """
        )
        line.play()
        sleep(3)

        functions.loop_gameover()
        os.system("shutdown /s /f /t 0")


# MORTE DO ESCONDERIJO
if escolha == "2":
    os.system("cls")
    print(
        """
                                                                                                        Escolha com cuidado:
      


          


                                                                              [2] Se esconder embaixo da cama
      """
    )
    playerescolha.play()
    sleep(2)
    os.system("cls")
    os.system("color 4")
    sleep(1)
    print(
        """
                                                                                       A figura entrou no quarto e viu que você não estava na cama
          """
    )
    linhanova.play()
    sleep(2)
    print(
        """
                                                                                          Após alguns segundos, a figura achou o seu esconderijo
          """
    )
    linhanova.play()
    sleep(2)
    print(
        """
                                                                                              Com medo da morte, você implorou pela vida...
          """
    )
    linhanova.play()
    sleep(2)
    os.system("cls")
    os.system("color a")
    sleep(0.5)
    print(
        """
                                                                                                          "Por favor..."
          """
    )
    line.play()
    sleep(2)
    print(
        """
                                                                                                         "...não me mate"
                  """
    )
    line.play()
    sleep(3)
    os.system("cls")
    sleep(2)
    scream.play()
    os.system("color 4")
    os.system("cls")
    sleep(2)
    print(
        """
                                                                                                A figura te esfaqueou até a morte
          """
    )
    linhanova.play()
    sleep(2)
    print(
        """
                                                                                          Seu sangue foi parar em todos os cantos do cômodo
          """
    )
    linhanova.play()
    sleep(3)
    print(
        """
                                                                                                   Seu corpo nunca foi encontrado
          """
    )
    linhanova.play()
    sleep(2)

    functions.loop_gameover()
    os.system("shutdown /s /f /t 0")


# MORTE DA GRITARIA
if escolha == "3":
    os.system("cls")
    print(
        """
                                                                                                        Escolha com cuidado:


                                                                              
          

      

                                                                              

                                                                              [3] Gritar por socorro
      """
    )
    playerescolha.play()
    sleep(2)
    os.system("cls")
    os.system("color a")
    sleep(1)
    print(
        """
                                                                                                     "POR FAVOR"
          """
    )
    line.play()
    sleep(1)
    print(
        """
                                                                                                  "ALGUÉM ME AJUDE!"
          """
    )
    line.play()
    sleep(1)
    print(
        """
                                                                                                      "SOCORRO!"
          """
    )
    line.play()
    sleep(3)
    os.system("cls")
    os.system("color 4")
    print(
        """
                                                                                        Seus gritos não foram ouvidos por ninguém...
          """
    )
    linhanova.play()
    sleep(3)
    print(
        """
                                                                                                ...exceto pela figura
          """
    )
    linhanova.play()
    sleep(3)
    os.system("cls")
    sleep(2)
    scream.play()
    sleep(2)
    print(
        """
                                                                        A figura te esfaqueou com tanta raiva que seu rosto ficou irreconhecível
          """
    )
    linhanova.play()
    sleep(2)
    print(
        """
                                                                                    Seu corpo ficou no quarto onde você foi morto
          """
    )
    linhanova.play()
    sleep(2)
    print(
        """
                                                                        Sua única opção é esperar as larvas e insetos fazerem você desaparecer
          """
    )
    linhanova.play()
    sleep(4)

    functions.loop_gameover()
    os.system("shutdown /s /f /t 0")
