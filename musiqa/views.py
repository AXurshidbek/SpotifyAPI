from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *



class QoshiqModelViewSet(ModelViewSet):
    queryset = Qoshiq.objects.all()
    serializer_class = QoshiqSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [ 'nom','janr']
    order_fields = ['davomiylik']
    pagination_class = PageNumberPagination
    pagination_class.page_size = 3

    def get_queryset(self):
        qoshiqlar = self.queryset
        janr = self.request.query_params.get('janr')
        qidiruv = self.request.query_params.get("qidiruv")
        if qidiruv:
            qoshiqlar = Qoshiq.objects.annotate(oxshashlik=TrigramSimilarity('nomm', qidiruv)
                                                ).filter(oxshashlik__gt=0.3).order_by('-oxshashlik')
        if janr:
            kinolar = qoshiqlar.filter(janr__contains=janr)
        return qoshiqlar
    def list(self, request, *args, **kwargs):
        qoshiqlar=self.queryset
        serializer=QoshiqSerializer(qoshiqlar, many=True)
        return Response(serializer.data)
class AlbomModelViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    search_fields = ['nom']
    order_fields = ['sana']

    def list(self, request, *args, **kwargs):
        albomlar=self.queryset
        serializer=AlbomSerializer(albomlar, many=True)
        return Response(serializer.data)



class QoshiqchiModelViewSet(ModelViewSet):
    queryset = Qoshiqchi.objects.all()
    serializer_class = QoshiqSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [ 'nom', 'davlat']
    order_fields = [ 'tugilgan_sana']
    def list(self, request, *args, **kwargs):
        qoshiqchilar=self.queryset
        serializer=QoshiqchiSerializer(qoshiqchilar, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def albomlar(self, request, pk):
        qoshiqchi = self.get_object()
        qoshiqchi_albomlari = qoshiqchi.albom_set.all()
        serializer = AlbomSerializer(qoshiqchi_albomlari, many=True)
        return Response(serializer.data)

