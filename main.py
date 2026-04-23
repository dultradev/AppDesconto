from src.models.desconto import DescontoVIP
from src.models.pedidos import Pedido

if __name__ == "__main__":
    pedido = Pedido("Leonardo", DescontoVIP())
    print(f"Valor antes do set: {pedido._valor}")
    pedido.setValor = 100
    valor_final = pedido.getValor
    print(f"Valor final: {pedido._valor}")