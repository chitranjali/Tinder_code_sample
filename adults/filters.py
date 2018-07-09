from django_filters import FilterSet

from .models import Adult

class AdultFilter(FilterSet):
    class Meta:
        model = Adult
        fields = {'sex':["contains"], 'race':["contains"], 'relationship':['contains']}

