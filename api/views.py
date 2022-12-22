from threading import local
from rest_framework import generics, status
from .models import Result
from .serializers import CreateResultSerializer, ResultSerializer, SearchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .util import explorer
import json
#from ..frontend.static.assets import "heroStats.json"

class ResultView(generics.ListAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    def get(self, request):
        allResults = Result.objects.all().values()
        return Response({"Message":"List of books", "Book list:" : allResults})

class CreateResultView(APIView):
    serializer_class = CreateResultSerializer
    def post(self, request, format = None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            hero = serializer.data.get('hero')
            heroID = serializer.data.get('heroID')
            item = serializer.data.get('item')
            itemID = serializer.data.get('itemID')
            usage = serializer.data.get('usage')
            winrate = serializer.data.get('winrate')
            queryTime = serializer.data.get('queryTime')
            totalMatches = serializer.data.get('totalMatches')
            result = Result(hero = hero, heroID = heroID, item = item, itemID = itemID, usage = usage, winrate = winrate, queryTime = queryTime, totalMatches = totalMatches)
            result.save()
            return Response(ResultSerializer(result).data, status = status.HTTP_201_CREATED)
        return Response(None, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class SearchView(APIView):
    def get(self, request):
        heroID = int(request.GET['heroID'])
        itemID = int(request.GET['itemID'])
        
        hero = "hero_adsasd"
        usage = 0.99
        winrate = 0.99
        queryTime = 0.77

        f = open("api/static/api/assets/itemStats.json")
        itemStats = json.load(f)
        print(heroID)
        print(itemID)
        #
        item_alias = ""
        for key, val in itemStats.items():
            if itemID == val['id']:
                item_alias = key
                item = val['dname']
                break
        print(item)
        print(item_alias)
        f = open("api/static/api/assets/heroStats.json")
        heroStats = json.load(f)
        for heroStat in heroStats:
            if heroID == heroStat['id']:
                hero = heroStat['localized_name']
                break
        ans = explorer.getStats2(heroID = heroID, itemName = item_alias)
        usage = ans['usage']
        winrate = ans['winrate']
        queryTime = ans['queryTime']
        totalMatches = ans['totalMatches']
        print(totalMatches)
        
        result = Result(hero = hero, heroID = heroID, item = item, itemID = itemID, usage = usage, winrate = winrate, queryTime = queryTime, totalMatches = totalMatches)
        result.save()
        return Response(ResultSerializer(result).data, status = status.HTTP_200_OK)
        