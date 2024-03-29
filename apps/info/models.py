from django.db import models
from apps.client.models import Client

TIPO_ENDERECO = [
    ('UNI', 'Único'),
    ('RES', 'Residencial'),
    ('COM', 'Comercial'),
    ('COB', 'Cobrança'),
    ('ENT', 'Entrega'),
    ('OUT', 'Outro'),
]

UF_SIGLA = [
    ('AC', 'AC'),
    ('AL', 'AL'),
    ('AP', 'AP'),
    ('AM', 'AM'),
    ('BA', 'BA'),
    ('CE', 'CE'),
    ('DF', 'DF'),
    ('ES', 'ES'),
    ('EX', 'EX'),
    ('GO', 'GO'),
    ('MA', 'MA'),
    ('MT', 'MT'),
    ('MS', 'MS'),
    ('MG', 'MG'),
    ('PA', 'PA'),
    ('PB', 'PB'),
    ('PR', 'PR'),
    ('PE', 'PE'),
    ('PI', 'PI'),
    ('RJ', 'RJ'),
    ('RN', 'RN'),
    ('RS', 'RS'),
    ('RO', 'RO'),
    ('RR', 'RR'),
    ('SC', 'SC'),
    ('SP', 'SP'),
    ('SE', 'SE'),
    ('TO', 'TO'),
]

COD_UF = [
    ('12', 'AC'),
    ('27', 'AL'),
    ('16', 'AP'),
    ('13', 'AM'),
    ('29', 'BA'),
    ('23', 'CE'),
    ('53', 'DF'),
    ('32', 'ES'),
    ('EX', 'EX'),
    ('52', 'GO'),
    ('21', 'MA'),
    ('51', 'MT'),
    ('50', 'MS'),
    ('31', 'MG'),
    ('15', 'PA'),
    ('25', 'PB'),
    ('41', 'PR'),
    ('26', 'PE'),
    ('22', 'PI'),
    ('33', 'RJ'),
    ('24', 'RN'),
    ('43', 'RS'),
    ('11', 'RO'),
    ('14', 'RR'),
    ('42', 'SC'),
    ('35', 'SP'),
    ('28', 'SE'),
    ('17', 'TO'),
]

TIPO_TELEFONE = [
    ('FIX', "Fixo"),
    ('CEL', "Celular"),
    ('FAX', "Fax"),
    ('OUT', "Outro"),
]

