class PdbAuthenticationMiddleware(object):
    def process_request(self, request):
        #auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        #if auth_header.startswith('PDB'):
            #token = auth_header[4:]
            # user = UserService.get_user(token)
            # if user -> request.pdbuser = user
        pass

    def process_response(self, request, response):
        return response
