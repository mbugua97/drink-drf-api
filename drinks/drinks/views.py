from rest_framework.decorators import APIView
from rest_framework.response  import Response

from . models import Drinks
from .serializers import Drink_Serializer


class drink(APIView):
    def get(self,request):
        drink=Drinks.objects.all()
        seri=Drink_Serializer(drink,many=True)
        return Response(seri.data)
    def post(self,request):
        data=request.data
        seri=Drink_Serializer(data=data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
class drinks(APIView):
    def get(self,request,pk):
        try:
            drink=Drinks.objects.filter(pk=pk).first()
            seri=Drink_Serializer(drink)
            if drink is  None:
                return Response('no such drink')
            else:
                return Response(seri.data)
        except:
            return Response('wrong input')
    def put(self,request,pk):
        drink=Drinks.objects.filter(pk=pk).first()
        if drink is None:
            return Response("no such drink")
        data=request.data
        seri=Drink_Serializer(drink,data=data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        return Response("did not save")
    def delete(self,request,pk):
        drink=Drinks.objects.filter(pk=pk).first()
        drink.delete()
        return Response("deleted save")