from enum import Enum

from rest_framework import status


class ResponseType(Enum):
    """
    API generic & common response types
    """
    resource_not_found = (status.HTTP_404_NOT_FOUND, 0, 'resource not found')
    server_error = (status.HTTP_500_INTERNAL_SERVER_ERROR, 0, 'server error')
