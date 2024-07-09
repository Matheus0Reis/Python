import tkinter as tk

class SistemaBancario:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema Bancário")
        self.master.geometry("300x200")

        # Menu
        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack(fill="both", expand=True)

        self.label_menu = tk.Label(self.menu_frame, text="Menu")
        self.label_menu.pack()

        self.button_criar_conta = tk.Button(self.menu_frame, text="Criar Conta", command=self.criar_conta)
        self.button_criar_conta.pack()

        self.button_realizar_operacao = tk.Button(self.menu_frame, text="Realizar Operação", command=self.realizar_operacao)
        self.button_realizar_operacao.pack()

        self.button_sair = tk.Button(self.menu_frame, text="Sair", command=self.master.destroy)
        self.button_sair.pack()

    def criar_conta(self):
        # Criar conta frame
        self.criar_conta_frame = tk.Frame(self.master)
        self.criar_conta_frame.pack(fill="both", expand=True)

        self.label_numero_conta = tk.Label(self.criar_conta_frame, text="Número da Conta:")
        self.label_numero_conta.pack()

        self.entry_numero_conta = tk.Entry(self.criar_conta_frame)
        self.entry_numero_conta.pack()

        self.label_saldo_inicial = tk.Label(self.criar_conta_frame, text="Saldo Inicial:")
        self.label_saldo_inicial.pack()

        self.entry_saldo_inicial = tk.Entry(self.criar_conta_frame)
        self.entry_saldo_inicial.pack()

        self.button_criar_conta_confirm = tk.Button(self.criar_conta_frame, text="Criar Conta", command=self.criar_conta_confirm)
        self.button_criar_conta_confirm.pack()

    def criar_conta_confirm(self):
        # Criar conta lógica aqui
        print("Conta criada com sucesso!")

    def realizar_operacao(self):
        # Realizar operação frame
        self.realizar_operacao_frame = tk.Frame(self.master)
        self.realizar_operacao_frame.pack(fill="both", expand=True)

        self.label_numero_conta = tk.Label(self.realizar_operacao_frame, text="Número da Conta:")
        self.label_numero_conta.pack()

        self.entry_numero_conta = tk.Entry(self.realizar_operacao_frame)
        self.entry_numero_conta.pack()

        self.label_operacao = tk.Label(self.realizar_operacao_frame, text="Operação:")
        self.label_operacao.pack()

        self.option_operacao = tk.StringVar()
        self.option_operacao.set("Depósito")

        self.option_menu_operacao = tk.OptionMenu(self.realizar_operacao_frame, self.option_operacao, "Depósito", "Saque", "Extrato")
        self.option_menu_operacao.pack()

        self.button_realizar_operacao_confirm = tk.Button(self.realizar_operacao_frame, text="Realizar Operação", command=self.realizar_operacao_confirm)
        self.button_realizar_operacao_confirm.pack()

    def realizar_operacao_confirm(self):
        # Realizar operação lógica aqui
        print("Operação realizada com sucesso!")

root = tk.Tk()
app = SistemaBancario(root)
root.mainloop()