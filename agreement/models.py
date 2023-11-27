from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Server side validation
BAD_WORDS = ["flask"]


def validate_no_bad_words(content):
    if any([word in content.lower() for word in BAD_WORDS]):
        raise ValidationError("This note contains bad words!")


class Agreement(models.Model):
    class Meta:
        ordering = ["-created"]

    AGREEMENT_LENGTH_M = [("12M", "12M"), ("24M", "24M"), ("36M", "36M")]
    STATUS = [("1", "1 - New"), ("2", "2 - Generated"), ("3", "3 - Signed"), ("4", "4 - Forwarded"),
              ("5", "5 - Shipped"), ("6", "6 - Delivery Confirmed")]

    agreement_date = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    company_name = models.CharField(max_length=100)
    tax_number = models.CharField(max_length=20)
    business_address_line_1 = models.CharField(max_length=80, verbose_name="Business address")
    business_address_line_2 = models.CharField(blank=True, max_length=80, verbose_name="Business address")
    business_zip_code = models.CharField(max_length=10)
    business_city = models.CharField(max_length=40)
    business_country = models.CharField(max_length=40)
    shipping_address_line_1 = models.CharField(blank=True, max_length=80)
    shipping_address_line_2 = models.CharField(blank=True, max_length=80)
    shipping_zip_code = models.CharField(blank=True, max_length=10)
    shipping_city = models.CharField(blank=True, max_length=40)
    shipping_country = models.CharField(blank=True, max_length=40)
    correspondence_address_line_1 = models.CharField(blank=True, max_length=80)
    correspondence_address_line_2 = models.CharField(blank=True, max_length=80)
    correspondence_zip_code = models.CharField(blank=True, max_length=10)
    correspondence_city = models.CharField(blank=True, max_length=40)
    correspondence_country = models.CharField(blank=True, max_length=40)
    email_1 = models.EmailField(verbose_name="Primary email")
    email_2 = models.EmailField(blank=True, verbose_name="Secondary email")
    phone_no_1 = models.CharField(max_length=20, verbose_name="Primary phone")
    phone_no_2 = models.CharField(blank=True, max_length=20, verbose_name="Secondary phone")
    price = models.FloatField()
    no_of_items = models.PositiveSmallIntegerField()
    agreement_length = models.CharField(choices=AGREEMENT_LENGTH_M, default=AGREEMENT_LENGTH_M[1], max_length=5)
    additional_info = models.TextField(blank=True, validators=[validate_no_bad_words])
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="agreement")
    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0][1], null=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
