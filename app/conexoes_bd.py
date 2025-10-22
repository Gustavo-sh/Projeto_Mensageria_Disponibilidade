import pyodbc
CONNECTION_STRING = "Driver={SQL Server};Server=primno4;Database=Robbyson;Trusted_Connection=yes;"
SCRIPT = f"""
        select chave_externa, 
        FORMAT(resultado_m0_disp, 'P') as Resultado_M0_Disponibilidade, 
        FORMAT(resultado_m1_disp, 'P') as Resultado_M1_Disponibilidade, 
        FORMAT(resultado_m2_disp, 'P') as Resultado_M2_Disponibilidade,
        FORMAT(meta_disp, 'P') as Meta_Disponibilidade,
        mreincidente_disponibilidade, 
        FORMAT(DATEADD(second, resultado_tempo_logado, '00:00:00'), 'HH:mm:ss') as Resultado_Tempo_Logado, 
        FORMAT(DATEADD(second, meta_tempo_logado, '00:00:00'), 'HH:mm:ss') as Meta_Tempo_Logado,
        FORMAT(DATEADD(second, resultado_nr17, '00:00:00'), 'HH:mm:ss') as resultado_nr17, 
        FORMAT(DATEADD(second, meta_nr17, '00:00:00'), 'HH:mm:ss') as meta_nr17, 
        FORMAT(resultado_abs, 'P') as Resultado_ABS, 
        FORMAT(meta_abs, 'P') as Meta_ABS,
        semana
        from rlt.MensageriaDisponibilidade
    """

def get_resultados():
    conn = pyodbc.connect(CONNECTION_STRING, timeout=20)
    cur = conn.cursor()
    cur.execute(SCRIPT)
    rows = cur.fetchall()
    resultados = {
        i[0]: {
            "Resultado_M0_Disp": i[1],
            "Resultado_M1_Disp": i[2],
            "Resultado_M2_Disp": i[3],
            "Meta_Disp": i[4],
            "MReincidente_Disponibilidade": i[5],
            "Resultado_Tempo_Logado": i[6],
            "Meta_Tempo_Logado": i[7],
            "Resultado_NR17": i[8],
            "Meta_NR17": i[9],
            "Resultado_ABS": i[10],
            "Meta_ABS": i[11],
            "Semana": i[12]
        }
    for i in rows} 

    cur.close()
    conn.close()
    return resultados