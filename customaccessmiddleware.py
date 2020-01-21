from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.http import JsonResponse
from .models import ApiKey

customtokenkey = settings.CUSTOMTOKENKEY

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):

        apikey = ApiKey.objects.order_by().values_list(
            'key', flat=True).distinct().filter(active_status__exact=True)
        list_apikey = list(apikey)

        try:
            request.COOKIES['sessionid']
        except KeyError:
            if request.META['PATH_INFO'] == '/' or request.META['PATH_INFO'] == '/login/':
                return None
            else:
                try:
                    metafleid = request.META['HTTP_'+customtokenkey]
                except KeyError:
                    metafleid = {
                        "error": True,
                        "message": "Access Forbidden"
                    }
                    return JsonResponse(metafleid)
                else:
                    metafleid = request.META['HTTP_'+customtokenkey]
                    if metafleid in list_apikey:
                        return None
                    else:
                        metafleid = {
                            "error": True,
                            "message": "Access Forbidden"
                        }
                        return JsonResponse(metafleid)

