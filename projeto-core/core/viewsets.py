from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, actions


class AtivosDividendosViewSet(viewsets.ViewSet):
    queryset = models.AtivosDividendos.objects.all()

    @action(methods=['GET'], detail=False)
    def create_or_update_ativos_e_dividendos(self, request, *args, **kwargs):
        actions.AtivosDividendosAction.create_or_update_ativos_e_dividendos()
        return Response(data='ok', status=200)


class CarteiraViewSet(viewsets.ViewSet):
    queryset = models.Carteira.objects.all()
