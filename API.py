from flask import Flask, jsonify, make_response, request

from flask_cors import CORS
import psycopg2
import json

app = Flask(__name__)

cors = CORS(app, origins=['*'])  # permitir solicitaçoes de todas origens

# Configurações do banco de dados
db_connection = psycopg2.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='admin',
    port='5432'
)

'''
# retorna todos os protudos
@app.route('/get_produto', methods=['GET'])
def get_produto():
    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute('SELECT * FROM loja.produto')
    results = comando.fetchall()
    comando.close()

    if results:
        for item in results:
            print(item)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Dado nao encontrado.'}))
        response = make_response(json.dumps({'message': 'Dado nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response
'''

'''
# busca um produto especifico pelo id
@app.route('/get_produto_id/<id>', methods=['GET'])
def get_protudo_id(id):
    id_new = str(id)

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute('SELECT * FROM loja.produto WHERE idProduto = ' + id_new)
    results = comando.fetchall()
    comando.close()

    if results:
        print(results)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Dado nao encontrado.'}))
        response = make_response(json.dumps({'message': 'Dado nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response
'''

'''
# Rota para criar um novo produto
@app.route('/criar_produto', methods=['POST'])
def create_produto():
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute(
        "INSERT INTO loja.produto (nomeProduto, estoqueProduto, descricao, preco, desconto, fotoProduto) VALUES (%s,%s,%s,%s,%s,%s)",
        (data['nomeProduto'], data['estoqueProduto'], data['descricao'], data['preco'],
         data['desconto'], data['fotoProduto']))

    db_connection.commit()
    comando.close()

    print(json.dumps({'message': 'Produto cadastrado com sucesso!'}))
    return json.dumps({'message': 'Produto cadastrado com sucesso!'})
'''

'''
# Rota para atualizar um produto
@app.route('/atualizar_produto/<id>', methods=['PUT'])
def update_produto(id):
    id_new = str(id)
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("UPDATE loja.produto SET nomeProduto=%s, estoqueProduto=%s, descricao=%s, preco=%s, "
                    "desconto=%s, fotoProduto=%s WHERE idProduto = %s",
                    (data['nomeProduto'], data['estoqueProduto'], data['descricao'],
                     data['preco'], data['desconto'], data['fotoProduto'], id_new))

    db_connection.commit()
    comando.close()

    print(json.dumps({'message': 'Produto atualizado com sucesso!'}))
    return json.dumps({'message': 'Produto atualizado com sucesso!'})
'''

'''
# Rota para deletar um produto
@app.route('/deletar_produto', methods=['DELETE'])
def delete_produto():
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("DELETE FROM loja.produto WHERE idProduto = %s", (data['idProduto'],))
    db_connection.commit()
    comando.close()

    print(json.dumps({'message': 'Produto deletado com sucesso.'}))
    return json.dumps({'message': 'Produto deletado com sucesso.'})
'''

'''
# Rota para criar uma nova categoria
@app.route('/criar_categoria', methods=['POST'])
def create_categoria():
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("INSERT INTO loja.categoria (nome) VALUES (%s)",
                    (data['nome_categoria'],))

    db_connection.commit()
    comando.close()

    print(json.dumps({'message': 'Categoria cadastrada com sucesso!'}))
    return json.dumps({'message': 'Categoria cadastrada com sucesso!'})
'''

'''
#listar id e nome de todas as categorias
@app.route('/listar_categorias', methods=['GET'])
def listar_categorias():
    comando = db_connection.cursor()
    db_connection.rollback()

    comando.execute('SELECT * FROM loja.Categoria')

    results = comando.fetchall()
    comando.close()

    if results:
        print(results)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Nenhuma categoria encontrada.'}))
        response = make_response(json.dumps({'message': 'Nenhuma categoria encontrada.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response
'''

'''
# Rota para registrar um produto em uma categoria
@app.route('/registrar_categoria_produto', methods=['POST'])
def registrar_categoria_produto():
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("INSERT INTO loja.ProdutoCategoria (idCategoria, idProduto) VALUES (%s, %s)",
                    (data['id_categoria'], data['id_produto']))

    db_connection.commit()
    comando.close()

    print(json.dumps({'message': 'Categoria foi cadastrada no produto com sucesso!'}))
    return json.dumps({'message': 'Categoria foi cadastrada no produto com sucesso!'})
'''

