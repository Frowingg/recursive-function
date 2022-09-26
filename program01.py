#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Una proprietaria terriera in California, Lida, eredita un
appezzamento di terreno. La superficie è modellata come un lotto
rettangolare di grandezza variabile. Il lotto di terra è
rappresentato come un'immagine codificata come lista di liste.

Per far fruttare l'appezzamento di terra, Lida decide di affittare la
terra ad altre persone. Per fare ciò, può decidere di dividere la
terra in quattro parti. Nel caso in cui decida di non affittare la sua
proprietà nessuna divisione è effettuata. Al contrario, nel caso in
cui la proprietà venga divisa in quattro sotto parti, delle linee di
demarcazione colorate vengono create, per tutelare i confini, appunto.
Le linee hanno uno spessore di un solo pixel. Non è dato sapere come
e dove le line verranno poste (non vi è una regolarità), e neppure
sappiamo quale è il colore che verrà usato a priori.  Conosciamo
solamente che le linee sono allineate agli assi.

I quattro locatari che ricevono le quattro proprietà potrebbero
prendere la solita decisione che Lida ha preso in precedenza oppure
no: essi potrebbero subaffittare ancora una volta le loro piccole
proprietà ad altre persone, oppure, potrebbero decidere di tenere la
terra tutta per loro. La decisione della suddivisione per ogni
locatario è indipendente alle altre. Per esempio, il locatario #1 può
decidere di subaffittare ancora, mentre il locatario #2 può tenere la
proprietà, mentre i locatari #3, #4 possono suddividere ancora. Quello
che sappiamo è che se subaffittano, dividono sempre in quattro
parti. Infatti, nel caso in cui dividano ancora la proprietà,
seguiranno una strategia simile di impostare i loro confini tracciando
delle linee di demarcazione degli stessi. Sicuramente useranno un
colore che è diverso dai colori usati da Lida (e da altri eventuali in
precedenza) tuttavia i quattro locatari usano il solito colore fra
loro, allo stesso livello di suddivisione.

NOTA: E' importante ricordare che il colore del background (bg) dell'
appezzamento non è dato (cioè non sappiamo a priori se il bg è
nero, bianco oppure blue). Sappiamo però che il colore di background
della terra NON è usato da nessuno dei locatari (ne da Lida) per
marcare i confini.

Il processo di suddivisione può continuare fino a quando tutti i
locatari in tutte gli appezzamenti decidono di smettere col subaffitto.
Questo processo descritto fino ad ora, ci porta all'immagine che è
data in input al vostro programma.

NOTA: Potete assumere che l'ipotetico appezzamento di terreno più
piccolo (rettangolo più piccolo possibile) abbia il lato più corto di
due pixel.

Riflettete bene sul problema e una volta che siete sicuri di una
soluzione, progettate su carta una soluzione (questa soluzione poi
deve essere descritta nella pseudo codice) e poi implementate un
programma ex1(input_file, output_file) che:
   - legge il file indicato dal parametro 'input_file' usando
     il modulo libreria 'images'.
   - pre-processa l'immagine, se necessario, e implementa una funzione
     *ricorsiva* per risolvere i requisiti sottostanti.
   - si deve contare tutte gli appezzamenti di terra che sono nell'
     immagine e restituire questo conteggio. 
     
     Il programma deve
     restituire il numero di rettangoli con il colore del background
     dell'immagine che vi sono presenti. Riferendosi alla figura
     semplificata sottostante:

        # +++++++++++++++++++
        # +-1-|-2-|---------+
        # ++++a+++|----5----+
        # +-3-|-4-|---------+
        # ++++++++b++++++++++
        # +-------|--7-|-8--+
        # +---6---|++++c+++++
        # +-------|-10-|-9--+
        # +++++++++++++++++++
  
    l'approccio deve restituire un intero che corrisponde a 10 in
    questo caso (numero totale di rettangoli). I numeri posti nella
    figura soprastante sono stati inseriti solo per chiarire il
    concetto. (I dati sono privi di tali numeri inseriti, ovviamente).
    - infine, dato che l'agenzia immobiliare deve registrare
    tutti i confini che sono creati, il programma deve costruire un'
    immagine di output di grandezza  1x(N+1). L'immagine codifica come
    primo pixel il colore del background. Poi, deve codificare la
    gerarchia dei colori di tutti gli N colori usati per suddividere
    la terra in sotto rettangoli. La gerarchia dei colori e' definita
    "visitando" prima in profondita' il lotto in alto a sx, poi in
    alto a dx, poi in basso a sx, e infine in basso a dx. I colori
    devono essere salvati in ordine inverso rispetto alla visita
    effettuata. Con riferimento all'immagine semplificata precedente,
    assumendo che i colori dei confini di demarcazione siano descritti
    dalla lettere al loro centro, allora l'immagine di output deve
    contenere:
             out_colors = bg b c a


    Un altro esempio un pochino piu' complesso:

         +++++++++++++++++++++++++++++++++++++
         +-1-|-2-|---------|--------|--------+
         ++++a+++|----5----|---6----|----7---+
         +-3-|-4-|---------|--------|--------+
         ++++++++b+++++++++|++++++++c+++++++++
         +-------|--9-|-10-|--------|--------+
         +--8----|++++d++++|---13---|---14---+
         +-------|-11-|-12-|--------|--------+
         ++++++++++++++++++e++++++++++++++++++
         +-15|-16|---------|--------|-21|-22-+
         ++++f+++|---19----|---20---|+++g+++++
         +-17|-18|---------|--------|-23|--24+
         ++++++++h+++++++++|++++++++l+++++++++
         +-------|-26-|-27-|--------|-31-|-32+
         +--25---|++++m++++|---30---|+++n+++++
         +-------|-29-|-28-|--------|-33-|-34+
         +++++++++++++++++++++++++++++++++++++

         num. rect: 34
         gerarchia dei colori:
         bg e l n g h m f c b d a


