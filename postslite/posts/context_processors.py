from django.conf import settings


def url_root(request):
    """
    Adds URL_ROOT to the context.
    """
    return {'URL_ROOT': settings.URL_ROOT}
