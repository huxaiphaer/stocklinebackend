from django import forms


class HousingCertificateSearchForm(forms.Form):

    customer = forms.CharField(label='Customer', max_length=100)
    product = forms.CharField(label='Product', max_length=100)
    warehouse = forms.CharField(label='Warehouse', max_length=100)
    season = forms.CharField(label='Season', max_length=100)
    entity = forms.CharField(label='Entity', max_length=100)
