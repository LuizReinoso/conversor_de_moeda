import requests
import locale
import customtkinter as ctk
from PIL import Image


def ValorDolarReal():
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    requisicao = requests.get(
        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    dicionarioJson = requisicao.json()

    valorDolar = float(dicionarioJson['USDBRL']['bid'])

    valorInseridoR = entrada.get()

    print(valorInseridoR)

    # ------------------Ajuste da pontuação do valor de enttrada--------------
    valorInseridoR = valorInseridoR.replace('.', '').replace(',', '.')

    try:
        valorInseridoR = float(valorInseridoR)
    except ValueError:
        resultado.configure(
            text="Valor INVÁLIDO! Digite apenas NÚMEROS.",
            fg_color="red",
            text_color="black",
            font=("lucida bright", 18, "bold"),
        )
        resultado.pack(padx=30, pady=30)
        return

    vConvertidoR = valorInseridoR * valorDolar
    vConvertidoR = locale.currency(vConvertidoR, grouping=True)

# ------------------------valor de saida dos PILA ----------------------------
    resultado.configure(
        text=f"O valor convertido para REAL fica: {vConvertidoR}",
        fg_color="#65B307",
        text_color="black",
        font=("lucida bright", 20, "bold"),
    )
    resultado.pack(padx=30, pady=30)


def ValorRealDolar():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    requisicao = requests.get(
        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    dicionarioJson = requisicao.json()

    valorDolar = float(dicionarioJson['USDBRL']['bid'])

# ------------------ entrada do valor digitado -------------------------------
    valorInseridoR = entrada.get()

# ------------------Ajuste da pontuação do valor de entrada-----------------
    valorInseridoR = valorInseridoR.replace('.', '').replace(',', '.')

    try:
        valorInseridoR = float(valorInseridoR)
    except ValueError:
        resultado.configure(
            text="Valor INVÁLIDO! Digite apenas NÚMEROS.",
            fg_color="red",
            text_color="black",
            font=("lucida bright", 18, "bold"),
        )
        resultado.pack(padx=30, pady=30)
        return

    vConvertidoR = valorInseridoR / valorDolar
    vConvertidoR = locale.currency(vConvertidoR, grouping=True)

    vConvertidoR_str = vConvertidoR.replace('$', 'US$ ')
# ---------------------------- valor de saida DOLETA--------------------------
    resultado.configure(
        text=f"O valor convertido para DOLAR fica: {vConvertidoR_str}",
        fg_color="#65B307",
        text_color="black",
        corner_radius=10,
        font=("lucida bright", 20, "bold"),
    )
    resultado.pack(padx=30, pady=30)


# --------------------------SubTitulo do sistema ------------------
root = ctk.CTk()
root.title("Conversor de Moeda 3000")
root.geometry("600x400")  # Ajuste o tamanho da janela conforme necessário

# --------------------------imagem de fundo----------------------------------------------
image_path = r"C:\Users\bruno\Desktop\conversor de moeda\muroPreto.jpeg"
bg_image = ctk.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(600, 400))
bg_label = ctk.CTkLabel(root, image=bg_image, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------------------Titulo principal-----------------------------------
titulo = ctk.CTkLabel(root,
                      text="Conversor de Moeda 3000",
                      fg_color="black",
                      font=("system", 30, "bold"),
                      text_color="#01c6c7", corner_radius=10)
titulo.pack(pady=30, padx=30)

# ------------------------Titulo de instrução---------------
subtitulo = ctk.CTkLabel(root,
                         text="Digite um valor:",
                         fg_color="black",
                         text_color="#01c6c7",
                         corner_radius=10,
                         font=("georgia", 18, "bold"))
subtitulo.pack(pady=10, padx=50)

# ------------------------Espaço para inserir valor---------------------
entrada = ctk.CTkEntry(root,
                       font=("lucida bright", 20, "bold"),
                       width=250,
                       height=30)
entrada.pack(padx=20, pady=20)

# ------------------------Botão de DOLAR > REAL--------------------------
botao = ctk.CTkButton(root,
                      text="Converter DOLAR para REAL",
                      font=("georgia", 15, "bold"),
                      fg_color="#01c6c7",
                      text_color="black",
                      hover_color="#0000cd",
                      command=ValorDolarReal)
botao.pack(pady=10)

# ------------------------Botão de REAL > DOLAR--------------------------
botao = ctk.CTkButton(root,
                      text="Converter REAL para DOLAR",
                      font=("georgia", 15, "bold"),
                      fg_color="#01c6c7",
                      text_color="black",
                      hover_color="#0000cd",
                      command=ValorRealDolar)
botao.pack(pady=10)

# ---------------------------output do resultado-------------------------
resultado = ctk.CTkLabel(root,
                         text="",
                         corner_radius=10)
resultado.pack(padx=30, pady=30)

root.mainloop()
