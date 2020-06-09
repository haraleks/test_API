from django.urls import path
from .views import ProgramView

# app_name = "programs"

program_detail = ProgramView.as_view({
    'get': 'list',
    'post': 'create',
})

urlpatterns = [
    path('programs/', program_detail, name='programs')
]
