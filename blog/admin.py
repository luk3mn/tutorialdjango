from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post)
@admin.register(Post) # esse "decoretor" tem a mesma função do código anterior (comentado), ou seja, registra o modelo para aparecer na interface
class PostAdmin(admin.ModelAdmin): # na classe está sendo escrito os campos que irão aparecer na tela de 'Posts' da interface de admin
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)} # preenche o campo slug automaticamente com o nome do titulo do post