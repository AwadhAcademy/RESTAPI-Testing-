from rest_framework.response import Response
from rest_framework.decorators import api_view
from yaml import serialize
from data.models import collection 
from .serializers import collectionSerlializers
@api_view(['GET'])
def getData(request):
    
    item=collection.objects.all()
    serializer=collectionSerlializers(item,many=True)

    return Response(serializer.data)

@api_view(['POST'])
def additem(request):
    serializer=collectionSerlializers(data=request.data)
    if( serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)