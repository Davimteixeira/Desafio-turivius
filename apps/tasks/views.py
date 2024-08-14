from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .filters import TaskFilter
from rest_framework.decorators import action


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [TaskFilter, filters.OrderingFilter]

    def get_queryset(self):
        # Retorna apenas as tasks que não foram deletadas logicamente
        return Task.objects.active()

    def destroy(self, request, *args, **kwargs):
        """
        Realiza o soft delete da task.
        """
        instance = self.get_object()
        instance.delete() 
        return Response({"message": "Task deleted successfully."}, status=status.HTTP_200_OK)

    
    @action(detail=True, methods=['post'], serializer_class=None)
    def restore(self, request, pk=None):
        """
        Restaura uma task deletada logicamente.
        """
        try:
            
            instance = Task.objects.get(pk=pk, is_deleted=True)  
            instance.restore() 
            return Response({"message": "Task restored successfully."}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found or not deleted."}, status=status.HTTP_404_NOT_FOUND)
