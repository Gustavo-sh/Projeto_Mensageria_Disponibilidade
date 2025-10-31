from utils import to_float_percent, checar_dados_disponibilidade

def mensagem_semana_1(db):
    texto =  f"""
                Olá, {db["nome"].split(" ")[0]}! 😊
                Você está participando do <b>Programa de Desenvolvimento do Agente em Home Office (PDAH)</b>, que tem o objetivo de <b>apoiar sua evolução no indicador de % Disponibilidade</b>.
                Percebemos que o seu resultado tem se mantido em <b>G4 há {db["reincidencia_disponibilidade"]} meses</b>, e no último mês você alcançou <b>{db["resultado_m1_disponibilidade"]} em disponibilidade</b>. Nosso foco agora é <b>trabalhar juntos para melhorar esse desempenho</b> 💪.
                Lembrando que, para permanecer no formato <b>home office</b>, o critério preferencial é <b>estar entre G1 e G2 no Robbyson</b> 🏠.
                Toda semana você receberá <b>dicas e informativos de sua evolução via Robbyson</b> 📈. Aproveite esse conteúdo e, sempre que precisar, <b>procure seu supervisor</b>, ele está à disposição para te apoiar nesse processo 🤝.
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
        Olá, {db["nome"].split(" ")[0]}! 🎉  
        <b>Parabéns!</b> Ficamos muito felizes em ver que você <b>evoluiu o seu resultado de % Disponibilidade</b> em relação ao mês anterior 🌟. Seu empenho está fazendo a diferença e <b>você está no caminho certo</b> 👏.  

        <b>Resultado mês anterior:</b> {db["resultado_m1_disponibilidade"]} Disponibilidade  
        <b>Resultado atual:</b> {db["resultado_m0_disponibilidade"]} Disponibilidade  

        Veja como estão os indicadores que compõem a sua disponibilidade:  
        <b>Tempo Logado – Meta:</b> {db["meta_tempo_logado"]} | <b>Resultado atual:</b> {db["resultado_tempo_logado"]}  
        <b>Pausa NR17 – Meta:</b> {db["meta_nr17"]} | <b>Resultado atual:</b> {db["resultado_nr17"]}  
        <b>ABS – Meta:</b> {db["meta_abs"]} | <b>Resultado atual:</b> {db["resultado_abs"]}  

        Mantenha o foco e siga cuidando dos detalhes que te fizeram evoluir 🔎. Cada melhoria conta e mostra o quanto <b>seu comprometimento tem dado resultado</b> 💪.  
        <b>Continue nessa trajetória, estamos torcendo por você!</b> 🚀
                """
        tipo = "evolucao"
    else:
        texto = f"""
        Olá, {db["nome"].split(" ")[0]}! 📍  
        Poxa, percebemos que <b>ainda não houve evolução no seu resultado de % Disponibilidade</b> em relação ao mês anterior 😕. Vamos juntos entender onde podemos melhorar? 💬  

        <b>Resultado mês anterior:</b> {db["resultado_m1_disponibilidade"]} Disponibilidade  
        <b>Resultado atual:</b> {db["resultado_m0_disponibilidade"]} Disponibilidade  

        Confira abaixo os indicadores que compõem a mensuração da disponibilidade:  
        <b>Tempo Logado – Meta:</b> {db["meta_tempo_logado"]} | <b>Resultado atual:</b> {db["resultado_tempo_logado"]}  
        <b>Pausa NR17 – Meta:</b> {db["meta_nr17"]} | <b>Resultado atual:</b> {db["resultado_nr17"]}  
        <b>ABS – Meta:</b> {db["meta_abs"]} | <b>Resultado atual:</b> {db["resultado_abs"]}  

        Observe onde estão <b>suas maiores oportunidades</b> e concentre seus esforços nesses pontos 🎯. Pequenas melhorias podem gerar <b>grande diferença no resultado final</b>.  

        Em caso de dúvidas ou se precisar de apoio, <b>procure seu supervisor</b> 🤝. Estamos aqui para <b>te ajudar nesse processo de evolução</b> 💪.
                """
        tipo = "involucao"
    return {"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": texto}

