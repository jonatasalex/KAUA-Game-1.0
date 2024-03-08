import random
import curses
from curses.textpad import rectangle
from pygame import mixer

mixer.init()
somsoco = mixer.Sound('soco.mp3')
somchute = mixer.Sound('chute.mp3')
somempurrao = mixer.Sound('empurrao.mp3')
somopcao = mixer.Sound('somopcao.mp3')


lista_caracteres = []
lista_de_npcs_sem_x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
i = 0



letra_a = [
    " aaaaaaaaaaaaa",
    " a::::::::::::a",
    " aaaaaaaaa:::::a",
    "           a::::a",
    "   aaaaaaaaa:::::a",
    "  aa::::::::::::a",
    " a:::: aaaa::::::a",
    "a::::a    a:::::a",
    "a::::a    a:::::a",
    "a:::::aaaa::::::a",
    "a::::::::::aa:::a",
    " aaaaaaaaaa  aaaa"]

lista_caracteres.append(letra_a)

letra_b = [
    "                    ",
    "bbbbbbbb            ",
    "b::::::b            ",
    "b::::::b            ",
    "b::::::b            ",
    " b:::::b            ",
    " b:::::bbbbbbbbb    ",
    " b::::::::::::::bb  ",
    " b::::::::::::::::b ",
    " b:::::bbbbb:::::::b",
    " b:::::b    b::::::b",
    " b:::::b     b:::::b",
    " b:::::b     b:::::b",
    " b:::::b     b:::::b",
    " b:::::bbbbbb::::::b",
    " b::::::::::::::::b ",
    " b:::::::::::::::b  ",
    " bbbbbbbbbbbbbbbb   "
]

lista_caracteres.append(letra_b)

letra_c = [
    "                    ",
    "    cccccccccccccccc",
    "  cc:::::::::::::::c",
    " c:::::::::::::::::c",
    "c:::::::cccccc:::::c",
    "c::::::c     ccccccc",
    "c:::::c             ",
    "c:::::c             ",
    "c::::::c     ccccccc",
    "c:::::::cccccc:::::c",
    " c:::::::::::::::::c",
    "  cc:::::::::::::::c",
    "    cccccccccccccccc"
]

lista_caracteres.append(letra_c)

letra_d = [
    "            dddddddd",
    "            d::::::d",
    "            d::::::d",
    "            d::::::d",
    "            d:::::d ",
    "    ddddddddd:::::d ",
    "  dd::::::::::::::d ",
    " d::::::::::::::::d ",
    "d:::::::ddddd:::::d ",
    "d::::::d    d:::::d ",
    "d:::::d     d:::::d ",
    "d:::::d     d:::::d ",
    "d:::::d     d:::::d ",
    "d::::::ddddd::::::dd",
    " d:::::::::::::::::d",
    "  d:::::::::ddd::::d",
    "   ddddddddd   ddddd"
]

lista_caracteres.append(letra_d)


letra_e = [
    "    eeeeeeeeeeee    ",
    "  ee::::::::::::ee  ",
    " e::::::eeeee:::::ee",
    "e::::::e     e:::::e",
    "e:::::::eeeee::::::e",
    "e:::::::::::::::::e ",
    "e::::::eeeeeeeeeee  ",
    "e:::::::e           ",
    "e::::::::e          ",
    " e::::::::eeeeeeee  ",
    "  ee:::::::::::::e  ",
    "    eeeeeeeeeeeeee  "
]

lista_caracteres.append(letra_e)

letra_f = [
    "    ffffffffffffffff  ",
    "   f::::::::::::::::f ",
    "  f::::::::::::::::::f",
    "  f::::::fffffff:::::f",
    "  f:::::f       ffffff",
    "  f:::::f             ",
    " f:::::::ffffff       ",
    " f::::::::::::f       ",
    " f::::::::::::f       ",
    " f:::::::ffffff       ",
    "  f:::::f             ",
    "  f:::::f             ",
    " f:::::::f            ",
    " f:::::::f            ",
    " f:::::::f            ",
    " fffffffff            "
]

lista_caracteres.append(letra_f)

letra_g = [
    "                    ",
    "   ggggggggg   ggggg",
    "  g:::::::::ggg::::g",
    " g:::::::::::::::::g",
    "g::::::ggggg::::::gg",
    "g:::::g     g:::::g ",
    "g:::::g     g:::::g ",
    "g:::::g     g:::::g ",
    "g::::::g    g:::::g ",
    "g:::::::ggggg:::::g ",
    " g::::::::::::::::g ",
    "  gg::::::::::::::g ",
    "    gggggggg::::::g ",
    "            g:::::g ",
    "gggggg      g:::::g ",
    "g:::::gg   gg:::::g ",
    " g::::::ggg:::::::g ",
    "  gg:::::::::::::g  ",
    "    ggg::::::ggg    ",
    "       gggggg       "
]

lista_caracteres.append(letra_g)

