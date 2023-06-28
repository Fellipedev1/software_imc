import mysql.connector
import tkinter as tk

# Função para calcular o IMC
def calcular_imc():
    nome = entry_nome.get()
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())
    imc = peso / (altura ** 2)
    resultado_imc.config(text=f"Senhor(a) {nome}, seu IMC é: {round(imc, 2)}")

    # Conexão com o banco de dados
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="acesso123",
        database="banco_imc"
    )

    # Criar um cursor para executar as consultas
    cursor = conexao.cursor()

    # Obter os valores dos campos de entrada
    idade = int(entry_idade.get())
    genero = genero_var.get()
    atleta = status_var.get()

    # Executar a consulta para inserir os dados na tabela
    consulta = "INSERT INTO dados_pacientes (nome, idade, genero, peso, altura, atleta, imc) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (nome, idade, genero, peso, altura, atleta, imc)
    cursor.execute(consulta, valores)

    # Fazer o commit das alterações e fechar a conexão
    conexao.commit()
    conexao.close()

    # Limpar os campos de entrada
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    genero_var.set("")  # Limpar seleção de gênero
    status_var.set("")  # Limpar seleção de status

# Função para limpar todos os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    genero_var.set("")  # Limpar seleção de gênero
    status_var.set("")  # Limpar seleção de status
    resultado_imc.config(text="")

# Criar a janela principal
window = tk.Tk()
window.title("Calculadora de IMC")

# Definir cor de fundo para a janela principal
window.configure(bg="lightgray")

# Criar um frame principal
frame = tk.Frame(window, bg="white", padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

# Criar os rótulos e campos de entrada
label_nome = tk.Label(frame, text="Nome Completo:", bg="light blue", font=("Arial", 12))
label_nome.pack()
entry_nome = tk.Entry(frame, font=("Arial", 12))
entry_nome.pack()

label_idade = tk.Label(frame, text="Idade:", bg="light blue", font=("Arial", 12))
label_idade.pack()
entry_idade = tk.Entry(frame, font=("Arial", 12))
entry_idade.pack()

label_genero = tk.Label(frame, text="Gênero:", bg="light blue", font=("Arial", 12))
label_genero.pack()

# Variável para armazenar o gênero selecionado
genero_var = tk.StringVar()

# Criar botões de seleção para os gêneros
radio_feminino = tk.Radiobutton(frame, text="Feminino", variable=genero_var, value="Feminino", bg="white", font=("Arial", 12))
radio_feminino.pack()

radio_masculino = tk.Radiobutton(frame, text="Masculino", variable=genero_var, value="Masculino", bg="white", font=("Arial", 12))
radio_masculino.pack()

label_peso = tk.Label(frame, text="Peso (kg):", bg="light blue", font=("Arial", 12))
label_peso.pack()
entry_peso = tk.Entry(frame, font=("Arial", 12))
entry_peso.pack()

label_altura = tk.Label(frame, text="Altura (m):", bg="light green", font=("Arial", 12))
label_altura.pack()
entry_altura = tk.Entry(frame, font=("Arial", 12))
entry_altura.pack()

label_atleta = tk.Label(frame, text="Você é:", bg="light green", font=("Arial", 12))
label_atleta.pack()

# Variável para armazenar o status selecionado (atleta ou paciente)
status_var = tk.StringVar()

# Criar botões de seleção para o status
radio_atleta = tk.Radiobutton(frame, text="Atleta", variable=status_var, value="Atleta", bg="white", font=("Arial", 12))
radio_atleta.pack()

radio_paciente = tk.Radiobutton(frame, text="Paciente", variable=status_var, value="Paciente", bg="white", font=("Arial", 12))
radio_paciente.pack()

button_calcular = tk.Button(frame, text="Calcular", command=calcular_imc, font=("Arial", 12))
button_calcular.pack()

# Adicionar espaçamento entre os botões
spacer_label = tk.Label(frame, text="", bg="white")
spacer_label.pack()

button_limpar = tk.Button(frame, text="Limpar", command=limpar_campos, font=("Arial", 12))
button_limpar.pack()

resultado_imc = tk.Label(frame, bg="white", font=("Arial", 12))
resultado_imc.pack()

# Iniciar o loop de eventos
window.mainloop()