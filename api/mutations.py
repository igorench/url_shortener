import graphene

from url_shortener.models import Url
from url_shortener.form_utils import get_absolute_short_path, get_clean_short_url


class DeleteUrlMutation(graphene.Mutation):
    class Arguments:
        original_url = graphene.String()

    errors = graphene.List(graphene.String)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, **args):
        original_url = args.get('original_url')
        errors = list()
        try:
            url = Url.objects.get(original_url=original_url)
            url.delete()
            success = True
        except Url.DoesNotExist as e:
             errors.append(str(e))
             success = False 

        return DeleteUrlMutation(errors=errors, success=success)



class CreateUrlMutation(graphene.Mutation):
    class Arguments:
        original_url = graphene.String() 
        short_url = graphene.String()

    errors = graphene.List(graphene.String)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, **args):
        original_url = args.get('original_url')
        short_url = args.get('short_url')
        cleaned_short_url = get_clean_short_url(short_url)
        absolute_short_url = get_absolute_short_path(cleaned_short_url)
        url = Url.objects.create(original_url=original_url, short_url=absolute_short_url)
        success = True

        return CreateUrlMutation(success=success)




class UpdateUrlMutation(graphene.Mutation):
    class Arguments:
        original_url = graphene.String()
        new_original_url = graphene.String()
        new_short_url = graphene.String()

    errors = graphene.List(graphene.String)
    success = graphene.Boolean()

    @staticmethod
    def mutate(root, info, **args):
        original_url = args.get('original_url')
        short_url = args.get('new_short_url')
        new_original_url = args.get('new_original_url')
        cleaned_short_url = get_clean_short_url(short_url)
        absolute_short_url = get_absolute_short_path(cleaned_short_url)
        errors = list()

        try:
            url = Url.objects.get(original_url=original_url)
            url.original_url = new_original_url
            url.short_url = absolute_short_url
            success = True
            url.save()
        except Url.DoesNotExist as e:
             errors.append(str(e))
             success = False 

        return UpdateUrlMutation(errors=errors, success=success)


'''
Example use
Go to localhost:8000/graphql/

mutation deleteUrl($originalUrl: String) {
    deleteUrl(originalUrl: $originalUrl) {
			errors
      success 
    }
}
'''