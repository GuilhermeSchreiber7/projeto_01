from django.contrib import admin
from .models import Estados
from .models import Cidade
from .models import pessoa

admin.site.register(Estados)
admin.site.register(Cidade)
admin.site.register(pessoa)