def mensagem_semana_5(db):
    texto = None
    tipo = None
    evoluiu_grupo = float(db["resultado_m0_disponibilidade"].replace("%", "")) >= 84.6
    evoluiu_porcentagem = None
    checar_dados = checar_dados_disponibilidade(db)
    if checar_dados is not None:
        return checar_dados
    if db["resultado_m1_disponibilidade"] == "Sem dados":
        evoluiu_porcentagem = to_float_percent(db["resultado_m0_disponibilidade"]) > to_float_percent(db["resultado_m2_disponibilidade"])
    else:
        evoluiu_porcentagem = to_float_percent(db["resultado_m0_disponibilidade"]) > to_float_percent(db["resultado_m1_disponibilidade"])

    if evoluiu_grupo and evoluiu_porcentagem:
        texto = f"""
        Olá, {db["nome"].split(" ")[0]}! 🎉  
        <b>Parabéns!</b> Estamos concluindo o <b>*PDAH*</b> e ficamos muito felizes em ver <b>sua evolução no indicador de % Disponibilidade</b> em relação ao mês anterior ⬆.  

        <b>Resultado (mês M-2):</b> {db["resultado_m2_disponibilidade"]} Disponibilidade  
        <b>Resultado (mês M-1):</b> {db["resultado_m1_disponibilidade"]} Disponibilidade  

        Seu empenho trouxe resultado e você <b>evoluiu de grupo</b> 🏆, o que mostra o quanto <b>seu comprometimento fez diferença</b>.  
        Por isso, <b>não será necessário participar de um novo ciclo do PDAH neste momento</b> 🙌.  
        Continue se dedicando e mantendo <b>essa boa performance</b> 💻.  

        <b>Parabéns pela conquista e siga firme nessa trajetória de evolução</b> 🌟.
        """
        tipo = r"evolucao % e grupo"
    elif evoluiu_porcentagem:
        texto = f"""
        Olá, {db["nome"].split(" ")[0]}! 🙌  
        <b>Parabéns pela sua dedicação!</b> 👏  
        Estamos concluindo o <b>Programa de Desenvolvimento do Agente em Home Office (PDAH)</b> e identificamos que você <b>evoluiu seu resultado de % Disponibilidade</b> em relação ao mês anterior 🌟.  

        <b>Resultado (mês M-2):</b> {db["resultado_m2_disponibilidade"]} Disponibilidade  
        <b>Resultado (mês M-1):</b> {db["resultado_m1_disponibilidade"]} Disponibilidade  

        Mesmo com essa melhora, você ainda permanece <b>em G4</b> no indicador ⚙, mas <b>não se preocupe</b>, vamos continuar juntos nesse processo até que você <b>avance de grupo</b> 💪.  
        Conte com o nosso apoio para <b>seguir evoluindo a cada ciclo</b> 🚀.
        """
        tipo = r"evolucao %"
    else:
        texto = f"""
        Olá, {db["nome"].split(" ")[0]}! 📍  
        Encerramos o <b>Programa de Desenvolvimento do Agente em Home Office (PDAH)</b> 🏠 e identificamos que, neste ciclo, <b>seu resultado de % Disponibilidade não evoluiu</b> em relação ao mês anterior 📉.  

        <b>Resultado (mês M-2):</b> {db["resultado_m2_disponibilidade"]} Disponibilidade  
        <b>Resultado (mês M-1):</b> {db["resultado_m1_disponibilidade"]} Disponibilidade  

        Sabemos que desafios acontecem 💭, mas é importante reforçar que <b>a evolução nesse indicador é essencial para a permanência no formato home office e para o seu crescimento dentro da operação</b> 🌱.  

        Por isso, você <b>seguirá com a gente em um novo ciclo do PDAH</b>, com <b>acompanhamento mais próximo</b> para apoiar sua melhoria 🤝.  
        Contamos com o seu <b>comprometimento para transformar esse resultado</b> 💪.  
        Estamos juntos nesse <b>propósito</b> ✨.
        """
        tipo = "involucao"
    return {"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": texto}