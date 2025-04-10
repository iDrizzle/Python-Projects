# 🧠 Sistema de Automação - TI

Este é um sistema de automação interna desenvolvido em **Python** com **CustomTkinter**, voltado para auxiliar a equipe de TI em tarefas rotineiras como cadastro de colaboradores, emissão de mensagens e organização de equipamentos.

## 🚀 Funcionalidades Atuais

- Tela principal com menu de opções
- Navegação entre páginas usando dicionário de frames
- Tela de cadastro de colaboradores (estrutura básica)
- Estrutura modular e pronta para expandir com novas páginas (ex: nota, termo, mensagem maestro)

---

## 🖥 Tecnologias Utilizadas

- Python 3.10+
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) (interface moderna para Tkinter)
- Pillow (para suporte a imagens, opcional)

---

## 📦 Estrutura do Projeto

projeto/ ├── app.py # Arquivo principal (controle da janela e navegação) ├── main_menu.py # Página do menu principal ├── register.py # Tela de cadastro de colaboradores ├── msg_maestro.py # (em desenvolvimento) ├── note.py # (em desenvolvimento) ├── term.py # (em desenvolvimento) ├── assets/ │ └── logo.png # Logo da empresa (opcional) └── README.md # Este arquivo

yaml
Copiar
Editar

---

## ▶️ Como Executar

1. **Instale as dependências:**

```bash
pip install customtkinter pillow
Execute o app:

bash
Copiar
Editar
python app.py
💡 Certifique-se de estar na pasta do projeto ao rodar o comando.

📝 A Fazer / Em Desenvolvimento
 Layout completo da tela de cadastro (nome, CPF, RG, equipamentos etc.)

 Tela de geração de mensagem de comissionamento

 Tela de emissão de termo

 Tela de envio de nota

 Tela de geração de mensagem maestro

 Integração com planilhas Excel (pandas)

🧩 Contribuindo
Fork este repositório

Crie uma branch com sua feature: git checkout -b minha-feature

Commit suas mudanças: git commit -m 'feat: adiciona nova funcionalidade'

Push para a branch: git push origin minha-feature

Abra um Pull Request

🛡 Licença
Este projeto é privado e voltado para fins internos da equipe de TI. Licenciamento pode ser definido futuramente.
