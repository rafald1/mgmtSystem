from django.db.models import Q
import django_filters
from .models import Agreement


class AgreementFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method="search", label="")

    class Meta:
        model = Agreement
        fields = ["query"]

    @staticmethod
    def search(queryset, _, value):
        return queryset.filter(
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value) |
            Q(company_name__icontains=value) |
            Q(tax_number__icontains=value) |
            Q(business_address_line_1__icontains=value) |
            Q(business_address_line_2__icontains=value) |
            Q(business_zip_code__icontains=value) |
            Q(business_city__icontains=value) |
            Q(business_country__icontains=value) |
            Q(email_1__icontains=value) |
            Q(email_2__icontains=value) |
            Q(phone_no_1__icontains=value) |
            Q(phone_no_2__icontains=value)
        )
