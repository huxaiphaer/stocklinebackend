from rest_framework import generics, response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from prealert.models import PreAlert
from prealert.serializers import PreAlertSerializer


class PreAlertView(generics.ListCreateAPIView):

    """PreAlert View."""
    queryset = PreAlert.objects.all()
    serializer_class = PreAlertSerializer
    authentication_classes = (JWTAuthentication,)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED,)
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)

