from rest_framework.renderers import BaseRenderer
from djangoldp.views import LDPViewSet, JSONLDRenderer, JSONLDParser
from rdflib import Graph, plugin


class TurtleRenderer(BaseRenderer):
    media_type = 'text/turtle'
    format = 'ttl'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        json_ld_rendered_content = JSONLDRenderer().render(data)

        g = Graph().parse(data=json_ld_rendered_content, format='json-ld')

        return g.serialize(format="turtle")


# TODO:
'''class TurtleParser(JSONLDParser):
    media_type = 'application/ld+json'

    def parse(self, stream, media_type=None, parser_context=None):
        data = super(JSONLDParser, self).parse(stream, media_type, parser_context)
        # compact applies the context to the data and makes it a format which is easier to work with
        # see: http://json-ld.org/spec/latest/json-ld/#compacted-document-form
        try:
            return jsonld.compact(data, ctx=settings.LDP_RDF_CONTEXT)
        except jsonld.JsonLdError as e:
            raise ParseError(str(e.cause))'''


class TurtleLDPViewSet(LDPViewSet):
    renderer_classes = (TurtleRenderer,)
    parser_classes = ()

    def dispatch(self, request, *args, **kwargs):
        '''overriden dispatch method to append some custom headers'''
        response = super().dispatch(request, *args, **kwargs)
        response["Accept-Post"] = "text/turtle"
        return response
