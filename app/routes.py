from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Cliente, Pet, Agendamento
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return redirect(url_for('main.login'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        if usuario == 'jael' and senha == '123456':
            return redirect(url_for('main.agenda'))
        else:
            flash('Usuário ou senha incorretos', 'danger')
    
    return render_template('login.html')

@bp.route('/agenda')
def agenda():
    # Busca todos os agendamentos ordenados por data e horário
    agendamentos = Agendamento.query.order_by(Agendamento.data, Agendamento.horario).all()
    return render_template('agenda.html', agendamentos=agendamentos)

@bp.route('/novo-agendamento', methods=['GET', 'POST'])
def novo_agendamento():
    if request.method == 'POST':
        nome_pet = request.form.get('pet')
        nome_tutor = request.form.get('tutor')
        servico = request.form.get('servico')
        data_str = request.form.get('data')
        horario = request.form.get('horario')
        observacao = request.form.get('observacao')

        try:
            # Converte a data
            data = datetime.strptime(data_str, '%Y-%m-%d').date()

            # Cria ou busca o Cliente (Tutor)
            cliente = Cliente.query.filter_by(nome=nome_tutor).first()
            if not cliente:
                cliente = Cliente(nome=nome_tutor, telefone="Não informado")
                db.session.add(cliente)
                db.session.flush()  # Para pegar o ID

            # Cria o Pet
            pet = Pet(nome=nome_pet, especie="Não informado", cliente_id=cliente.id)
            db.session.add(pet)
            db.session.flush()

            # Cria o Agendamento
            novo = Agendamento(
                data=data,
                horario=horario,
                servico=servico,
                status="Agendado",
                observacao=observacao,
                pet_id=pet.id,
                cliente_id=cliente.id
            )
            db.session.add(novo)
            db.session.commit()

            flash(f'Agendamento de {nome_pet} realizado com sucesso!', 'success')
            return redirect(url_for('main.feedback'))

        except Exception as e:
            db.session.rollback()
            flash('Erro ao salvar agendamento. Tente novamente.', 'danger')
            return redirect(url_for('main.novo_agendamento'))
    
    return render_template('novo_agendamento.html')

@bp.route('/feedback')
def feedback():
    return render_template('feedback.html')

@bp.route('/excluir/<int:id>')
def excluir_agendamento(id):
    agendamento = Agendamento.query.get_or_404(id)
    db.session.delete(agendamento)
    db.session.commit()
    flash('Agendamento excluído com sucesso!', 'success')
    return redirect(url_for('main.agenda'))