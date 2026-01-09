class PrintRequestMiddleware:
    """
    Print every request path and method
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # আগের print
        # print(f"🔥 Request: {request.method} {request.path}")
        
        # নতুন করে flush=True ব্যবহার
        print(f"🔥 Request: {request.method} {request.path}", flush=True)
        
        response = self.get_response(request)
        return response
