import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType

from url_shortener.models import (
    Url
)

class UrlType(DjangoObjectType):
    class Meta:
        model = Url


class Query(object):
    get_urls = graphene.List(UrlType)
    get_by_original_url = graphene.Field(UrlType, original_url=graphene.String())

    def resolve_get_urls(self, info, **kwargs):
        return Url.objects.all()

    def resolve_get_by_original_url(self, info, original_url):
        return Url.objects.get(original_url=original_url)
  

'''
Example use
Go to localhost:8000/graphql/


query getByOriginalUrl($originalUrl: String){
  getByOriginalUrl(originalUrl: $originalUrl) {
    id
    originalUrl
    createdAt
    text
    clicks
    shortUrl
  }
}

'''