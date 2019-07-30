import urllib.request
import urllib.parse

def frete(cod, GOCEP, HERECEP, peso, formato, comprimento, altura, largura, diametro, mao_propria='n',
          valor_declarado=0, aviso_recebimento='n', empresa='', senha='', toback='xml',IndicaCalculo=1):
    
    fields = {
        'nCdEmpresa': '',
        'sDsSenha': '',
        'nCdServico': cod,
        'sCepOrigem': HERECEP,
        'sCepDestino': GOCEP,
        'nVlPeso': peso,
        'nCdFormato': formato,
        'nVlComprimento': comprimento,
        'nVlAltura': altura,
        'nVlLargura': largura,
        'nVlDiametro': diametro,
        'sCdMaoPropria': mao_propria,
        'nVlValorDeclarado': valor_declarado,
        'sCdAvisoRecebimento': aviso_recebimento,
        'StrRetorno': toback,
        'nIndicaCalculo' : IndicaCalculo
        }

    params = urllib.parse.urlencode(fields)
    url = ("http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?"+params)
    f = urllib.request.urlopen(url)
    a = f.read()

    return a

# with a dictionary paramenter - the field order doesn't matter
fields = {
          "cod": "04510", 
          "GOCEP": "05821080",
          "HERECEP": "05425070",
          "peso": 1,
          "formato": 1, #1 - caixa/pacote #2 – Formato rolo/prisma #3 - Envelope
          "comprimento": 80,
          "altura": 50, 
          "largura": 20,
          "diametro": 0
          }

print (frete(**fields))