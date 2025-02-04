from django.db import models

class Estados(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} - {self.estado.sigla}"


class pessoa (models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.email}) - {self.cidade.nome} - {self.data_nascimento}"