letra_h = [
    "hhhhhhh             ",
    "h:::::h             ",
    "h:::::h             ",
    "h:::::h             ",
    " h::::h hhhhh       ",
    " h::::hh:::::hhh    ",
    " h::::::::::::::hh  ",
    " h:::::::hhh::::::h ",
    " h::::::h   h::::::h",
    " h:::::h     h:::::h",
    " h:::::h     h:::::h",
    " h:::::h     h:::::h",
    " h:::::h     h:::::h",
    " h:::::h     h:::::h",
    " h:::::h     h:::::h",
    " hhhhhhh     hhhhhhh",
    "                     "
]

lista_caracteres.append(letra_h)

letra_i = [
    "  iiii  ",
    " i::::i ",
    "  iiii  ",
    "        ",
    "iiiiiii ",
    "i:::::i ",
    " i::::i ",
    " i::::i ",
    " i::::i ",
    " i::::i ",
    " i::::i ",
    " i::::i ",
    " i::::i ",
    "i::::::i",
    "i::::::i",
    "i::::::i",
    "iiiiiiii"
]

lista_caracteres.append(letra_i)

letra_j = [
    "             jjjj ",
    "            j::::j",
    "             jjjj ",
    "                  ",
    "           jjjjjjj",
    "           j:::::j",
    "            j::::j",
    "            j::::j",
    "            j::::j",
    "            j::::j",
    "            j::::j",
    "            j::::j",
    "            j::::j",
    "            j::::j",
    "            j::::j",
    "  jjjj      j::::j",
    " j::::jj   j:::::j",
    " j::::::jjj::::::j",
    "  jj::::::::::::j ",
    "    jjj::::::jjj  ",
    "       jjjjjj     "
]

lista_caracteres.append(letra_j)

letra_k = [
    "                   ",
    "                   ",
    "kkkkkkkk           ",
    "k::::::k           ",
    "k::::::k           ",
    "k::::::k           ",
    " k:::::k    kkkkkkk",
    " k:::::k   k:::::k ",
    " k:::::k  k:::::k  ",
    " k:::::k k:::::k   ",
    " k::::::k:::::k    ",
    " k:::::::::::k     ",
    " k:::::::::::k     ",
    " k::::::k:::::k    ",
    "k::::::k k:::::k   ",
    "k::::::k  k:::::k  ",
    "k::::::k   k:::::k ",
    "kkkkkkkk    kkkkkkk"
]

lista_caracteres.append(letra_k)

letra_l = [
    "        ",
    "lllllll ",
    "l:::::l ",
    "l:::::l ",
    "l:::::l ",
    " l::::l ",
    " l::::l ",
    " l::::l ",
    " l::::l ",
    " l::::l ",
    " l::::l ",
    " l::::l ",
    "l::::::l",
    "l::::::l",
    "l::::::l",
    "llllllll",
    "        ",
    "        "
]

lista_caracteres.append(letra_l)

letra_m = [
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "                        ",
    "   mmmmmmm    mmmmmmm   ",
    " mm:::::::m  m:::::::mm ",
    "m::::::::::mm::::::::::m",
    "m::::::::::::::::::::::m",
    "m:::::mmm::::::mmm:::::m",
    "m::::m   m::::m   m::::m",
    "m::::m   m::::m   m::::m",
    "m::::m   m::::m   m::::m",
    "m::::m   m::::m   m::::m",
    "m::::m   m::::m   m::::m",
    "mmmmmm   mmmmmm   mmmmmm"
]

lista_caracteres.append(letra_m)

letra_n = [
    "                 ",
    "                 ",
    "                  ",
    "nnnn  nnnnnnnn    ",
    "n:::nn::::::::nn  ",
    "n::::::::::::::nn ",
    "nn:::::::::::::::n",
    "  n:::::nnnn:::::n",
    "  n::::n    n::::n",
    "  n::::n    n::::n",
    "  n::::n    n::::n",
    "  n::::n    n::::n",
    "  n::::n    n::::n",
    "  nnnnnn    nnnnnn",
    "                  ",
    "                  "
]

lista_caracteres.append(letra_n)

letra_o = [
    "                 ",
    "                 ",
    "   ooooooooooo   ",
    " oo:::::::::::oo ",
    "o:::::::::::::::o",
    "o:::::ooooo:::::o",
    "o::::o     o::::o",
    "o::::o     o::::o",
    "o::::o     o::::o",
    "o::::o     o::::o",
    "o:::::ooooo:::::o",
    "o:::::::::::::::o",
    " oo:::::::::::oo ",
    "   ooooooooooo   ",
    "                 ",
    "                 "
]

lista_caracteres.append(letra_o)

letra_p = [
    "                    ",
    "ppppp   ppppppppp   ",
    "p::::ppp:::::::::p  ",
    "p:::::::::::::::::p ",
    "pp::::::ppppp::::::p",
    " p:::::p     p:::::p",
    " p:::::p     p:::::p",
    " p:::::p     p:::::p",
    " p:::::p    p::::::p",
    " p:::::ppppp:::::::p",
    " p::::::::::::::::p ",
    " p::::::::::::::pp  ",
    " p::::::pppppppp    ",
    " p:::::p            ",
    " p:::::p            ",
    "p:::::::p           ",
    "p:::::::p           ",
    "p:::::::p           ",
    "ppppppppp           "
]

