import json

from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination


class LargeResponsePagination(PageNumberPagination):
    page_size = 100
    max_page_size = 10000
    page_size_query_param = 'page_size'


class StandardResponsePagination(PageNumberPagination):
    page_size = 20
    max_page_size = 1000
    page_size_query_param = 'page_size'


class CustomJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # If the view throws an error, `data` will contain an `errors` key. We want
        # the default JSONRenderer to handle rendering errors, so we need to
        # check for this case.
        errors = data.get('errors', None)

        if errors is not None:
            # As mentioned about, we will let the default JSONRenderer handle
            # rendering errors.
            return super(CustomJSONRenderer, self).render(data)

        # If all is well, we can render our data.
        return json.dumps({'data': data})

