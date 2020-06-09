from rest_framework import viewsets, status
from rest_framework.response import Response

from . import permissions
from .models import Program
from .permissions import AdminAccessPermission
from .serializers import ProgramSerializer


class ProgramView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    permission_classes = [AdminAccessPermission]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous != True:
            if user.is_staff:
                return Program.objects.all()
            else:
                return Program.objects.filter(user_report_id=user.report_id)
        else:
            return None

    def create(self, request):
        data = request.data
        print(data)
        # Create an article from the above data
        serializer = ProgramSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        # return Response({"success": "program '{}' created successfully".format(program_saved.title)})
        return Response(serializer.data, status=status.HTTP_201_CREATED)
