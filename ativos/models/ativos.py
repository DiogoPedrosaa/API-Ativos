from django.db import models

class Fabricante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag
    

class Setor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Ativo(models.Model):
    patrimonio = models.IntegerField(blank=True)
    serial = models.CharField(max_length=50, blank=True)
    defeito = models.CharField(blank=True, max_length=100)
    data = models.DateField()
    tempo_uso = models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True)
    modelo = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Ativo {self.patrimonio}"






    





