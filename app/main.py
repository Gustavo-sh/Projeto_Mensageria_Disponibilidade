import datetime
import os
from conexoes_bd import get_resultados
import pandas as pd

mensagens = []

def mensagem_semana_1(db):
    texto =  f"""
                Olá, {db["matricula"]}! Você está participando do Programa de Desenvolvimento do Agente em Home Office (PDAH), 
                que tem o objetivo de apoiar sua evolução no indicador de % de Disponibilidade.
                Percebemos que o seu resultado tem se mantido em G4 há {db["reincidencia_disponibilidade"]} meses, 
                e no último mês você alcançou {db["resultado_m1_disponibilidade"]} em disponibilidade. 
                Nosso foco agora é trabalhar juntos para melhorar esse desempenho.
                Lembrando que, para permanecer no formato home office, o critério preferencial é estar entre G1 e G2 na Robbyson.
                Toda semana você receberá dicas e informativos de sua evolução via Robbyson. 
                Aproveite esse conteúdo e, sempre que precisar, procure seu supervisor — ele está à disposição para te apoiar nesse processo.
            """
    mensagens.append({"Matricula": db["matricula"], "tipo": "abertura", "semana":db["semana"], "Mensagem": texto})

def mensagem_semanas_2_3_4(db):
    texto = None
    tipo = None
    evoluiu_porcentagem = None
    if db["resultado_m0_disponibilidade"] == None:
        mensagens.append({"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": "Sem dados disponibilidade Mês Atual."})
        return 
    elif db["resultado_m1_disponibilidade"] == None and db["resultado_m2_disponibilidade"] == None:
        mensagens.append({"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": "Sem dados disponibilidade Mês Anterior e dois Meses Atras."})
        return 
    elif db["resultado_m1_disponibilidade"] == None:
        
        evoluiu_porcentagem = float(db["resultado_m0_disponibilidade"].replace("%", "")) > float(db["resultado_m2_disponibilidade"].replace("%", ""))
    else:
        evoluiu_porcentagem = float(db["resultado_m0_disponibilidade"].replace("%", "")) > float(db["resultado_m1_disponibilidade"].replace("%", ""))
    if evoluiu_porcentagem:
        texto = f"""
        Olá, {db["matricula"]}!
        Parabéns! Ficamos muito felizes em ver que você evoluiu o seu resultado de % de Disponibilidade em relação ao mês anterior. Seu empenho está fazendo a diferença — continue assim! 
        Resultado mês anterior: {db["resultado_m1_disponibilidade"]} Disponibilidade
        Resultado atual: {db["resultado_m0_disponibilidade"]} Disponibilidade
        Veja como estão os indicadores que compõem a sua disponibilidade:
        Tempo Logado – Meta: {db["meta_tempo_logado"]} | Resultado atual: {db["resultado_tempo_logado"]}
        Pausa NR17 – Meta: {db["meta_nr17"]} | Resultado atual: {db["resultado_nr17"]}
        ABS – Meta: {db["meta_abs"]} | Resultado atual: {db["resultado_abs"]}
        Mantenha o foco e siga cuidando dos detalhes que te fizeram evoluir. Cada melhoria conta e mostra o quanto seu comprometimento tem dado resultado.
        Continue nessa trajetória, estamos torcendo por você!
                """
        tipo = "evolucao"
    else:
        texto = f"""
        Olá, {db["matricula"]}!
        Poxa, percebemos que ainda não houve evolução no seu resultado de % de Disponibilidade em relação ao mês anterior. Vamos juntos entender onde podemos melhorar?
        Resultado mês anterior: {db["resultado_m1_disponibilidade"]} Disponibilidade
        Resultado atual: {db["resultado_m0_disponibilidade"]} Disponibilidade
        Confira abaixo os indicadores que compõem a mensuração da disponibilidade:
        Tempo Logado – Meta: {db["meta_tempo_logado"]} | Resultado atual: {db["resultado_tempo_logado"]}
        Pausa NR17 – Meta: {db["meta_nr17"]} | Resultado atual: {db["resultado_nr17"]}
        ABS – Meta: {db["meta_abs"]} | Resultado atual: {db["resultado_abs"]}
        Observe onde estão suas maiores oportunidades e concentre seus esforços nesses pontos — pequenas melhorias podem gerar uma grande diferença no resultado final.
        Em caso de dúvidas ou se precisar de apoio, procure seu supervisor. Estamos aqui para te ajudar nesse processo de evolução! 
                """
        tipo = "involucao"
    mensagens.append({"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": texto})

