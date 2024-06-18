import django_filters
from .models import Blog

class BlogFilter(django_filters.FilterSet):
 # name=django_filters.CharFilter(lookup_expr='iexact')
  keyword=django_filters.filters.CharFilter(field_name="title",lookup_expr="icontains")
  class Meta:
    model=Blog
    fields=['keyword']