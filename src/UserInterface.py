import matplotlib.pyplot as plt
import PySimpleGUI as sg
import os

# Create options for the dropdown tab
class TelaAgenda:
    
    def __init__(self):
        
        layout = [
            [sg.Text('Nomeio o Trabalho')],
            [sg.Input(key='-InputNome-', size=(20,1))],
            [sg.Text('Marque o prazo do seu trabalho'), sg.Text('Tempo estimado para conclusão')],
            [sg.Input(key='-Calendar-', size=(20,1)), sg.CalendarButton('Calendário', close_when_date_chosen=True,  target='-Calendar-', location=(0,0), no_titlebar=False, format='%d-%m-%Y',), sg.Input(key='-Estimativa-', size=(20,1), pad=5)],
            [sg.Button('Adicionar'), sg.Button('Limpar'), sg.Exit('Concluir')]
        ]

        self.window = sg.Window('Agenda de Entregas', layout, size=(550, 250))
        self.trabalhos = []
        
    def Desenhar_Janela(self):
        flag = 1
        keys_to_clear = ['-InputNome-', '-Calendar-', '-Estimativa-']
        while True:           
            # print(self.values['-Calendar-'])
            # print(type(self.values['-Calendar-']))      
            
            self.event, self.values = self.window.read()
            
            if self.event in (sg.WIN_CLOSED, 'Concluir'):
                break  
            elif flag == 1 and self.event == 'Adicionar':
                #print('ENTROU')
                self.trabalhos.append(self.values['-InputNome-'])
                self.trabalhos.append(self.values['-Calendar-'])
                self.trabalhos.append(self.values['-Estimativa-'])
                sg.popup('Trabalho Adicionado. Não esqueca de limpar para adicionar um novo')
                flag = 0
            elif flag == 0 and self.event == 'Limpar':
                for keys in keys_to_clear:
                    self.window[keys]('')
                flag = 1
            
        self.window.close()


def main():
    UI = TelaAgenda()
    UI.Desenhar_Janela()
    print(UI.trabalhos)
    
if __name__ == "__main__":
    main()
 