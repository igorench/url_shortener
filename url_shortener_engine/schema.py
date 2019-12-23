import graphene

from api.schema import Query as UrlsQuery
from api.mutations import (
    CreateUrlMutation,
    DeleteUrlMutation,
    UpdateUrlMutation
)


class Query(UrlsQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_url = CreateUrlMutation.Field()
    delete_url = DeleteUrlMutation.Field() 
    update_url = UpdateUrlMutation.Field() 


schema = graphene.Schema(query=Query, mutation=Mutation)
