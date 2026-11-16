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
    return render_template('agenda.html')

@bp.route('/novo-agendamento', methods=['GET', 'POST'])
def novo_agendamento():
    if request.method == 'POST':
        pet = request.form.get('pet')
        tutor = request.form.get('tutor')
        servico = request.form.get('servico')
        data = request.form.get('data')
        horario = request.form.get('horario')
        observacao = request.form.get('observacao')

        flash(f'Agendamento de {pet} realizado com sucesso para {data} às {horario}!', 'success')
        return redirect(url_for('main.feedback'))
    
    return render_template('novo_agendamento.html')

@bp.route('/feedback')
def feedback():
    return render_template('feedback.html')