def session_key_middleware(get_response):
    def middleware(request):
        if not request.session.session_key:
            request.session.save()
        response = get_response(request)
        print(f"SESSION KEY : {request.session.session_key}")
        return response

    return middleware
