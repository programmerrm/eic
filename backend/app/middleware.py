class PrintRequestMiddleware:
    """
    Print every request path and method
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print URL and method
        print(f"🔥 Request: {request.method} {request.path}")
        response = self.get_response(request)
        return response
