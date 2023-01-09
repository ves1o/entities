from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from .models import Entity
from .serializers import EntitySerializer


class EntityList(ListModelMixin, GenericAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        serializer = EntitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(modified_by=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