lista_caracteres.append(letra_p)

letra_q = [
     "                    ",
    "   qqqqqqqqq   qqqqq",
    "  q:::::::::qqq::::q",
    " q:::::::::::::::::q",
    "q::::::qqqqq::::::qq",
    "q:::::q     q:::::q ",
    "q:::::q     q:::::q ",
    "q:::::q     q:::::q ",
    "q::::::q    q:::::q ",
    "q:::::::qqqqq:::::q ",
    " q::::::::::::::::q ",
    "  qq::::::::::::::q ",
    "    qqqqqqqq::::::q ",
    "            q:::::q ",
    "            q:::::q ",
    "           q:::::::q",
    "           q:::::::q",
    "           q:::::::q",
    "           qqqqqqqqq"
]

lista_caracteres.append(letra_q)

letra_r = [
    "rrrrr   rrrrrrrrr   ",
    "r::::rrr:::::::::r  ",
    "r:::::::::::::::::r ",
    "rr::::::rrrrr::::::r",
    " r:::::r     r:::::r",
    " r:::::r     rrrrrrr",
    " r:::::r            ",
    " r:::::r            ",
    " r:::::r            ",
    " r:::::r            ",
    " r:::::r            ",
    " rrrrrrr            ",
    "                    "
]

lista_caracteres.append(letra_r)

letra_s = [
    "    ssssssssss   ",
    "  ss::::::::::s  ",
    "ss:::::::::::::s ",
    "s::::::ssss:::::s",
    " s:::::s  ssssss ",
    "   s::::::s      ",
    "      s::::::s   ",
    "ssssss   s:::::s ",
    "s:::::ssss::::::s",
    "s::::::::::::::s ",
    " s:::::::::::ss  ",
    "  sssssssssss    "
]

lista_caracteres.append(letra_s)

letra_t = [
    "         tttt          ",
    "      ttt:::t          ",
    "      t:::::t          ",
    "      t:::::t          ",
    "ttttttt:::::ttttttt    ",
    "t:::::::::::::::::t    ",
    "t:::::::::::::::::t    ",
    "tttttt:::::::tttttt    ",
    "      t:::::t          ",
    "      t:::::t          ",
    "      t:::::t          ",
    "      t:::::t    tttttt",
    "      t::::::tttt:::::t",
    "      tt::::::::::::::t",
    "        tt:::::::::::tt",
    "          ttttttttttt  ",
    "                        "
]

lista_caracteres.append(letra_t)

letra_u = [
    "                  ",
    "                  ",
    "                  ",
    "                  ",
    "uuuuuu    uuuuuu  ",
    "u::::u    u::::u  ",
    "u::::u    u::::u  ",
    "u::::u    u::::u  ",
    "u::::u    u::::u  ",
    "u::::u    u::::u  ",
    "u::::u    u::::u  ",
    "u::::u    u::::u  ",
    "u:::::uuuu:::::u  ",
    "u:::::::::::::::uu",
    " u:::::::::::::::u",
    "  uu::::::::uu:::u",
    "    uuuuuuuu  uuuu"
]

lista_caracteres.append(letra_u)

letra_v = [
    "                         ",
    "                         ",
    "vvvvvvv           vvvvvvv",
    " v:::::v         v:::::v ",
    "  v:::::v       v:::::v  ",
    "   v:::::v     v:::::v   ",
    "    v:::::v   v:::::v    ",
    "     v:::::v v:::::v     ",
    "      v:::::v:::::v      ",
    "       v:::::::::v       ",
    "        v:::::::v        ",
    "         v:::::v         ",
    "          v:::v          ",
    "           vvv           ",
    "                         ",
    "                         "
]

lista_caracteres.append(letra_v)

letra_w = [
    "                                          ",
    "                                          ",
    "                                          ",
    "wwwwwww           wwwww           wwwwwww",
    " w:::::w         w:::::w         w:::::w ",
    "  w:::::w       w:::::::w       w:::::w  ",
    "   w:::::w     w:::::::::w     w:::::w   ",
    "    w:::::w   w:::::w:::::w   w:::::w    ",
    "     w:::::w w:::::w w:::::w w:::::w     ",
    "      w:::::w:::::w   w:::::w:::::w      ",
    "       w:::::::::w     w:::::::::w       ",
    "        w:::::::w       w:::::::w        ",
    "         w:::::w         w:::::w         ",
    "          w:::w           w:::w          ",
    "           www             www           "
]

lista_caracteres.append(letra_w)


letra_y = [
    "                         ",
    "yyyyyyy           yyyyyyy",
    " y:::::y         y:::::y ",
    "  y:::::y       y:::::y  ",
    "   y:::::y     y:::::y   ",
    "    y:::::y   y:::::y    ",
    "     y:::::y y:::::y     ",
    "      y:::::y:::::y      ",
    "       y:::::::::y       ",
    "        y:::::::y        ",
    "         y:::::y         ",
    "        y:::::y          ",
    "       y:::::y           ",
    "      y:::::y            ",
    "     y:::::y             ",
    "    y:::::y              ",
    "   y:::::y               ",
    "  yyyyyyy                "
]

