from rest_framework.views import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getAllRooms(request, format=None):
   rooms = [RoomSerializer(room).data for room in Room.objects.all()]
   return Response(rooms)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getRoom(request, pk):
   room = get_object_or_404(Room, pk=pk)
   return Response(RoomSerializer(room).data)
   
@api_view(['POST'])
def createRoom(request):
   serializer = RoomSerializer(data=request.data)
       
   if not serializer.is_valid():
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
   room = serializer.save()
   return Response(RoomSerializer(room).data)