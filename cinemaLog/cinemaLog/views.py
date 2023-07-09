from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf

class GeneratePDF(View):
    def get(self, request,*args, **kawrgs):
        template=get_template('invoice.html')
        context= {
            "invoice_id": 123,
            "customer_name": "JhonCooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html=  template.render(context)
        return HttpResponse(html)