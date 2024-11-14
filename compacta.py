from tkinter import Tk, filedialog, Button, Label, OptionMenu, StringVar
from pdfc.pdf_compressor import compress
import os
from PyPDF2 import PdfReader, PdfWriter
import threading


def comprimir_e_dividir(arquivo, output_label, modo_compressao):
    caminho_saida = os.path.splitext(arquivo)[0] + '_comprimido.pdf'
    mapa_compressao = {
        "Padrão": 0,
        "Pré-Impressão": 1,
        "Impressão": 2,
        "eBook": 3,
        "Potência máxima": 4
    }

    power = mapa_compressao.get(modo_compressao, 4)
    compress(arquivo, caminho_saida, power)

    if os.path.getsize(caminho_saida) > 8 * 1024 * 1024:
        divisor(caminho_saida, output_label)
    else:
        output_label.config(text="Processo concluído.")

def divisor(caminho_arquivo, output_label):
    pdf = PdfReader(caminho_arquivo)
    pdf_writer = PdfWriter()
    cont = 0

    for page in range(len(pdf.pages)):
        pdf_writer.add_page(pdf.pages[page])
        
        if page % 1 == 0:
            output_filename = caminho_arquivo[:-4] + '_' + str(cont + 1) + '.pdf'
            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)
                if os.path.getsize(output_filename) > 8 * 1024 * 1024:
                    cont += 1
                    pdf_writer = PdfWriter()

    output_label.config(text="Processo concluído.")

def selecionar_arquivos():
    def selecionar_arquivos_thread():
        output_label.config(text="Processando...") 
        root = Tk()
        root.withdraw()

        arquivos = filedialog.askopenfilenames(title="Selecione os arquivos", filetypes=[("PDF Files", "*.pdf")])

        if arquivos:
            for arquivo in arquivos:
                comprimir_e_dividir(arquivo, output_label, modo_compressao_var.get())

    window = Tk()
    window.title("Compressor e divisor PDF")
    output_label = Label(window, width=40, height=5, font=("Arial", 12))
    output_label.pack()

    modos_compressao = ["Padrão", "Pré-Impressão", "Impressão", "eBook", "Potência máxima"]
    modo_compressao_var = StringVar(window)
    modo_compressao_var.set(modos_compressao[4])
    modo_compressao_dropdown = OptionMenu(window, modo_compressao_var, *modos_compressao)
    modo_compressao_dropdown.pack()

    select_button = Button(window, text="Selecionar Arquivos", command=selecionar_arquivos_thread)
    select_button.pack(pady=10)
    window.mainloop()

selecionar_arquivos()
