from flask import*

import dao

app = Flask(__name__)
app.secret_key = 'ajhk23h423'


@app.route("/")
def paginicial():
    return render_template('inicio2.html')

@app.route('/pagaddresenha')
def mostrar_pag_add_resenha():
    return render_template('addresenha.html')

@app.route('/salvarresenha', methods =['POST'])
def salvar_resenha():
    titulo = request.form.get('titulo')
    resenha = request.form.get('resenha')
    login = session['login']
    dao.inserir_resenha(titulo, resenha, login)

    resenhas = dao.listar_livros(login)


    return render_template('lista.html', lista=resenhas)



@app.route('/enviar-dados' , methods =['POST', 'GET'])
def paglivros():

    if request.method == 'POST':

        login = request.form.get('nome')
        senha = request.form.get('senha')


        if len(dao.login(login, senha)) > 0:
            session['login'] = login
            return render_template('livros.html')
        else:
            return render_template('inicio2.html', msg='usuário ou senha incorretos')

    else:
        if 'login' in session:
            return render_template('livros.html')
        else:
            return render_template('inicio2.html')

@app.route("/pagcadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/cadastrar_user",methods=['POST'])
def fazercadastro():
    nome = request.form.get('nome')
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    if dao.inserir_user(nome, usuario, senha):
     msg = 'usuario inserido com sucesso'
     return render_template('inicio2.html' , texto=msg)

    else:
        msg = 'usuario nao inserido'
        return render_template('inicio2.html', texto=msg)




if __name__ == '__main__':
        app.run(debug=True)

