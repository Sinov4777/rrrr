from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminTur(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Tur,AdminTur)

class AdminPort(admin.ModelAdmin):
    list_display = ['id', 'nomi','date','tur','rasm1','vaqt']

admin.site.register(Portfolio,AdminPort)

class AdminServise(admin.ModelAdmin):
    list_display = ['id', 'nomi','vaqt','malumot','rasm1']

admin.site.register(Servise,AdminServise)

class AdminTeam(admin.ModelAdmin):
    list_display = ['id','ism','vaqt','malumot','rasm1','lavozim']

admin.site.register(Team,AdminTeam)

class AdminMurojaat(admin.ModelAdmin):
    list_display = ['id','name','gmail','title','text','date']

admin.site.register(Murojaat,AdminMurojaat)

class AdminGmails(admin.ModelAdmin):
    list_display = ['id','gmails']

admin.site.register(GMAIL,AdminGmails)