NOTA: è vietato importare/usare altre librerie o aprire file tranne
quello indicato

NOTA: il sistema di test riconosce la presenza di ricorsione SOLO se
    la funzione/metodo ricorsivo è definita a livello esterno.  NON
    definite la funzione ricorsiva all'interno di un'altra
    funzione/metodo altrimenti fallirete tutti i test.

lotto rettangolare di grandezza variabile (immagine codificata come lista di liste)

nel caso in
cui la proprietà venga divisa in quattro sotto parti, delle linee di
demarcazione colorate vengono create, per tutelare i confini, appunto.
Le linee hanno uno spessore di un solo pixel. Non è dato sapere come
e dove le line verranno poste (non vi è una regolarità), e neppure
sappiamo quale è il colore che verrà usato a priori.  Conosciamo
solamente che le linee sono allineate agli assi.

se subaffittano, dividono sempre in quattro
parti

 Potete assumere che l'ipotetico appezzamento di terreno più
piccolo (rettangolo più piccolo possibile) abbia il lato più corto di
due pixel.

   - legge il file indicato dal parametro 'input_file' usando
     il modulo libreria 'images'.
   - pre-processa l'immagine, se necessario, e implementa una funzione
     *ricorsiva* per risolvere i requisiti sottostanti
     
1) implementa una funzione
  *ricorsiva* per risolvere i requisiti sottostanti
  
2) Il programma deve
     restituire il numero di rettangoli con il colore del background
     dell'immagine che vi sono presenti.
     
3)il programma deve costruire un'immagine di output di grandezza  1x(N+1) 
    che deve contenere:
        1)primo pixel il colore del background
        2)codificare la
        gerarchia dei colori di tutti gli N colori usati per suddividere
        la terra in sotto rettangoli.
            1)La gerarchia dei colori e' definita
            "visitando" prima in profondita' il lotto in alto a sx, poi in
            alto a dx, poi in basso a sx, e infine in basso a dx.
            2)I colori
            devono essere salvati in ordine inverso rispetto alla visita
            effettuata
            
            
            +++++++++++++++++++++++++++++++++++++
            +-1-|-2-|---------|--------|--------+
            ++++a+++|----5----|---6----|----7---+
            +-3-|-4-|---------|--------|--------+
            ++++++++b+++++++++|++++++++c+++++++++
            +-------|--9-|-10-|--------|--------+
            +--8----|++++d++++|---13---|---14---+
            +-------|-11-|-12-|--------|--------+
            ++++++++++++++++++e++++++++++++++++++
            +-15|-16|---------|--------|-21|-22-+
            ++++f+++|---19----|---20---|+++g+++++
            +-17|-18|---------|--------|-23|--24+
            ++++++++h+++++++++|++++++++l+++++++++
            +-------|-26-|-27-|--------|-31-|-32+
            +--25---|++++m++++|---30---|+++n+++++
            +-------|-29-|-28-|--------|-33-|-34+
            +++++++++++++++++++++++++++++++++++++

            num. rect: 34
            gerarchia dei colori:
            bg e l n g h m f c b d a
