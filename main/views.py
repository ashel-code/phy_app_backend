from django.shortcuts import render
from django.db.migrations import serializer
from rest_framework import generics, status
from .serializers import *
from rest_framework.response import Response
from django.http import FileResponse
from itertools import chain


# Create your views here.
class GetMessagesAPI(generics.ListCreateAPIView):
    def post(self, request):
        min = self.request.GET.get('latest_message')
        max = self.request.GET.get('earliest_message')
        final = self.request.GET.get('end_user')
        login = self.request.GET.get('login')
        hash = self.request.GET.get('hash')

        trueHash = Users.objects.get(login=login)
        if hash == trueHash:
            queryset0 = Messages.objects.filter(date__gte=min, date__lt=max, endUser=final, primaryUser=login)
            queryset1 = Messages.objects.filter(date__gte=min, date__lt=max, endUser=login, primaryUser=final)
            queryset = list(chain(queryset0, queryset1))
            serializer_for_queryset = MessagesSerializer(instance=queryset, many=True)

            return Response(serializer_for_queryset.data)

class SendMessage(generics.ListCreateAPIView):
    def post(self, request):
        final = self.request.GET.get('end_user')
        login = self.request.GET.get('login')
        hash = self.request.GET.get('hash')
        text = self.request.GET.get('text')

        trueHash = Users.objects.get(login=login)
        if hash == trueHash:
            serializer = MessagesSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request)
            return Response(status=status.HTTP_201_CREATED)


