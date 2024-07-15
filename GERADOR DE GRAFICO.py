import tkinter as Tk
from tkinter import messagebox
from tkinter import ttk
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
import pandas as pd
from tkinter import filedialog

#MENSAGEM DE ERRO 
def error():
    messagebox.showwarning('ERRO', 'Preenche direito idiota do caralho!')

#janela barra ----------------------------------------------------------------------------------------------------------------------------------------------------
#GERAR GRAFICOS
def gerategraph(style,tipo):
    try:
        x = xentry.get().split(',')
        plt.style.use(style)
        if tipo == 'bar':
            y = [float(num) for num in yentry.get().split(',')]
            plt.bar(x, y)
            plt.ylim(ymin=0, ymax=max(y) + 10)
        elif tipo == 'plot':
            y = [float(num) for num in yentry.get().split(',')]
            y = [0] + y
            x= ['.'] + x
            plt.plot(x,y)
            plt.ylim(bottom=0,ymax=max(y) + 5)

        elif tipo == 'pie':
             y = [float(num) for num in yentry.get().split(',')]
             label = x
             plt.pie(y,labels=label,autopct='%1.1f%%')

        plt.xlabel(xlabelentry.get())
        plt.ylabel(ylabelentry.get())
        plt.grid(True, alpha=0.3)
        plt.show()
    except Exception as e:
        error()
        print(e)

#IMPORTA O CSV E GERA O GRAFICO
def importcsv(style,tipocsv):
    plt.style.use(style)
    arquivo = filedialog.askopenfilename()
    df= pd.read_csv(arquivo)
    xcon = str(nomex.get())
    ycon = str(nomey.get())
    legenda = df[xcon].tolist()

    if tipocsv == 'bar':
        grafico = df.plot.bar(x=xcon,y=ycon)
    elif tipocsv == 'plot':
        grafico = df.plot(x=xcon,y=ycon)
    elif tipocsv =='pie':
        grafico = df.plot.pie(y=ycon,labels=legenda,legend=True)
        
    
    plt.show()

#Janela de geração de grafico de barra e de linha e de pizza
def rootbarplot(style,tipagem):
    global xentry,yentry,xlabelentry,ylabelentry,nomex,nomey
  #configuração Janela
    root2 = Tk.Toplevel()
    root2.geometry('700x350+690+300')
    root2.configure(bg='#191919')
    framecinza = Tk.Frame(root2,bg='#1e4267',width=700,height=700)
    framecinza.place(relx=0.70,rely=0.0)

  #TEXTO / LABEL DA JANELA2
  #x
    labelx = Tk.Label(root2, text='Digite sua lista de X:', bg='#191919', fg='white', font=('Helvetica', 12))
    labelx.place(relx=0.10, rely=0.09)
    labelx2 = Tk.Label(root2, text='Legenda de X:', bg='#191919', fg='white', font=('Helvetica', 12))
    labelx2.place(relx=0.10, rely=0.24)
    #y
    labely = Tk.Label(root2, text='Digite sua lista de Y:', bg='#191919', fg='white', font=('Helvetica', 12))
    labely.place(relx=0.10, rely=0.39)
    labely2 = Tk.Label(root2, text='Legenda de Y:', bg='#191919', fg='white', font=('Helvetica', 12))
    labely2.place(relx=0.10, rely=0.54)
    #
    labelcb = Tk.Label(root2, text='Selecione o tema:', bg='#1e4267', fg='white', font=('Helvetica', 11))
    labelcb.place(relx=0.74, rely=0.09)

    #configuração da combobox
    opcao_selecionada = Tk.StringVar()
    opcao_selecionada.set(style)
    combobox = ttk.Combobox(root2, textvariable=opcao_selecionada, values=['dark_background', 'ggplot', 'classic', 'bmh'])
    combobox.place(relx=0.75, rely=0.15)

    #campos de entrada
    #x
    xentry = Tk.Entry(root2, width=60)
    xentry.place(relx=0.10, rely=0.15)
    xlabelentry = Tk.Entry(root2, width=60)
    xlabelentry.place(relx=0.10, rely=0.30)
    #y
    yentry = Tk.Entry(root2, width=60)
    yentry.place(relx=0.10, rely=0.45)
    ylabelentry = Tk.Entry(root2, width=60)
    ylabelentry.place(relx=0.10, rely=0.60)

    #botão para gerar o grafico
    calculate = Tk.Button(root2, width=20, fg='#191919', font=('Helvetica', 12), bg='white', text='GERAR', command=lambda: gerategraph(opcao_selecionada.get(),tipagem))
    calculate.place(relx=0.35, rely=0.80)
    
    #importar o csv
    textimport= Tk.Label(root2,text='IMPORTE UM .CSV',font=('Helvetica',10),bg='#1e4267',fg='white')
    textimport.place(relx=0.75,rely=0.23)
    namex= Tk.Label(root2,text='Nome coluna x',font=('Helvetica',8),bg='#1e4267',fg='white')
    namex.place(relx=0.75,rely=0.30)
    namey= Tk.Label(root2,text='Nome coluna y',font=('Helvetica',8),bg='#1e4267',fg='white')
    namey.place(relx=0.75,rely=0.45)
    nomex= Tk.Entry(root2)
    nomex.place(relx=0.75,rely=0.35)
    nomey = Tk.Entry(root2)
    nomey.place(relx=0.75,rely=0.50)
    botao= Tk.Button(root2,width=10,text='importe',command=lambda:importcsv(opcao_selecionada.get(),tipagem))
    botao.place(relx=0.75,rely=0.58)

