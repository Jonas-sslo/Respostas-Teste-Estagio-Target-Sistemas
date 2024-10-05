sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

def faturamento_mensal():
    total_mensal = sp + rj + mg + es + outros
 
    sp_percentual = (sp/total_mensal) * 100
    rj_percentual = (rj/total_mensal) * 100
    mg_percentual = (mg/total_mensal) * 100
    es_percentual = (es/total_mensal) * 100
    outros_percentual = (outros/total_mensal) * 100
   
    print(
        f"""
        SP = {sp_percentual:.2f}%
        RJ = {rj_percentual:.2f}%
        MG = {mg_percentual:.2f}%
        ES = {es_percentual:.2f}%
        OUTROS = {outros_percentual:.2f}%
        """)
    return sp_percentual, rj_percentual, mg_percentual, es_percentual, outros_percentual

faturamento_mensal()