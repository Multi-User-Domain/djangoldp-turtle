from django.db import models

from djangoldp.models import Model

from djangoldp_turtle.views import TurtleLDPViewSet


class TurtleCircle(Model):
    name = models.CharField(max_length=255, blank=True)

    class Meta(Model.Meta):
        anonymous_perms = ['view', 'add', 'delete', 'add', 'change', 'control']
        authenticated_perms = ["inherit"]
        rdf_type = 'hd:circle'
        view_set = TurtleLDPViewSet
