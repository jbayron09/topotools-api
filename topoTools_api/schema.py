import graphene

import accounts.schema
import equipments.schema


class Query(
    accounts.schema.Query,
    equipments.schema.Query,
    graphene.ObjectType):
    pass


class Mutation(
    accounts.schema.Mutation,
    equipments.schema.Mutation,
    graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
