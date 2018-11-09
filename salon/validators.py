from django.core.exceptions import ValidationError
from phonenumber_field.validators import validate_international_phonenumber


def validate_phone_number(phone):
    phone = phone.replace(' ', '')
    phone = phone.replace('-', '')
    phone = phone.replace('(', '')
    phone = phone.replace(')', '')
    if not phone.isdigit():
        raise ValidationError("Неправильный формат номера телефона.")
    try:
        if phone.startswith('7') and len(phone) == 11:
            validate_international_phonenumber('+%s' % phone)
        elif phone.startswith('8') and len(phone) == 11:
            validate_international_phonenumber('+7%s' % phone[1:])
        elif phone.startswith('9') and len(phone) == 10:
            validate_international_phonenumber('+7%s' % phone)
        else:
            validate_international_phonenumber(phone)
    except ValidationError as e:
        raise ValidationError("Неправильный формат номера телефона.")