lista_caracteres.append(letra_y)

letra_z = [
    "                 ",
    "zzzzzzzzzzzzzzzzz",
    "z:::::::::::::::z",
    "z::::::::::::::z ",
    "zzzzzzzz::::::z  ",
    "      z::::::z   ",
    "     z::::::z    ",
    "    z::::::z     ",
    "   z::::::z      ",
    "  z::::::zzzzzzzz",
    " z::::::::::::::z",
    "z:::::::::::::::z",
    "zzzzzzzzzzzzzzzzz",
    "                 "
]

lista_caracteres.append(letra_z)



jogador_lista = [
    "      @@@@@@@@@     ",
    "   @@:::::::::@@   ",
    " @@:::::::::::::@@ ",
    "@:::::::@@@:::::::@",
    "@::::::@   @::::::@",
    "@:::::@  @@@@:::::@",
    "@:::::@  @::::::::@",
    "@:::::@  @::::::::@",
    "@:::::@  @:::::::@@",
    "@:::::@  @@@@@@@@  ",
    "@::::::@           ",
    "@:::::::@@@@@@@@   ",
    " @@:::::::::::::@  ",
    "   @@:::::::::::@  ",
    "     @@@@@@@@@@@   "
]



boss_lista = [
    
 '    &&&&&&&&&&     ',
 '   &::::::::::&    ',
 '  &::::&&&:::::&   ', 
 ' &::::&   &::::&   ',  
 ' &::::&   &::::&   ',  
 '  &::::&&&::::&    ',   
 '  &::::::::::&     ',    
 '   &:::::::&&      ',     
 '  &::::::::&   &&&&',
 ' &:::::&&::&  &:::&',
 '&:::::&  &::&&:::&&',
 '&:::::&   &:::::&  ',  
 '&:::::&    &::::&  ',  
 '&::::::&&&&::::::&&',
 ' &&::::::::&&&::::&',
 '  &&&&&&&&   &&&&& ',
    ]









def movplayer(key,matriz,player,rastro,vento):
    andou = False
    y = 0
    x = 0
    if key == ord('d') or key == ord('D') or key == ord('a') or key == ord('A'):
    
        y = 0
        x = 0

        for linha in matriz:
            if andou == True:
                andou = False
                return rastro
                break
            x = 0
            for elemento in linha:
                if elemento == player:

                    if key == ord('d') or key == ord('D'):
                        rastro = matriz[y][x+1]
                        matriz[y][x] = vento
                        matriz[y][x+1] = player
                        andou = True
                        break
                    elif key == ord('a') or key == ord('A'):
                        rastro = matriz[y][x-1]
                        matriz[y][x] = vento
                        matriz[y][x-1] = player
                        andou = True
                        break


                x = x + 1
            
            y = y + 1

    elif key == ord('w') or key == ord('W') or key == ord('s') or key == ord('S'):
        y = 0
        x = 0
        for linha in matriz:
            if andou == True:
                andou = False
                return rastro
                
            x = 0
            for elemento in linha:
                if elemento == player:

                    if key == ord('w') or key == ord('W'):
                        rastro = matriz[y-1][x]
                        matriz[y][x] = vento
                        matriz[y-1][x] = player
                        andou = True
                        break
                    elif key == ord('s') or key == ord('S'):
                        rastro = matriz[y+1][x]
                        matriz[y][x] = vento
                        matriz[y+1][x] = player
                        andou = True
                        break

                x = x + 1
            
            y = y + 1



def npcmov(direcao,matriz,npc,listadecoli):
    andou = False
    y = 0
    x = 0
    if direcao == 1 or direcao == 3:
        y = 0
        x = 0

        for linha in matriz:
            if andou == True:
                andou = False
                break
            x = 0
            for elemento in linha:
                if elemento == npc:

                    if direcao == 1:
                        for elementos in listadecoli:
                            if matriz[y-1][x] == elementos:
                                andou = True
                                break
                        
                        if andou == True:
                            break
                        else:
                            #esse if é pra garantir que o boneco não "saia" da matriz, mas na verdade ele vai pro índicie -1, que é o final, queremos evitar isso com esse if
                            if y-1 == -1:
                                pass
                            else:
                                matriz[y][x] = ' '
                                matriz[y-1][x] = npc
                            andou = True
                            break

                    
                    elif direcao == 3:
                        for elementos in listadecoli:
                            try:
                                if matriz[y+1][x] == elementos:
                                    andou = True
                                    break
                            except:
                                pass
                        if andou == True:
                            break
                        else:
                            # try-except pra evitar que o npc saia do mapa
                            try:
                                matriz[y+1][x] = npc
                                matriz[y][x] = ' '
                            except:
                                pass
                            
                            andou = True
                            break


                x = x + 1
            
            y = y + 1

    elif direcao == 2 or direcao == 4:
        y = 0
        x = 0

        for linha in matriz:
            x = 0
            for elemento in linha:
                if elemento == npc:

                    if direcao == 2:
                        for elementos in listadecoli:
                            if matriz[y][x-1] == elementos:
                                andou = True
                                break
                        if andou == True:
                            break

                        matriz[y][x] = ' '
                        matriz[y][x-1] = npc
                        andou = True
                        break

                    elif direcao == 4:

                        for elementos in listadecoli:
                            if matriz[y][x+1] == elementos:
                                andou = True
                                break

                        if andou == True:
                            break
                        matriz[y][x] = ' '
                        matriz[y][x+1] = npc
                        andou = True
                        break

                x = x + 1
            
            y = y + 1



