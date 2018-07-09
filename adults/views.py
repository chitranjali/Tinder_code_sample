from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from .models import Adult
from django.db.models import Count
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .tables import AdultTable
from .filters import AdultFilter

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'adults/charts.html', {"customers": 10})


class FilteredAdultListView(SingleTableMixin, FilterView):
    table_class = AdultTable
    model = Adult
    template_name = 'adults/adult_list.html'
    # paginate_by = 25
    filterset_class = AdultFilter


class ChartData(APIView):

    def get(self, request, format=None):
        fieldname = 'relationship'
        adults_rel_status = Adult.objects.values(fieldname).order_by(fieldname).annotate(the_count=Count(fieldname))
        rel_lables = []
        no_of_people = []

        for each_rel_type in adults_rel_status:
            status = each_rel_type.get('relationship')
            people = each_rel_type.get('the_count')
            rel_lables.append(status)
            no_of_people.append(people)

        male_count = Adult.objects.filter(sex=" Male").count()
        female_count = Adult.objects.filter(sex=" Female").count()

        labels = ["Males", "Females"]
        default_items = [male_count, female_count]

        data = {
                "labels": labels,
                "default": default_items,
                "rel_lables": rel_lables,
                "no_of_people": no_of_people,
        }
        return Response(data)
