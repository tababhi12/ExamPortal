from django.core.exceptions import ValidationError

def validate_phone(value):
    if len(str(value)) != 10:
        raise ValidationError('Phone Number should be of 10 length')
    return value
    
def validate_userid(value):
    if ' ' in value:
        raise ValidationError('Spaces are not allowed')
    return value

def validate_status_l1(value):
    if 'pending' == value:
        raise ValidationError('Please Select Hired or reject')
    return value