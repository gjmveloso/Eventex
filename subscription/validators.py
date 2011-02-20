# encoding: utf-8
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

def CpfValidator(value):
    if not value.isdigit():
        raise ValidationEror(_(u'O CPF deve conter apenas números'))
    if len(value) != 11:
        raise ValidationError(_(u'O CPF deve conter 11 dígitos'))

    


