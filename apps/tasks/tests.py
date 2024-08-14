from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.tasks.models import Task
from apps.accounts.models import CustomUser

class TaskViewSetTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass', email='test@email.com')
        self.client.login(username='testuser', password='testpass') 
        
        self.register_url = reverse('register_user')

        self.url = reverse('tasks-list')  

    def register_user(self, name, email):
        """Método auxiliar para registrar um usuário"""
        data = {
            "name": name,
            "email": email,
        }
        response = self.client.post(self.register_url, data, format='json')
        return response

    def test_create_task(self):
        """Teste para criar uma nova tarefa"""
        data = {
            "title": "Nova Tarefa",
            "description": "Descrição da nova tarefa",
            "due_date": "2024-08-15"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_tasks(self):
        """Teste para listar tarefas"""
        Task.objects.create(title="Tarefa 1", description="Descrição 1", due_date="2024-08-15")
        Task.objects.create(title="Tarefa 2", description="Descrição 2", due_date="2024-08-16")
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_task(self):
        """Teste para atualizar uma tarefa existente"""
        task = Task.objects.create(title="Tarefa Atualizar", description="Descrição", due_date="2024-08-15")
        url = reverse('tasks-detail', args=[task.id])  #

        data = {
            "title": "Tarefa Atualizada",
            "description": "Descrição Atualizada",
            "due_date": "2024-08-16"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()

    def test_delete_task(self):
        """Teste para deletar uma tarefa existente"""
        task = Task.objects.create(title="Tarefa Deletar", description="Descrição", due_date="2024-08-15")
        url = reverse('tasks-detail', args=[task.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_task_delete_success_message(self):
        """Teste para verificar a mensagem de sucesso ao deletar uma tarefa"""
        task = Task.objects.create(title="Tarefa Deletar", description="Descrição", due_date="2024-08-15")
        url = reverse('tasks-detail', args=[task.id])

        response = self.client.delete(url)
        self.assertEqual(response.data, {"message": "Task deleted successfully."})

    def test_filter_by_title(self):
        """Teste para filtrar tarefas pelo título"""
        Task.objects.create(title="Tarefa Importante", description="Descrição", due_date="2024-08-15")
        Task.objects.create(title="Tarefa Secundária", description="Descrição", due_date="2024-08-16")

        response = self.client.get(self.url, {'title': 'Importante'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_by_due_date(self):
        """Teste para filtrar tarefas pela data de vencimento"""
        Task.objects.create(title="Tarefa 1", description="Descrição", due_date="2024-08-15")
        Task.objects.create(title="Tarefa 2", description="Descrição", due_date="2024-08-16")

        response = self.client.get(self.url, {'due_date': '2024-08-15'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_user(self):
        """Teste para registrar um novo usuário"""
        response = self.register_user("newuser", "newuser@example.com")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_access_tasks(self):
        """Teste para verificar que um usuário não autenticado não pode acessar as tarefas"""
        self.client.logout()  
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  #
