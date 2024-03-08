import curses
from curses.textpad import rectangle
from pygame import mixer
import random
from funcoes import combate
from funcoes import movplayer
from funcoes import npcmov    
from funcoes import criarmatrizes
from funcoes import colisao
from funcoes import movplayerrepor
from funcoes import ler_txt_e_colocar_na_matriz
from funcoes import cadaver_npc

mixer.init()
somopcao = mixer.Sound('somopcao.mp3')
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
                stdscr.clear()
                return cor_player
            elif acaoselecionada == 1:
                cor_player = 'rosa'
                stdscr.clear()
                return cor_player
            elif acaoselecionada == 2:
                cor_player = 'azul'
                stdscr.clear()
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



    




def game(stdscr,cor_player):
    
    mixer.init()
    mixer.music.unload()
    mixer.music.load('musicajogo.wav')
    mixer.music.play(-1)

    altura_janela_de_fundo,largura_janela_de_fundo = stdscr.getmaxyx()
    

    i = 0

    janela_de_fundo = curses.newwin(altura_janela_de_fundo , largura_janela_de_fundo , 0, 0)
    janela_de_fundo.border()
    

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
    modocombate = False
    lista_info_combate = []
    modopause = False
    lista1 = []
    lista2 = []
    altura_janela_de_jogo = altura_janela_de_fundo - 10
    largura_janela_de_jogo = largura_janela_de_fundo - 10
    matriz = []
    matriz2 = []
    matriz3 = []
    chances = 0
    listaconsumiveis = ['%','*','6']
    menupause = ['CONTINUAR','CONFIGURAÇÕES','MENU PRINCIPAL', 'SAIR']
    acaoatualindex = 0
    acaomenuconfig = 0

    curses.init_pair(7,165,curses.COLOR_BLACK)
    curses.init_pair(6,19,curses.COLOR_YELLOW)
    curses.init_pair(20, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(9, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    if cor_player == 'vermelho':
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
    elif cor_player == 'rosa':
        curses.init_pair(5, 205, curses.COLOR_BLACK)
    elif cor_player == 'azul':
        curses.init_pair(5, 20, curses.COLOR_BLACK)

    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_WHITE)
    curses.init_pair(4, 61, curses.COLOR_YELLOW)

    colidiu = 0
    verificadordecolisao = colidiu

    lista_elementosquesaoadicionados = []

    while chances < 400:
        lista_elementosquesaoadicionados.append(' ')
        chances = chances + 1

    chances = 0

    while chances < 1:
        lista_elementosquesaoadicionados.append('.')
        chances = chances + 1

    chances = 0

    comprimentodajanela = altura_janela_de_jogo
    larguradajanela = largura_janela_de_jogo
    

    while i < largura_janela_de_jogo:
        i = i + 1

        lista1.append(' ')
        


    i = 0
    while i < altura_janela_de_jogo:
        i = i + 1
        lista2.append(' ')
        


    lista1.pop()
    lista2.pop()

    variacaox = 4
    variacaoy = 5
    
    
    x= int(largura_janela_de_jogo//2)
    y= int(altura_janela_de_jogo//2)
    coordenada_y_do_player = x
    coordenada_x_do_player = y
    player = '@'
    rastro = ' '
    vida_player = 100
    vida_maxima_player = 100
    stamina_player = 100
    stamina_maxima_player = 100
    comprimento = 0
    largura = 0
    nivel_jogador = 1
    chefe_morreu = False

    criarmatrizes(comprimentodajanela,larguradajanela,matriz2,lista_elementosquesaoadicionados,20)
    criarmatrizes(comprimentodajanela,larguradajanela,matriz,lista_elementosquesaoadicionados,1)

    file_path = 'mapa.txt'  
    content_matrix = ler_txt_e_colocar_na_matriz(file_path)



    lista_npcs = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z','&']

    
    matriz[y-1][x-1] = player
    altura_atual_do_player = y - 1
    altura_inicial_do_player = y -1
    contagem_de_loops_ja_rodados = 0
    lista_colisao_player = ['.','-','|','#','&']
    lista_colisao_npc = ['.', player,'-','|','#','%','+','*','x','&']
    
    for elemento in lista_npcs:
        lista_colisao_player.append(elemento)
        lista_colisao_npc.append(elemento)
    

    #TELA DE ABERTURA

    passou_pela_duas_telas = False
    while True:
        
        if passou_pela_duas_telas == True:
            break
        

        janela_de_fundo.addstr(altura_janela_de_fundo//2-10,largura_janela_de_fundo//2-(108)//2,'Na Era dos Dragões, quando o vento sussurrava segredos ancestrais e as árvores guardavam memórias milenares,')
        janela_de_fundo.addstr(altura_janela_de_fundo//2-8,largura_janela_de_fundo//2-(110)//2,'uma terra mágica e vasta erguia-se sob os céus. Esta terra era conhecida como KAUA. Em KAUA, lendas ancestrais')
        janela_de_fundo.addstr(altura_janela_de_fundo//2-6,largura_janela_de_fundo//2-(108)//2,'e magia entrelaçavam-se com a teia do destino. Elfos sábios, anões forjadores e humanos destemidos habitavam')
        janela_de_fundo.addstr(altura_janela_de_fundo//2-4,largura_janela_de_fundo//2-(110)//2,'essas terras, cada um trazendo consigo sua própria história e propósito. Contudo, trevas ameaçam o equilíbrio.')
        janela_de_fundo.addstr(altura_janela_de_fundo//2-2,largura_janela_de_fundo//2-(114)//2,'Um mal ancestral, adormecido por eras, começa a se agitar nas profundezas da terra. Os ventos gélidos da desolação')
        janela_de_fundo.addstr(altura_janela_de_fundo//2,largura_janela_de_fundo//2-(99)//2,'sopram de terras proibidas. Você, escolhido pelo destino, ergue-se como a última esperança de KAUA.')
        janela_de_fundo.addstr(altura_janela_de_fundo//2+2,largura_janela_de_fundo//2-(101)//2,'Desbrave os reinos perdidos, aprenda os segredos da magia ancestral e forje alianças inquebrantáveis.')
        janela_de_fundo.addstr(altura_janela_de_fundo//2+4,largura_janela_de_fundo//2-(116)//2,'Agora, você se depara com um desafio sobrenatural: adentrar o sinistro castelo do Senhor Sombrio que habita em KAUA.')
        janela_de_fundo.addstr(altura_janela_de_fundo//2+6,largura_janela_de_fundo//2-(110)//2,'Com armas em punho e coragem no coração, é chegada a hora de enfrentar as trevas e confrontar o mal ancestral.')
        janela_de_fundo.addstr(altura_janela_de_fundo//2+8,largura_janela_de_fundo//2-(93)//2,'Embarque nesta saga para salvar KAUA e tornar-se parte de uma lenda que ecoará pelos séculos.')
        janela_de_fundo.addstr(altura_janela_de_fundo//2+10,largura_janela_de_fundo//2-(36)//2,'O destino de KAUA está em suas mãos.')
        janela_de_fundo.addstr(altura_janela_de_fundo-3,largura_janela_de_fundo//2-(30)//2,'Pressione Enter para continuar')

        janela_de_fundo.refresh()
        tecla_continuar = janela_de_fundo.getch()

        if tecla_continuar == curses.KEY_ENTER or tecla_continuar in [10,12]:
            janela_de_fundo.clear()
            janela_de_fundo.border()
            
            #TELA DE INSTRUÇÕES
            
            while True:

                janela_de_fundo.addstr(altura_janela_de_fundo//8,largura_janela_de_fundo//2-(23//2),'Instruções para o Jogo:')
                janela_de_fundo.addstr(altura_janela_de_fundo//4,largura_janela_de_fundo//2-(18//2),'Controles do Jogo:')
                janela_de_fundo.addstr(altura_janela_de_fundo//4+2,largura_janela_de_fundo//2-(47//2),'W/A/S/D: Movem o personagem pela terra de KAUA.')
                janela_de_fundo.addstr(altura_janela_de_fundo//4+4,largura_janela_de_fundo//2-(95//2),'Q: Entra no modo de combate, preparando-se para enfrentar os inimigos que cruzarem seu caminho.')
                janela_de_fundo.addstr(altura_janela_de_fundo//4+6,largura_janela_de_fundo//2-(108//2),'P: Entra no modo de pausa, permitindo que o jogador ajuste configurações e tome um breve respiro na jornada.')
                
                janela_de_fundo.addstr(altura_janela_de_fundo//4+9,largura_janela_de_fundo//2-(9//2),'Inimigos:')

                janela_de_fundo.addstr(altura_janela_de_fundo//4+11,largura_janela_de_fundo//2-(110//2),'Letras: São seus adversários comuns durante a aventura, representando os desafios que você encontrará em KAUA.')
                
                janela_de_fundo.attron(curses.color_pair(6))
                janela_de_fundo.addch(altura_janela_de_fundo//4+13,largura_janela_de_fundo//2-(110//2),'&')
                janela_de_fundo.attroff(curses.color_pair(6))

                janela_de_fundo.addstr(altura_janela_de_fundo//4+13,largura_janela_de_fundo//2-(110//2)+1,': É o poderoso Senhor Sombrio, a fonte do mal que ameaça KAUA. Prepare-se para um confronto épico quando enfrentá-lo.')
                


                janela_de_fundo.addstr(altura_janela_de_fundo//4+16,largura_janela_de_fundo//2-(10//2),'Elementos:')

                janela_de_fundo.attron(curses.color_pair(20))
                janela_de_fundo.addch(altura_janela_de_fundo//4+18,largura_janela_de_fundo//2-(132//2),'x')
                janela_de_fundo.attroff(curses.color_pair(20))


                janela_de_fundo.addstr(altura_janela_de_fundo//4+18,largura_janela_de_fundo//2-(132//2)+1,': Representa o corpo dos inimigos derrotados. Marca o local onde os desafios foram superados e serve como testemunho de sua coragem.')



                janela_de_fundo.attron(curses.color_pair(7))
                janela_de_fundo.addch(altura_janela_de_fundo//4+20,largura_janela_de_fundo//2-(135//2),'*')
                janela_de_fundo.attroff(curses.color_pair(7))

                janela_de_fundo.addstr(altura_janela_de_fundo//4+20,largura_janela_de_fundo//2-(135//2)+1,': Representa um elemento de cura. Ao encontrá-lo, sua vitalidade será restaurada, permitindo que continue a jornada com força renovada.')

                janela_de_fundo.attron(curses.color_pair(2))
                janela_de_fundo.addch(altura_janela_de_fundo//4+22,largura_janela_de_fundo//2-(101//2),'%')
                janela_de_fundo.attroff(curses.color_pair(2))

                janela_de_fundo.addstr(altura_janela_de_fundo//4+22,largura_janela_de_fundo//2-(101//2)+1,': É um elemento poderoso que aumenta sua vida máxima. Ao coletá-lo, você fortalecerá sua resistência.') 

                janela_de_fundo.addstr(altura_janela_de_fundo-3,largura_janela_de_fundo//2-(30)//2,'Pressione Enter para continuar')


                janela_de_fundo.refresh()
                tecla_continuar = janela_de_fundo.getch()
                if tecla_continuar == curses.KEY_ENTER or tecla_continuar in [10,12]:
                    passou_pela_duas_telas = True
                    break

            break




    janela_de_fundo.clear()


    janela_de_jogo = curses.newwin(altura_janela_de_jogo, largura_janela_de_jogo, variacaox, variacaoy)
    janela_de_jogo.border()
    janela_de_jogo.keypad(True)

    #AJUSTE DA MASMORRA NA TELA

    if largura_janela_de_jogo > 250:
        espaco = largura_janela_de_jogo//3

    if largura_janela_de_jogo > 220 and largura_janela_de_jogo < 250:
        espaco = largura_janela_de_jogo//4

    if largura_janela_de_jogo < 200 and largura_janela_de_jogo> 160:
        espaco = largura_janela_de_jogo//12


    if largura_janela_de_jogo > 200 and largura_janela_de_jogo < 220:
        espaco = largura_janela_de_jogo//5


    if largura_janela_de_jogo > 120 and largura_janela_de_jogo < 160:
        espaco = largura_janela_de_jogo//8

    if largura_janela_de_jogo<120 and largura_janela_de_jogo > 110:
        espaco = -5
    
    if largura_janela_de_jogo > 100 and largura_janela_de_jogo < 120:
        espaco = -2



    for linha in content_matrix:
        largura = 0
        for elemento in linha:
            try:
                matriz2[comprimento][largura+(espaco)] = elemento
                largura = largura + 1

            except:
                pass

        comprimento = comprimento + 1

    janela_de_jogo.nodelay(1)


    lista_aleatoriar_quantas_pocoes_vao_aparecer = []

    chances = 0


    while chances < 700:
        lista_aleatoriar_quantas_pocoes_vao_aparecer.append(' ')
        chances = chances + 1

    chances = 0

    while chances < 6:
        lista_aleatoriar_quantas_pocoes_vao_aparecer.append('*')
        chances = chances + 1

    chances = 0

    while chances < 2:
        lista_aleatoriar_quantas_pocoes_vao_aparecer.append('%')
        chances = chances + 1


    largura = 0
    comprimento = 0
    
    for linha in matriz2:
        largura = 0
        for elemento in linha:
            try:
                if matriz2[comprimento][largura] == ' ':
                    index_da_lista = random.randint(0,len(lista_aleatoriar_quantas_pocoes_vao_aparecer))
                    matriz2[comprimento][largura] = lista_aleatoriar_quantas_pocoes_vao_aparecer[index_da_lista]
                
                largura = largura + 1

            except:
                largura = largura + 1
                pass

        comprimento = comprimento + 1


    



    #LOOP DO JOGO
    while True:
        
        
        if cor_player == 'vermelho':
            curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        elif cor_player == 'rosa':
            curses.init_pair(5, 205, curses.COLOR_BLACK)
        elif cor_player == 'azul':
            curses.init_pair(5, 20, curses.COLOR_BLACK)

        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        

        janela_de_jogo.border()
        janela_de_fundo.border()
        janela_de_fundo.refresh()
        key = janela_de_jogo.getch()
        janela_de_jogo.timeout(200)
        


        
        if modopause == False:
            if key == ord('q') or key == ord('Q'):

                if modocombate == True:
                    modocombate = False
                    
                elif modocombate == False:
                    modocombate = True
                    
        if modocombate == True:
            lista_info_combate.append(vida_player)
            lista_info_combate.append(stamina_player)
            lista_info_combate.append(True)
            lista_info_combate.append(vida_maxima_player)
            lista_info_combate.append(stamina_maxima_player)
            lista_info_combate.append(nivel_jogador)
            lista_info_combate.append(False)
            
            
            combate(janela_de_jogo,janela_de_fundo,altura_janela_de_fundo,largura_janela_de_fundo,altura_janela_de_jogo,largura_janela_de_jogo,matriz,player,lista_npcs,lista_info_combate,cor_player)
            
            if lista_info_combate[8] == True:
                cadaver_npc(matriz,lista_info_combate[7],player)
                vida_maxima_player = lista_info_combate[3] + vida_maxima_player//10
                nivel_jogador = lista_info_combate[5] + 1
                stamina_maxima_player = stamina_maxima_player + stamina_maxima_player//12

            try:
                if lista_info_combate[9] == '&':
                    chefe_morreu = True
            except:
                pass
            
            modocombate = lista_info_combate[2]
            vida_player = lista_info_combate[0]
            stamina_player = lista_info_combate[1]
            lista_info_combate = []

        
        
        #movimentação do player
        if modocombate == False and modopause == False:
            if key == ord('d') or key == ord('D'):

                if coordenada_y_do_player == largura_janela_de_fundo - 12:
                    pass
                
                else:
                    verificadordecolisao = 0
                    colidiu = 0
                    for objeto in lista_colisao_player:
                        
                        verificadordecolisao = colisao('d',player,objeto,matriz,colidiu) + verificadordecolisao

                    if verificadordecolisao == 0:
                        
                        if rastro != ' ':
                            if rastro not in listaconsumiveis:
                                movplayerrepor(key,matriz,player,rastro)
                                rastro = ' '
                            
                            else:
                                rastro = ' '
                        
                        if rastro == ' ':

                            rastro = movplayer(key,matriz,player,rastro,' ')
                            if rastro == '%':
                                vida_maxima_player += nivel_jogador * 4
                            if rastro == '*':
                                if vida_player<vida_maxima_player:
                                    if vida_player + (vida_maxima_player // 20) > vida_maxima_player:
                                        vida_player = vida_maxima_player
                                    else:
                                        vida_player += vida_maxima_player // 20

                            
                                else:
                                    pass
                                # o número 6 é um consumível que serve como cheat no jogo, caso o player queira ir direto enfrentar o boss
                            if rastro == '6':
                                    nivel_jogador = 100
                                    vida_maxima_player = 10000
                                    vida_player = 10000
                            
                        coordenada_y_do_player = coordenada_y_do_player + 1

                    else:
                        pass

            elif key == ord('a') or key == ord('A'):

                if coordenada_y_do_player == 1:
                    pass

                else:
                    verificadordecolisao = 0
                    colidiu = 0
                    for objeto in lista_colisao_player:
                        verificadordecolisao = colisao('a',player,objeto,matriz,colidiu) + verificadordecolisao
                    if verificadordecolisao == 0:
                        if rastro != ' ':
                            if rastro not in listaconsumiveis:
                                movplayerrepor(key,matriz,player,rastro)
                                rastro = ' '
                            else:
                                rastro = ' '
                        if rastro == ' ':
                            rastro = movplayer(key,matriz,player,rastro,' ')
                            if rastro == '%':
                                vida_maxima_player += nivel_jogador * 4
                            if rastro == '*':
                                if vida_player<vida_maxima_player:
                                    if vida_player + (vida_maxima_player // 20) > vida_maxima_player:
                                        vida_player = vida_maxima_player
                                    else:
                                        vida_player += vida_maxima_player // 20
                                else:
                                    pass
                            if rastro == '6':
                                    nivel_jogador = 100
                                    vida_maxima_player = 10000
                                    vida_player = 10000

                        coordenada_y_do_player = coordenada_y_do_player - 1

                    else:
                        pass

            if key == ord('w') or key == ord('W') or key == ord('s') or key == ord('S'):
                if key == ord('w') or key == ord('W'):
                    if altura_inicial_do_player == altura_atual_do_player:
                        pass
                    else:
                        verificadordecolisao = 0
                        colidiu = 0
                        for objeto in lista_colisao_player:
                            verificadordecolisao = colisao('w',player,objeto,matriz,colidiu) + verificadordecolisao
                        if verificadordecolisao == 0:
                            altura_atual_do_player = altura_atual_do_player - 1
                            
                            try:
                                
                                if rastro != ' ':
                                    if rastro not in listaconsumiveis:
                                        movplayerrepor(key,matriz,player,rastro)
                                        rastro = ' '
                                        matriz.insert(0,matriz3.pop())
                                        matriz2.insert(0,matriz.pop())
                                    
                                    else:
                                        rastro = ' '

                                
                                if rastro == ' ':

                                    rastro = movplayer(key,matriz,player,rastro,' ')
                                    if rastro == '%':
                                        vida_maxima_player += nivel_jogador * 4

                                    if rastro == '*':
                                        if vida_player<vida_maxima_player:
                                            if vida_player + (vida_maxima_player // 20) > vida_maxima_player:
                                                vida_player = vida_maxima_player
                                            else:
                                                vida_player += vida_maxima_player // 20
                                        else:
                                            pass

                                    if rastro == '6':
                                        nivel_jogador = 100
                                        vida_maxima_player = 10000
                                        vida_player = 10000

                                    matriz.insert(0,matriz3.pop())
                                    matriz2.insert(0,matriz.pop())
                                
                                coordenada_x_do_player = coordenada_x_do_player - 1
                                

                            except:
                                pass
                        
                        else:
                            pass
            
                elif key == ord('s') or key == ord('S'):
                    
                    verificadordecolisao = 0
                    colidiu = 0

                    for objeto in lista_colisao_player:
                        
                        verificadordecolisao = colisao('s',player,objeto,matriz,colidiu) + verificadordecolisao

                    if verificadordecolisao == 0:
                        altura_atual_do_player = altura_atual_do_player + 1

                        try:

                            

                            if rastro != ' ':
                                if rastro not in listaconsumiveis:
                                    movplayerrepor(key,matriz,player,rastro)
                                    rastro = ' '
                                    matriz3.append(matriz.pop(0))
                                    matriz.append(matriz2.pop(0))
                                else:
                                    rastro = ' '
                            if rastro == ' ':
                                rastro = movplayer(key,matriz,player,rastro,' ')
                                if rastro == '%':
                                    vida_maxima_player += nivel_jogador * 4
                                if rastro == '*':
                                    if vida_player<vida_maxima_player:
                                        if vida_player + (vida_maxima_player // 20) > vida_maxima_player:
                                            vida_player = vida_maxima_player
                                        else:
                                            vida_player += vida_maxima_player // 20
                                    else:
                                        pass
                                if rastro == '6':
                                    nivel_jogador = 100
                                    vida_maxima_player = 10000
                                    vida_player = 10000
                                    
                                matriz3.append(matriz.pop(0))
                                matriz.append(matriz2.pop(0))

                            coordenada_x_do_player = coordenada_x_do_player + 1

                            y = 0
                            x = 0
                            
                        except:
                            criarmatrizes(comprimentodajanela,larguradajanela,matriz2,lista_elementosquesaoadicionados,2)
                            
                            matriz.append(matriz2.pop(0))
                            if rastro != ' ':
                                if rastro not in listaconsumiveis:
                                    movplayerrepor(key,matriz,player,rastro)
                                    rastro = ' '
                                    matriz3.append(matriz.pop(0))
                                    matriz.append(matriz2.pop(0))
                                
                                else:
                                    rastro = ' '
                            
                            if rastro == ' ':

                                rastro = movplayer(key,matriz,player,rastro,' ')
                                if rastro == '%':
                                    vida_maxima_player += nivel_jogador * 4
                                
                                if rastro == '*':
                                    if vida_player<vida_maxima_player:
                                        if vida_player + (vida_maxima_player // 20) > vida_maxima_player:
                                            vida_player = vida_maxima_player
                                        else:
                                            vida_player += vida_maxima_player // 20
                                    else:
                                        pass   

                                if rastro == '6':
                                    nivel_jogador = 100
                                    vida_maxima_player = 10000
                                    vida_player = 10000

                                matriz3.append(matriz.pop(0))
                                matriz.append(matriz2.pop(0))

                            coordenada_x_do_player = coordenada_x_do_player + 1

                            y = 0
                            x = 0
                    else:

                        pass
                    
        #menu de pausa
        if modocombate == False:
            if key == ord('p') or key == ord('P'):
                if modopause == True:
                    modopause = False
                    
                elif modopause == False:
                    modopause = True
                    janela_de_jogo.clear()
                    
        if modopause == True:
            curses.napms(50)
            altura = altura_janela_de_jogo
            largura = largura_janela_de_jogo
            for idx, acao in enumerate(menupause):
                curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
                x = largura//2 - len(acao)//2 - 2
                y = altura - 15 + idx 
                if idx == acaoatualindex:
                    janela_de_jogo.attron(curses.color_pair(1))
                    janela_de_jogo.addstr(y, x, acao)
                    janela_de_jogo.attroff(curses.color_pair(1))
                else:
                    janela_de_jogo.addstr(y, x, acao)

            mudança = 0
            janela_de_jogo.attron(curses.color_pair(9))
            for linha in titulo:
                for elemento in linha:
                    
                    janela_de_jogo.addstr(altura//8+mudança,largura//2-(40//2)-1,elemento)
                    mudança += 1

            janela_de_jogo.attroff(curses.color_pair(9))




            if key == ord('w') or key == ord('W'):
                if acaoatualindex > 0:
                    somopcao.play()
                    acaoatualindex = acaoatualindex - 1
            elif key == ord('s') or key == ord('S'):
                if acaoatualindex < len(menupause)-1:
                    somopcao.play()
                    acaoatualindex = acaoatualindex + 1 
            elif key == curses.KEY_ENTER or key in [10,12]: 
                if acaoatualindex == 0:
                    modopause = False
                elif acaoatualindex == 1:
                    cor_player = print_menu_config(janela_de_jogo,acaomenuconfig,cor_player)

                elif acaoatualindex == 2:
                    
                    mixer.init()
                    mixer.music.unload()
                    mixer.music.load('musicajogo2.wav')
                    mixer.music.play(-1)

                    return None
            
                elif acaoatualindex == 3:
                    curses.endwin()
                    quit()

            for idx, acao in enumerate(menupause):

                curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

                x = largura//2 - len(acao)//2 - 2
                y = altura - 15 + idx 
                if idx == acaoatualindex:
                    janela_de_jogo.attron(curses.color_pair(1))
                    janela_de_jogo.addstr(y, x, acao)
                    janela_de_jogo.attroff(curses.color_pair(1))
                else:
                    janela_de_jogo.addstr(y, x, acao)                            

            janela_de_jogo.border()                


        if modocombate == False and modopause == False:
            
            if contagem_de_loops_ja_rodados%2 == 0:
                if stamina_player < stamina_maxima_player:

                    if stamina_player + (nivel_jogador * 2) > stamina_maxima_player:
                        stamina_player = stamina_maxima_player
                    else: 
                        stamina_player += nivel_jogador * 2

                
                for npc in lista_npcs:
                    direcao = random.randint(1, 4)
                    
                    if direcao == 1:
                        
                        npcmov(1,matriz,npc,lista_colisao_npc)
                            

                    elif direcao == 2:
                        npcmov(2,matriz,npc,lista_colisao_npc)
                            
                    elif direcao == 3:
                        npcmov(3,matriz,npc,lista_colisao_npc)
                            
                    elif direcao == 4:

                        npcmov(4,matriz,npc,lista_colisao_npc)
                            

        else:
            pass


        #parte do código responsável por imprimir a matriz na tela

        if modocombate == False and modopause == False:
            comprimento = 1
            largura = 1
            while comprimento < comprimentodajanela-1:
                largura = 1
                
                while largura < larguradajanela-1:
                    if matriz[comprimento-1][largura-1] == player:
                        janela_de_jogo.attron(curses.color_pair(5))
                        janela_de_jogo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                        janela_de_jogo.attroff(curses.color_pair(5))
                    
                    elif matriz[comprimento-1][largura-1] == '-' or matriz[comprimento-1][largura-1] == '|' :
                        janela_de_jogo.attron(curses.color_pair(4))
                        janela_de_jogo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                        janela_de_jogo.attroff(curses.color_pair(4))

                    elif matriz[comprimento-1][largura-1] == '+':
                        janela_de_jogo.attron(curses.color_pair(3))
                        janela_de_jogo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                        janela_de_jogo.attroff(curses.color_pair(3))

                    elif matriz[comprimento-1][largura-1] == '#':
                        janela_de_jogo.attron(curses.color_pair(4))
                        janela_de_jogo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                        janela_de_jogo.attroff(curses.color_pair(4))

                    elif matriz[comprimento-1][largura-1] == 'x':
                        janela_de_jogo.attron(curses.color_pair(20))
                        janela_de_jogo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                        janela_de_jogo.attroff(curses.color_pair(20))

                    elif matriz[comprimento-1][largura-1] == '&':
                        janela_de_jogo.attron(curses.color_pair(6))
                        janela_de_jogo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                        janela_de_jogo.attroff(curses.color_pair(6))
                    
                    elif matriz[comprimento-1][largura-1] == '%':
                        janela_de_jogo.attron(curses.color_pair(2))
                        janela_de_jogo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                        janela_de_jogo.attroff(curses.color_pair(2))
                    
                    elif matriz[comprimento-1][largura-1] == '*':
                        janela_de_jogo.attron(curses.color_pair(7))
                        janela_de_jogo.addch(comprimento,largura,matriz[comprimento-1][largura-1])
                        janela_de_jogo.attroff(curses.color_pair(7))
                    
                    else:

                        janela_de_jogo.addch(comprimento,largura,matriz[comprimento-1][largura-1])

                    largura = largura + 1

                comprimento = comprimento + 1

            
                
        

        if modopause == False:
            janela_de_fundo.clear()

            if vida_maxima_player < 999:
                if vida_player < 100:

                    rectangle(janela_de_fundo,altura_janela_de_fundo-6,largura_janela_de_fundo//4-1,altura_janela_de_fundo-4,largura_janela_de_fundo//4+11)
                    janela_de_fundo.addstr(altura_janela_de_fundo-5,largura_janela_de_fundo//4,f'VIDA:{vida_player}/{vida_maxima_player}')

                else:
                    rectangle(janela_de_fundo,altura_janela_de_fundo-6,largura_janela_de_fundo//4-1,altura_janela_de_fundo-4,largura_janela_de_fundo//4+12)
                    janela_de_fundo.addstr(altura_janela_de_fundo-5,largura_janela_de_fundo//4,f'VIDA:{vida_player}/{vida_maxima_player}')

            
            if vida_maxima_player > 999:
                if vida_maxima_player < 9999:

                    rectangle(janela_de_fundo,altura_janela_de_fundo-6,largura_janela_de_fundo//4-1,altura_janela_de_fundo-4,largura_janela_de_fundo//4+14)
                    janela_de_fundo.addstr(altura_janela_de_fundo-5,largura_janela_de_fundo//4,f'VIDA:{vida_player}/{vida_maxima_player}')
                else:
                    rectangle(janela_de_fundo,altura_janela_de_fundo-6,largura_janela_de_fundo//4-1,altura_janela_de_fundo-4,largura_janela_de_fundo//4+19)
                    janela_de_fundo.addstr(altura_janela_de_fundo-5,largura_janela_de_fundo//4,f'VIDA:{vida_player}/{vida_maxima_player}')    

            if nivel_jogador < 100:
                rectangle(janela_de_fundo,altura_janela_de_fundo-6,(largura_janela_de_fundo//4)*3-1,altura_janela_de_fundo-4,(largura_janela_de_fundo//4)*3+8)
                janela_de_fundo.addstr(altura_janela_de_fundo-5,(largura_janela_de_fundo//4) * 3, f'NÍVEL:{nivel_jogador}')

            else:
                rectangle(janela_de_fundo,altura_janela_de_fundo-6,(largura_janela_de_fundo//4)*3-1,altura_janela_de_fundo-4,(largura_janela_de_fundo//4)*3+9)
                janela_de_fundo.addstr(altura_janela_de_fundo-5,(largura_janela_de_fundo//4) * 3, f'NÍVEL:{nivel_jogador}')

            if stamina_player <= 100:

                rectangle(janela_de_fundo,altura_janela_de_fundo-6,(largura_janela_de_fundo//2)-1,altura_janela_de_fundo-4,(largura_janela_de_fundo//2)+15)
                janela_de_fundo.addstr(altura_janela_de_fundo-5,(largura_janela_de_fundo//2),f'STAMINA:{stamina_player}/{stamina_maxima_player}')

            elif stamina_player > 100 and stamina_player < 1000:
                rectangle(janela_de_fundo,altura_janela_de_fundo-6,(largura_janela_de_fundo//2)-1,altura_janela_de_fundo-4,(largura_janela_de_fundo//2)+17)
                janela_de_fundo.addstr(altura_janela_de_fundo-5,(largura_janela_de_fundo//2),f'STAMINA:{stamina_player}/{stamina_maxima_player}')
            elif stamina_player > 100 and stamina_player > 1000:
                rectangle(janela_de_fundo,altura_janela_de_fundo-6,(largura_janela_de_fundo//2)-1,altura_janela_de_fundo-4,(largura_janela_de_fundo//2)+19)
                janela_de_fundo.addstr(altura_janela_de_fundo-5,(largura_janela_de_fundo//2),f'STAMINA:{stamina_player}/{stamina_maxima_player}')

        else:
            janela_de_fundo.clear()
            

        


        
        contagem_de_loops_ja_rodados = contagem_de_loops_ja_rodados + 1
        
        
        if vida_player <=0:

            mixer.music.unload()
            mixer.music.load('derrota.wav')
            mixer.music.play()
            janela_de_jogo.clear()
            janela_de_fundo.clear()
            janela_de_fundo.refresh()

            

            janela_de_jogo.refresh()
            tecla = 0
            janela_de_jogo.nodelay(0)

            while True:
                if tecla == curses.KEY_ENTER or tecla in [10,12]:
                    break



                janela_de_jogo.addstr(altura_janela_de_jogo//4,largura_janela_de_jogo//2-(140//2),'Em KAUA, até os mais bravos enfrentam adversidades intransponíveis. Após uma batalha árdua, o aventureiro cai derrotado, exaurido pela luta.')

                janela_de_jogo.addstr(altura_janela_de_jogo//4+2,largura_janela_de_jogo//2-(139//2), 'KAUA permanece mergulhada nas sombras, e a ameaça do Senhor Sombrio permanece inabalável. Seu nome será lembrado, mas a esperança se apaga.')

                janela_de_jogo.addstr(altura_janela_de_jogo//4+4,largura_janela_de_jogo//2-(88//2), 'O sacrifício do aventureiro será lembrado em KAUA, uma história de coragem e tenacidade.')
                janela_de_jogo.addstr(altura_janela_de_jogo-3,largura_janela_de_jogo//2-(30//2),'Pressione Enter para continuar')

                janela_de_jogo.refresh()
                tecla = janela_de_jogo.getch()

            
            janela_de_jogo.clear()

            mixer.music.unload()
            mixer.music.load('musicajogo2.wav')
            mixer.music.play(-1)

            return None
        

        
        if chefe_morreu == True:         
            mixer.music.unload()
            mixer.music.load('vitoria.wav')
            mixer.music.play()
            janela_de_jogo.clear()
            janela_de_fundo.clear()
            janela_de_fundo.refresh()
            tecla = 0
            janela_de_jogo.nodelay(0)
            while True:
                if tecla == curses.KEY_ENTER or tecla in [10,12]:
                    break



                janela_de_jogo.addstr(altura_janela_de_jogo//4,largura_janela_de_jogo//2-(90//2),'Com determinação e bravura, o aventureiro enfrenta o Senhor Sombrio em um embate titânico.')
                                                                                                     
                janela_de_jogo.addstr(altura_janela_de_jogo//4+2,largura_janela_de_jogo//2-(130//2),'Golpe após golpe, a luz da esperança vence as trevas que assolavam KAUA. O Senhor Sombrio é derrotado, e sua maldição é dissipada.')

                janela_de_jogo.addstr(altura_janela_de_jogo//4+4,largura_janela_de_jogo//2-(127//2),'Uma onda de alívio e triunfo percorre cada centímetro da terra, como se a própria natureza celebrasse a vitória do aventureiro.')

                janela_de_jogo.addstr(altura_janela_de_jogo//4+6,largura_janela_de_jogo//2-(73//2),'O castelo, outrora envolto em sombras, agora brilha com uma luz radiante.')
                
                janela_de_jogo.addstr(altura_janela_de_jogo//4+8,largura_janela_de_jogo//2-(96//2),'Os habitantes de KAUA erguem suas vozes em gratidão, reconhecendo o herói que trouxe a salvação.')

                janela_de_jogo.addstr(altura_janela_de_jogo//4+8,largura_janela_de_jogo//2-(118//2),'O aventureiro tornou-se uma lenda viva, cujo nome será cantado em canções e lembrado em contos por gerações vindouras.')

                janela_de_jogo.addstr(altura_janela_de_jogo//4+10,largura_janela_de_jogo//2-(101//2),'Parabéns, herói, por salvar KAUA e deixar um legado que ecoará eternamente pelos corredores do tempo.')

                janela_de_jogo.addstr(altura_janela_de_jogo-3,largura_janela_de_jogo//2-(30//2),'Pressione Enter para continuar')
                
                
                janela_de_jogo.refresh()
                tecla = janela_de_jogo.getch()

            
            janela_de_jogo.clear()
            mixer.music.unload()
            mixer.music.load('musicajogo2.wav')
            mixer.music.play(-1)

            return None
        
        

