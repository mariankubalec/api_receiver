from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Body
from .serializers import BodySerializer


def visualizer(request):
    return HttpResponse("Hello world!")


def index(request):
    to_return = "Hello, this is your body: "
    last_body = Body.objects.last()
    if last_body:
        to_return += str(last_body)
    print(to_return)
    return HttpResponse(to_return)


class ReceiveAddView(APIView):

    def post(self, request):
        Body.body_text = request.data

        data_serializer = {k: v for k, v in request.data.items() if v != ''}
        serializer = BodySerializer(data=data_serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(request.data)
    