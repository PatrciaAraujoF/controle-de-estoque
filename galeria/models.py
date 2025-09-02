from django.db import models

class Peca(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome


class DetalhesPeca(models.Model):
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE, related_name='detalhes')
    codigo = models.CharField(max_length=50, unique=True)
    veiculo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    quantidade_inicial = models.IntegerField()
    quantidade_final = models.IntegerField(null=True, blank=True)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.quantidade_final is None:
            self.quantidade_final = self.quantidade_inicial
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalhes de {self.peca.nome}"
