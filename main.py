#janela ==> 500 x 500
#titulo
#campos para selecionar as moedas de origem e de destino
#botao pra converter 
#lista de exibiçao com nomes das moedas 

#importara biblioteca que vai faer a janela
import customtkinter
from pegar_moedas import conversoes_disponiveis, nomes_moedas
from pegar_cotacao import pegar_cotacao_moeda

#criar e configurar as janelas
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("600x700")
janela.title("conversor de moedas-confia.com")
janela.iconbitmap("livro.ico")

dic_conversoes_disponiveis = conversoes_disponiveis()

#criar botao e demais elementos 
titulo = customtkinter.CTkLabel(janela, text="°º°Conversor de Moedas°º°", font=("Consolas", 38), text_color="#efc549")
textoorigem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("Consolas", 20))
textodestino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("Consolas", 20))

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list (dic_conversoes_disponiveis.keys()), command=carregar_moedas_destino, font=("", 10))
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["selecione uma moeda de origem"], font=("", 10))

def convertermoeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")

botaoconverter = customtkinter.CTkButton(janela, text="converter", text_color="black", command=convertermoeda, font=("", 20), fg_color='#efc549', hover_color="#ffd811")

listamoedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="", font=("", 20))

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(listamoedas, text=f"{codigo_moeda}: {nome_moeda}", font=("", 10), text_color="#618530")
    texto_moeda.pack(padx=5, pady=5)



#moeda1 = customtkinter.CTkLabel(listamoedas, text="USD: Dolar americano")^^
#moeda2 = customtkinter.CTkLabel(listamoedas, text="EUR: Euro")           ^^
#moeda3 = customtkinter.CTkLabel(listamoedas, text="BRL: Real brasileiro")^^
#moeda4 = customtkinter.CTkLabel(listamoedas, text="BTC: Biticoen")       ^^
#moeda1.pack() ^^
#moeda2.pack() ^^
#moeda3.pack() ^^
#moeda4.pack() ^^


#colocar elementos criados na tela
titulo.pack(padx=30, pady=40)
textoorigem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=2, pady=0)
textodestino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=2, pady=0)
botaoconverter.pack(padx=20, pady=30)
texto_cotacao_moeda.pack(padx=20, pady=30)
listamoedas.pack(padx=10, pady=0)


#rodar a janela 
janela.mainloop()