import django_tables2 as tables
from .models import Adult

class AdultTable(tables.Table):
    class Meta:
        model = Adult
