# AgendaPatinha

MVP de sistema de agendamento para o **Pet Shop Patinha**, desenvolvido como parte da disciplina de Projeto de Software.

## Sobre o Projeto

O AgendaPatinha é um Produto Mínimo Viável (MVP) criado para resolver a desorganização dos agendamentos de banho e tosa do Pet Shop Patinha, localizado em Paranaguá/PR. 

Atualmente os agendamentos são realizados de forma desorganizada pelo WhatsApp, gerando conflitos de horário, perda de mensagens e sobrecarga da proprietária. Este sistema oferece uma solução simples, leve e acessível para organização da agenda.

## Problema que Resolve
- Desorganização de agendamentos via WhatsApp
- Conflitos de horário
- Falta de visão clara da agenda diária e semanal
- Perda de tempo com gestão manual

## Público-alvo
- **Usuária direta:** Proprietária do Pet Shop Patinha
- **Impactados indiretos:** Tutores de animais da cidade de Paranaguá

## Tecnologias Utilizadas
- **Python 3.12**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**
- **HTML + CSS + Bootstrap 5**

## Arquitetura
Arquitetura Monolítica em Camadas:
- Camada de Apresentação
- Camada de Regras de Negócio
- Camada de Persistência

## Como rodar o projeto localmente

```bash
# Clone o repositório
git clone https://github.com/Gutzcybersec/agenda-patinha-mvp.git
cd agenda-patinha-mvp

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python run.py
