from rest_framework.filters import BaseFilterBackend
from django.db.models import Q

class TaskFilter(BaseFilterBackend):
    
    def filter_queryset(self, request, queryset, view):
        title = request.query_params.get('title', None)
        due_date = request.query_params.get('due_date', None)

        if title:
            queryset = queryset.filter(Q(title__icontains=title))

        if due_date:
            queryset = queryset.filter(due_date=due_date)

        return queryset
