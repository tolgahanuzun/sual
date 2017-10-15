from rest_framework.permissions import BasePermission


class UserIsOwnerQuestions(BasePermission):

    def has_object_permission(self, request, view, questions):
        return request.user.id == questions.user.id