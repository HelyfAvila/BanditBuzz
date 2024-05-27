from flask import Flask, render_template, request, redirect, flash
import mysql.connector
app = Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

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
    return redirect('/cadastro')
    #return 'gravou'



@app.route('/cadastrar_cliente', methods=['POST'])
def inserir_cliente():
    nome = request.form['txt_nome']
    nascimento = request.form['txt_nascimento']
    cpf = request.form['txt_cpf']
    rg = request.form['txt_rg']
    email = request.form['txt_email']
    endereco = request.form['txt_endereco']
    bairro = request.form['txt_bairro']
    cidade = request.form['txt_cidade']
    estado = request.form['txt_estado']
    cep = request.form['txt_cep']
    db = mysql.connector.connect(host='201.23.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='E$tud@_m@1$',
                                 database='aula_fatec')
    mycursor = db.cursor() #Para executar algo no banco
    query = "INSERT INTO xinim_tbcliente ( name , dateofbirty, CPF, RG, email, address, neighborhood, city, state, zipCode ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nome, nascimento, cpf, rg, email, endereco, bairro, cidade, estado, cep)
    mycursor.execute(query,values)
    db.commit()
    return redirect('/clientes')

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
    return render_template('alterar.html', opcao='alterar',  usuarios=resultado)

@app.route('/update_usuario', methods=['POST']) #faz alteração em dados do banco
def update_usuario():
    id = request.form['txt_id']
    nome = request.form['txt_nome']
    cpf = request.form['txt_cpf']
    email = request.form['txt_email']
    senha = request.form['txt_senha']
    db = mysql.connector.connect(host='201.23.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='E$tud@_m@1$',
                                 database='aula_fatec')
    mycursor = db.cursor()
    query = "update xinim_tbusuario set nome = '" + nome + "', cpf = '" + cpf + "', email = '" + email + "', senha = '" + senha + "' where id = " + id
    print(query)
    #usa se aspas simples quando a variável trata-se de uma string (texto)
    mycursor.execute(query)
    db.commit() #duas formas de fechar uma transação, ou com commit ou rollback (salva ou desfaz)
    return redirect('/cadastro') #Não pode retornar uma rota post, tem que ser o site principal por exemplo

@app.route('/delete_usuario/<user>')
def delete_usuario(user):
    db = mysql.connector.connect(host='201.23.3.86',
                                 port=5000,
                                 user='usr_aluno',
                                 password='E$tud@_m@1$',
                                 database='aula_fatec')
    mycursor = db.cursor()
    query = "DELETE FROM xinim_tbusuario WHERE id = %s" 
    mycursor.execute(query, (user,))
    db.commit() 
    return redirect('/?deleted=True')

# Executa o aplicativo Flask
if __name__ == "__main__":
    # Ativa o modo de depuração
    app.run(debug=True)

