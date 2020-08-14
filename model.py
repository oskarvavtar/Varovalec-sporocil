abeceda_stevke_presledek = ["a", "b", "c", "č", "ć", "d", "đ", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "š", "t", "u", "v", "w", "x", "y", "z", "ž", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
abeceda = ["a", "b", "c", "č", "ć", "d", "đ", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "š", "t", "u", "v", "w", "x", "y", "z", "ž"]
stevke = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ang_abeceda_stevke = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

###################################################################################################

class Besedilo:
    
    def __init__(self, besedilo):
        self.besedilo = besedilo
        self.dolzina = len(self.besedilo)
        self.geslo = None
        self.dolzina_gesla = 0
        
    def __repr__(self):
        return f"Besedilo: {self.besedilo}"

    def __str__(self):
        return f"{self.besedilo}"

    def __len__(self):
        return self.dolzina

    ###############################################################################################

    def nastavi_geslo(self, geslo):
        self.geslo = geslo
        self.dolzina_gesla = len(geslo)

    ###############################################################################################
    @staticmethod
    def premik_znaka_desno(znak, n, abc):
        indeks = abc.index(znak)
        nov_indeks = indeks + int(n)
        while nov_indeks >= len(abc):
            nov_indeks -= len(abc)
        return nov_indeks

    @staticmethod
    def premik_znaka_levo(znak, n, abc):
        indeks = abc.index(znak)
        nov_indeks = indeks - int(n)
        while nov_indeks < 0:
            nov_indeks += len(abc)
        return nov_indeks

    @staticmethod
    def ustreznost_sub():
        for i in range(self.dolzina_gesla):
            if self.geslo[i] not in stevke:
                return False
        return True
    
    def rot13(self):
        tekst = self.besedilo.lower()
        nov_tekst = ""
        for i in range(self.dolzina):
            if tekst[i] in abeceda_stevke_presledek:
                nov_tekst += abeceda_stevke_presledek[self.premik_znaka_desno(tekst[i], 21, abeceda_stevke_presledek)]
            else:
                nov_tekst += tekst[i]
        return nov_tekst

    def zakodiraj_cezar(self, tekst):
        nov_tekst = ""
        for i in range(self.dolzina):
            if tekst[i] in abeceda:
                nov_tekst += abeceda[self.premik_znaka_desno(tekst[i], self.geslo, abeceda)]
            elif tekst[i] in stevke:
                nov_tekst += stevke[self.premik_znaka_desno(tekst[i], self.geslo, stevke)]
            else:
                nov_tekst += tekst[i]
        return nov_tekst

    def dekodiraj_cezar(self, tekst):
        nov_tekst = ""
        for i in range(self.dolzina):
            if tekst[i] in abeceda:
                nov_tekst += abeceda[self.premik_znaka_levo(tekst[i], self.geslo, abeceda)]
            elif tekst[i] in stevke:
                nov_tekst += stevke[self.premik_znaka_levo(tekst[i], self.geslo, stevke)]
            else:
                nov_tekst += tekst[i]
        return nov_tekst

    def cezarjeva_sifra(self, zakodiraj=True):
        if self.geslo == None:
            raise Exception("Prosim nastavi geslo.")
        if self.ustreznost_sub():
            tekst = self.besedilo.lower()
            if zakodiraj:
                return self.zakodiraj_cezar(tekst) 
            else:
                return self.dekodiraj_cezar(tekst)    
        else:
            raise Exception("Geslo more biti naravno število.")

    def zakodiraj_po_stevkah(self, tekst):
        nov_tekst = ""
        n = 0
        for i in range(self.dolzina):
            if tekst[i] in abeceda:
                nov_tekst += abeceda[self.premik_znaka_desno(tekst[i], self.geslo[n], abeceda)]
            elif tekst[i] in stevke:
                nov_tekst += stevke[self.premik_znaka_desno(tekst[i], self.geslo[n], stevke)]
            else:
                nov_tekst += tekst[i]
            n += 1
            if n == self.dolzina_gesla:
                n = 0
        return nov_tekst

    def dekodiraj_po_stevkah(self, tekst):
        nov_tekst = ""
        n = 0
        for i in range(self.dolzina):
            if tekst[i] in abeceda:
                nov_tekst += abeceda[self.premik_znaka_levo(tekst[i], self.geslo[n], abeceda)]
            elif tekst[i] in stevke:
                nov_tekst += stevke[self.premik_znaka_levo(tekst[i], self.geslo[n], stevke)]
            else:
                nov_tekst += tekst[i]
            n += 1
            if n == self.dolzina_gesla:
                n = 0
        return nov_tekst

    def substitucija_po_stevkah(self, zakodiraj=True):
        if self.geslo == None:
            raise Exception("Prosim nastavi geslo.")
        if self.ustreznost_sub():
            tekst = self.besedilo.lower()
            if zakodiraj:
                return self.zakodiraj_po_stevkah(tekst)
            else:
                return self.dekodiraj_po_stevkah(tekst)    
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
        znaki = ustvari_seznam(self)
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
    
    @staticmethod
    def oba_v_tabeli(prvi, drugi):
        if prvi in abeceda_stevke_presledek and drugi in abeceda_stevke_presledek:
            return True
        else:
            return False

    def ustreznost_poli(self):
        for i in range(self.dolzina_gesla):
            if self.geslo[i] not in abeceda_stevke_presledek:
                return False
        return True

    def poligrafska_substitucija(self):
        if ustreznost_poli(self):
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
                    nov_tekst += char1 + char2
            return nov_tekst
        else:
            raise Exception("Geslo ne sme vsebovati posebnih znakov.")

    ###############################################################################################

    def ustreznost_xor(self):
        for i in range(self.dolzina):
            if self.besedilo[i] not in ang_abeceda_stevke:
                return False
        for i in range(len(self.geslo)):
            if self.geslo[i] not in ang_abeceda_stevke:
                return False
        return True

    def xor(self):
        if self.ustreznost_xor():
            nov_tekst = ""
            for i in range(self.dolzina):
                char = self.besedilo[i]
                char_key = self.geslo[i % self.dolzina_gesla]
                nov_tekst += chr(ord(char) ^ ord(char_key))
            return nov_tekst
        else:
            raise Exception("Besedilo mora biti sestavljeno le iz črk angelške abeceda in številk, zapisano brez presledkov.")
    
if __name__ == "__main__":
    besedilo = Besedilo("")
    besedilo.nastavi_geslo("")
    print(besedilo.xor())
        
    

