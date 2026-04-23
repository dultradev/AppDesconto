from src.services.pedido_service import PedidoService
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium 
from src.models.pedidos import Pedido
if __name__ == "__main__":
    pedido = Pedido("Leonardo", DescontoVIP())
    print(f"Valor antes do set: {pedido._valor}")
    pedido.setValor = 100
    valor_final = pedido.getValor
    print(f"Valor final: {pedido._valor}")

    service = PedidoService()
    """Criando pedidos e aplicando descontos"""
    pedido1 = Pedido("Cliente A" , DescontoNormal ())
    pedido1.setValor = 100.0 # Definindo o valor original do pedido
    pedido2 = Pedido("cliente B", DescontoVIP())
    pedido2.setValor = 200.0 # Definindo o valor original do pedido
    pedido3 = Pedido("cliente C", DescontoPremium())
    pedido3.setValor= 300.0 # Definindo o valor original do pedido
    # Aqui você pode criar pedidos, aplicar descontos e processar os pedidos service. adicionar_pedido(pedido1) service.adicionar_pedido(pedido2) service. adicionar_pedido(pedido3)


    service.adicionar_pedido(pedido1) 
    service.adicionar_pedido(pedido2) 
    service. adicionar_pedido(pedido3)

    service.processar_pedidos()