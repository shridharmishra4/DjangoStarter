from django.conf.urls import url

from .Views.GreetView import GreetView
from V1.Views.SwaggerSchemaView import SwaggerSchemaView


urlpatterns = [
    url(r'^$', SwaggerSchemaView.as_view()),
    url(r'^V1/Greet/(?P<username>[-\w]+)/',
        GreetView.as_view(), name="name"),


]