BANCOS = [
    ('001', '001 - BANCO DO BRASIL S.A.'),
    ('003', '003 - BANCO DA AMAZONIA S.A.'),
    ('004', '004 - BANCO DO NORDESTE DO BRASIL S.A.'),
    ('012', '012 - BANCO STANDARD DE INVESTIMENTOS S.A.'),
    ('014', '014 - NATIXIS BRASIL S.A. BANCO MÚLTIPLO'),
    ('019', '019 - BANCO AZTECA DO BRASIL S.A.'),
    ('021', '021 - BANESTES S.A. BANCO DO ESTADO DO ESPIRITO SANTO'),
    ('024', '024 - BANCO DE PERNAMBUCO S.A. - BANDEPE'),
    ('025', '025 - BANCO ALFA S.A.'),
    ('029', '029 - BANCO BANERJ S.A.'),
    ('031', '031 - BANCO BEG S.A.'),
    ('033', '033 - BANCO SANTANDER (BRASIL) S.A.'),
    ('036', '036 - BANCO BRADESCO BBI S.A.'),
    ('037', '037 - BANCO DO ESTADO DO PARÁ S.A.'),
    ('040', '040 - BANCO CARGILL S.A.'),
    ('041', '041 - BANCO DO ESTADO DO RIO GRANDE DO SUL S.A.'),
    ('044', '044 - BANCO BVA S.A.'),
    ('045', '045 - BANCO OPPORTUNITY S.A.'),
    ('047', '047 - BANCO DO ESTADO DE SERGIPE S.A.'),
    ('062', '062 - HIPERCARD BANCO MÚLTIPLO S.A.'),
    ('063', '063 - BANCO IBI S.A. - BANCO MÚLTIPLO'),
    ('065', '065 - BANCO LEMON S.A.'),
    ('066', '066 - BANCO MORGAN STANLEY S.A.'),
    ('069', '069 - BPN BRASIL BANCO MÚLTIPLO S.A.'),
    ('070', '070 - BRB - BANCO DE BRASILIA S.A.'),
    ('072', '072 - BANCO RURAL MAIS S.A.'),
    ('073', '073 - BB BANCO POPULAR DO BRASIL S.A.'),
    ('074', '074 - BANCO J. SAFRA S.A.'),
    ('075', '075 - BANCO CR2 S/A'),
    ('076', '076 - BANCO KDB DO BRASIL S.A.'),
    ('077', '077 - BANCO INTERMEDIUM S/A'),
    ('078', '078 - BES INVESTIMENTO DO BRASIL S.A. - BANCO DE INVESTIMENTO'),
    ('079', '079 - JBS BANCO S/A'),
    ('081', '081 - CONCÓRDIA BANCO S.A.'),
    ('082', '082 - BANCO TOPÁZIO S.A.'),
    ('083', '083 - BANCO DA CHINA BRASIL S.A'),
    ('096', '096 - BANCO BM&F DE SERVIÇOS DE LIQUIDAÇÃO E CUSTÓDIA S.A.'),
    ('104', '104 - CAIXA ECONOMICA FEDERAL'),
    ('107', '107 - BANCO BBM S/A'),
    ('151', '151 - BANCO NOSSA CAIXA S.A.'),
    ('184', '184 - BANCO ITAÚ BBA S.A.'),
    ('204', '204 - BANCO BRADESCO CARTÕES S.A.'),
    ('208', '208 - BANCO UBS PACTUAL S.A.'),
    ('212', '212 - BANCO MATONE S.A.'),
    ('213', '213 - BANCO ARBI S.A.'),
    ('214', '214 - BANCO DIBENS S.A.'),
    ('215', '215 - BANCO COMERCIAL E DE INVESTIMENTO SUDAMERIS S.A.'),
    ('217', '217 - BANCO JOHN DEERE S.A.'),
    ('218', '218 - BANCO BONSUCESSO S.A.'),
    ('222', '222 - BANCO CALYON BRASIL S.A.'),
    ('224', '224 - BANCO FIBRA S.A.'),
    ('225', '225 - BANCO BRASCAN S.A.'),
    ('229', '229 - BANCO CRUZEIRO DO SUL S.A.'),
    ('230', '230 - UNICARD BANCO MÚLTIPLO S.A.'),
    ('233', '233 - BANCO GE CAPITAL S.A.'),
    ('237', '237 - BANCO BRADESCO S.A.'),
    ('241', '241 - BANCO CLASSICO S.A.'),
    ('243', '243 - BANCO MÁXIMA S.A.'),
    ('246', '246 - BANCO ABC BRASIL S.A.'),
    ('248', '248 - BANCO BOAVISTA INTERATLANTICO S.A.'),
    ('249', '249 - BANCO INVESTCRED UNIBANCO S.A.'),
    ('250', '250 - BANCO SCHAHIN S.A.'),
    ('254', '254 - PARANÁ BANCO S.A.'),
    ('260', '260 - NU PAGAMENTOS S.A.'),
    ('263', '263 - BANCO CACIQUE S.A.'),
    ('265', '265 - BANCO FATOR S.A.'),
    ('266', '266 - BANCO CEDULA S.A.'),
    ('300', '300 - BANCO DE LA NACION ARGENTINA'),
    ('318', '318 - BANCO BMG S.A.'),
    ('320', '320 - BANCO INDUSTRIAL E COMERCIAL S.A.'),
    ('341', '341 - BANCO ITAÚ S.A.'),
    ('366', '366 - BANCO SOCIETE GENERALE BRASIL S.A.'),
    ('370', '370 - BANCO WESTLB DO BRASIL S.A.'),
    ('376', '376 - BANCO J.P. MORGAN S.A.'),
    ('389', '389 - BANCO MERCANTIL DO BRASIL S.A.'),
    ('394', '394 - BANCO FINASA BMC S.A.'),
    ('399', '399 - HSBC BANK BRASIL S.A. - BANCO MULTIPLO'),
    ('409', '409 - UNIBANCO-UNIAO DE BANCOS BRASILEIROS S.A.'),
    ('412', '412 - BANCO CAPITAL S.A.'),
    ('422', '422 - BANCO SAFRA S.A.'),
    ('453', '453 - BANCO RURAL S.A.'),
    ('456', '456 - BANCO DE TOKYO-MITSUBISHI UFJ BRASIL S/A'),
    ('464', '464 - BANCO SUMITOMO MITSUI BRASILEIRO S.A.'),
    ('473', '473 - BANCO CAIXA GERAL - BRASIL S.A.'),
    ('477', '477 - CITIBANK N.A.'),
    ('479', '479 - BANCO ITAUBANK S.A.'),
    ('487', '487 - DEUTSCHE BANK S.A. - BANCO ALEMAO'),
    ('488', '488 - JPMORGAN CHASE BANK, NATIONAL ASSOCIATION'),
    ('492', '492 - ING BANK N.V.'),
    ('494', '494 - BANCO DE LA REPUBLICA ORIENTAL DEL URUGUAY'),
    ('495', '495 - BANCO DE LA PROVINCIA DE BUENOS AIRES'),
    ('505', '505 - BANCO CREDIT SUISSE (BRASIL) S.A.'),
    ('600', '600 - BANCO LUSO BRASILEIRO S.A.'),
    ('604', '604 - BANCO INDUSTRIAL DO BRASIL S.A.'),
    ('610', '610 - BANCO VR S.A.'),
    ('611', '611 - BANCO PAULISTA S.A.'),
    ('612', '612 - BANCO GUANABARA S.A.'),
    ('613', '613 - BANCO PECUNIA S.A.'),
    ('623', '623 - BANCO PANAMERICANO S.A.'),
    ('626', '626 - BANCO FICSA S.A.'),
    ('630', '630 - BANCO INTERCAP S.A.'),
    ('633', '633 - BANCO RENDIMENTO S.A.'),
    ('634', '634 - BANCO TRIANGULO S.A.'),
    ('637', '637 - BANCO SOFISA S.A.'),
    ('638', '638 - BANCO PROSPER S.A.'),
    ('641', '641 - BANCO ALVORADA S.A.'),
    ('643', '643 - BANCO PINE S.A.'),
    ('652', '652 - ITAÚ UNIBANCO BANCO MÚLTIPLO S.A.'),
    ('653', '653 - BANCO INDUSVAL S.A.'),
    ('654', '654 - BANCO A.J. RENNER S.A.'),
    ('655', '655 - BANCO VOTORANTIM S.A.'),
    ('707', '707 - BANCO DAYCOVAL S.A.'),
    ('719', '719 - BANIF - BANCO INTERNACIONAL DO FUNCHAL (BRASIL), S.A.'),
    ('721', '721 - BANCO CREDIBEL S.A.'),
    ('734', '734 - BANCO GERDAU S.A'),
    ('735', '735 - BANCO POTTENCIAL S.A.'),
    ('738', '738 - BANCO MORADA S.A'),
    ('739', '739 - BANCO BGN S.A.'),
    ('740', '740 - BANCO BARCLAYS S.A.'),
    ('741', '741 - BANCO RIBEIRAO PRETO S.A.'),
    ('743', '743 - BANCO SEMEAR S.A.'),
    ('745', '745 - BANCO CITIBANK S.A.'),
    ('746', '746 - BANCO MODAL S.A.'),
    ('747', '747 - BANCO RABOBANK INTERNATIONAL BRASIL S.A.'),
    ('748', '748 - BANCO COOPERATIVO SICREDI S.A.'),
    ('749', '749 - BANCO SIMPLES S.A.'),
    ('751', '751 - DRESDNER BANK BRASIL S.A. BANCO MULTIPLO'),
    ('752', '752 - BANCO BNP PARIBAS BRASIL S.A.'),
    ('753', '753 - NBC BANK BRASIL S. A. - BANCO MÚLTIPLO'),
    ('756', '756 - BANCO COOPERATIVO DO BRASIL S.A. - BANCOOB'),
    ('757', '757 - BANCO KEB DO BRASIL S.A.'),
]


class Address(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=TIPO_ENDERECO)
    public_place = models.CharField(max_length=255)
    number = models.CharField(max_length=16)
    neighborhood = models.CharField(max_length=64)
    country = models.CharField(max_length=32, default='Brasil')
    city = models.CharField(max_length=64)
    uf = models.CharField(max_length=3, choices=UF_SIGLA)

    def __str__(self):
        return f'{self.public_place}, {self.number}, {self.neighborhood}, {self.city}'

class Phone(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type = models.CharField(max_length=8, choices=TIPO_TELEFONE)
    phone = models.CharField(max_length=32)

    def __str__(self):
        return self.phone

class Email(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Bank(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    bank = models.CharField(max_length=3, choices=BANCOS)
    agency = models.CharField(max_length=8)
    acount = models.CharField(max_length=32)
    digit = models.CharField(max_length=8)

    def __str__(self):
        return f'{self.bank} - Ag: {self.agency}-{self.digit}'

class Document(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type = models.CharField(max_length=32)
    document = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.titypepo} - {self.document}'
