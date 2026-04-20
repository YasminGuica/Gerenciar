# Gerenciar

Um gerenciador de tarefas simples via linha de comando (CLI) que permite criar, listar, atualizar e remover tarefas, com suporte a status, prazos e prioridades. Os dados são persistidos em arquivos JSON.

---

## 🚀 Funcionalidades

* ✅ Criar tarefas
* 📋 Listar tarefas
* ✏️ Atualizar tarefas
* ❌ Remover tarefas
* 🔄 Marcar como concluída ou pendente
* ⏰ Definir prazos (deadline)
* ⚡ Definir prioridades (baixa, média, alta)
* 💾 Persistência em JSON ou CSV

---

## 🛠️ Tecnologias Utilizadas

* Linguagem: (Python,Node.js )
* Biblioteca padrão: Manipulação de arquivos (JSON),datetime
---

## 📂 Estrutura do Projeto

```
 gerenciador-tarefas
 ┣  main.py
 ┣  tasks.json
 ┗  README.md
```
## 📊 Estrutura da Tarefa

```json
{
  "id": 1,
  "titulo": "Estudar programação",
  "status": "pendente",
  "prazo": "2026-05-01",
  "prioridade": "alta"
}
```

## 📌 Possíveis Melhorias

* Filtros por status, prioridade ou prazo
* Interface gráfica (GUI)
* Integração com banco de dados
* Notificações de prazo

---

