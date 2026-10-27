from rest_framework.response import Response

from rest_framework import viewsets, status

from .serializers import URLMappingSerializer


class URLMappingViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = URLMappingSerializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            mapping = serializer.save()
            if hasattr(mapping, "_is_created") and mapping._is_created:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
