from unittest import result
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import KDS
from django.db.models import Count
# Create your views here.
class EditorChartView(TemplateView):
    template_name = 'activity_dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        result = (KDS.objects
            .values('section')
            .annotate(dcount=Count('section'))
            .order_by()
            )
        print(result)
        context["qs"] = result
        return context