'''
# buscar categorias do produto pelo id do produto
@app.route('/buscar_categoria_produto/<idProduto>', methods=['GET'])
def buscar_categoria_produtod(idProduto):
    idProduto_new = str(idProduto)

    comando = db_connection.cursor()
    db_connection.rollback()

    comando.execute('SELECT c.nome FROM loja.Categoria c '
                    'INNER JOIN loja.ProdutoCategoria pc ON c.idCategoria = pc.idCategoria '
                    'WHERE pc.idProduto = %s;', (idProduto_new,))

    results = comando.fetchall()
    comando.close()

    if results:
        print(results)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Produto nao encontrado.'}))
        response = make_response(json.dumps({'message': 'Produto nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response
'''


# retorna todos os protudos em prodmoçao
@app.route('/get_promocoes', methods=['GET'])
def get_promocoes():
    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute('SELECT * FROM loja.produto WHERE emOferta = true')
    results = comando.fetchall()
    comando.close()

    if results:
        for item in results:
            print(item)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Dado nao encontrado.'}))
        response = make_response(json.dumps({'message': 'Dado nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response


# retorna lista de produtos pelo nome
@app.route('/busca_produto/<nomeProduto>', methods=['GET'])
def busca_produto(nomeProduto):
    nomeProduto_new = str(nomeProduto)

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute(
        'SELECT * FROM loja.produto WHERE lower(nomeProduto) like lower(%s) ORDER BY (estoqueproduto = 0) ASC, '
        'lower(nomeProduto) ASC',
        ('%' + nomeProduto_new + '%',))

    results = comando.fetchall()
    comando.close()

    if results:
        print(results)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Dado nao encontrado.'}))
        response = make_response(json.dumps({'message': 'Dado nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response


# filtrar produtos pelo nome da categoria
@app.route('/filtrar_produto_categoria/<nomeCategoria>', methods=['GET'])
def filtrar_produto_categoria(nomeCategoria):
    nomeCategoria_new = str(nomeCategoria)

    comando = db_connection.cursor()
    db_connection.rollback()

    comando.execute('SELECT * FROM loja.Produto p'
                    ' INNER JOIN loja.ProdutoCategoria pc ON p.idProduto = pc.idProduto'
                    ' INNER JOIN loja.Categoria c ON pc.idCategoria = c.idCategoria'
                    ' WHERE LOWER(c.nome) = LOWER(%s)'
                    ' ORDER BY (p.estoqueproduto = 0) ASC, LOWER(p.nomeProduto) ASC;', (nomeCategoria_new,))

    results = comando.fetchall()
    comando.close()

    if results:
        print(results)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Produto nao encontrado.'}))
        response = make_response(json.dumps({'message': 'Produto nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response


# Rota para criar um novo cliente
# ela cria o cliente, cria sua lista de desejos e cria seu carrinho
@app.route('/criar_login_cliente', methods=['POST'])
def criar_login_cliente():
    data = request.get_json()

    # Inicia a transação
    comando = db_connection.cursor()

    try:
        # Inserir o cliente
        comando.execute("INSERT INTO loja.Cliente (nome, email, senha) VALUES (%s, %s, MD5(%s))",
                        (data['nome'], data['email'], data['senha']))

        # Recuperar o ID do cliente inserido
        comando.execute("SELECT idCliente FROM loja.Cliente WHERE email = %s", (data['email'],))
        id_cliente = comando.fetchone()[0]

        # Inserir o carrinho para o cliente
        comando.execute("INSERT INTO loja.Carrinho DEFAULT VALUES RETURNING idCarrinho")
        id_carrinho = comando.fetchone()[0]

        # Atualizar o cliente com o ID do carrinho
        comando.execute("UPDATE loja.Cliente SET idCarrinho = %s WHERE idCliente = %s", (id_carrinho, id_cliente))

        # Inserir a lista de desejos para o cliente
        comando.execute("INSERT INTO loja.ListaDeDesejos DEFAULT VALUES RETURNING idListaDesejos")
        id_lista_desejos = comando.fetchone()[0]

        # Atualizar o cliente com o ID da lista de desejos
        comando.execute("UPDATE loja.Cliente SET idListaDesejos = %s WHERE idCliente = %s",
                        (id_lista_desejos, id_cliente))

        # Commit das operações no banco de dados
        db_connection.commit()

        # Fechar o cursor
        comando.close()

        return jsonify({'message': 'Usuário criado com sucesso!'}), 201

    except Exception as e:
        # Em caso de erro, rollback da transação e retorno de mensagem de erro
        db_connection.rollback()
        return jsonify({'error': str(e)}), 500


# Rota para atualizar dados de cliente
@app.route('/atualizar_dados_cliente', methods=['POST'])
def atualizar_dados_cliente():
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("UPDATE loja.cliente SET nome=%s, cpf=%s, telefoneContato=%s, genero=%s WHERE idCliente = %s",
                    (data['nome'], data['cpf'], data['telefoneContato'],
                     data['genero'], data['idCliente']))

    db_connection.commit()
    comando.close()

    return "1"


# rota para atualizar email do cliente
@app.route('/atualizar_email_cliente', methods=['POST'])
def atualizar_email_cliente():
    data = request.get_json()

    comando = db_connection.cursor()
    try:
        comando.execute("UPDATE loja.cliente SET email=%s WHERE idCliente = %s",
                        (data['emailNovo'], data['idCliente']))

        db_connection.commit()
        comando.close()
        return jsonify({'message': 'Email atualizado com sucesso!'}), 201

    except Exception as e:
        # Em caso de erro, rollback da transação e retorno de mensagem de erro
        db_connection.rollback()
        return jsonify({'error': str(e)}), 500


# rota para atualizar senha do cliente
@app.route('/atualizar_senha_cliente', methods=['POST'])
def atualizar_senha_cliente():
    data = request.get_json()

    comando = db_connection.cursor()
    try:
        comando.execute("UPDATE loja.cliente SET senha = MD5(%s) WHERE idCliente = %s",
                        (data['senhaNova'], data['idCliente']))

        db_connection.commit()
        comando.close()
        return jsonify({'message': 'Senha atualizada com sucesso!'}), 201

    except Exception as e:
        # Em caso de erro, rollback da transação e retorno de mensagem de erro
        db_connection.rollback()
        return jsonify({'error': str(e)}), 500


# Rota para validar login
# retorna idCliente, ou erro caso email ou senha este estejam errados
@app.route('/validar_login_cliente', methods=['POST'])
def validar_login_cliente():
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("SELECT idCliente from loja.cliente WHERE email = %s and senha = MD5(%s)",
                    (data['email'], data['senha']))

    result = comando.fetchone()
    comando.close()

    if result:
        id_cliente = str(result[0])
        response = make_response(jsonify(result))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return id_cliente

    else:
        print(json.dumps({'message': 'Usuario nao encontrado.'}))
        response = make_response(json.dumps({'message': 'Dado nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return '-1'


# Rota para obter dados do cliente pelo id
@app.route('/get_cliente', methods=['POST'])
def get_cliente():
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("SELECT * FROM loja.cliente WHERE idCliente = %s", (data['idClienteLogado'],))
    result = comando.fetchone()
    comando.close()

    if result:
        print(result)
        cliente_dict = {
            'idCliente': result[0],
            'genero': result[1],
            'nome': result[2],
            'email': result[3],
            'senha': result[4],
            'cpf': result[5],
            'telefoneContato': result[6],
            'idListaDesejos': result[7],
            'idCarrinho': result[8],
            'idEnderecoPrincipal': result[9]
        }
        response = make_response(jsonify(cliente_dict))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Usuario nao encontrado.'}))
        response = make_response(json.dumps({'message': 'Dado nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return 'Erro desconhecido.'


# retorna todos os protudos da lista de desejos pelo idListaDesejos do cliente
@app.route('/get_lista_desejos', methods=['POST'])
def get_lista_desejos():
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("SELECT p.* FROM loja.ProdutoListaDesejos pld JOIN loja.Produto p ON pld.idProduto = p.idProduto "
                    "WHERE pld.idListaDesejos = %s", (data['idListaDesejos'],))
    results = comando.fetchall()
    comando.close()

    if results:
        for item in results:
            print(item)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Lista de desejos vazia.'}))
        response = make_response(json.dumps({'message': 'Dado nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response


# verifica se o produto esta na lista de desejos para manter icone atualizado
@app.route('/verificar_produto_lista_desejos', methods=['POST'])
def verificar_produto_lista_desejos():
    data = request.get_json()

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("SELECT * FROM loja.ProdutoListaDesejos WHERE idProduto = %s AND idListaDesejos = %s",
                    (data['idProduto'], data['idListaDesejos']))
    results = comando.fetchone()
    comando.close()

    if results:
        print(json.dumps({'message': 'Produto esta na lista de desejos.'}))
        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return "1"

    else:
        print(json.dumps({'message': 'Produto nao esta na lista de desejos.'}))
        response = make_response(json.dumps({'message': 'Dado nao encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return "0"


# Rota para adicionar produto na lista de desejos do cliente
@app.route('/adicionar_lista_desejos', methods=['POST'])
def adicionar_lista_desejos():
    data = request.get_json()

    idProduto = data['idProduto']
    idCliente = data['idCliente']

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("SELECT idListaDesejos FROM loja.cliente WHERE idCliente = %s", (idCliente,))
    idListaDesejos = comando.fetchone()[0]

    comando.execute("INSERT INTO loja.ProdutoListaDesejos (idProduto, idListaDesejos) VALUES (%s, %s)",
                    (idProduto, idListaDesejos))

    db_connection.commit()
    comando.close()

    print(json.dumps({'message': 'O produto foi adicionado a lista de desejos.'}))
    return "1"


# Rota para remover produto da lista de desejos do cliente
@app.route('/remover_lista_desejos', methods=['POST'])
def remover_lista_desejos():
    data = request.get_json()

    idProduto = data['idProduto']
    idCliente = data['idCliente']

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("SELECT idListaDesejos FROM loja.cliente WHERE idCliente = %s", (idCliente,))
    idListaDesejos = comando.fetchone()[0]

    comando.execute(
        "DELETE FROM loja.ProdutoListaDesejos WHERE idProduto = %s AND idListaDesejos = %s",
        (idProduto, idListaDesejos))

    db_connection.commit()
    comando.close()
    message = {'message': 'O produto foi removido da lista de desejos.'}
    print(json.dumps(message))
    return "1"


# Rota para buscar os endereços do cliente pelo id cliente
@app.route('/get_enderecos_cliente', methods=['POST'])
def get_enderecos_cliente():
    data = request.get_json()

    idClienteLogado = data['idClienteLogado']

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("SELECT * FROM loja.endereco WHERE idCliente = %s", (idClienteLogado,))
    results = comando.fetchall()
    comando.close()

    if results:
        for item in results:
            print(item)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Lista de enderecos vazia.'}))
        return "-1"


# Rota para adicionar endereço para o cliente
@app.route('/adicionar_endereco_cliente', methods=['POST'])
def adicionar_endereco_cliente():
    data = request.get_json()

    estado = data['estado']
    cidade = data['cidade']
    cep = data['cep']
    endereco = data['endereco']
    bairro = data['bairro']
    numero = data['numero']
    complemento = data['complemento']
    idCliente = data['idCliente']

    comando = db_connection.cursor()
    db_connection.rollback()

    try:
        comando.execute("""
            INSERT INTO loja.Endereco (estado, cidade, cep, endereco, bairro, numero, complemento, idCliente)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING idEndereco;
        """, (estado, cidade, cep, endereco, bairro, numero, complemento, idCliente))

        # Recuperar o ID do endereço recém-adicionado
        idEndereco = comando.fetchone()[0]

        comando.execute("""
            UPDATE loja.Cliente
            SET idEnderecoPrincipal = %s
            WHERE idCliente = %s;
        """, (idEndereco, idCliente))

        db_connection.commit()
        comando.close()
        print(json.dumps({'message': 'O endereco foi adicionado.'}))
        return "1"

    except Exception as e:
        if db_connection:
            db_connection.rollback()
        print(f"Erro desconhecido: {e}")
        return "-1"


@app.route('/remover_endereco_cliente', methods=['POST'])
def remover_endereco_cliente():
    data = request.get_json()

    idEndereco = data['idEndereco']
    idCliente = data['idCliente']

    comando = db_connection.cursor()
    db_connection.rollback()

    try:
        # Verificar se o endereço a ser removido é o principal do cliente
        comando.execute("""
            SELECT idEnderecoPrincipal FROM loja.Cliente WHERE idCliente = %s;
        """, (idCliente,))
        idEnderecoPrincipal = comando.fetchone()[0]

        if idEnderecoPrincipal == idEndereco:
            # Se for o endereço principal, atualize o cliente para não ter endereço principal
            comando.execute("""
                UPDATE loja.Cliente
                SET idEnderecoPrincipal = null
                WHERE idCliente = %s;
            """, (idCliente,))

        # Remover o endereço
        comando.execute("""
            DELETE FROM loja.Endereco WHERE idEndereco = %s AND idCliente = %s;
        """, (idEndereco, idCliente))

        db_connection.commit()
        comando.close()
        print(json.dumps({'message': 'O endereco foi removido.'}))
        return "1"

    except Exception as e:
        if db_connection:
            db_connection.rollback()
        print(f"Erro desconhecido: {e}")
        return "-1"


@app.route('/atualizar_endereco_cliente', methods=['POST'])
def atualizar_endereco_cliente():
    data = request.get_json()

    estado = data['estado']
    cidade = data['cidade']
    cep = data['cep']
    endereco = data['endereco']
    bairro = data['bairro']
    numero = data['numero']
    complemento = data['complemento']
    idClienteLogado = data['idClienteLogado']
    idEnderecoSelecionado = data['idEnderecoSelecionado']
    tornarEnderecoPrincipal = data['tornarEnderecoPrincipal']

    comando = db_connection.cursor()
    db_connection.rollback()

    try:
        comando.execute("""
            UPDATE loja.Endereco
            SET estado = %s, cidade = %s, cep = %s, endereco = %s, bairro = %s, numero = %s, complemento = %s
            WHERE idEndereco = %s;
        """, (estado, cidade, cep, endereco, bairro, numero, complemento, idEnderecoSelecionado))

        # Se tornarEnderecoPrincipal for verdadeiro, atualizar idEnderecoPrincipal na tabela Cliente
        if tornarEnderecoPrincipal:
            comando.execute("""
                UPDATE loja.Cliente
                SET idEnderecoPrincipal = %s
                WHERE idCliente = %s;
            """, (idEnderecoSelecionado, idClienteLogado))

        db_connection.commit()
        comando.close()
        print(json.dumps({'message': 'O endereco foi atualizado.'}))
        return "1"

    except Exception as e:
        if db_connection:
            db_connection.rollback()
        print(f"Erro desconhecido: {e}")
        return "-1"


@app.route('/get_produtos_carrinho_cliente', methods=['POST'])
def get_produtos_carrinho_cliente():
    data = request.get_json()
    idcarrinho = data['idCarrinho']

    try:
        comando = db_connection.cursor()
        db_connection.rollback()

        # Consulta SQL para obter os produtos vinculados aos itens do carrinho
        comando.execute("""
            SELECT p.*
            FROM loja.item i
            JOIN loja.produto p ON i.idproduto = p.idProduto
            WHERE i.idcarrinho = %s
            ORDER BY i.idItem DESC
        """, (idcarrinho,))

        produtos = comando.fetchall()
        comando.close()

        if produtos:
            response = make_response(jsonify(produtos))
            response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
            return response
        else:
            print(json.dumps({'message': 'Carrinho vazio.'}))
            return "-1"

    except Exception as e:
        print(f"Erro ao obter produtos do carrinho: {e}")
        return jsonify({'message': 'Erro ao obter produtos do carrinho.'}), 500


# Rota para buscar os itens que estao no carrinho do cliente
@app.route('/get_itens_carrinho_cliente', methods=['POST'])
def get_itens_carrinho_cliente():
    data = request.get_json()

    idcarrinho = data['idCarrinho']

    comando = db_connection.cursor()
    db_connection.rollback()
    comando.execute("SELECT * FROM loja.item WHERE idcarrinho = %s ORDER BY idItem DESC", (idcarrinho,))
    results = comando.fetchall()
    comando.close()

    if results:
        for item in results:
            print(item)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        print(json.dumps({'message': 'Carrinho vazio.'}))
        return "-1"


# Rota para adicionar itens no carrinho do cliente
@app.route('/adicionar_item_carrinho', methods=['POST'])
def adicionar_item_carrinho():
    data = request.get_json()

    idProduto = data['idProduto']
    idCliente = data['idCliente']

    comando = db_connection.cursor()
    db_connection.rollback()

    try:
        # Verificar o estoque disponível do produto
        comando.execute(
            "SELECT estoqueProduto FROM loja.Produto WHERE idProduto = %s",
            (idProduto,))
        estoque = comando.fetchone()

        if not estoque:
            raise ValueError("Produto não encontrado")

        estoque_disponivel = estoque[0]

        # Verificar se o produto já está no carrinho do cliente
        comando.execute(
            "SELECT quantidade FROM loja.Item WHERE idProduto = %s AND idCarrinho = (SELECT idCarrinho FROM loja.Cliente WHERE idCliente = %s)",
            (idProduto, idCliente))
        registro = comando.fetchone()

        if registro:
            # Se o produto já está no carrinho, calcule a nova quantidade
            nova_quantidade = registro[0] + 1

            if nova_quantidade > estoque_disponivel:
                return "-1"

            comando.execute(
                "UPDATE loja.Item SET quantidade = %s WHERE idProduto = %s AND idCarrinho = (SELECT idCarrinho FROM loja.Cliente WHERE idCliente = %s)",
                (nova_quantidade, idProduto, idCliente))
        else:
            # Caso contrário, adicione o produto ao carrinho com quantidade 1
            if estoque_disponivel < 1:
                return "-1"

            comando.execute(
                "INSERT INTO loja.Item (idProduto, idCarrinho, quantidade) VALUES (%s, (SELECT idCarrinho FROM loja.Cliente WHERE idCliente = %s), %s)",
                (idProduto, idCliente, 1))

        db_connection.commit()
        return "1"
    except Exception as e:
        db_connection.rollback()
        print(f"Erro ao adicionar item ao carrinho: {e}")
        return "0"
    finally:
        comando.close()


@app.route('/remover_item_carrinho', methods=['POST'])
def remover_item_carrinho():
    data = request.get_json()

    idProduto = data['idProduto']
    idCliente = data['idCliente']

    comando = db_connection.cursor()
    db_connection.rollback()

    try:
        # Verificar se o produto está no carrinho do cliente
        comando.execute(
            "SELECT quantidade FROM loja.Item WHERE idProduto = %s AND idCarrinho = (SELECT idCarrinho FROM loja.Cliente WHERE idCliente = %s)",
            (idProduto, idCliente))
        registro = comando.fetchone()

        if not registro:
            return "-1"  # Produto não está no carrinho

        quantidade_atual = registro[0]

        if quantidade_atual == 1:
            return "-1"  # Se a quantidade for 1, retorna -1

        # Caso contrário, diminui a quantidade em 1
        nova_quantidade = quantidade_atual - 1

        comando.execute(
            "UPDATE loja.Item SET quantidade = %s WHERE idProduto = %s AND idCarrinho = (SELECT idCarrinho FROM loja.Cliente WHERE idCliente = %s)",
            (nova_quantidade, idProduto, idCliente))

        db_connection.commit()
        return "1"
    except Exception as e:
        db_connection.rollback()
        print(f"Erro ao remover item do carrinho: {e}")
        return "0"
    finally:
        comando.close()


# Rota para remover itens do carrinho do cliente
@app.route('/remover_produto_carrinho', methods=['POST'])
def remover_produto_carrinho():
    data = request.get_json()

    idProduto = data['idProduto']
    idCliente = data['idCliente']

    comando = db_connection.cursor()
    db_connection.rollback()

    try:
        # Verificar se o produto está no carrinho do cliente
        comando.execute(
            "SELECT COUNT(*) FROM loja.Item WHERE idProduto = %s AND idCarrinho = (SELECT idCarrinho FROM loja.Cliente WHERE idCliente = %s)",
            (idProduto, idCliente))
        produto_existente = comando.fetchone()[0]

        if produto_existente > 0:
            # Remover o produto do carrinho
            comando.execute(
                "DELETE FROM loja.Item WHERE idProduto = %s AND idCarrinho = (SELECT idCarrinho FROM loja.Cliente WHERE idCliente = %s)",
                (idProduto, idCliente))
            db_connection.commit()
            comando.close()
            return "1"
        else:
            comando.close()
            return "-1"
    except Exception as e:
        db_connection.rollback()
        print(f"Erro ao remover item do carrinho: {e}")
        return "-1"
    finally:
        comando.close()


# Rota para cadastrar uma venda e atualizar estoque dos produtos
@app.route('/cadastrar_venda', methods=['POST'])
def cadastrar_venda():
    try:
        data = request.get_json()

        # Extrair os dados da venda
        dataPedido = data['dataPedido']
        status = data['status']
        detalhesPedido = data['detalhesPedido']
        formaPagamento = data['formaPagamento']
        idCarrinho = data['idCarrinho']
        itensList = data['itensList']  # Lista de itens do carrinho

        comando = db_connection.cursor()
        db_connection.rollback()

        # Verificar se todos os itens têm estoque suficiente
        for item in itensList:
            idProduto = item['idProduto']
            quantidadeComprada = item['quantidade']

            # Obter o estoque atual do produto
            comando.execute("""
                SELECT estoqueProduto FROM loja.Produto WHERE idProduto = %s;
            """, (idProduto,))
            estoque_atual = comando.fetchone()[0]

            if estoque_atual < quantidadeComprada:
                return "-1"  # Retorna erro se algum item não tiver estoque suficiente

        # Inserir a venda na tabela Venda
        comando.execute("""
            INSERT INTO loja.Venda (dataPedido, status, detalhesPedido, formaPagamento, idCarrinho)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING idVenda;
        """, (dataPedido, status, detalhesPedido, formaPagamento, idCarrinho))

        # Limpar o carrinho do cliente
        comando.execute("""
            DELETE FROM loja.Item WHERE idCarrinho = %s;
        """, str(idCarrinho))

        # Atualizar os estoques dos produtos
        for item in itensList:
            idProduto = item['idProduto']
            quantidadeComprada = item['quantidade']

            # Obter o estoque atual do produto
            comando.execute("""
                SELECT estoqueProduto FROM loja.Produto WHERE idProduto = %s;
            """, (idProduto,))
            estoque_atual = comando.fetchone()[0]

            # Subtrair a quantidade comprada do estoque atual
            novo_estoque = estoque_atual - quantidadeComprada

            # Atualizar o estoque no banco de dados
            comando.execute("""
                UPDATE loja.Produto
                SET estoqueProduto = %s
                WHERE idProduto = %s;
            """, (novo_estoque, idProduto))

        db_connection.commit()
        comando.close()
        print(json.dumps({'message': 'Pedido realizado.'}))
        return "1"

    except Exception as e:
        if db_connection:
            db_connection.rollback()
        print(f"Erro desconhecido: {e}")
        return "-1"



# Rota para buscar os endereços do cliente pelo id cliente
@app.route('/get_pedidos_cliente', methods=['POST'])
def get_pedidos_cliente():
    data = request.get_json()

    idClienteLogado = data['idClienteLogado']

    comando = db_connection.cursor()
    db_connection.rollback()


    comando.execute("SELECT idCarrinho FROM loja.Cliente WHERE idCliente = %s", (idClienteLogado,))
    idCarrinho = comando.fetchone()

    if idCarrinho:
        # Buscar todos os pedidos relacionados ao idCarrinho do cliente
        comando.execute("SELECT * FROM loja.Venda WHERE idCarrinho = %s", (idCarrinho,))
        results = comando.fetchall()
        comando.close()

        if results:
            print(results)
            response = make_response(jsonify(results))
            response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
            return response
        else:
            print(json.dumps({'message': 'Nenhum pedido encontrado.'}))
            return "-1"

    else:
        comando.close()
        print(json.dumps({'message': 'Erro desconhecido.'}))
        return "-1"


@app.route('/get_produtos_filtro_intervalo', methods=['POST'])
def get_produtos_filtro_intervalo():

    data = request.get_json()
    intervaloValor = data['intervaloValor']

    # Definir os limites de preço com base no intervalo fornecido
    if intervaloValor == 'ate R$199':
        min_preco = 0
        max_preco = 199
    elif intervaloValor == 'de R$200 ate R$399':
        min_preco = 200
        max_preco = 399
    elif intervaloValor == 'de R$400 ate R$599':
        min_preco = 400
        max_preco = 599
    elif intervaloValor == 'acima de R$600':
        min_preco = 600
        max_preco = None
    else:
        return make_response(jsonify({'message': 'Intervalo de valor inválido.'}), 400)

    comando = db_connection.cursor()
    db_connection.rollback()

    # Construir a consulta SQL com base nos limites de preço
    if max_preco is not None:
        query = 'SELECT * FROM loja.produto WHERE (preco - (preco * desconto)) BETWEEN %s AND %s'
        params = (min_preco, max_preco)
    else:
        query = 'SELECT * FROM loja.produto WHERE (preco - (preco * desconto)) >= %s'
        params = (min_preco,)

    comando.execute(query, params)
    results = comando.fetchall()
    comando.close()

    if results:
        for item in results:
            print(item)

        response = make_response(jsonify(results))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response

    else:
        response = make_response(jsonify({'message': 'Nenhum produto encontrado.'}))
        response.headers['Access-Control-Allow-Origin'] = '*'  # Permitir solicitações de qualquer origem
        return response


if __name__ == '__main__':
    app.run(port=5000, host="localhost", debug=True)