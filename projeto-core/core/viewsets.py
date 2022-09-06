from rest_framework import viewsets
from rest_framework.decorators import action

from . import models, actions


class AtivosDividendosViewSet(viewsets.ViewSet):
    queryset = models.AtivosDividendos.objects.all()

    @action(methods=['GET'], detail=False)
    def show_employee_list(self, request, *args, **kwargs):
        result = actions.AtivosDividendosAction.create_or_update_ativos_e_dividendos()
        self.queryset = result
        return super(EmployeeViewSet, self).list(request, *args, **kwargs)

