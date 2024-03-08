import curses
from pygame import mixer


from funcoes import criarmatrizes
from jogo import game
menujogo = ['NOVO JOGO', 'CONFIGURAÇÕES', 'SAIR']

somopcao = mixer.Sound('somopcao.mp3')
def print_menu(stdscr, acaoselecionada,xmenu,ymenu):
    
    altura, largura = stdscr.getmaxyx()
    curses.init_pair(9, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    for idx, acao in enumerate(menujogo):

        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        x = largura//2 - len(acao)//2 - 2
        y = altura - 5  + idx 
        if idx == acaoselecionada:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, acao)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, acao)

    titulo = [
        
 
    [' __                                     '],                                                                                         
    ['|  \                                    '],                                                                                       
    ['| $$   __  ______   __    __   ______   '],
    ['| $$  /  \|      \ |  \  |  \ |      \  '],
    ['| $$_/  $$ \$$$$$$\| $$  | $$  \$$$$$$\ '],
    ['| $$   $$ /      $$| $$  | $$ /      $$ '],
    ['| $$$$$$\|  $$$$$$$| $$__/ $$|  $$$$$$$ '],
    ['| $$  \$$\ \$$    $$ \$$   $$  \$$   $$ '],
    [' \$$   \$$ \$$$$$$$  \$$$$$$   \$$$$$$$ '],
    ['                                        '],
    ['                                        '],
    ['                                        ']

            
        
    ]


    mudança = 0
    stdscr.attron(curses.color_pair(9))
    for linha in titulo:
        for elemento in linha:
            stdscr.addstr(xmenu//8+mudança,ymenu//2-(40//2),elemento)
            mudança += 1

    



    image = [
    ["              _         _              "],
    ["  __   ___.--'_`.     .'_`--.___   __  "],
    [" ( _`.'. -   'o` )   ( 'o`   - .`.'_ ) "], 
    [" _\.'_'      _.-'     `-._      `_`./_ "], 
    ["( \`. )    //\`         '/\\    ( .'/ )"], 
    [" \_`-'`---'\\__,       ,__//`---'`-'_/ "], 
    ["  \`        `-\         /-'        '/  "], 
    ["  `                               '    "] 




        ]



    mudança = 0
    for linha in image:
        for elemento in linha:
            stdscr.addstr(xmenu//2+mudança,ymenu//2-(39//2),elemento)
            mudança += 1
    

    stdscr.attroff(curses.color_pair(9))
    stdscr.border()


def print_menu_config(stdscr, acaoselecionada,cor_player):
    stdscr.clear()
    menuconfig =['VERMELHO','ROSA','AZUL']
    while True:
        key = stdscr.getch()

        if key == ord('w') or key == ord('W'): 
            if acaoselecionada > 0:
                    somopcao.play()
                    acaoselecionada = acaoselecionada - 1
        elif key == ord('s') or key == ord('S'):
            if acaoselecionada < len(menuconfig)-1:
                somopcao.play()
                acaoselecionada = acaoselecionada + 1 
        elif key == curses.KEY_ENTER or key in [10,12]: 
            
            if acaoselecionada == 0:
                cor_player = 'vermelho'
                return cor_player
            elif acaoselecionada == 1:
                cor_player = 'rosa'
                return cor_player
            elif acaoselecionada == 2:
                cor_player = 'azul'
                return cor_player

        

        altura, largura = stdscr.getmaxyx()


        for idx, acao in enumerate(menuconfig):

            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

            x = largura//2 - len(acao)//2 - 2
            y = altura - 5  + idx 
            if idx == acaoselecionada:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, acao)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, acao)



        
        
        stdscr.addstr(altura//4,largura//2-(35//2),'Qual será a cor do seu personagem?')

        stdscr.border()



    
def splash_screen(stdscr,xmenu,ymenu):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(9, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    stdscr.border()
    curses.napms(2000)

    titulo = [
        
 
    [' __                                     '],                                                                                         
    ['|  \                                    '],                                                                                       
    ['| $$   __  ______   __    __   ______   '],
    ['| $$  /  \|      \ |  \  |  \ |      \  '],
    ['| $$_/  $$ \$$$$$$\| $$  | $$  \$$$$$$\ '],
    ['| $$   $$ /      $$| $$  | $$ /      $$ '],
    ['| $$$$$$\|  $$$$$$$| $$__/ $$|  $$$$$$$ '],
    ['| $$  \$$\ \$$    $$ \$$   $$  \$$   $$ '],
    [' \$$   \$$ \$$$$$$$  \$$$$$$   \$$$$$$$ '],
    ['                                        '],
    ['                                        '],
    ['                                        ']

            
        
    ]



    image = [
["              _         _              "],
["  __   ___.--'_`.     .'_`--.___   __  "],
[" ( _`.'. -   'o` )   ( 'o`   - .`.'_ ) "], 
[" _\.'_'      _.-'     `-._      `_`./_ "], 
["( \`. )    //\`         '/\\    ( .'/ )"], 
[" \_`-'`---'\\__,       ,__//`---'`-'_/ "], 
["  \`        `-\         /-'        '/  "], 
["  `                               '    "] 




    ]



    mudança = 0
    stdscr.attron(curses.color_pair(9))
    for linha in titulo:
        for elemento in linha:
            if mudança < 3:
                curses.napms(100)
            elif mudança == 3:
                curses.napms(200)

            elif mudança == 4:
                curses.napms(250)
            
            else:
                curses.napms(150)
            
            
            stdscr.addstr(xmenu//8+mudança,ymenu//2-(40//2),elemento)
            stdscr.refresh()
            mudança += 1





    mudança = 0
    stdscr.attron(curses.color_pair(9))
    for linha in image:
        for elemento in linha:
            if mudança < 3:
                curses.napms(100)
            elif mudança == 3:
                curses.napms(200)

            elif mudança == 4:
                curses.napms(250)
            
            else:
                curses.napms(150)
            
            
            stdscr.addstr(xmenu//2+mudança,ymenu//2-(39//2),elemento)
            stdscr.refresh()
            mudança += 1



            stdscr.refresh()

    stdscr.attroff(curses.color_pair(9))

    curses.napms(1000)


 
def main(stdscr):
    mixer.init()
    mixer.music.unload()
    mixer.music.load('musicajogo2.wav')
    mixer.music.play(-1)
    global menujogo
    comprimento_da_janela_de_fundo,largura_da_janela_de_fundo = stdscr.getmaxyx()
    x_da_janela_do_menu = comprimento_da_janela_de_fundo - 14
    y_da_janela_do_menu = largura_da_janela_de_fundo-largura_da_janela_de_fundo//2
    matriz = []
    matriz2 = []
    chances = 0
    cor_player = 'vermelho'

    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    lista_caracteres = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ",
    "ν", "ξ", "ο", "π", "ρ", "σ", "τ", "υ", "φ", "χ", "ψ", "ω",
    "Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ",
    "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω"]
    
    lista_elementosquesaoadicionados = []

    for elementos in lista_caracteres:
        lista_elementosquesaoadicionados.append(elementos)

    while chances < 200:
        lista_elementosquesaoadicionados.append(' ')
        chances = chances + 1

    chances = 0

    while chances < 1:
        lista_elementosquesaoadicionados.append('.')
        chances = chances + 1
    
    
    criarmatrizes(comprimento_da_janela_de_fundo,largura_da_janela_de_fundo,matriz2,lista_elementosquesaoadicionados,20)
    criarmatrizes(comprimento_da_janela_de_fundo,largura_da_janela_de_fundo,matriz,lista_elementosquesaoadicionados,1)

    janela_de_fundo = curses.newwin(comprimento_da_janela_de_fundo, largura_da_janela_de_fundo)
    janela_de_fundo.border()
    janela_de_fundo.nodelay(1)

    janela_do_menu = curses.newwin(x_da_janela_do_menu,y_da_janela_do_menu,4,largura_da_janela_de_fundo//4)
    acaoatualindex = 0
    
    splash_screen(janela_do_menu,x_da_janela_do_menu,y_da_janela_do_menu)

    janela_do_menu.border()
    
    janela_do_menu.nodelay(1)

    curses.curs_set(0)

    print_menu(janela_do_menu, acaoatualindex,x_da_janela_do_menu,y_da_janela_do_menu)
   
    contagem_dos_loops = 0
    
    rodadas = y_da_janela_do_menu * 20

    while True:
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        

        
        key = janela_do_menu.getch()
        
         
        if key == ord('w') or key == ord('W'): 
            if acaoatualindex > 0:
                somopcao.play()
                acaoatualindex = acaoatualindex - 1
        elif key == ord('s') or key == ord('S'): 
            if acaoatualindex < len(menujogo)-1:
                somopcao.play()
                acaoatualindex = acaoatualindex + 1 
        elif key == curses.KEY_ENTER or key in [10,12]: 
            if acaoatualindex == 0:
                game(janela_de_fundo,cor_player)
            elif acaoatualindex == 1:
                cor_player = print_menu_config(janela_do_menu,0,cor_player)

            elif acaoatualindex == 2:
                curses.endwin()
                quit()
              

              
        if contagem_dos_loops%rodadas == 0:

            try:
                matriz.append(matriz2.pop(0))
                matriz.pop(0)
                

            except:
                criarmatrizes(comprimento_da_janela_de_fundo,largura_da_janela_de_fundo,matriz2,lista_elementosquesaoadicionados,20)

            
        if contagem_dos_loops%rodadas == 0:
            janela_de_fundo.clear()
            curses.napms(50)
            comprimento = 1
            largura = 1
            janela_de_fundo.attron(curses.color_pair(2))
            while comprimento < comprimento_da_janela_de_fundo-1:
                largura = 1
                
                while largura < largura_da_janela_de_fundo-1:
                    if comprimento> 4 and comprimento < comprimento_da_janela_de_fundo - 10:
                        if largura> largura_da_janela_de_fundo//4 and largura < comprimento_da_janela_de_fundo - largura_da_janela_de_fundo//4:
                            pass
                        else:
                            
                            janela_de_fundo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                            



                    else:
                        
                        janela_de_fundo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                        

                        
                    largura = largura + 1

                comprimento = comprimento + 1

            comprimento = 1
            largura = 1
            janela_de_fundo.attroff(curses.color_pair(2))
        else:
            pass
               

        contagem_dos_loops = contagem_dos_loops + 1

        
        print_menu(janela_do_menu,acaoatualindex,x_da_janela_do_menu,y_da_janela_do_menu)
        janela_de_fundo.refresh()


variavel = input('maximize a tela e aperte enter')


curses.wrapper(main)





