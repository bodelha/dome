import numpy as np
import json
from datetime import datetime, timedelta

# Configurações iniciais para 3 meses retroativos
end_date = datetime.now()  # Data final no momento atual
start_date = end_date - timedelta(days=90)  # Data inicial para 3 meses atrás

# Inicializando lista de dados
data = []

# Gerar dados por minuto ao longo dos três meses
current_date = start_date
while current_date <= end_date:
    # Determinar o mês e ajustar as médias para temperatura e umidade
    month_idx = (current_date.month - start_date.month) % 3

    # Temperatura e umidade externa com variação aleatória
    temp_external_avg = [24, 27, 25]  # Temperaturas médias para cada mês
    humidity_external_avg = [70, 75, 80]  # Umidade média para cada mês
    temp_external = temp_external_avg[month_idx] + np.random.normal(0, 2)
    humidity_external = humidity_external_avg[month_idx] + np.random.normal(0, 5)

    # Luminosidade simulada com mais variabilidade, incluindo nuvens e intensidade
    hour = current_date.hour
    if 6 <= hour < 18:  # Período diurno
        # A luminosidade varia de forma mais fluida durante o dia
        base_luminosity = np.random.uniform(0.3, 1)  # Luminosidade variável durante o dia
        # Simula uma chance de nuvens mais densas reduzindo a luminosidade
        if np.random.rand() < 0.2:  # 20% de chance de nuvens densas
            luminosity = base_luminosity * np.random.uniform(0.2, 0.5)
        else:
            luminosity = base_luminosity
    else:  # Período noturno
        luminosity = 0  # Durante a noite, a luminosidade é zero

    # Temperatura interna (baseada na externa mais variação relacionada à luminosidade)
    temp_internal = temp_external + np.random.uniform(5, 15)  # Temperatura interna sempre mais quente

    # Umidade interna (deve ser um pouco mais baixa que a umidade externa)
    humidity_internal = humidity_external - np.random.uniform(10, 25)

    # Adicionar linha de dados simulados com timestamp em Unix (epoch)
    data.append({
        "time": int(current_date.timestamp()),
        "externalTemperature": temp_external,
        "externalHumidity": humidity_external,
        "internalTemperature": temp_internal,
        "internalHumidity": humidity_internal,
        "luminosity": luminosity,
        "batteryLevel": 100.0  # Supondo nível de bateria máximo
    })

    # Avança para o próximo minuto
    current_date += timedelta(minutes=1)

# Salvar como arquivo JSON
with open('dados_mockados_estufa_franca.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
