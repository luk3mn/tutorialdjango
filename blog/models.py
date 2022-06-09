# Nesse arquivo ficam os models,
# Tem os campo e comportamento dos dados 
# armazenados, sendo mapeados para uma 
# tabela pro banco de dados
# - Cada model é uma classe python que herda
#   a classe model do django
# - Alguns atributos dessa classe serão campos
#   da tabela
# - O Django fornece uma api para acessar o banco
#   de dados com código python e converte para a
#   linguagem sql de acordo com o banco de dados
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

# tabela para armazenar os posts
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 'on_delete=models.CASCADE' -> faz com que o post seja deletado caso o usuário seja deletado
    body = models.TextField() # campo ideal para o corpo do post, pois não tem um tamanho máximo
    created = models.DateTimeField(auto_now_add=True) # 'auto_now_add=True' add automaticamente a data e hora da criacao do artigo
    updated = models.DateTimeField(auto_now=True) # 'auto_now=True' atualiza o campo a cada atualização

    class Meta:
        ordering = ("-created",)

    # DENTRO DA CLASSE POST -> Visualiza na lista de post da interface 'admin' o titulo do post
    def __str__(self):
        return self.title

    # Cria um esquema para clicar nos links e redirecionar as páginas dos postes
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug}) # serve para definir a url de um recurso "post"