def criarmatrizes(x,y,matriz,lista,vezes_que_as_linhas_vao_ser_criadas):

    h = 1
    w = 1
    
    while h < (x-1) * vezes_que_as_linhas_vao_ser_criadas:
        w = 1
        linhaz = []
        while w < y-1:
            for elemento in lista:
                chancedeaparecer = random.randint(0,len(lista)-1)
                

                linhaz.append(lista[chancedeaparecer])
                w = w + 1


        matriz.append(linhaz)
        h = h + 1




def colisao(direcao,personagem,barreira,matriz,variaveldecolisao):
    x = 0 
    y = 0
    variaveldecolisao = 0
    
    if direcao == 'd' or direcao == 4 or direcao == 'D':

        for linha in matriz:

            x = 0

            for elemento in linha:

                if elemento == personagem:

                    try:
                        if matriz[y][x+1]==barreira:
                            variaveldecolisao = variaveldecolisao + 1
                            return variaveldecolisao
                        else:
                            return 0

                    except:
                        pass
                
                x = x + 1
            y = y + 1
        return 0


    elif direcao == 'a' or direcao == 2 or direcao == 'A':

        for linha in matriz:
            x = 0
            for elemento in linha:

                if elemento == personagem:


                    try:
                        if matriz[y][x-1]==barreira:
                            variaveldecolisao = variaveldecolisao + 1
                            return variaveldecolisao
                        else:
                            return 0

                    except:
                        pass  

                x = x + 1

            y = y + 1
        return 0

    elif direcao == 's' or direcao == 3 or direcao == 'S':
        variaveldecolisao =0

        for linha in matriz:
            x = 0

            for elemento in linha:

                if elemento == personagem:
                    a = x
                    b = y

                    try:

                        if matriz[y+1][x] == barreira:
                            variaveldecolisao = variaveldecolisao + 1
                            return variaveldecolisao
                        else:
                            return 0

                            
                            

                    except:
                        break

                x = x + 1
            y = y + 1
        return 0

        

    elif direcao == 'w' or direcao == 1 or direcao == 'W':

        for linha in matriz:
            x = 0

            for elemento in linha:

                if elemento == personagem:


                    try:
                        if matriz[y-1][x] == barreira:
                            variaveldecolisao = variaveldecolisao + 1
                            return variaveldecolisao
                        else:
                            return 0

                    except:
                        pass

                x = x + 1

            y = y + 1 
        return 0
            


    

def movplayerrepor(key,matriz,player,rastro):
    andou = False
    y = 0
    x = 0
    if key == ord('d') or key == ord('D') or key == ord('a') or key == ord('A'):
    
        y = 0
        x = 0

        for linha in matriz:
            if andou == True:
                andou = False
                return rastro
                break
            x = 0
            for elemento in linha:
                if elemento == player:

                    if key == ord('d') or key == ord('D'):
                        
                        matriz[y][x] = rastro
                        matriz[y][x+1] = player
                        andou = True
                        break
                    elif key == ord('a') or key == ord('A'):
                        matriz[y][x] = rastro
                        matriz[y][x-1] = player
                        andou = True
                        break


                x = x + 1
            
            y = y + 1

    elif key == ord('w') or key == ord('W') or key == ord('s') or key == ord('S'):
        y = 0
        x = 0
        for linha in matriz:
            if andou == True:
                andou = False
                return rastro
                break
            x = 0
            for elemento in linha:
                if elemento == player:

                    if key == ord('w') or key == ord('W'):
                        matriz[y][x] = rastro
                        matriz[y-1][x] = player
                        andou = True
                        break
                    elif key == ord('s') or key == ord('S'):
                        matriz[y][x] = rastro
                        matriz[y+1][x] = player
                        andou = True
                        break

                x = x + 1
            
            y = y + 1



def ler_txt_e_colocar_na_matriz(file_path):
    matrix = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matrix.append(list(line))  
    return matrix