root = Tk.Tk()
#FINAL JANELA BARRA ------------------------------------------------------------------------------------------------------------------------------
#INICIO MENU ------------------------------------------------------------------------------------------------------------------------------
def rootconfigure():
    root.geometry('900x500+580+300')
    root.resizable(False, False)
    root.title('GERADOR GRAFICOS')
    root.configure(bg='#191919')
    #logo
    '''img = Image.open('IMAGENS/CAPYBARA IMAGES/LOGO1.png')
    img = img.resize((60,60))
    logo = ImageTk.PhotoImage(img)
    logoplc = Tk.Label(root,image=logo,borderwidth=0,highlightthickness=0)
    button.image = logo
    logoplc.place(relx=0.03,rely=0.03)'''


def button(width, height, relx, rely, style, image_path,grafico):
    command = lambda: rootbarplot(style,grafico)
    img = Image.open(image_path)
    img = img.resize((width, height))
    photo = ImageTk.PhotoImage(img)
    button = Tk.Button(root, width=width, height=height, bg='white', command=command, image=photo, compound=Tk.LEFT,borderwidth=0,highlightthickness=0)
    button.image = photo  # Manter uma referência para evitar que a imagem seja destruída
    button.place(relx=relx, rely=rely)


def buttons1screen():
    button(200, 200, 0.05, 0.27, 'dark_background', 'IMAGENS/CAPYBARA IMAGES/OIP1.jpg','bar')
    button(200, 200, 0.373, 0.27, 'dark_background', 'IMAGENS/CAPYBARA IMAGES/PLOT1.jpg','plot')
    button(200, 200, 0.70, 0.27, 'dark_background', 'IMAGENS/CAPYBARA IMAGES/PIE1.jpg','pie')

def textmenu():
    bar = Tk.Label(root,text='BAR',font=('JetBrainsMono',40),fg='white',bg='#191919')
    bar.place(relx=0.095,rely=0.70)
    bar = Tk.Label(root,text='PLOT',font=('JetBrainsMono',40),fg='white',bg='#191919')
    bar.place(relx=0.405,rely=0.70)
    bar = Tk.Label(root,text='PIE',font=('JetBrainsMono',40),fg='white',bg='#191919')
    bar.place(relx=0.760,rely=0.70)


#trazendo funções
buttons1screen()
textmenu()
rootconfigure()
root.mainloop()
#FINAL MENU ------------------------------------------------------------------------------------------------------------------------------