from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User, auth
from django.contrib import messages
from travello.models import Destination
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from travello.serializers import DestinationSerializer
from rest_framework import generics, mixins
#List all Destinations and create new one
# Destinations/city/
class DestinationList(APIView):
    def get(self, request):
        dests = Destination.objects.all()
        serializer = DestinationSerializer(dests, many=True)
        return Response(serializer.data)
    def post(self):
        pass

class DestinationRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = DestinationSerializer
    def get_queryset(self):
        return Destination.objects.all()
class DestinationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = DestinationSerializer

    def get_queryset(self):
        qs = Destination.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title_icontains=query)|Q(content_icontains=query)).distinct()
            return qs
        def perform_create(self, serializer):
            serializer.save(user=self.request.user)
        def post(self, request, *args, **kwargs):
            return self.create(request, *args, **kwargs)
