import graphene
import predictions.schema
import poems.schema

class Query(predictions.schema.Query, poems.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
