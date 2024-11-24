from django.utils.translation import gettext_lazy as _
from graphql import OperationType
from graphql_jwt.exceptions import PermissionDenied


class LoginRequiredMiddleware:
    @property
    def safe_operations(self) -> list[str]:
        return [
            "tokenAuth",
            "createUser",
        ]

    def resolve(self, next, root, info, **kwargs):
        if info.field_name in self.safe_operations:
            return next(root, info, **kwargs)

        if not info.context.user.is_authenticated:
            raise PermissionDenied(_("You do not have permission to perform this action."))

        return next(root, info, **kwargs)


class UserDataMiddleware:
    def resolve(self, next, root, info, **kwargs):
        if info.operation.operation == OperationType.QUERY:
            # Permitir consultar el esquema
            if info.field_name == "__schema":
                return next(root, info, **kwargs)

            user = info.context.user
            if not user.is_authenticated:
                raise PermissionDenied(_("Authentication required to perform this action."))

            if hasattr(root, "user") and root.user != user:
                raise PermissionDenied(_("You do not have permission to view this data."))

        return next(root, info, **kwargs)