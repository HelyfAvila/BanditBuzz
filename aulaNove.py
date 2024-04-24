from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_usuario', methods=['POST'])
def inserir_usuario():
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    email = request.form['txt_email']
    senha = request.form['txt_senha']
    db = mysql.connector.connect(host='201.23.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='E$tud@_m@1$',
                                 database='aula_fatec')
    mycursor = db.cursor() #Para executar algo no banco
    query = "INSERT INTO xinim_tbusuario ( nome , cpf, email, senha ) VALUES (%s, %s, %s, %s)"
    values = (nome, cpf, email, senha)
    mycursor.execute(query,values)
    db.commit()
    return 'gravou'
@app.route('/consultar')
def listar_usuario():
    db = mysql.connector.connect(host='201.23.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='E$tud@_m@1$',
                                 database='aula_fatec')
    mycursor = db.cursor()
    query = 'SELECT nome, CPF, email, id FROM xinim_tbusuario' #armazena query 
    mycursor.execute(query) #executa a query declarada acima
    resultado = mycursor.fetchall() #fetch (pega os itens um a um), o "all " atrelado serve para pegar tudo
    return render_template('usuarios.html', usuarios=resultado)

@app.route('/alterar_usuario/<user>') #carrregar a página de cadastro
def alterar_usuario(user):
    db = mysql.connector.connect(host='201.23.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='E$tud@_m@1$',
                                 database='aula_fatec')
    mycursor = db.cursor()
    query = "SELECT nome, CPF, email, id FROM xinim_tbusuario where id =  " + user
    mycursor.execute(query)
    resultado = mycursor.fetchall()
    return render_template('alterar.html', usuarios=resultado)
# Executa o aplicativo Flask
if __name__ == "__main__":
    # Ativa o modo de depuração
    app.run(debug=True)

