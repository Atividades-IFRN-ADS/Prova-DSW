from django.db import models

# Create your models here.
class Modalidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(choices=[("individual", "Individual"), ("coletivo", "Coletivo")], default="individual", max_length=20)
    max_atletas = models.PositiveIntegerField()

    class Meta:
        verbose_name = "modalidade"
        verbose_name_plural = "modalidades"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Equipe(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    curso = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "equipe"
        verbose_name_plural = "equipes"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Tecnico(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=100)
    equipe = models.OneToOneField(
        Equipe,
        on_delete=models.CASCADE,
        related_name="tecnico",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "técnico"
        verbose_name_plural = "técnicos"
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Atleta(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50, unique=True)
    data_nascimento = models.DateField()
    equipe = models.ForeignKey(
        Equipe,
        on_delete=models.PROTECT,
        related_name="atletas",
    )
    modalidades = models.ManyToManyField(
        Modalidade,
        related_name="atletas",
        blank=True,
    )

    class Meta:
        verbose_name = "atleta"
        verbose_name_plural = "atletas"
        ordering = ["nome"]

    def __str__(self):
        return self.nome