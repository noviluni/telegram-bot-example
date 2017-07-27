import requests

def obtenirEquivalencia(quantitat, divisaEntrada, divisaSortida):
    p = {"base": divisaEntrada}
    url = "http://api.fixer.io/latest"

    resposta = requests.get(url, params=p)
    tipusCanvi = resposta.json()
    
    equivalencia = tipusCanvi["rates"][divisaSortida]
    total = float(equivalencia) * float(quantitat)
    resultat = str(quantitat)+" "+divisaEntrada+" equivalen a: "+str(total)+" "+divisaSortida
    return resultat

