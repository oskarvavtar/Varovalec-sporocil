abeceda_stevke_presledek = ["a", "b", "c", "č", "ć", "d", "đ", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "š", "t", "u", "v", "w", "x", "y", "z", "ž", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
abeceda = ["a", "b", "c", "č", "ć", "d", "đ", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "š", "t", "u", "v", "w", "x", "y", "z", "ž"]
stevke = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ang_abeceda_stevke = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

###################################################################################################

class Besedilo:

    def __init__(self, besedilo, geslo=None):
        self.besedilo = besedilo
        self.dolzina = len(self.besedilo)
        if geslo = None:
            pass
        else:
            self.geslo = geslo
            self.dolzina_gesla = len(self.geslo)
        self.opravilo = opravilo

    def __repr__(self):
        return f"Besedilo: {self.besedilo}"

    def __str__(Self):
        return f"{self.besedilo}"

    def __len__(self):
        return self.dolzina

    ###############################################################################################

    def premik_znaka_desno(i, n, abc):
        indeks = abc.index(i)
        nov_indeks = indeks + i
        while nov_indeks >= len(abc):
            nov_indeks -= len(abc)
        return nov_indeks

    def premik_znaka_levo(i, n, abc):
        indeks = abc.index(i)
        nov_indeks = indeks - i
        while nov_indeks < 0:
            nov_indeks += len(abc)
        return nov_indeks
    
    def rot13(self):
        tekst = self.besedilo.lower()
        nov_tekst = ""
        for i in range(self.dolzina):
            if tekst[i] in abeceda_stevke_presledek:
                nov_tekst += abeceda_stevke_presledek[premik_znaka_desno(i, 21, abeceda_stevke_presledek)]
            else:
                nov_tekst += tekst[i]
        return nov_tekst

    def cezarjeva_sifra(self, zakodiraj=True):
        if type(self.geslo) == int: #????????
            tekst = self.besedilo.lower():
            nov_tekst = ""
            if zakodiraj:
                for i in range(self.dolzina):
                    if tekst[i] in abeceda:
                        nov_tekst += abeceda[premik_znaka_desno(i, self.geslo, abeceda)]
                    elif tekst[i] in stevke:
                        nov_tekst += stevke[premik_znaka_desno(i, self.geslo, stevke)]
                    else:
                        nov_tekst += tekst[i]
            else:
                for i in range(self.dolzina):
                    if tekst[i] in abeceda:
                        nov_tekst += abeceda[premik_znaka_levo(i, self.geslo, abeceda)]
                    elif tekst[i] in stevke:
                        nov_tekst += stevke[premik_znaka_levo(i, self.geslo, stevke)]
                    else:
                        nov_tekst += tekst[i]
            return nov_tekst
        else:
            raise Exception("Geslo more biti celo število.")

    def substitucija_po_stevkah(self, zakodiraj=True):
        if type(self.geslo) == int: #????????
            tekst = self.besedilo.lower()
            nov_tekst = ""
            n = 0
            if zakodiraj:
                for i in range(self.dolzina):
                    if tekst[i] in abeceda:
                        nov_tekst += abeceda[premik_znaka_desno(i, self.geslo[n], abeceda)]
                    elif tekst[i] in stevke:
                        nov_tekst += stevke[premik_znaka_desno(i, self.geslo[n], stevke)]
                    else:
                        nov_tekst += tekst[i]
                    n += 1
                    if n == self.dolzina_gesla:
                        n = 0
            else:
                for i in range(self.dolzina):
                    if tekst[i] in abeceda:
                        nov_tekst += abeceda[premik_znaka_levo(i, self.geslo[n], abeceda)]
                    elif tekst[i] in stevke:
                        nov_tekst += stevke[premik_znaka_levo(i, self.geslo[n], stevke)]
                    else:
                        nov_tekst += tekst[i]
                    n += 1
                    if n == self.dolzina_gesla:
                        n = 0
            return nov_tekst
        else:
            raise Exception("Geslo more biti številsko.")

    ###############################################################################################

    def poli_seznam(self):
        znaki = []
        for i in range(self.dolzina_gesla):
            if self.geslo[i] not in znaki:
                znaki.append(self.geslo[i])
        for znak in abeceda_stevke_presledek:
            if znak not in znaki:
                znaki.append(char)
        return znaki

    def poli_tabela(self):
        znaki = ustvari_seznam(self):
        tabela = []
        n = 0
        for i in range(6):
            vrstica = []
            for j in range(7):
                vrstica.append(znaki[n])
                n += 1
            tabela.append(vrstica)
        return tabela
    
    def sodo_besedilo(self):
        if self.dolzina % 2 == 1:
            self.besedilo += " "
        return self.besedilo
    
    def oba_v_tabeli(prvi, drugi):
        if prvi in abeceda_stevke_presledek and drugi in abeceda_stevke_presledek:
            return True
        else:
            return False

    def poligrafska_substitucija(self):
        tekst = sodo_besedilo(self).lower()
        nov_tekst = ""
        for i in range(0, self.dolzina, 2):
            char1, char2 = tekst[i], tekst[i+1]
            if oba_v_tabeli(char1, char2):
                seznam, tabela = poli_seznam(self), poli_tabela(self)
                indeks1, indeks2 = seznam.index(char1), seznam.index(char2)
                pozicija1, pozicija2 = [indeks1 // 7, indeks1 % 7], [indeks2 // 7, indeks2 % 7]
                if pozicija1[0] == pozicija2[0] or pozicija1[1] == pozicija2[1]:
                    nova_pozicija1, nova_pozicija2 = pozicija2, pozicija1
                else:
                    nova_pozicija1, nova_pozicija2 = [pozicija1[0], pozicija2[1]], [pozicija2[0], pozicija1[1]]
                nov_tekst += tabela[nova_pozicija1[0]][nova_pozicija1[1]] + tabela[nova_pozicija2[0]][nova_pozicija2[1]]
            else:
                nov_tekst += char1 + char 2
        return nov_tekst

    ###############################################################################################

    def preveri_ustreznost(self):
        for i in range(self.dolzina):
            if self.besedilo[i] not in ang_abeceda_stevke:
                return False
        for i in range(self.dolzina_gesla):
            if self.geslo[i] not in ang_abeceda_stevke:
                return False
        return True


    def xor(self):
        if preveri_ustreznost:
            nov_tekst = ""
            for i in range(self.dolzina):
                char = self.besedilo[i]
                char_key = self.geslo[i % self.dolzina_gesla]
                nov_tekst += char(ord(char) ^ ord(char_key))
            return nov_tekstv
        else:
            raise Exception("Besedilo mora biti sestavljeno le iz črk angelške abeceda in številk, zapisano brez presledkov.")

        
        
    