def combate(win,win3,altura_win3,largura_win3,altura_win,largura_win,matriz,player,lista_npcs,lista_info,cor_player):
    
    lista_npcs_encontrados = []
    lista_ataques = ['soco','chute','empurrão','meter o pé']
    y = 0
    x = 0
    l = False
    sem_inimigos = False
    npc_que_irei_lutar = ' '
    ja_limpou_a_tela10 = False
    ja_limpou_a_tela100 = False
    curses.init_pair(10,19,curses.COLOR_YELLOW)
    if cor_player == 'vermelho':
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
    elif cor_player == 'rosa':
        curses.init_pair(5, 205, curses.COLOR_BLACK)
    elif cor_player == 'azul':
        curses.init_pair(5, 20, curses.COLOR_BLACK)
    

    
    for linha in matriz:
            if l == True:
                l = False
                break
            x = 0
            for elemento in linha:
                if elemento == player:
                    
                    
                    #down left

                    if matriz[y+2][x-2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+2][x-2])


                    if matriz[y+1][x-1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+1][x-1])



                    #down right

                    if matriz[y+1][x+1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+1][x+1])


                    if matriz[y+2][x+2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+2][x+2])


                    #up right
                    
                    if matriz[y-1][x+1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-1][x+1])


                    if matriz[y-2][x+2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-2][x+2])


                    #up left

                    if matriz[y-2][x-2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-2][x-2])


                    if matriz[y-1][x-1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-1][x-1])


                    
                    #left
                    if matriz[y][x-1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y][x-1])

                    if matriz[y][x-2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y][x-2])


                    
                    #right
                    if matriz[y][x+1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y][x+1])

        
                    if matriz[y][x+2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y][x+2])

                    
                    #down

                    if matriz[y+1][x] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+1][x])

                    
                    
                    if matriz[y+2][x] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+2][x])
                    

                    #up

                    if matriz[y-1][x] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-1][x])

                    
                    
                    if matriz[y-2][x] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-2][x])

                    
                    #up center
                    if matriz[y-2][x+1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-2][x+1])


                    if matriz[y-2][x-1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-2][x-1])

                    
                    #mid up center

                    if matriz[y-1][x-2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-1][x-2])


                    if matriz[y-1][x+2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y-1][x+2])


                    #mid down center
                    if matriz[y+1][x-2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+1][x-2])

                    
                    
                    if matriz[y+1][x+2] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+1][x+2])


                    #down center

                    if matriz[y+2][x-1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+2][x-1])

                    if matriz[y+2][x+1] in lista_npcs:
                        lista_npcs_encontrados.append(matriz[y+2][x+1])



                    
                    if len(lista_npcs_encontrados) == 0:
                        l = True
                        sem_inimigos = True

                    break

                x = x + 1
            y = y + 1
    


    if sem_inimigos == False:
        win.clear()
        win.nodelay(1)
        acaoatualindex = 0
        luta = False
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        
        while True:
            i = 0
            key = win.getch()

            
                        
                

            win.addstr(1,largura_win//2-15,'Com qual inimigo desejas lutar?')


            for idx, inimigo in enumerate(lista_npcs_encontrados):

                

                y = altura_win//2 - len(inimigo)//2 - 2 + idx
                x = largura_win//2  
                if idx == acaoatualindex:
                    win.attron(curses.color_pair(1))
                    win.addch(y, x, inimigo)
                    win.attroff(curses.color_pair(1))
                else:
                    win.attron(curses.color_pair(2))
                    win.addch(y, x, inimigo)
                    win.attroff(curses.color_pair(2))


            if key == ord('w') or key == ord('W'): 
                if acaoatualindex > 0:
                    acaoatualindex = acaoatualindex - 1
            elif key == ord('s') or key == ord('S'):
                if acaoatualindex < len(lista_npcs_encontrados)-1:
                    acaoatualindex = acaoatualindex + 1 
            
            elif key == curses.KEY_ENTER or key in [10,13]:

                
                    
                npc_que_irei_lutar = lista_npcs_encontrados[acaoatualindex]
                luta = True
                break
                    

 
                    
        linha_sub = []
        lista_npc_combate = []
        i = 0

        for npc in lista_de_npcs_sem_x:
            if npc_que_irei_lutar == npc:
                for linha in lista_caracteres[i]:
                    linha_sub = []
                    for elemento in linha:
                        linha_sub.append(elemento)

                    lista_npc_combate.append(linha_sub)
            elif npc_que_irei_lutar == '&':
                mixer.music.unload()
                mixer.music.load('bosssong.wav')
                mixer.music.play(-1)
                
                for linha in boss_lista:
                    linha_sub = []
                    for elemento in linha:
                        linha_sub.append(elemento)

                    lista_npc_combate.append(linha_sub)
                break

            i+=1



        if luta == True:

            if npc_que_irei_lutar == '&':

                level_npc = 3000//lista_info[5]
                vida_npc = 50+(level_npc*30)
                dano_npc = 5 + level_npc*10

            else:
                level_npc = random.randint(1,lista_info[5]+(lista_info[5]//2))

                    
                vida_npc = 50+(level_npc*6)
                dano_npc = 5 + level_npc*3
            
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
            curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
            quantidade_de_linhas = 0
            win3.border()
            win.clear()
            win.border()
            acaoatualindex = 0
            dano_soco = 1 + 5*(lista_info[5])
            dano_chute = 10 + 5*(lista_info[5])
            dano_empurrao = 1 + 2*(lista_info[5])
            
            while True:
                
                quantidade_de_linhas = 0
                quantidade_de_colunas = 0
                
                
                
                win3.border()
                win3.refresh()
                win.border()
                key = win.getch()
                




                for index, ataque in enumerate(lista_ataques):

                    

                    y = altura_win//2 + index
                    x = largura_win//2 - (len(ataque)//2) + 2 
                    if index == acaoatualindex:
                        win.attron(curses.color_pair(1))
                        win.addstr(y, x, ataque)
                        win.attroff(curses.color_pair(1))
                    else:
                        win.attron(curses.color_pair(2))
                        win.addstr(y, x, ataque)
                        win.attroff(curses.color_pair(2))


                if key == ord('w') or key == ord('W'): 
                    if acaoatualindex > 0:
                        somopcao.play()
                        acaoatualindex = acaoatualindex - 1
                elif key == ord('s') or key == ord('S'): 
                    if acaoatualindex < len(lista_ataques)-1:
                        somopcao.play()
                        acaoatualindex = acaoatualindex + 1 
                
                elif key == curses.KEY_ENTER or key in [10,14]:

                    if acaoatualindex == 0:
                        somsoco.play()
                        vida_npc = vida_npc - dano_soco
                        lista_info[1] = lista_info[1] - 5 + lista_info[5]
                        curses.napms(500)
                        lista_info[0] = lista_info[0] - dano_npc

                    if acaoatualindex == 1:
                        somchute.play()    
                        vida_npc = vida_npc - dano_chute
                        lista_info[1] = lista_info[1] - 10 + lista_info[5]
                        curses.napms(500)
                        lista_info[0] = lista_info[0] - dano_npc

                    if acaoatualindex == 2:
                        somempurrao.play()
                        vida_npc = vida_npc - dano_empurrao
                        lista_info[1] = lista_info[1] - 2 + lista_info[5]
                        curses.napms(500)
                        lista_info[0] = lista_info[0] - dano_npc



                
                    if acaoatualindex == 3:
                        luta = False


                    pass

                
                    
                for linhas in lista_npc_combate:
                    quantidade_de_linhas += 1

                for lines in lista_npc_combate:
                    for colunas in lines:
                        quantidade_de_colunas +=1
                    break
                        


                y=0
                x=0

                if npc_que_irei_lutar == '&':
                    win.attron(curses.color_pair(6))
                    for linha in lista_npc_combate:
                        
                        x=0
                        for caractere in linha:
                            if caractere != ' ':
                                win.addch(altura_win-quantidade_de_linhas-quantidade_de_linhas//2+y,largura_win-quantidade_de_colunas-10+x,caractere)
                            x+=1
                        y+=1
                    win.attroff(curses.color_pair(6))



                else:



                    for linha in lista_npc_combate:
                        
                        x=0
                        for caractere in linha:
                            win.addch(altura_win-quantidade_de_linhas-quantidade_de_linhas//2+y,largura_win-quantidade_de_colunas-10+x,caractere)
                            x+=1
                        y+=1

                


                y=0
                x=0

                win.attron(curses.color_pair(5))
                for linha in jogador_lista:

                    x = 0

                    for caractere in linha:
                        win.addstr(altura_win-quantidade_de_linhas-quantidade_de_linhas//2+y,10+x,caractere)
                        x +=1
                    y+=1

                win.attroff(curses.color_pair(5))


                win3.clear()
                

                if lista_info[3]<999:
                    if lista_info[0] < 100:

                        
                        
                        rectangle(win3,altura_win3-6,largura_win3//4-1,altura_win3-4,largura_win3//4+11)
                        win3.addstr(altura_win3-5,largura_win3//4,f'VIDA:{lista_info[0]}/{lista_info[3]}')
                    else:
                        rectangle(win3,altura_win3-6,largura_win3//4-1,altura_win3-4,largura_win3//4+12)
                        win3.addstr(altura_win3-5,largura_win3//4,f'VIDA:{lista_info[0]}/{lista_info[3]}')

                if lista_info[3]>999:
                    if lista_info[3]<9999:
                        rectangle(win3,altura_win3-6,largura_win3//4-1,altura_win3-4,largura_win3//4+14)
                        win3.addstr(altura_win3-5,largura_win3//4,f'VIDA:{lista_info[0]}/{lista_info[3]}')
                    else:
                        rectangle(win3,altura_win3-6,largura_win3//4-1,altura_win3-4,largura_win3//4+19)
                        win3.addstr(altura_win3-5,largura_win3//4,f'VIDA:{lista_info[0]}/{lista_info[3]}')

                if lista_info[5] < 100:
                    rectangle(win3,altura_win3-6,(largura_win3//4)*3-1,altura_win3-4,(largura_win3//4)*3+8)
                    win3.addstr(altura_win3-5,(largura_win3//4) * 3, f'NÍVEL:{lista_info[5]}')
                else:
                    rectangle(win3,altura_win3-6,(largura_win3//4)*3-1,altura_win3-4,(largura_win3//4)*3+9)
                    win3.addstr(altura_win3-5,(largura_win3//4) * 3, f'NÍVEL:{lista_info[5]}')


                if lista_info[1] <= 100:
                    
                    rectangle(win3,altura_win3-6,(largura_win3//2)-1,altura_win3-4,(largura_win3//2)+15)
                    win3.addstr(altura_win3-5,(largura_win3//2),f'STAMINA:{lista_info[1]}/{lista_info[4]}')

                elif lista_info[1] > 100 and lista_info[1] < 1000:
                    rectangle(win3,altura_win3-6,(largura_win3//2)-1,altura_win3-4,(largura_win3//2)+17)
                    win3.addstr(altura_win3-5,(largura_win3//2),f'STAMINA:{lista_info[1]}/{lista_info[4]}')

                elif lista_info[1] > 100 and lista_info[1] > 1000:
                    rectangle(win3,altura_win3-6,(largura_win3//2)-1,altura_win3-4,(largura_win3//2)+19)
                    win3.addstr(altura_win3-5,(largura_win3//2),f'STAMINA:{lista_info[1]}/{lista_info[4]}')

                # rectangle(win,sh//4)
                win.addstr(1,largura_win//2-8,f'Level do Inimigo:{level_npc}')
                
                
                
                if ja_limpou_a_tela10 == False:
                    if vida_npc < 10:
                        win.clear()
                        ja_limpou_a_tela10 = True

                if ja_limpou_a_tela100 == False:
                    if vida_npc<100:
                        win.clear()
                        ja_limpou_a_tela100 = True

                    

                win.addstr(3,largura_win//2-8,f'Vida do Inimigo:{vida_npc}')
                
                
                if vida_npc <= 0 :
                    luta = False

                if lista_info[0]<=0 or lista_info[1]<=0:
                    luta = False
                    
                

                if luta == False and vida_npc <= 0:
                    lista_info[2] = False
                    lista_info.append(npc_que_irei_lutar)
                    lista_info.append(True)
                    if npc_que_irei_lutar == '&':
                        lista_info.append(npc_que_irei_lutar)
                    return lista_info
                
                if luta == False and vida_npc > 0:
                    if npc_que_irei_lutar == '&':

                        mixer.music.unload()
                        mixer.music.load('musicajogo.wav')
                        mixer.music.play(-1)

                    lista_info[2] = False
                    lista_info.append('nada')
                    lista_info.append(False)
                    
                    return lista_info

                
                

                
    else:
        lista_info.append('nada')
        lista_info.append(False)
        lista_info[2] = False
        return lista_info



                
def cadaver_npc(matriz,npc,player):
    y = 0
    x = 0
    l = False


    for linha in matriz:
            if l == True:
                l = False
                break
            x = 0
            for elemento in linha:
                if elemento == player:
                    

                    #down left

                    if matriz[y+2][x-2] == npc:
                        matriz[y+2][x-2] = 'x'


                    if matriz[y+1][x-1] == npc:
                        matriz[y+1][x-1] = 'x'



                    #down right

                    if matriz[y+1][x+1] == npc:
                        matriz[y+1][x+1] = 'x'


                    if matriz[y+2][x+2] == npc:
                        matriz[y+2][x+2] = 'x'


                    #up right
                    
                    if matriz[y-1][x+1] == npc:
                        matriz[y-1][x+1] = 'x'


                    if matriz[y-2][x+2] == npc:
                        matriz[y-2][x+2] = 'x'


                    #up left

                    if matriz[y-2][x-2] == npc:
                        matriz[y-2][x-2] = 'x'


                    if matriz[y-1][x-1] == npc:
                        matriz[y-1][x-1] = 'x'


                    
                    #left
                    if matriz[y][x-1] == npc:
                        matriz[y][x-1] = 'x'

                    if matriz[y][x-2] == npc:
                        matriz[y][x-2] = 'x'


                    
                    #right
                    if matriz[y][x+1] == npc:
                        matriz[y][x+1] = 'x'


                    if matriz[y][x+2] == npc:
                        matriz[y][x+2] = 'x'

                    
                    #down

                    if matriz[y+1][x] == npc:
                        matriz[y+1][x] = 'x'

                    
                    
                    if matriz[y+2][x] == npc:
                        matriz[y+2][x] = 'x'
                    

                    #up

                    if matriz[y-1][x] == npc:
                        matriz[y-1][x] = 'x'

                    
                    
                    if matriz[y-2][x] == npc:
                        matriz[y-2][x] = 'x'

                    
                    #up center
                    if matriz[y-2][x+1] == npc:
                        matriz[y-2][x+1] = 'x'


                    if matriz[y-2][x-1] == npc:
                        matriz[y-2][x-1] = 'x'

                    
                    #mid up center

                    if matriz[y-1][x-2] == npc:
                        matriz[y-1][x-2] = 'x'


                    if matriz[y-1][x+2] == npc:
                        matriz[y-1][x+2] = 'x'


                    #mid down center
                    if matriz[y+1][x-2] == npc:
                        matriz[y+1][x-2] = 'x'

                    
                    
                    if matriz[y+1][x+2] == npc:
                        matriz[y+1][x+2] = 'x'


                    #down center

                    if matriz[y+2][x-1] == npc:
                        matriz[y+2][x-1] = 'x'

                    if matriz[y+2][x+1] == npc:
                        matriz[y+2][x+1] = 'x'


                x = x + 1
            y = y + 1        
