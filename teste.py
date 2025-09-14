def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = [101, 102, 103, 104]

    # Entrada das reservas solicitadas
    reservas_solicitadas = [102, 105, 101, 103]

    # TODO: Crie o processamento das reservas:
    confirmadas = []
    recusadas = []

    # TODO: Verifique se cada reserva ;pode ser confirmada com base na disponibilidade dos quartos:
    for reserva in range(len(quartos_disponiveis)):
        if reservas_solicitadas in quartos_disponiveis:
            confirmadas.append(reservas_solicitadas)

        else:
            recusadas.append(reservas_solicitadas)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", " ".join(map(str, confirmadas)))
    print("Reservas recusadas:", " ".join(map(str, recusadas)))


# Chamada da função principal
processar_reservas()