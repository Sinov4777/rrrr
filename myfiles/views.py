import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def home(malumot):
     if 'gggg' in malumot.POST:
         matn = malumot.POST.get('gggg')
         soz = str(matn).strip()
         qidirish33 = Q(ism__icontains=soz) |Q(lavozim__icontains=soz) |Q(vaqt__icontains=soz) |Q(malumot__icontains=soz) | Q(link_Twitter__icontains=soz) | Q(link_Facebook__icontains=soz) | Q(link_Instagram__icontains=soz) | Q(link_Linkedin__icontains=soz)
         odamlar = Team.objects.filter(qidirish33)
         ishlar = Servise.objects.filter()
         ishlarimiz = Portfolio.objects.filter()
         return render(malumot, 'index.html', {'team':odamlar,'servis':ishlar,'works': ishlarimiz})
     elif 'jjjj' in malumot.POST:
        matn = malumot.POST.get('jjjj')
        soz = str(matn).strip()
        qidirish2 = Q(nomi__icontains = soz)|  Q(vaqt__icontains = soz)| Q(malumot__icontains = soz)
        ishlar = Servise.objects.filter(qidirish2)
        ishlarimiz = Portfolio.objects.filter()
        odamlar = Team.objects.filter()
        return render(malumot, 'index.html', {'servis': ishlar,'works': ishlarimiz,'team':odamlar})
     elif 'malumot' in malumot.POST:
        matn = malumot.POST.get('malumot')
        soz = str(matn).strip()
        qidirish = Q(nomi__icontains = soz)| Q(cleant_nomi__icontains = soz)| Q(date__icontains = soz)| Q(link__icontains = soz)| Q(malumot__icontains = soz)| Q(tur__id__icontains = soz)
        ishlarimiz = Portfolio.objects.filter(qidirish)
        ishlar = Servise.objects.filter()
        odamlar = Team.objects.filter()
        return render(malumot, 'index.html', {'works': ishlarimiz,'servis': ishlar,'team':odamlar})
     elif 'dddd' in malumot.POST:
        gmailiii = malumot.POST.get('dddd')
        GMAIL(gmails=gmailiii).save()
     elif malumot.method == 'POST':
        ismi = malumot.POST.get('ismii')
        gmaili = malumot.POST.get('email')
        subject = malumot.POST.get('subject')
        matn =malumot.POST.get('message')
        vaqti = datetime.datetime.now()
        Murojaat(name=ismi,gmail=gmaili,title=subject,text=matn,date=vaqti).save()
        ishlarimiz = Portfolio.objects.all()
        ishlar = Servise.objects.all()
        odamlar = Team.objects.all()
        return render(malumot,'index.html',{'works':ishlarimiz,'servis':ishlar,'team':odamlar})
     else:
        odamlar = Team.objects.filter()
        ishlar = Servise.objects.filter()
        ishlarimiz = Portfolio.objects.filter()
        return render(malumot, 'index.html', {'works': ishlarimiz,'servis':ishlar,'team':odamlar})

def inner(malumot):
    return render(malumot,'inner_page.html')

def portfolio(malumot,id):
    if malumot.method == 'POST':
        gmailii= malumot.POST.get('llll')
        GMAIL(gmails=gmailii).save()
    ishlarimiz = Portfolio.objects.get(id=id)
    return render(malumot,'portfolio-details.html',{'work':ishlarimiz})

def servise(malumot):
    return render(malumot,'index.html',)

