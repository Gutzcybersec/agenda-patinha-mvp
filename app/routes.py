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
        
        # Login simples para o MVP (usuário: jael / senha: 123456)
        if usuario == 'jael' and senha == '123456':
            return redirect(url_for('main.agenda'))
        else:
            flash('Usuário ou senha incorretos', 'danger')
    
    return render_template('login.html')

@bp.route('/agenda')
def agenda():
    agendamentos = Agendamento.query.order_by(Agendamento.data, Agendamento.horario).all()
    return render_template('agenda.html', agendamentos=agendamentos)

@bp.route('/novo-agendamento', methods=['GET', 'POST'])
def novo_agendamento():
    if request.method == 'POST':
        # Por enquanto só redireciona com sucesso (vamos melhorar depois)
        flash('Agendamento realizado com sucesso!', 'success')
        return redirect(url_for('main.feedback'))
    
    return render_template('agenda.html')

@bp.route('/feedback')
def feedback():
    return render_template('feedback.html')