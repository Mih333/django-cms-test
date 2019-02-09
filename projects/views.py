import json

from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TextureChoice, TextureOption, Item

from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class MainView(APIView):

    def get(self, request):
        return render(request, 'main.html', {
            'choices': TextureChoice.position_choice,
            'textures': TextureOption.objects.all()
        })

    template_name = 'main.html'


class SaveOption(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication]

    def post(self, request):
        data = json.loads(request.data.get('data'))
        records = []
        for d in data:
            records.append(TextureChoice(position=d['position'],
                                         option=TextureOption.objects.get(id=d['option'])))
        TextureChoice.objects.bulk_create(records)
        return Response({'data': 'ok'})
