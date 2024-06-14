#janela ==> 500 x 500
#titulo
#campos para selecionar as moedas de origem e de destino
#botao pra converter 
#lista de exibiçao com nomes das moedas 

#importara biblioteca que vai faer a janela
import customtkinter

#criar e configurar as janelas
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

janela = customtkinter.CTk()
janela.geometry("600x700")

#criar botao e demais elementos 
titulo = customtkinter.CTkLabel(janela, text="°º°Conversor de Moedas°º°", font=("", 38), text_color="#efc549")
textoorigem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("", 20))
textodestino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("", 20))
campoorigem = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"], font=("", 10))
campodestino = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"], font=("", 10))

def convertermoeda():
    print("converter moeda")
botaoconverter = customtkinter.CTkButton(janela, text="converter", text_color="black", command=convertermoeda, font=("", 20), fg_color='#efc549', hover_color="#ffd811")

listamoedas = customtkinter.CTkScrollableFrame(janela)

moedasdisponiveis = ["USD: Dolar americano", "EUR: Euro", "BRL: Real brasileiro", "BTC: Biticoen"]
for moedas in moedasdisponiveis:
    textomoeda = customtkinter.CTkLabel(listamoedas, text=moedas, font=("", 10), text_color="#618530")
    textomoeda.pack(padx=10, pady=10)
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
campoorigem.pack(padx=2, pady=0)
textodestino.pack(padx=10, pady=10)
campodestino.pack(padx=2, pady=0)
botaoconverter.pack(padx=20, pady=30)
listamoedas.pack(padx=10, pady=0)


#rodar a janela 
janela.mainloop()