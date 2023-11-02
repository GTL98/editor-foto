# --- Importar a biblioteca --- #
import customtkinter as ctk
from widgets_imagem import *


# --- Criar a classe do App -- #
class App(ctk.CTk):
    """Classe responsável por criar o app."""
    def __init__(self):
        """Função responsável por iniciar as variáveis do app."""
        # --- Setup --- #
        super().__init__()
        ctk.set_appearance_mode('dark')  # aparência da tela do app
        self.geometry('1000x600')  # dimesões da tela
        self.title('Editor de Foto')  # título da janela
        self.minsize(800, 500)  # limita o tamanho mínimo da tela

        # --- Layout do App --- #
        self.rowconfigure(0, weight=1)  # linha 0
        self.columnconfigure(0, weight=2)  # coluna 0
        self.columnconfigure(1, weight=6)  # coluna 2

        # --- Widgets do App --- #
        ImportarImagem(self, self.importar_imagem)

        # --- Executar o App --- #
        self.mainloop()

    def importar_imagem(self, caminho):
        """Função responsável por importar a imagem."""
        print(caminho)


if __name__ == '__main__':
    App()
