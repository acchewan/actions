import time


def request_time_middleware(get_response):
    def middleware(request):
        start_time = time.time()
        response = get_response(request)
        end_time = time.time()-start_time
        print(f"Request processing time: {end_time:.2f} seconds")
        return response
    return middleware
