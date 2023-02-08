import requests


class Cotacao:
    def __init__(self):
        self.cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        self.cotacoes_dic = self.cotacoes.json()
        self.cotacao_dolar_br = self.cotacoes_dic["USDBRL"]["bid"]
        self.cotacao_euro_br = self.cotacoes_dic['EURBRL']['bid']
        self.cotacao_btc_br = self.cotacoes_dic['BTCBRL']['bid']

    def cotacao_dolar(self):
        print(self.cotacao_dolar_br)

    def cotacao_euro(self):
        print(self.cotacao_euro_br)

    def cotacao_btc(self):
        print(self.cotacao_btc_br)


c1 = Cotacao()
c1.cotacao_btc()
