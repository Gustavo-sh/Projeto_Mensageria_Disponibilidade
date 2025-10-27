def checar_dados_disponibilidade(db):
    if db["resultado_m0_disponibilidade"] == "Sem dados":
        return {"Matricula": db["matricula"], "tipo": "Sem dados", "semana":db["semana"], "Mensagem": "Sem dados disponibilidade Mês Atual."}
    elif db["resultado_m1_disponibilidade"] == "Sem dados" and db["resultado_m2_disponibilidade"] == "Sem dados":
        return {"Matricula": db["matricula"], "tipo": "Sem dados", "semana":db["semana"], "Mensagem": "Sem dados disponibilidade Mês Anterior e dois Meses Atras."}
    return None

def to_float_percent(valor):
    try:
        return float(str(valor).replace("%", "").strip())
    except (TypeError, ValueError):
        return 0.0