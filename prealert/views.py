from django.views.decorators.csrf import csrf_protect
from rest_framework import generics, response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.translation import gettext_lazy as _

from customer.models import Product, Customer
from prealert.forms import HousingCertificateSearchForm
from prealert.models import PreAlert, WeighBridge, GuaranteedGoods
from prealert.serializers import PreAlertSerializer, WeighBridgeSerializer, \
    GuaranteedGoodsSerializer
from users.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


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
                                     status=status.HTTP_201_CREATED, )
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

    def put(self, request, *args, **kwargs):
        pre_alert = self.get_pre_alert_by_id(kwargs.get("id"))
        _customer = Customer.objects.filter(id=kwargs.get('id')).first()
        _product = Product.objects.filter(id=kwargs.get('id')).first()
        _user = User.objects.filter(id=kwargs.get('id')).first()

        if pre_alert:
            pre_alert.quantity = request.data.get("quantity")
            pre_alert.contract_number = request.data.get("contract_number")
            pre_alert.from_or_origin = request.data.get("from_or_origin")
            pre_alert.commentaries = request.data.get("commentaries")
            pre_alert.type = request.data.get("type")
            pre_alert.weight = request.data.get("weight")
            pre_alert.notifications = request.data.get("notifications")
            pre_alert.status = request.data.get("status")
            pre_alert.priority = request.data.get("priority")
            pre_alert.customer = _customer
            pre_alert.product = _product
            pre_alert.user = _user

            pre_alert.save()
            return response.Response(
                {'message': _('Pre-Alert has been edited.')},
                status=status.HTTP_200_OK)


class WeighBridgeView(generics.ListCreateAPIView):
    queryset = WeighBridge.objects.all()
    serializer_class = WeighBridgeSerializer


class WeighBridgeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeighBridge.objects.all()
    serializer_class = WeighBridgeSerializer

    def get_weigh_bridge_by_id(self, _id: int):
        """Get Weigh Bridge by id. """
        try:
            obj = WeighBridge.objects.get(id=_id)
            return obj
        except WeighBridge.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        weigh_bridge = self.get_weigh_bridge_by_id(kwargs.get("id"))
        if not weigh_bridge:
            return response.Response({
                'errors': _('Sorry, Weigh bridge with the specified id does'
                            'not exist')
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(weigh_bridge,
                                           context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        weigh_bridge = self.get_weigh_bridge_by_id(kwargs.get("id"))
        if weigh_bridge:
            weigh_bridge.delete()
        return response.Response(
            {'message': _('Weigh bridge has been deleted')},
            status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        weigh_bridge = self.get_weigh_bridge_by_id(kwargs.get("id"))
        _product = Product.objects.filters(id=kwargs.get('id')).first()
        _user = User.objects.filters(id=kwargs.get('id')).first()

        if weigh_bridge:
            weigh_bridge.vehicle_number = request.data.get("vehicle_number")
            weigh_bridge.transporter = request.data.get("transporter")
            weigh_bridge.vehicle_reg_num = request.data.get("vehicle_reg_num")
            weigh_bridge.account_id = request.data.get("account_id")
            weigh_bridge.commodity = _product
            weigh_bridge.user = _user
            weigh_bridge.time = request.data.get("time")
            weigh_bridge.trailer_reg_num = request.data.get("trailer_reg_num")
            weigh_bridge.entry_date = request.data.get("entry_date")
            weigh_bridge.exit_time = request.data.get("exit_time")
            weigh_bridge.print_date = request.data.get("print_date")
            weigh_bridge._import = request.data.get("_import")
            weigh_bridge._export = request.data.get("_export")
            weigh_bridge.client_name = request.data.get("client_name")
            weigh_bridge.from_destination = request.data.get("from_destination")
            weigh_bridge.to_destination = request.data.get("to_destination")
            weigh_bridge.first_weight = request.data.get("first_weight")
            weigh_bridge.second_name = request.data.get("second_name")
            weigh_bridge.net_weight = request.data.get("net_weight")
            weigh_bridge.status = request.data.get("status")

            weigh_bridge.save()
            return response.Response(
                {'message': _('Weigh bridge has been edited.')},
                status=status.HTTP_200_OK)


class GuaranteedGoodsView(generics.ListCreateAPIView):
    queryset = GuaranteedGoods.objects.all()
    serializer_class = GuaranteedGoodsSerializer


class GuaranteedGoodsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GuaranteedGoods.objects.all()
    serializer_class = GuaranteedGoodsSerializer

    def get_guarantee_goods_by_id(self, _id: int):
        """Get Weigh Bridge by id. """
        try:
            obj = GuaranteedGoods.objects.get(id=_id)
            return obj
        except GuaranteedGoods.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        guaranteed_goods = self.get_guarantee_goods_by_id(kwargs.get("id"))
        if not guaranteed_goods:
            return response.Response({
                'errors': _('Sorry, Guaranteed with the specified id does'
                            'not exist')
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(guaranteed_goods,
                                           context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        guaranteed_goods = self.get_guarantee_goods_by_id(kwargs.get("id"))
        if guaranteed_goods:
            guaranteed_goods.delete()
        return response.Response(
            {'message': _('Guaranteed goods has been deleted.')},
            status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        guaranteed_goods = self.get_guarantee_goods_by_id(kwargs.get("id"))

        if guaranteed_goods:
            guaranteed_goods.batch_number = request.data.get("batch_number")
            guaranteed_goods.quantity = request.data.get("quantity")
            guaranteed_goods.quantity_pledged = request.data.get("quantity_pledged")
            guaranteed_goods.theoretical_weight = request.data.get("theoretical_weight")
            guaranteed_goods.theoretical_weight_pledged = request.data.get("theoretical_weight_pledged")
            guaranteed_goods.actual_weight = request.data.get("actual_weight")
            guaranteed_goods.actual_weight_guaranteed = request.data.get("actual_weight_guaranteed")
            guaranteed_goods.priority = request.data.get("priority")

            guaranteed_goods.save()
            return response.Response(
                {'message': _('Guaranteed goods have been edited.')},
                status=status.HTTP_200_OK)


# @csrf_protect
# def search_housing_certificate_view(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = HousingCertificateSearchForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = HousingCertificateSearchForm()
#
#     return render(
#         request, 'admin/search_housing_certificate.html', {'form': form}
#     )
