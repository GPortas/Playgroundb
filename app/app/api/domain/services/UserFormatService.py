from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class UserFormatService:

    def has_valid_fields(self, user):
        return len(user.get_nickname()) > 2 and len(user.get_password()) > 4 and self.__validate_email(user.get_email())

    def __validate_email(self, email):
        try:
            validate_email(email)
            valid_email = True
        except ValidationError:
            valid_email = False
        return valid_email
