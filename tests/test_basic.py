from app import create_app, db
from app.models import Cliente, Pet, Agendamento

def test_app_existe():
    app = create_app()
    assert app is not None

def test_criar_cliente():
    app = create_app()
    with app.app_context():
        cliente = Cliente(nome="Maria Silva", telefone="41999999999")
        db.session.add(cliente)
        db.session.commit()
        
        cliente_db = Cliente.query.filter_by(nome="Maria Silva").first()
        assert cliente_db is not None
        assert cliente_db.telefone == "41999999999"

def test_rota_login():
    app = create_app()
    client = app.test_client()
    response = client.get('/login')
    assert response.status_code == 200