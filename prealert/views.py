from rest_framework import generics, response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.translation import gettext_lazy as _

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


class PreAlertDetail(generics.GenericAPIView):

    """PreAlert Detail."""
    queryset = PreAlert.objects.all()
    serializer_class = PreAlertSerializer
    authentication_classes = (JWTAuthentication,)

    def get_pre_alert_by_id(self, _id: int):
        """Get pre-alert by id. """
        try:
            obj = PreAlert.objects.get(id=_id)
            return obj
        except PreAlert.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        pre_alert = self.get_pre_alert_by_id(kwargs.get("id"))
        if not pre_alert:
            return response.Response({
                'errors': _('Sorry, Pre-Alert post with the specified id does'
                            'not exist')
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(pre_alert,
                                           context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        pre_alert = self.get_pre_alert_by_id(kwargs.get("id"))
        if pre_alert:
            pre_alert.delete()
        return response.Response(
            {'message': _('Pre Alert has been deleted')},
            status=status.HTTP_200_OK)




