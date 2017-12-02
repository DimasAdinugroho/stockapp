# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from stockcore.serializers import StockSerializer, getModel


class IndexList(APIView):
    def get(self, request, format=None):
        return JsonResponse({'message': 'Testing'}, status=status.HTTP_200_OK)


class StockList(generics.ListCreateAPIView):
    serializer_class = StockSerializer

    def post(self, request):
        time_range_list = ['2h', '1h', '1m', '5m']  # 1 minute, 5 minute, 1 hour, 2 hour
        param = request.data
        symbol_name = param['symbol']
        time_range = param['range']
        print time_range
        Model = getModel(symbol_name)

        if time_range is None:
            time_range = 'latest'

        now = datetime.datetime.now()
        if time_range.lower() == '1m':
            end = now - datetime.timedelta(minutes=1)
            queryset = Model.objects.filter(itemtime__range=[now, end])
            response = StockSerializer(queryset, many=True)
        elif time_range.lower() == '5m':
            end = now - datetime.timedelta(minutes=5)
            queryset = Model.objects.filter(itemtime__range=[now, end])
            response = StockSerializer(queryset, many=True)
        elif time_range.lower() == '1h':
            end = now - datetime.timedelta(minutes=60)
            queryset = Model.objects.filter(itemtime__range=[now, end])
            response = StockSerializer(queryset, many=True)
        elif time_range.lower() == '2h':
            end = now - datetime.timedelta(minutes=60*2)
            queryset = Model.objects.filter(itemtime__range=[now, end])
            response = StockSerializer(queryset, many=True)
        else:
            queryset = Model.objects.latest('itemtime')
            response = StockSerializer(queryset)

        return JsonResponse(
            {'data': response.data},
            status=status.HTTP_201_CREATED, safe=False
        )


class StockPost(generics.ListCreateAPIView):
    """
    Return stock data and post stock to database
        get: Get data from stock
        post: Put stock data to database
    """
    serializer_class = StockSerializer

    def get(self, request):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `range` query parameter in the URL.

        latest:
            Models.objects.latest('itemtime')
        1M, 5M, 1H,:
            Models.objects.filter(itemtime__range=[now, end])

        """
        time_range_list = ['2h', '1h', '1m', '5m']  # 1 minute, 5 minute, 1 hour, 2 hour
        symbol_name = request.GET.get('symbol')
        time_range = request.GET.get('range')

        Model = getModel(symbol_name)

        if time_range is None:
            time_range = 'latest'

        now = datetime.datetime.now()
        if time_range.lower() == '1m':
            end = now - datetime.timedelta(minutes=1)
            queryset = Model.objects.filter(itemtime__range=[now, end])
            response = StockSerializer(queryset, many=True)
        elif time_range.lower() == '5m':
            end = now - datetime.timedelta(minutes=5)
            queryset = Model.objects.filter(itemtime__range=[now, end])
            response = StockSerializer(queryset, many=True)
        elif time_range.lower() == '1h':
            end = now - datetime.timedelta(minutes=60)
            queryset = Model.objects.filter(itemtime__range=[now, end])
            response = StockSerializer(queryset, many=True)
        elif time_range.lower() == '2h':
            end = now - datetime.timedelta(minutes=60*2)
            queryset = Model.objects.filter(itemtime__range=[now, end])
            response = StockSerializer(queryset, many=True)
        else:
            queryset = Model.objects.latest('itemtime')
            response = StockSerializer(queryset)

        return JsonResponse(
            {'data': response.data},
            status=status.HTTP_201_CREATED, safe=False
        )

    def post(self, request, format=None):
        """ Post to the Database
        """
        param = request.DATA
        symbol = param['symbol']
        data = param['data']
        data['itemtime'] = datetime.datetime.now()
        serializer = StockSerializer(data=data, context={'model': getModel(symbol)})
        if serializer.is_valid():
            serializer.save()  # rags: using=symbol
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

