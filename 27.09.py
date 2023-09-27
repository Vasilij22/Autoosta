import PySimpleGUI as psg

class info():
    def __init__(self,stacijas,atbraukšanas_laiks,izbraukšanas_laiks,cena,visa_ceļa_laiks,autobusa_numurs):
        self.stacijas = stacijas
        self.atbraukšanas_laiks = atbraukšanas_laiks
        self.izbraukšanas_laiks = izbraukšanas_laiks
        self.cena = cena
        self.visa_ceļa_laiks = visa_ceļa_laiks
        self.autobusa_numurs = autobusa_numurs

    def apskate(self):
        print(self.stacijas)
        print(self.atbraukšanas_laiks)
        print(self.izbraukšanas_laiks)
        print(self.cena)
        print(self.visa_ceļa_laiks)
        print(self.autobusa_numurs)

    def saglabat(self):
        with open('autoosta.txt','w',encoding="utf-8") as fails:
            fails.write('-Autoostas informacija-\n')
            fails.write(f"Veids: {self.stacijas}\n")
            fails.write(f"Modelis: {self.atbraukšanas_laiks}\n")
            fails.write(f"Cena: {self.izbraukšanas_laiks}\n")
            fails.write(f"Veids: {self.cena}EUR\n")
            fails.write(f"Modelis: {self.visa_ceļa_laiks}\n")
            fails.write(f"Cena: {self.autobusa_numurs}\n")

psg.theme('Dark blue')

logi = [
    [psg.Text('Autoostas informacija')],
    [psg.Text('Stacijas'),psg.InputText()],
    [psg.Text('Izbraukšanas_laiks'),psg.InputText()],
    [psg.Text('Atbraukšanas_laiks'),psg.InputText()],
    [psg.Text('Cena'),psg.InputText()],
    [psg.Text('Visa_ceļa_laiks'),psg.InputText()],
    [psg.Text('Autobusa_numurs'),psg.InputText()],
    [psg.Button('Saglabat')]
]

logi2 = [
    [psg.Text('Rediģešana')],
    [psg.Text('Stacijas'),psg.InputText()],
    [psg.Text('Izbraukšanas_laiks'),psg.InputText()],
    [psg.Text('Atbraukšanas_laiks'),psg.InputText()],
    [psg.Text('Cena'),psg.InputText()],
    [psg.Text('Visa_ceļa_laiks'),psg.InputText()],
    [psg.Text('Autobusa_numurs'),psg.InputText()],
    [psg.Button('Redeģet')]
]

logugruppa = [[
    psg.TabGroup(
        [
            [
                psg.Tab('Autoostas informacija', logi),
                psg.Tab('Redeģešana',logi2)
            ]
        ]
    ),
    psg.Button('Aizvert')
    
]]

window = psg.Window('Window tittle', logugruppa)

while True:
    event,values = window.read()
    
    if event == "Saglabat":
        print(values)
        stacijas = values[0]
        atbraukšanas_laiks = values[1]
        izbraukšanas_laiks = values[2]
        cena = values[3]
        visa_ceļa_laiks = values[4]
        autobusa_numurs = values[5]
        jauns = info(stacijas,atbraukšanas_laiks,izbraukšanas_laiks,cena,visa_ceļa_laiks,autobusa_numurs)
        jauns.saglabat()

        event,values = window.read()
    if event in (psg.WIN_CLOSED,'Aizvert'):
        break

window.close()
