"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexitade (ruim)
"""

velocidade = 61  # velodidade atual do carro
local_carro = 101  # localaa em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # a distância onde o ragaar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and local_carro <= (
    LOCAL_1 + RADAR_RANGE
)

if velocidade_carro_passou_radar_1:
    print("Velocidade carro passou do radar 1")

if carro_passou_radar_1 and velocidade_carro_passou_radar_1:
    print("carro multado em radar 1")
