from django import forms

from prealert.models import HousingCertificateSearchModel


class HousingCertificateSearchForm(forms.ModelForm):

    class Meta:
        model = HousingCertificateSearchModel
        fields = "__all__"
