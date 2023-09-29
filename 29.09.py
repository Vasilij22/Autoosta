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

    def laboshana(self,stacijas,atbraukšanas_laiks,izbraukšanas_laiks,cena,visa_ceļa_laiks,autobusa_numurs):
        self.stacijas = stacijas
        self.atbraukšanas_laiks = atbraukšanas_laiks
        self.izbraukšanas_laiks = izbraukšanas_laiks
        self.cena = cena
        self.visa_ceļa_laiks = visa_ceļa_laiks
        self.autobusa_numurs = autobusa_numurs

    def saglabat(self):
        with open('autoosta.txt','w',encoding="utf-8") as fails:
            fails.write('-Autoostas informacija-\n')
            fails.write(f"Veids: {self.stacijas}\n")
            fails.write(f"Modelis: {self.atbraukšanas_laiks}H\n")
            fails.write(f"Cena: {self.izbraukšanas_laiks}H\n")
            fails.write(f"Veids: {self.cena}EUR\n")
            fails.write(f"Modelis: {self.visa_ceļa_laiks}H\n")
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
    [psg.Button('Rediģet')]
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
    psg.Button('Aizvert'),
    psg.Button('Apskate')
    
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

    if event == "Rediģet":
        stacijas = values[6]
        atbraukšanas_laiks = values[7]
        izbraukšanas_laiks = values[8]
        cena = values[9]
        visa_ceļa_laiks = values[10]
        autobusa_numurs = values[11]
        jauns.laboshana(stacijas,atbraukšanas_laiks,izbraukšanas_laiks,cena,visa_ceļa_laiks,autobusa_numurs)
        jauns.saglabat()

    if event == "Apskate":
        psg.theme("BlueMono")
        layout = [
                  [psg.Text("Autoostas informacija")],
                  [psg.Text("Stacijas: " + jauns.stacijas)],
                  [psg.Text("Atbraukšanas_laiks: " + jauns.atbraukšanas_laiks)],
                  [psg.Text("Izbraukšanas_laiks: " + jauns.izbraukšanas_laiks)],
                  [psg.Text("Cena: " + jauns.cena)],
                  [psg.Text("Visa_ceļa_laiks: " + jauns.visa_ceļa_laiks)],
                  [psg.Text("Autobusa_numurs: " + jauns.autobusa_numurs)]
                  ]
        window = psg.Window('',layout)
        event,values = window.read()
    if event in (psg.WIN_CLOSED,'Aizvert'):
        break

window.close()
