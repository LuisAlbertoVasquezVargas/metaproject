from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id', 'hero', 'heroID', 'item', 'itemID', 'winrate', 'usage', 'queryTime', 'totalMatches')

class CreateResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('hero', 'heroID', 'item', 'itemID', 'winrate', 'usage', 'queryTime', 'totalMatches')
        
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('heroID', 'itemID')