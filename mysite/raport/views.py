from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db import models
import datetime
from django.utils import timezone
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Tellimus, Toode

    
def index(request):
    error = False
    if 'q1' and 'q2'in request.GET:
        q1 = request.GET['q1']
        q2 = request.GET['q2']
        if not q1:
            error = True
        elif not q2:
            error = True
        else:
            tellimused = Tellimus.objects.filter(kuupaev__range=(q1, q2))
            tellimused = tellimused.order_by('-kuupaev')
            s = {}
            for t in tellimused:
                date=str(t.kuupaev).split('-')
                date=date[2]+'.'+date[1]+'.'+date[0]
                if date not in s:
                    s[date] = [t]
                else:
                    s[date].append(t)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="raport.pdf"'
            p = canvas.Canvas(response)
            x=100
            y=750
            for date in s:
                p.drawString(x,y,str(date))
                hind = 0
                y-=15
                for t in s[date]:
                    p.drawString(x+10,y,str(t))
                    y-=15
                    hind += t.toode.hind*t.kogus
                p.drawString(x,y,'Summa - ' + str(hind) + ' EUR')
                y-=30
            p.showPage()
            p.save()
            return response
    return render(request, 'raport/search_form.html', {'error': error})
    
