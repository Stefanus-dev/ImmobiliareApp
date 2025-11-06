import sqlite3

# Costanti menu
AGGIUNGI_CASA = 1
CANCELLA_CASA = 2
CERCA_CASE = 3
CASE_IN_GESTIONE = 4
QUIT_CHOICE = 5

# Tabella sigle provincia
sigle_pv = [
"AG","AL","AN","AO","AQ","AR","AP","AT","AV","BA",
"BT","BL","BN","BG","BI","BO","BZ","BS","BR","CA",
"CL","CB","CI","CE","CT","CZ","CH","CO","CS","CR",
"KR","CN","EN","FM","FE","FI","FG","FC","FR","GE",
"GO","GR","IM","IS","SP","LT","LE","LC","LI","LO",
"LU","MC","MN","MS","MT","VS","ME","MI","MO","MB",
"NA","NO","NU","OG","OT","OR","PD","PA","PR","PV",
"PG","PU","PE","PC","PI","PT","PN","PZ","PO","RG",
"RA","RC","RE","RI","RN","RO","SA","SS","SV","RM",
"SI","SR","SO","TA","TE","TR","TO","TP","TN","TV",
"TS","UD","VA","VE","VB","VC","VR","VV","VI","VT"
]

class Persona:
    def __init__(self, nome, cognome, tel, cell):
        self.__nome = nome
        self.__cognome = cognome
        self.__tel = tel
        self.__cell = cell

    def get_nome(self): return self.__nome
    def get_cognome(self): return self.__cognome
    def get_tel(self): return self.__tel
    def get_cell(self): return self.__cell

    def get_all_info(self):
        return self.__nome + "," + self.__cognome + "," + self.__tel + "," + self.__cell


class Casa:
    def __init__(self, codice, prezzo, n_vani, mq, ascensore, condominio,
                 garage, indirizzo, cap, comune, provincia, proprietario):

        self._codice = codice
        self._prezzo = prezzo
        self._n_vani = n_vani
        self._mq = mq
        self._ascensore = ascensore
        self._condominio = condominio
        self._garage = garage
        self._indirizzo = indirizzo
        self._cap = cap
        self._comune = comune
        self._provincia = provincia
        self._proprietario = proprietario

    def __str__(self):
        return (
            f"\nCodice: {self._codice}"
            f"\n\tPrezzo: {self._prezzo:.2f} €"
            f"\n\tN. vani: {self._n_vani}"
            f"\n\tMetri quadri: {self._mq}"
            f"\n\tAscensore: {self._ascensore}"
            f"\n\tCondominio: {self._condominio}"
            f"\n\tGarage: {self._garage}"
            f"\n\tIndirizzo: {self._indirizzo}"
            f"\n\tCAP: {self._cap}"
            f"\n\tComune: {self._comune}"
            f"\n\tProvincia: {self._provincia}"
            f"\n---- PROPRIETARIO ----\n{self._proprietario.get_all_info()}"
        )

# ✅ CREA DB (NOME TABELLA CORRETTO)
def crea_db():
    conn = sqlite3.connect("case.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS case_immobili (
            codice TEXT PRIMARY KEY,
            prezzo REAL,
            n_vani INTEGER,
            mq REAL,
            ascensore TEXT,
            condominio TEXT,
            garage TEXT,
            indirizzo TEXT,
            cap TEXT,
            comune TEXT,
            provincia TEXT,
            nome_prop TEXT,
            cognome_prop TEXT,
            tel_prop TEXT,
            cell_prop TEXT
        )
    """)
    conn.commit()
    conn.close()

# ✅ SALVA SU DB
def salva_case(d):
    conn = sqlite3.connect("case.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM case_immobili")
    for casa in d.values():
        p = casa._proprietario
        cur.execute("""
            INSERT INTO case_immobili VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (casa._codice, casa._prezzo, casa._n_vani, casa._mq,
              casa._ascensore, casa._condominio, casa._garage, casa._indirizzo,
              casa._cap, casa._comune, casa._provincia,
              p.get_nome(), p.get_cognome(), p.get_tel(), p.get_cell()))
    conn.commit()
    conn.close()

# ✅ CARICA DA DB
def carica_case(d):
    conn = sqlite3.connect("case.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM case_immobili")
    for r in cur.fetchall():
        p = Persona(r[11], r[12], r[13], r[14])
        c = Casa(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], p)
        d[r[0]] = c
    conn.close()
    print(f"\t>>> {len(d)} CASE in gestione <<<")

def display_menu():
    print("""
MENU
1) Inserire una nuova casa
2) Eliminare una casa
3) Cerca case per prezzo
4) Stampa tutte le case
5) Esci
""")

def chiedi_numero(prompt, tipo):
    while True:
        try:
            return float(input(prompt)) if tipo == "float" else int(input(prompt))
        except:
            print("Valore non valido.")

def chiedi_s_n(prompt):
    while True:
        s = input(prompt).upper()
        if s in ["S","N"]: return s

def chiedi_cap():
    while True:
        s = input("CAP (5 cifre): ")
        if len(s)==5 and s.isdigit(): return s
        print("CAP non valido")

def chiedi_sigla_pv():
    while True:
        s = input("Provincia: ").upper()
        if s in sigle_pv: return s
        print("Provincia non valida")

def chiedi_info_casa(cod):
    p = Persona(input("Nome proprietario: "), input("Cognome: "), input("Tel: "), input("Cell: "))
    return Casa(cod,
        chiedi_numero("Prezzo: ","float"),
        chiedi_numero("Numero vani: ","int"),
        chiedi_numero("Metri quadri: ","float"),
        chiedi_s_n("Ascensore [S/N]? "),
        chiedi_s_n("Condominio [S/N]? "),
        chiedi_s_n("Garage [S/N]? "),
        input("Indirizzo: "),
        chiedi_cap(),
        input("Comune: "),
        chiedi_sigla_pv(),
        p
    )

def main():
    crea_db()
    agenzia = {}
    carica_case(agenzia)
    modifiche = False
    choice = 0

    while choice != QUIT_CHOICE:
        display_menu()
        choice = chiedi_numero("Scelta: ", "int")

        if choice == AGGIUNGI_CASA:
            codice = input("Codice: ").upper()
            if codice not in agenzia:
                agenzia[codice] = chiedi_info_casa(codice)
                modifiche = True
            else:
                print("Codice già presente.")

        elif choice == CANCELLA_CASA:
            codice = input("Codice da eliminare: ").upper()
            if codice in agenzia:
                del agenzia[codice]
                modifiche=True
                print("Casa eliminata.")
            else:
                print("Codice non trovato.")

        elif choice == CASE_IN_GESTIONE:
            for c in agenzia.values():
                print(c)

    if modifiche:
        salva_case(agenzia)
        print("Modifiche salvate.")

main()
