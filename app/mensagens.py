from utils import to_float_percent, checar_dados_disponibilidade

def mensagem_semana_1(db):
    texto =  f"""
                Olá,  {db["nome"].split(" ")[0]}! 😊
                Eu sou o Robby e tô passando pra dar uma noticia super legal! Você está participando do Robby ON na Disponibilidade, criado para apoiar sua evolução no indicador de % de Disponibilidade.
                No último mês, seu resultado foi {db["resultado_m1_disponibilidade"]}, e nos últimos períodos ele apareceu entre G3 e G4.
                A partir de agora, vamos trabalhar juntos para melhorar isso com constância 💪
                Toda semana eu vou te enviar aqui na Robbyson dicas rápidas + um resumo da sua evolução.
                E sempre que precisar, chama seu supervisor: ele é seu parceiro nesse processo🤝
                Conta comigo,
                Robby
            """
    return {"Matricula": db["matricula"], "tipo": "abertura", "semana":db["semana"], "Mensagem": texto}

def mensagem_semanas_2_3_4(db):
    texto = None
    tipo = None
    evoluiu_porcentagem = None
    checar_dados = checar_dados_disponibilidade(db)
    if checar_dados is not None:
        return checar_dados
    if db["resultado_m1_disponibilidade"] == "Sem dados":
        evoluiu_porcentagem = to_float_percent(db["resultado_m0_disponibilidade"]) > to_float_percent(db["resultado_m2_disponibilidade"])
    else:
        evoluiu_porcentagem = to_float_percent(db["resultado_m0_disponibilidade"]) > to_float_percent(db["resultado_m1_disponibilidade"])
    if evoluiu_porcentagem:
        texto = f"""
        Fala, {db["nome"].split(" ")[0]}! 🎉
        Boa! Acredita que você evoluiu sua % de Disponibilidade em relação ao mês anterior? Parabéns pelo seu esforço! 👏
        Mês anterior: {db["resultado_m1_disponibilidade"]}
        Mês atual: {db["resultado_m0_disponibilidade"]}
        Pra manter a subida, confere os pilares da sua disponibilidade:
        Tempo logado — Meta: {db["meta_tempo_logado"]} | Atual: {db["resultado_tempo_logado"]}
        Pausa NR17 — Meta: {db["meta_nr17"]} | Atual: {db["resultado_nr17"]}
        ABS — Meta: {db["meta_abs"]} | Atual: {db["resultado_abs"]}
        Seu próximo nível é repetir o que funcionou e ajustar o que ainda oscila 🔎
        Sigo te acompanhando por aqui 🚀
        Robby
                """
        tipo = "evolucao"
    else:
        texto = f"""
        Olá, {db["nome"].split(" ")[0]}!
        Vi aqui que sua % de Disponibilidade não evoluiu em relação ao mês anterior. Bora ajustar a rota juntos?
        Mês anterior: {db["resultado_m1_disponibilidade"]}
        Mês atual: {db["resultado_m0_disponibilidade"]}
        Pra encontrar a alavanca mais rápida, confere os componentes:
        Tempo logado — Meta: {db["meta_tempo_logado"]} | Atual: {db["resultado_tempo_logado"]}
        Pausa NR17 — Meta: {db["meta_nr17"]} | Atual: {db["resultado_nr17"]}
        ABS — Meta: {db["meta_abs"]} | Atual: {db["resultado_abs"]}
        Escolhe 1 ponto pra atacar primeiro 🎯 (o que estiver mais distante da meta costuma dar ganho mais rápido). Se quiser, chama seu supervisor pra montar um plano simples de 7 dias 🤝
        Tamo junto,
        Robby
                """
        tipo = "involucao"
    return {"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": texto}

def mensagem_semana_5(db):
    texto = None
    tipo = None
    evoluiu_grupo = False
    if db["resultado_m0_disponibilidade"] != "Sem dados":
        if db["grupo"] == 3 and float(db["resultado_m0_disponibilidade"].replace("%", "")) >= 94:
            evoluiu_grupo = True
        else:
            evoluiu_grupo = True if float(db["resultado_m0_disponibilidade"].replace("%", "")) >= 84.6 else False
    evoluiu_porcentagem = None
    checar_dados = checar_dados_disponibilidade(db)
    if checar_dados is not None:
        return checar_dados
    if db["resultado_m1_disponibilidade"] == "Sem dados":
        evoluiu_porcentagem = to_float_percent(db["resultado_m0_disponibilidade"]) > to_float_percent(db["resultado_m2_disponibilidade"]) if db["resultado_m0_disponibilidade"] != "Sem dados" else False
    else:
        evoluiu_porcentagem = to_float_percent(db["resultado_m0_disponibilidade"]) > to_float_percent(db["resultado_m1_disponibilidade"]) if db["resultado_m0_disponibilidade"] != "Sem dados" else False

    if evoluiu_grupo and evoluiu_porcentagem:
        texto = f"""
        Ei, {db["nome"].split(" ")[0]}! 🎉
        Encerramos o ciclo do Robby ON e seu resultado melhorou na % de Disponibilidade, e melhor: você virou de grupo!! 🏆
        M-2: {db["resultado_m2_disponibilidade"]}
        M-1: {db["resultado_m1_disponibilidade"]}
        Isso mostra que seu esforço teve impacto real.
        Neste momento, você não precisa seguir no próximo ciclo de acompanhamento 🙌
        Seu desafio agora é simples: manter o padrão que te trouxe até aqui 💻
        Parabéns!
        Robby
        """
        tipo = r"evolucao % e grupo"
    elif evoluiu_porcentagem:
        texto = f"""
        Fala, {db["nome"].split(" ")[0]}! 🙌
        Fechamos o ciclo do Robby ON e eu vi sua evolução na % de Disponibilidade — parabéns pela dedicação! 👏
        M-2: {db["resultado_m2_disponibilidade"]}
        M-1: {db["resultado_m1_disponibilidade"]}
        Mesmo com a melhora, você ainda aparece em G3/G4 por enquanto. E isso não é rótulo, é só o ponto de partida do próximo ciclo, tá? Vamos seguir juntos até você virar de grupo 💪
        Conta comigo,
        Robby
        """
        tipo = r"evolucao %"
    else:
        texto = f"""
        Olá, {db["nome"].split(" ")[0]}!
        Encerramos o Robby ON e identificamos que, neste ciclo, seu resultado de % de Disponibilidade não evoluiu em relação ao mês anterior.
        Resultado (mês M-2): {db["resultado_m2_disponibilidade"]} Disponibilidade
        Resultado (mês M-1): {db["resultado_m1_disponibilidade"]} Disponibilidade
        Sei que desafios acontecem 💭, mas é importante reforçar que a evolução nesse indicador é essencial para o seu crescimento dentro da operação.
        Por isso, você seguirá com a gente em um novo ciclo de acompanhamento até a sua melhoria.
        Conto com o seu comprometimento para transformar esse resultado 💪. Estamos juntos nesse propósito ✨. Abraços, Robby!
        """
        tipo = "involucao"
    return {"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": texto}