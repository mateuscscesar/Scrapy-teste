import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    cpf = input("Digite o cpf da certidao:\n")

    start_urls = [
        "http://servicos.receita.fazenda.gov.br/Servicos/certidao/CNDConjuntaSegVia/ResultadoSegVia.asp?Origem=1&Tipo=2&NI=%s&Senha=" %cpf 
    ]

    def parse(self, response):
        self.log("ACESSANDO URL: %s" % response.url)

        page = response.url.split("/")[-2]
        filename = 'quotes-%s.pdf' % page
        with open(filename, 'wb') as f: #testar tirando o b
            f.write(response.body.decode("utf-8"))
        self.log('Saved file %s' % filename)
        