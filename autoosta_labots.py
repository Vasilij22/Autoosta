import PySimpleGUI as ps
import mysql.connector

class Autoosta():
    
    def __init__(self,stacijas,stacijas_nosaukums,transporta_veids,transporta_cena,transporta_numurs,izbraukšanas_laiks,atbraukšanas_laiks,ceļa_pavaditasLaiks,ceļa_maršrutsKM):
        self.stacijas = stacijas
        self.stacijas_nosaukums = stacijas_nosaukums
        self.transporta_veids = transporta_veids
        self.transporta_cena = transporta_cena
        self.transporta_numurs = transporta_numurs
        self.izbraukšanas_laiks = izbraukšanas_laiks
        self.atbraukšanas_laiks = atbraukšanas_laiks
        self.ceļa_pavaditasLaiks = ceļa_pavaditasLaiks
        self.ceļa_maršrutsKM = ceļa_maršrutsKM

    
    def Autoostas_info(self):
        with open('autoosta.txt','w',encoding="utf-8") as fails:
            fails.write('-Autoostas informacija-\n')
            fails.write(f"Veids: {self.stacijas}\n")
            fails.write(f"Stacija: {self.stacijas_nosaukums}\n")
            fails.write(f"T.Veids: {self.transporta_veids}\n")
            fails.write(f"Cena: {self.transporta_cena}EUR\n")
            fails.write(f"T.Numurs: {self.transporta_numurs}\n")
            fails.write(f"IzbraukšanasLaiks: {self.izbraukšanas_laiks}\n")
            fails.write(f"AtbraukšanasLaiks: {self.atbraukšanas_laiks}\n")
            fails.write(f"CeļaLaiks: {self.ceļa_pavaditasLaiks}\n")
            fails.write(f"CeļaMaršruts: {self.ceļa_maršrutsKM}\n")
        

    def Autoostas_info_print(self):
        print(self.stacijas)
        print(self.stacijas_nosaukums)
        print(self.transporta_veids)
        print(self.transporta_cena)
        print(self.transporta_numurs)
        print(self.izbraukšanas_laiks)
        print(self.atbraukšanas_laiks)
        print(self.ceļa_pavaditasLaiks)
        print(self.ceļa_maršrutsKM)


ps.theme('Black')

logi = [

        [ps.Text('Autoostas informacija')],
        [ps.Text('Stacijas'),ps.InputText()],
        [ps.Text('Stacijas_nosaukums'),ps.InputText()],
        [ps.Text('Transporta_veids'),ps.InputText()],
        [ps.Text('Transporta_cena'),ps.InputText()],
        [ps.Text('Transporta_numurs'),ps.InputText()],
        [ps.Text('Izbraukšanas_laiks'),ps.InputText()],
        [ps.Text('Atbraukšanas_laiks'),ps.InputText()],
        [ps.Text('Ceļa_pavaditasLaiks'),ps.InputText()],
        [ps.Text('Ceļa_maršrutsKM'),ps.InputText()],
        [ps.Button('Saglabat'), ps.Button('Apskate'), ps.Button('Beigt')]    
        ]
window = ps.Window('Autoosta', logi)

while True:
    event,values = window.read()

    if event in (ps.WIN_CLOSED, 'Beigt'):
        break

    if event == 'Saglabat':
        print(values)
        print(values)
        stacijas = values[0]
        stacijas_nosaukums= values[1]
        transporta_veids= values[2]
        transporta_cena= values[3]
        transporta_numurs= values[4]
        izbraukšanas_laiks= values[5]
        atbraukšanas_laiks= values[6]
        ceļa_pavaditasLaiks= values[7]
        ceļa_maršrutsKM= values[8]
        save = Autoosta(stacijas,stacijas_nosaukums,transporta_veids,transporta_cena,transporta_numurs,izbraukšanas_laiks,atbraukšanas_laiks,ceļa_pavaditasLaiks,ceļa_maršrutsKM)
        save.Autoostas_info()
        save.Autoostas_info_print()

        db = mysql.connector.connect(host="localhost",database="autoosta",user="root",password="12345")

        cursor = db.cursor()
    if event == 'Apskate':
        ps.theme("Black")
        logs = [
                [ps.Text("Apskatit datus")],
                [ps.Text(stacijas)],
                [ps.Text(stacijas_nosaukums)],
                [ps.Text(transporta_veids)],
                [ps.Text(transporta_cena)],
                [ps.Text(transporta_numurs)],
                [ps.Text(izbraukšanas_laiks)],
                [ps.Text(atbraukšanas_laiks)],
                [ps.Text(ceļa_pavaditasLaiks)],
                [ps.Text(ceļa_maršrutsKM)],

                ]
        window2 = ps.Window('',logs)
        while True:
            event,values = window2.read()
            if event in (ps.WIN_CLOSED,):
                break

window2.close()
window.close()
