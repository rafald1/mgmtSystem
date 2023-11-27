import django_tables2 as tables
from .models import Agreement


class AgreementTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)
    name = tables.Column(order_by=("last_name", "first_name"))

    class Meta:
        attrs = {"class": "table table-hover", "thead": {"class": "table-light"}}
        model = Agreement
        template_name = "bootstrap_htmx.html"

        fields = ["selection", "id", "agreement_date", "name", "company_name", "tax_number", "business_address_line_1",
                  "business_zip_code", "business_city", "business_country", "email_1",
                  "phone_no_1", "price", "no_of_items", "agreement_length", "status"]
