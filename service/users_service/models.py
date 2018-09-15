import re

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _

# reference: https://djangosnippets.org/snippets/10601/
error_messages = {
    'invalid': _("Invalid CPF number."),
    'digits_only': _("This field requires only numbers."),
    'max_digits': _("This field requires exactly 11 digits."),
}


def dv_maker(v):
    if v >= 2:
        return 11 - v
    return 0


def validate_cpf(value):
    """
    Value can be either a string in the format XXX.XXX.XXX-XX or an
    11-digit number.
    """

    if value in EMPTY_VALUES:
        return u''
    if not value.isdigit():
        value = re.sub("[-\.]", "", value)
    orig_value = value[:]
    try:
        int(value)
    except ValueError:
        raise ValidationError(error_messages['digits_only'])
    if len(value) != 11:
        raise ValidationError(error_messages['max_digits'])
    orig_dv = value[-2:]

    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
    new_1dv = dv_maker(new_1dv % 11)
    value = value[:-2] + str(new_1dv) + value[-1]
    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
    new_2dv = dv_maker(new_2dv % 11)
    value = value[:-1] + str(new_2dv)
    if value[-2:] != orig_dv:
        raise ValidationError(error_messages['invalid'])

    return orig_value


class User(AbstractUser):
    name = models.CharField(max_length=50, null=False, blank=False)
    cpf = models.CharField(unique=True, max_length=14, validators=[validate_cpf])
    email = models.EmailField('Email Address', unique=True)
    address = models.CharField(max_length=100, null=False, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []


class Camera(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    user = models.ForeignKey('User', related_name='dono', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=50)
    common_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100, null=False, blank=True)