def mensagem_semana_5(db):
    texto = None
    tipo = None
    evoluiu_grupo = float(db["resultado_m0_disponibilidade"].replace("%", "")) >= float(84.6)
    evoluiu_porcentagem = None
    if db["resultado_m0_disponibilidade"] == None:
        mensagens.append({"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": "Sem dados disponibilidade Mês Atual."})
        return 
    elif db["resultado_m1_disponibilidade"] == None and db["resultado_m2_disponibilidade"] == None:
        mensagens.append({"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": "Sem dados disponibilidade Mês Anterior e dois Meses Atras."})
        return 
    elif db["resultado_m1_disponibilidade"] == None:
        
        evoluiu_porcentagem = float(db["resultado_m0_disponibilidade"].replace("%", "")) > float(db["resultado_m2_disponibilidade"].replace("%", ""))
    else:
        evoluiu_porcentagem = float(db["resultado_m0_disponibilidade"].replace("%", "")) > float(db["resultado_m1_disponibilidade"].replace("%", ""))

    if evoluiu_grupo and evoluiu_porcentagem:
        texto = f"""
        Olá, {db["matricula"]}!
        Parabéns! Estamos concluindo o Programa de Desenvolvimento do Agente em Home Office (PDAH) e ficamos muito felizes em ver a sua evolução no indicador de % de Disponibilidade em relação ao mês anterior.
        Resultado (mês M-2): {db["resultado_m2_disponibilidade"]} Disponibilidade
        Resultado (mês M-1): {db["resultado_m1_disponibilidade"]} Disponibilidade
        Resultado (mês M-0): {db["resultado_m0_disponibilidade"]} Disponibilidade
        Seu empenho trouxe resultado e você evoluiu de grupo, o que mostra o quanto seu comprometimento fez diferença. 
        Por isso, não será necessário participar de um novo ciclo do PDAH neste momento, continue se dedicando e mantendo essa boa performance.
        Parabéns pela conquista e siga firme nessa trajetória de evolução!
        """
        tipo = r"evolucao % e grupo"
    elif evoluiu_porcentagem:
        texto = f"""
        Olá, {db["matricula"]}!
        Parabéns pela sua dedicação! Estamos concluindo o Programa de Desenvolvimento do Agente em Home Office (PDAH) e identificamos que você evoluiu seu resultado de % de Disponibilidade em relação ao mês anterior.
        Resultado (mês M-2): {db["resultado_m2_disponibilidade"]} Disponibilidade
        Resultado (mês M-1): {db["resultado_m1_disponibilidade"]} Disponibilidade
        Resultado (mês M-0): {db["resultado_m0_disponibilidade"]} Disponibilidade
        Mesmo com essa melhora, você ainda permanece em G4 no indicador, mas não se preocupe, vamos continuar juntos nesse processo até que você avance de grupo. Conte com o nosso apoio para seguir evoluindo a cada ciclo! 
        """
        tipo = r"evolucao %"
    else:
        texto = f"""
        Olá, {db["matricula"]}!
        Encerramos o Programa de Desenvolvimento do Agente em Home Office (PDAH) e identificamos que, neste ciclo, seu resultado de % de Disponibilidade não evoluiu em relação ao mês anterior.
        Resultado (mês M-2): {db["resultado_m2_disponibilidade"]} Disponibilidade
        Resultado (mês M-1): {db["resultado_m1_disponibilidade"]} Disponibilidade
        Resultado (mês M-0): {db["resultado_m0_disponibilidade"]} Disponibilidade
        Sabemos que desafios acontecem, mas é importante reforçar que a evolução nesse indicador é essencial para a permanência no formato home office e para o seu crescimento dentro da operação. Por isso, você seguirá com a gente em um novo ciclo do PDAH, com acompanhamento mais próximo para apoiar sua melhoria.
        Contamos com o seu comprometimento para transformar esse resultado no próximo mês. Estamos juntos nesse propósito! 
        """
        tipo = "involucao"
    mensagens.append({"Matricula": db["matricula"], "tipo": tipo, "semana":db["semana"], "Mensagem": texto})

def main():
    resultados = get_resultados()
    for matricula, dados in resultados.items():

        db = {"matricula": matricula, "resultado_m0_disponibilidade": dados["Resultado_M0_Disp"], "resultado_m1_disponibilidade": dados["Resultado_M1_Disp"], 
              "resultado_m2_disponibilidade": dados["Resultado_M2_Disp"], "reincidencia_disponibilidade": dados["MReincidente_Disponibilidade"],
              "resultado_tempo_logado": dados["Resultado_Tempo_Logado"], "meta_tempo_logado": dados["Meta_Tempo_Logado"], "resultado_nr17": dados["Resultado_NR17"], "meta_nr17": dados["Meta_NR17"], 
              "resultado_abs": dados["Resultado_ABS"], "meta_abs": dados["Meta_ABS"], "semana": 5}
        
        if db["semana"] == 1:
            mensagem_semana_1(db)
        elif db["semana"] == 2 or db["semana"] == 3 or db["semana"] == 4:
            mensagem_semanas_2_3_4(db)
        elif db["semana"] == 5:
            mensagem_semana_5(db)
        
    df_mensagens = pd.DataFrame(mensagens)
    caminho_arquivo = os.path.join(os.getcwd(), "mensagens_geradas.xlsx")
    df_mensagens.to_excel(caminho_arquivo, index=False)

if __name__ == "__main__":
    main()