from django.db import models

class TaskQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_deleted=False)

class Task(models.Model):
    title = models.CharField(max_length=255) 
    description = models.TextField() 
    due_date = models.DateField()  #YYYY-MM-DD
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    # Usar o gerenciador personalizado
    objects = TaskQuerySet.as_manager() 
    active_objects = TaskQuerySet.as_manager()  # Gerenciador para objetos ativos

    def delete(self):
        """
        Realiza o soft delete, marcando a task como deletada.
        """
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        """
        Remove permanentemente o objeto do banco de dados.
        """
        super(Task, self).delete()

    def restore(self):
        """
        Restaura um objeto deletado logicamente, marcando-o como não deletado.
        """
        self.is_deleted = False
        self.save()

    class Meta:
        verbose_name = "Task"  
        verbose_name_plural = "Tasks"  
        db_table = 'tasks'  

    def __str__(self):
        return self.title
