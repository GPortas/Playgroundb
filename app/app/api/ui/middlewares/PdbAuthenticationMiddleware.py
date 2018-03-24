from app.api.domain.services.UserService import UserService


class PdbAuthenticationMiddleware(object):
    def process_request(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header.startswith('PDB'):
            token = auth_header[4:]
            user_service = UserService()
            user = user_service.get_user_by_auth_token(token)
            if user is not None:
                request.pdbuser = user
            else:
                request.pdbuser = None

    def process_response(self, request, response):
        return response
