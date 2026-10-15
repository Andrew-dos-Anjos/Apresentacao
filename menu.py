from time import sleep
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import importlib

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk() 
janela.title('Business_Company - AUTO')
janela.geometry('575x350')

# ================= EXEMPLOS DE FUNÇÕES REAIS FUTURAS =================
# Aqui você criará as funções com as automações reais em Python (ex: Selenium, PyAutoGUI, etc.)

def exemplo_gerico():
    messagebox.showinfo("Executando", "Esta automação ainda não foi implementada.")

def simulacao():
    import visual
    importlib.reload(visual)  # Força o Python a rodar o arquivo de novo

def limpeza():
    import limpar
    importlib.reload(limpar)

# ================= CONFIGURAÇÃO PERSONALIZADA DE CADA SOFTWARE =================
# Adicione ou mude os textos e funções abaixo. É aqui que você personaliza tudo!

dados_softwares = {
    'Dominio': [
        {"nome": "Automação 1", "desc": "Explicação personalizada para a automação 1 do Domínio.", "func": exemplo_gerico},
        {"nome": "Automação 2", "desc": "Explicação personalizada para a automação 2 do Domínio.", "func": exemplo_gerico},
        {"nome": "Automação 3", "desc": "Explicação personalizada para a automação 3 do Domínio.", "func": exemplo_gerico},
        {"nome": "Automação 4", "desc": "Explicação personalizada para a automação 4 do Domínio.", "func": exemplo_gerico},
        {"nome": "Automação 5", "desc": "Explicação personalizada para a automação 5 do Domínio.", "func": exemplo_gerico},
    ],
    'Alterdata': [
        {"nome": "Automação 1", "desc": "Explicação personalizada para a automação 1 do Alterdata.", "func": exemplo_gerico},
        {"nome": "Automação 2", "desc": "Explicação personalizada para a automação 2 do Alterdata.", "func": exemplo_gerico},
        {"nome": "Automação 3", "desc": "Explicação personalizada para a automação 3 do Alterdata.", "func": exemplo_gerico},
        {"nome": "Automação 4", "desc": "Explicação personalizada para a automação 4 do Alterdata.", "func": exemplo_gerico},
        {"nome": "Automação 5", "desc": "Explicação personalizada para a automação 5 do Alterdata.", "func": exemplo_gerico},
    ],
    'Conta Azul': [
        {"nome": "Automação 1", "desc": "Explicação da automação 1 do Conta Azul.", "func": exemplo_gerico},
        {"nome": "Automação 2", "desc": "Explicação da automação 2 do Conta Azul.", "func": exemplo_gerico},
        {"nome": "Automação 3", "desc": "Explicação da automação 3 do Conta Azul.", "func": exemplo_gerico},
        {"nome": "Automação 4", "desc": "Explicação da automação 4 do Conta Azul.", "func": exemplo_gerico},
        {"nome": "Automação 5", "desc": "Explicação da automação 5 do Conta Azul.", "func": exemplo_gerico},
    ],
    'Omie': [
        {"nome": "Cadastro_NFe", "desc": "Demonstração cadastro de Nota Fiscal simulado.", "func": simulacao},
        {"nome": "Exclusão_NFe", "desc": "Demonstração exclusão do cadastro de Nota Fiscal simulado.", "func": limpeza},
        {"nome": "Automação 3", "desc": "Explicação da automação 3 do Omie.", "func": exemplo_gerico},
        {"nome": "Automação 4", "desc": "Explicação da automação 4 do Omie.", "func": exemplo_gerico},
        {"nome": "Automação 5", "desc": "Explicação da automação 5 do Omie.", "func": exemplo_gerico},
    ],
    'TOTVS': [
        {"nome": "Automação 1", "desc": "Explicação da automação 1 do TOTVS.", "func": exemplo_gerico},
        {"nome": "Automação 2", "desc": "Explicação da automação 2 do TOTVS.", "func": exemplo_gerico},
        {"nome": "Automação 3", "desc": "Explicação da automação 3 do TOTVS.", "func": exemplo_gerico},
        {"nome": "Automação 4", "desc": "Explicação da automação 4 do TOTVS.", "func": exemplo_gerico},
        {"nome": "Automação 5", "desc": "Explicação da automação 5 do TOTVS.", "func": exemplo_gerico},
    ],
    'Acessorias': [
        {"nome": "Automação 1", "desc": "Explicação da automação 1 do Acessorias.", "func": exemplo_gerico},
        {"nome": "Automação 2", "desc": "Explicação da automação 2 do Acessorias.", "func": exemplo_gerico},
        {"nome": "Automação 3", "desc": "Explicação da automação 3 do Acessorias.", "func": exemplo_gerico},
        {"nome": "Automação 4", "desc": "Explicação da automação 4 do Acessorias.", "func": exemplo_gerico},
        {"nome": "Automação 5", "desc": "Explicação da automação 5 do Acessorias.", "func": exemplo_gerico},
    ],
    'Senior HCM': [
        {"nome": "Automação 1", "desc": "Explicação da automação 1 do Senior HCM.", "func": exemplo_gerico},
        {"nome": "Automação 2", "desc": "Explicação da automação 2 do Senior HCM.", "func": exemplo_gerico},
        {"nome": "Automação 3", "desc": "Explicação da automação 3 do Senior HCM.", "func": exemplo_gerico},
        {"nome": "Automação 4", "desc": "Explicação da automação 4 do Senior HCM.", "func": exemplo_gerico},
        {"nome": "Automação 5", "desc": "Explicação da automação 5 do Senior HCM.", "func": exemplo_gerico},
    ],
    'Apdata': [
        {"nome": "Automação 1", "desc": "Explicação da automação 1 do Apdata.", "func": exemplo_gerico},
        {"nome": "Automação 2", "desc": "Explicação da automação 2 do Apdata.", "func": exemplo_gerico},
        {"nome": "Automação 3", "desc": "Explicação da automação 3 do Apdata.", "func": exemplo_gerico},
        {"nome": "Automação 4", "desc": "Explicação da automação 4 do Apdata.", "func": exemplo_gerico},
        {"nome": "Automação 5", "desc": "Explicação da automação 5 do Apdata.", "func": exemplo_gerico},
    ]
}