"""

#import images
from images import load
from images import save
#from images import visd

def codifica_img(img, n_ret = 0):
    #visd(img)    
    dizio_y = {}
    dizio_x = {}
    dizio_n_px = {}
    dizio_px_finale_y = {}
    dizio_px_finale_x = {}  
    ordine = []
    bg = img[0][0]
    dizio_n_bg = {bg:-1}
    b = len(img[0])-1
    h = len(img)-1
    
    for y, line in enumerate(img):
        if y == 1:
            if dizio_n_bg[bg] == b:
                n_ret += 1
                return [ordine, n_ret]  
        for x, pixel in enumerate(line):    
            if pixel != bg:
                    if x == b:
                       dizio_px_finale_x[pixel] = x+1
                    elif  y == h:
                       dizio_px_finale_y[pixel] = y+1
                    elif x == 0:
                        dizio_y[pixel] = y                    
                    elif y == 0:
                        dizio_x[pixel] = x
                    if pixel not in dizio_n_px:
                        dizio_n_px[pixel] = 0
                    else:
                        dizio_n_px[pixel] += 1
            else:
                if y == 0:
                    dizio_n_bg[bg] += 1
                                        
    #scorro l'img e mi salvo le coordinate con x e y uguali a 0 
    #e il num di px per ogni px 
        

    #se l'img non ha divisione conto un rettangolo e mi fermo
        
    for px in dizio_n_px:
        
    #per ogni px in dizio_n_px 
    
        if len(img) + len(img[0]) == dizio_n_px[px]+2 and px in dizio_px_finale_y and px in dizio_px_finale_x:
            
        #se la demarcazione divide la img in 4
        
            if len(dizio_n_px) < 2:                
                ordine += [px]
                n_ret += 4     
                break
            #se non ci sono demarcazione più profonde aggiunge 4 ret al conto
            #e il suo colore per l'img finale
                
            else:  
                
            #se si divide ulteriormente                
                                
                temp_y = dizio_y[px]
                temp_x = dizio_x[px]
                img_a = img[:temp_y]
                img_b = img[temp_y+1:]
                
                #salvo la metà alta e la metà bassa come due img diverse
                
                img_a_sx = []
                img_a_dx = []
                img_b_sx = []
                img_b_dx = [] 
                for line in img_a:
                    img_a_sx.append(line[:temp_x])                        
                    img_a_dx.append(line[temp_x+1:])                    
                for line in img_b:
                    img_b_sx.append(line[:temp_x])
                    img_b_dx.append(line[temp_x+1:]) 
                   
                    
                #creo 4 img: 
                    #1) il primo quarto in altro a sinistra
                    #2) secondo quarto in altro a destra
                    #3) terzo quarto in basso a sinistra
                    #4) quarto quarto in basso a dastra
                    
                # visd(img_a_sx)
                # visd(img_a_dx)
                # visd(img_b_sx)
                # visd(img_b_dx)
                ok1 = codifica_img(img_a_sx, n_ret)
                ok2 = codifica_img(img_a_dx, n_ret)
                ok3 = codifica_img(img_b_sx, n_ret)
                ok4 = codifica_img(img_b_dx, n_ret)
                
                #processo le 4 img con lo stesso algoritmo  portandomi appresso il numero
                #dei rettangoli e l'ordine della gerarchia dei colori. il processo si
                #interromperà solo quando avrà processato l'ultima immagine in 
                #basso a destra più profonde possibile
                                
                ordine += [px] + ok4[0] + ok3[0] + ok2[0] + ok1[0]
                n_ret += ok1[1] + ok2[1] + ok3[1] + ok4[1]
                break                    
            
                #al termine della ricerca in profondità salvo l'ordine della gerarchia 
                #dei colori in ordine inverso e salvo anche il numero dei rettangolo
             
    return [ordine, n_ret]

    #ritorno per la funzione principale il risultato del processo dell'img intera

def ex1(input_file, output_file):
    img = load(input_file)
    ris = codifica_img(img)
    ordine = [img[0][0]] + ris[0]
    save([ordine], output_file)    
    return ris[1]

if __name__ == '__main__':
    # write your tests here
    pass
