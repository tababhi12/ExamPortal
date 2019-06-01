from django.core.exceptions import ValidationError

def validate_phone(value):
    if len(str(value)) != 10:
        raise ValidationError('Phone Number should be of 10 length')
    return value
    
def validate_userid(value):
    if ' ' in value:
        raise ValidationError('Spaces are not allowed')
    return value

def validate_email(value):
    if not 'capgemini' in value:
        raise ValidationError('Please enter capgemini email address')
    return value

def validate_security_token(value):
    if value != '@1234$':
        raise ValidationError('Please enter correct security token')
    return value