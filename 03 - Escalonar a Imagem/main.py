# --- Importar a biblioteca --- #
import customtkinter as ctk
from widgets_imagem import *
from PIL import Image, ImageTk


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
        self.imagem_importar = ImportarImagem(self, self.importar_imagem)

        # --- Executar o App --- #
        self.mainloop()

    def importar_imagem(self, caminho):
        """Função responsável por importar a imagem."""
        self.imagem = Image.open(caminho)
        self.imagem_razao = self.imagem.size[0] / self.imagem.size[1]
        self.imagem_tk = ImageTk.PhotoImage(self.imagem)  # colocar a imagem no Tkinter
        self.imagem_importar.grid_forget()  # tira o botão de abrir a imagem
        self.imagem_saida = ImagemSaida(self, self.redimensionar_imagem)

    def redimensionar_imagem(self, evento):
        """Função responsável por redimensionar a imagem para caber no app."""
        # --- Razão atual do Canvas --- #
        canvas_razao = evento.width / evento.height

        # --- Redimensionar a imagem --- #
        if canvas_razao > self.imagem_razao:  # canvas é mais largo que a imagem
            imagem_altura = int(evento.height)
            imagem_largura = int(imagem_altura * self.imagem_razao)
        else:  # canvas é mais alto que a imagem
            imagem_largura = int(evento.width)
            imagem_altura = int(imagem_largura / self.imagem_razao)

        # --- Colocar a imagem na tela do app --- #
        self.imagem_saida.delete('all')
        imagem_redimensionada = self.imagem.resize((imagem_largura, imagem_altura))
        self.imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
        self.imagem_saida.create_image(
            evento.width / 2,
            evento.height / 2,
            image=self.imagem_tk
        )


if __name__ == '__main__':
    App()
