import streamlit as st
from models import Cliente, Pedido

# Função para exibir clientes e seus pedidos
def exibir_clientes():
    clientes = Cliente.get_all()
    for cliente in clientes:
        st.write(f"Cliente: {cliente.nome} (ID: {cliente.id_cliente})")
        pedidos = Pedido.get_all()=
        for pedido in pedidos:
            if pedido.id_cliente == cliente.id_cliente:
                st.write(f"- Pedido: {pedido.descricao} (ID: {pedido.id_pedido})")

# Função para o CRUD de Cliente
def cliente_crud():
    st.subheader("Cadastrar / Editar Cliente")
    nome_cliente = st.text_input("Nome do Cliente")
    cliente_id = st.text_input("ID do Cliente (deixe em branco para novo cliente)")
    if st.button("Salvar Cliente"):
        if cliente_id:  # Editar
            cliente = Cliente(id_cliente=int(cliente_id), nome=nome_cliente)
            cliente.save()
            st.success(f"Cliente ID {cliente_id} atualizado.")
        else:  # Criar
            cliente = Cliente(nome=nome_cliente)
            cliente.save()
            st.success(f"Novo Cliente {nome_cliente} criado.")

# Função para o CRUD de Pedido
def pedido_crud():
    st.subheader("Cadastrar / Editar Pedido")
    cliente_id = st.number_input("ID do Cliente", min_value=1)
    descricao_pedido = st.text_input("Descrição do Pedido")
    pedido_id = st.text_input("ID do Pedido (deixe em branco para novo pedido)")
    
    if st.button("Salvar Pedido"):
        if pedido_id:  # Editar
            pedido = Pedido(id_pedido=int(pedido_id), id_cliente=cliente_id, descricao=descricao_pedido)
            pedido.save()
            st.success(f"Pedido ID {pedido_id} atualizado.")
        else:  # Criar
            pedido = Pedido(id_cliente=cliente_id, descricao=descricao_pedido)
            pedido.save()
            st.success(f"Novo Pedido criado para o Cliente ID {cliente_id}.")

# Função principal
def main():
    st.title("Sistema CRUD de Clientes e Pedidos")
    
    # Operações CRUD
    st.sidebar.title("Operações CRUD")
    operacao = st.sidebar.radio("Escolha a operação", ("Cadastrar Cliente", "Cadastrar Pedido", "Visualizar Registros"))

    if operacao == "Cadastrar Cliente":
        cliente_crud()
    elif operacao == "Cadastrar Pedido":
        pedido_crud()
    else:
        exibir_clientes()

if __name__ == "__main__":
    main()
