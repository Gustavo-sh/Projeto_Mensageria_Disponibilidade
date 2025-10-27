from conexoes_bd import get_resultados
from mensagens import mensagem_semana_1, mensagem_semanas_2_3_4, mensagem_semana_5
from pathlib import Path
import pandas as pd

def main():
    resultados = get_resultados()
    mensagens = []
    for matricula, dados in resultados.items():

        db = {"matricula": matricula, "resultado_m0_disponibilidade": dados["Resultado_M0_Disp"], "resultado_m1_disponibilidade": dados["Resultado_M1_Disp"], 
              "resultado_m2_disponibilidade": dados["Resultado_M2_Disp"], "reincidencia_disponibilidade": dados["MReincidente_Disponibilidade"],
              "resultado_tempo_logado": dados["Resultado_Tempo_Logado"], "meta_tempo_logado": dados["Meta_Tempo_Logado"], "resultado_nr17": dados["Resultado_NR17"], "meta_nr17": dados["Meta_NR17"], 
              "resultado_abs": dados["Resultado_ABS"], "meta_abs": dados["Meta_ABS"], "semana": 5}
        
        for chave, valor in db.items():
            if valor == None:
                db[chave] = "Sem dados"

        if db["semana"] == 1:
            mensagens.append(mensagem_semana_1(db))
        elif db["semana"] == 2 or db["semana"] == 3 or db["semana"] == 4:
            mensagens.append(mensagem_semanas_2_3_4(db))
        elif db["semana"] == 5:
            mensagens.append(mensagem_semana_5(db))

    if not mensagens:
        print("⚠️ Nenhuma mensagem gerada — verifique os dados.")
        return
    df_mensagens = pd.DataFrame(mensagens)
    caminho_arquivo = Path.cwd() / "mensagens_geradas.xlsx"
    df_mensagens.to_excel(caminho_arquivo, index=False)
    print(f"✅ {len(mensagens)} mensagens geradas.")
    print(f"📄 Arquivo salvo em: {caminho_arquivo}")

if __name__ == "__main__":
    main()