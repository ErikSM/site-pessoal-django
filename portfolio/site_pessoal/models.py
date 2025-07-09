from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo

class Habilidade(models.Model):
    nome = models.CharField(max_length=50)
    nivel = models.IntegerField()  # 0-100

    def __str__(self):
        return self.nome
