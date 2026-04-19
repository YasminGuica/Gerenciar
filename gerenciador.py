import json
from datetime import datetime

ARQUIVO = "tasks.json"
tasks = []
next_id = 1

def criar_tarefa(titulo, prazo="", prioridade="média"):
    global next_id
    task = {
        "id": next_id,
        "titulo": titulo,
        "status": "pendente",
        "prazo": prazo,
        "prioridade": prioridade
    }
    tasks.append(task)
    next_id += 1

def listar_tarefas():
    if not tasks:
        print("\nNenhuma tarefa cadastrada.")
        return
    
    for t in tasks:
        print(f"""
ID: {t['id']}
Título: {t['titulo']}
Status: {t['status']}
Prazo: {t.get('prazo', '-')}
Prioridade: {t.get('prioridade', '-')}
------------------------""")

def atualizar_status(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "concluído"
            print(f"Tarefa {task_id} concluída!")
            return
    print(f"Tarefa com ID {task_id} não encontrada.")

def deletar_tarefa(task_id):
    global tasks
    tamanho_antes = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) < tamanho_antes:
        print(f"Tarefa {task_id} deletada!")
    else:
        print(f"Tarefa com ID {task_id} não encontrada.")

def salvar():
    with open(ARQUIVO, "w") as f:
        json.dump(tasks, f, indent=4)

def carregar():
    global tasks, next_id
    try:
        with open(ARQUIVO, "r") as f:
            tasks = json.load(f)
            if tasks:
                next_id = max(t["id"] for t in tasks) + 1
            else:
                next_id = 1
    except FileNotFoundError:
        tasks = []
        next_id = 1

def menu():
    carregar()
    
    while True:
        print("\n=== SISTEMA DE TAREFAS ===")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Deletar tarefa")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            titulo = input("Título: ")
            prazo = input("Prazo (YYYY-MM-DD) [opcional]: ")
            print("Prioridades: baixa, média, alta")
            prioridade = input("Prioridade [média]: ").lower()
            
            if not prioridade or prioridade not in ["baixa", "média", "alta"]:
                prioridade = "média"
            
            criar_tarefa(titulo, prazo, prioridade)
            salvar()
            print("Tarefa criada com sucesso!")

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            try:
                tid = int(input("ID da tarefa a concluir: "))
                atualizar_status(tid)
                salvar()
            except ValueError:
                print("ID inválido!")

        elif opcao == "4":
            try:
                tid = int(input("ID da tarefa a deletar: "))
                deletar_tarefa(tid)
                salvar()
            except ValueError:
                print("ID inválido!")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()