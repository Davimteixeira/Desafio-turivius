from rest_framework_nested import routers
from django.urls import path, include
from .views import TaskViewSet, RestoreTaskView

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:pk>/restore/', RestoreTaskView.as_view(), name='restore-task'),
]
