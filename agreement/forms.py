from django import forms
from django.core.exceptions import ValidationError

from .models import Agreement


class AgreementStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ["status"]


class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        # fields = "__all__"
        exclude = ["user", "status"]
        widgets = {
            "agreement_date": forms.DateInput(attrs={"class": "form-control my-2", "type": "date"}),
            "first_name": forms.TextInput(attrs={"class": "form-control my-2"}),
            "last_name": forms.TextInput(attrs={"class": "form-control my-2"}),
            "company_name": forms.TextInput(attrs={"class": "form-control my-2"}),
            "tax_number": forms.TextInput(attrs={"class": "form-control my-2"}),
            "business_address_line_1": forms.TextInput(attrs={"class": "form-control my-2"}),
            "business_address_line_2": forms.TextInput(attrs={"class": "form-control my-2"}),
            "business_zip_code": forms.TextInput(attrs={"class": "form-control my-2"}),
            "business_city": forms.TextInput(attrs={"class": "form-control my-2"}),
            "business_country": forms.TextInput(attrs={"class": "form-control my-2"}),
            "shipping_address_line_1": forms.TextInput(attrs={"class": "form-control my-2"}),
            "shipping_address_line_2": forms.TextInput(attrs={"class": "form-control my-2"}),
            "shipping_zip_code": forms.TextInput(attrs={"class": "form-control my-2"}),
            "shipping_city": forms.TextInput(attrs={"class": "form-control my-2"}),
            "shipping_country": forms.TextInput(attrs={"class": "form-control my-2"}),
            "correspondence_address_line_1": forms.TextInput(attrs={"class": "form-control my-2"}),
            "correspondence_address_line_2": forms.TextInput(attrs={"class": "form-control my-2"}),
            "correspondence_zip_code": forms.TextInput(attrs={"class": "form-control my-2"}),
            "correspondence_city": forms.TextInput(attrs={"class": "form-control my-2"}),
            "correspondence_country": forms.TextInput(attrs={"class": "form-control my-2"}),
            "email_1": forms.TextInput(attrs={"class": "form-control my-2"}),
            "email_2": forms.TextInput(attrs={"class": "form-control my-2"}),
            "phone_no_1": forms.TextInput(attrs={"class": "form-control my-2"}),
            "phone_no_2": forms.TextInput(attrs={"class": "form-control my-2"}),
            "price": forms.TextInput(attrs={"class": "form-control my-2"}),
            "no_of_items": forms.TextInput(attrs={"class": "form-control my-2", "type": "number"}),
            "agreement_length": forms.Select(attrs={"class": "form-control my-2"}),
            "additional_info": forms.Textarea(attrs={"class": "form-control my-2"})
        }
        labels = {
            "agreement_date": "Agreement Date:",
            "first_name": "First Name:",
            "last_name": "Last Name:",
            "company_name": "Company Name:",
            "tax_number": "Tax Number:",
            "business_address_line_1": "Address Line 1 (Business):",
            "business_address_line_2": "Address Line 2 (Business):",
            "business_zip_code": "Zip Code (Business):",
            "business_city": "City (Business):",
            "business_country": "Country (Business):",
            "shipping_address_line_1": "Address Line 1 (Shipping):",
            "shipping_address_line_2": "Address Line 2 (Shipping):",
            "shipping_zip_code": "Zip Code (Shipping):",
            "shipping_city": "City (Shipping):",
            "shipping_country": "Country (Shipping):",
            "correspondence_address_line_1": "Address Line 1 (Correspondence):",
            "correspondence_address_line_2": "Address Line 2 (Correspondence):",
            "correspondence_zip_code": "Zip Code (Correspondence):",
            "correspondence_city": "City (Correspondence):",
            "correspondence_country": "Country (Correspondence):",
            "email_1": "Primary E-Mail Address:",
            "email_2": "Secondary E-Mail Address:",
            "phone_no_1": "Primary Phone No.:",
            "phone_no_2": "Secondary Phone No.:",
            "price": "Price per Unit:",
            "no_of_items": "No. of Items:",
            "agreement_length": "Agreement Length in Months:",
            "additional_info": "Additional Information:"
        }

    # Client side validation
    def clean_additional_info(self):
        additional_info = self.cleaned_data["additional_info"]
        if "django" not in additional_info.lower():
            raise ValidationError("We only accept agreements with 'Django' in the additional information section!")
        return additional_info
