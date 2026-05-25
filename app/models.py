from django.db import models


# RF03
class Local(models.Model):
    regiao = models.CharField(max_length=100, verbose_name="Região")
    coordenada = models.CharField(max_length=100, verbose_name="Coordenada")

    def __str__(self):
        return self.regiao

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"


# RF09
class Severidade(models.Model):
    grau = models.CharField(max_length=50, verbose_name="Grau")

    def __str__(self):
        return self.grau

    class Meta:
        verbose_name = "Severidade"
        verbose_name_plural = "Severidades"


# RF07
class DadosSatelites(models.Model):
    satelite = models.CharField(max_length=100, verbose_name="Satélite")
    dados_fornecidos = models.TextField(verbose_name="Dados Fornecidos")

    def __str__(self):
        return self.satelite

    class Meta:
        verbose_name = "Dados Satélite"
        verbose_name_plural = "Dados Satélites"


# RF04
class AcaoCausadora(models.Model):
    tipo = models.CharField(max_length=100, verbose_name="Tipo")
    gerou_queimada = models.BooleanField(verbose_name="Gerou Queimada")

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "Ação Causadora"
        verbose_name_plural = "Ações Causadoras"


# RF05
class Biodiversidade(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    severidade = models.ForeignKey(Severidade, on_delete=models.CASCADE)
    dados_satelites = models.ForeignKey(DadosSatelites, on_delete=models.CASCADE)

    descricao = models.TextField(verbose_name="Observações")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Biodiversidade"
        verbose_name_plural = "Biodiversidades"


# RF05
class PerdaHabitat(models.Model):
    area_total_danificada = models.FloatField(
        verbose_name="Área Total Danificada"
    )

    quant_especies_prejudicadas = models.IntegerField(
        verbose_name="Quantidade Espécies Prejudicadas"
    )

    biodiversidade = models.ForeignKey(
        Biodiversidade,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.area_total_danificada} km²"

    class Meta:
        verbose_name = "Perda Habitat"
        verbose_name_plural = "Perdas Habitat"


# RF02
class EspeciesRisco(models.Model):
    especie = models.CharField(max_length=100, verbose_name="Espécie")
    quantia = models.IntegerField(verbose_name="Quantia")

    severidade = models.ForeignKey(
        Severidade,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.especie

    class Meta:
        verbose_name = "Espécie em Risco"
        verbose_name_plural = "Espécies em Risco"


# RF02
class Especies(models.Model):
    classificacao = models.CharField(
        max_length=100,
        verbose_name="Classificação"
    )

    quantidade = models.IntegerField(verbose_name="Quantidade")

    local = models.ForeignKey(
        Local,
        on_delete=models.CASCADE
    )

    especies_risco = models.ForeignKey(
        EspeciesRisco,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.classificacao

    class Meta:
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"


# RF01
class Queimada(models.Model):
    area_km = models.FloatField(verbose_name="Área KM")
    duracao = models.IntegerField(verbose_name="Duração")
    data = models.DateField(verbose_name="Data")

    local = models.ForeignKey(
        Local,
        on_delete=models.CASCADE
    )

    perda_habitat = models.ForeignKey(
        PerdaHabitat,
        on_delete=models.CASCADE
    )

    severidade = models.ForeignKey(
        Severidade,
        on_delete=models.CASCADE
    )

    dados_satelites = models.ForeignKey(
        DadosSatelites,
        on_delete=models.CASCADE
    )

    acao_causadora = models.ForeignKey(
        AcaoCausadora,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.local} - {self.data}"

    class Meta:
        verbose_name = "Queimada"
        verbose_name_plural = "Queimadas"


# RF06
class Relatorio(models.Model):
    nome_pesquisador = models.CharField(
        max_length=100,
        verbose_name="Nome Pesquisador"
    )

    pesquisa = models.TextField(verbose_name="Pesquisa")
    data = models.DateField(verbose_name="Data")

    dados_satelites = models.ForeignKey(
        DadosSatelites,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome_pesquisador

    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"


# RF06
class Cidades(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Cidade")

    local = models.ForeignKey(
        Local,
        on_delete=models.CASCADE
    )

    queimadas = models.ForeignKey(
        Queimada,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


# RF08
class PoliciaAmbiental(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")

    local = models.ForeignKey(
        Local,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Polícia Ambiental"
        verbose_name_plural = "Polícias Ambientais"


# RF10
class Investimento(models.Model):
    quantia = models.FloatField(verbose_name="Quantia")
    data = models.DateField(verbose_name="Data")

    queimadas = models.ForeignKey(
        Queimada,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"R$ {self.quantia}"

    class Meta:
        verbose_name = "Investimento"
        verbose_name_plural = "Investimentos"


# RF11
class Acoes(models.Model):
    acao_feita = models.CharField(
        max_length=100,
        verbose_name="Ação Feita"
    )

    data = models.DateField(verbose_name="Data")

    organizacao = models.CharField(
        max_length=100,
        verbose_name="Organização"
    )

    def __str__(self):
        return self.acao_feita

    class Meta:
        verbose_name = "Ação"
        verbose_name_plural = "Ações"


# RF14
class ClimaTempo(models.Model):
    tipo = models.CharField(max_length=100, verbose_name="Tipo")
    influencia = models.CharField(max_length=100, verbose_name="Influência")
    tempo = models.CharField(max_length=100, verbose_name="Tempo")

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = "Clima Tempo"
        verbose_name_plural = "Climas Tempo"


# RF15
class Historico(models.Model):
    data = models.DateField(verbose_name="Data")

    queimada = models.ForeignKey(
        Queimada,
        on_delete=models.CASCADE
    )

    policia = models.ForeignKey(
        PoliciaAmbiental,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Histórico {self.data}"

    class Meta:
        verbose_name = "Histórico"
        verbose_name_plural = "Históricos"
