# --- Importar a biblioteca --- #
import customtkinter as ctk
from configuracoes import *
from tkinter import filedialog, Canvas


# --- Criar a classe de importação da imagem --- #
class ImportarImagem(ctk.CTkFrame):
    """Classe responsável por importar a imagem:
    1. Cobrir a tela inteira.
    2. O botão deve estar no meio da tela.
    3. Deve estar escrito 'Abrir Imagem' no botão."""
    def __init__(self, parent, func_importar):
        """Função responsável por inicializar as variáveis da classe."""
        # --- Setup inicial --- #
        super().__init__(master=parent)
        self.func_importar = func_importar

        # --- Colocar o layout da tela --- #
        self.grid(column=0, columnspan=2, row=0, sticky='nsew')

        # --- Botão --- #
        ctk.CTkButton(
            self,
            text='Abrir Imagem',
            command=self.tela_selecao_imagem
        ).pack(expand=True)

    def tela_selecao_imagem(self):
        """Função responsável por abrir a tela de seleção de imagem."""
        caminho = filedialog.askopenfile().name
        self.func_importar(caminho)


class ImagemSaida(Canvas):
    """Classe responsável por colocar a imagem na tela do app."""
    def __init__(self, parent):
        """Função responsável por inicializar as variáveis."""
        super().__init__(
            master=parent,
            background=COR_FUNDO,
            bd=0,
            highlightthickness=0,
            relief='ridge')
        self.grid(row=0, column=1, sticky='nwes')
