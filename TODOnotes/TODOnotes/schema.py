import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from notes.models import ToDo, Project
from users.models import User


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        id = graphene.ID()
    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.get(id=kwargs.get('id'))
        user.email = kwargs.get('email')
        user.save()
        return cls(user=user)

class UserCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)

    user = graphene.Field(UserType)
    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.create(**kwargs)
        return UserCreateMutation(user=user)

class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    users = graphene.List(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        User.objects.get(id=kwargs.get('id')).delete()
        return cls(users=User.objects.all())


class Mutations(ObjectType):
    update_user = UserUpdateMutation.Field()
    create_user = UserCreateMutation.Field()
    delete_user = UserDeleteMutation.Field()

class Query(graphene.ObjectType):
    # project_all_devs = graphene.List(ProjectType, developers=graphene.Int(required=False))
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=False))
    todo_by_user = graphene.List(ToDoType, user_todo=graphene.Int(required=False))
    all_todoes = graphene.List(ToDoType)
    all_projects = graphene.List(ProjectType)
    all_userss = graphene.List(UserType)

    # def resolve_project_all_devs(self, project_id):
    #     if project_id:


    def resolve_todo_by_user(self, root, user_todo=None):
        if user_todo:
            return ToDo.objects.filter(user_todo_id__user_todo=user_todo)
        return ToDo.objects.all()

    def resolve_user_by_id(self, root, id=None):
        if id:
            return User.objects.get(id=id)
        return User.objects.all()

    def resolve_all_todoes(self, root, info):
        return ToDo.objects.all()

    def resolve_all_projects(self, root, info):
        return Project.objects.all()

    def resolve_all_userss(self, root, info):
        return User.objects.all()

schema = graphene.Schema(
    # query=Query,
    mutation=Mutations
    )