# ================= FUNÇÕES DE NAVEGAÇÃO =================

def abrir_software(nome_software):
    tela_softw.pack_forget()
    for tela in telas_softwares.values():
        tela.pack_forget()
    telas_softwares[nome_software].pack(fill='both', expand=True, pady=20, padx=20)

def voltar_inicio():
    for tela in telas_softwares.values():
        tela.pack_forget()
    tela_softw.pack(side='top', pady=20)


# ================= TELA PRINCIPAL (CONTAINER) =================

tela_inicio = ctk.CTkFrame(janela)
tela_inicio.pack(fill='both', expand=True)


# ================= 1. MENU INICIAL DE SOFTWARES =================

tela_softw = ctk.CTkFrame(tela_inicio)
tela_softw.pack(side='top', pady=20) 

tela_softw.columnconfigure((0, 1), pad=20)
tela_softw.rowconfigure((0, 1, 2, 3, 4, 5, 6), pad=8)

# --- BLOCO DE CIMA ---
ctk.CTkLabel(tela_softw, text='Contabil', font=("Arial", 14, "bold")).grid(row=0, column=0)
ctk.CTkLabel(tela_softw, text='Financeiro', font=("Arial", 14, "bold")).grid(row=0, column=1)

ctk.CTkButton(tela_softw, text='Dominio', command=lambda: abrir_software('Dominio')).grid(row=1, column=0)
ctk.CTkButton(tela_softw, text='Alterdata', command=lambda: abrir_software('Alterdata')).grid(row=2, column=0)

ctk.CTkButton(tela_softw, text='Conta Azul', command=lambda: abrir_software('Conta Azul')).grid(row=1, column=1)
ctk.CTkButton(tela_softw, text='Omie', command=lambda: abrir_software('Omie'), border_width=3, border_color="black").grid(row=2, column=1)

# Espaçador
ctk.CTkLabel(tela_softw, text='').grid(row=3, column=0, columnspan=2)

# --- BLOCO DE BAIXO ---
ctk.CTkLabel(tela_softw, text='ADM', font=("Arial", 14, "bold")).grid(row=4, column=0)
ctk.CTkLabel(tela_softw, text='RH', font=("Arial", 14, "bold")).grid(row=4, column=1)

ctk.CTkButton(tela_softw, text='TOTVS', command=lambda: abrir_software('TOTVS')).grid(row=5, column=0)
ctk.CTkButton(tela_softw, text='Acessorias', command=lambda: abrir_software('Acessorias')).grid(row=6, column=0)

ctk.CTkButton(tela_softw, text='Senior HCM', command=lambda: abrir_software('Senior HCM')).grid(row=5, column=1)
ctk.CTkButton(tela_softw, text='Apdata', command=lambda: abrir_software('Apdata')).grid(row=6, column=1)


# ================= 2. MONTAGEM AUTOMÁTICA DAS TELAS INDIVIDUAIS =================

telas_softwares = {}

for nome, lista_automacoes in dados_softwares.items():
    frame_software = ctk.CTkFrame(tela_inicio)
    ctk.CTkLabel(frame_software, text=f"Automações do {nome}", font=("Arial", 18, "bold")).pack(pady=15)
    
    conteudo_grid = ctk.CTkFrame(frame_software, fg_color="transparent")
    conteudo_grid.pack(fill='both', expand=True, padx=10)
    conteudo_grid.columnconfigure(0, weight=0, pad=15)
    conteudo_grid.columnconfigure(1, weight=1)         
    conteudo_grid.rowconfigure((0, 1, 2, 3, 4), pad=12) 
    
    # Montando cada um dos 5 botões com seus dados únicos definidos no dicionário
    for indice, auto in enumerate(lista_automacoes):
        # Botão Individual
        btn_auto = ctk.CTkButton(
            conteudo_grid, 
            text=auto["nome"],  # Nome personalizado
            command=auto["func"],  # Função real associada
            width=140
        )
        btn_auto.grid(row=indice, column=0, sticky="w")
        
        # Texto Individual
        lbl_desc = ctk.CTkLabel(conteudo_grid, text=auto["desc"], anchor="w", justify="left")
        lbl_desc.grid(row=indice, column=1, sticky="w")
    
    ctk.CTkButton(frame_software, text='← Voltar', fg_color='#4A4A4A', hover_color='#333333', command=voltar_inicio).pack(side='bottom', pady=15)
    telas_softwares[nome] = frame_software

janela.mainloop()
