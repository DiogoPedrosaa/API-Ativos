from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Fabricante, Tag, Ativo, Setor
from django.test import TestCase



class FabricanteViewTest(APITestCase):
    def setUp(self):
        self.list_url = reverse('fabricante-list-create')  # Substitua 'fabricante-list' pelo nome registrado na URL
        self.data = {'nome': 'Fabricante Teste'}

    def test_list_fabricantes(self):
        Fabricante.objects.create(nome="Fabricante Existente")
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_fabricante(self):
        response = self.client.post(self.list_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Fabricante.objects.count(), 1)
        self.assertEqual(Fabricante.objects.first().nome, self.data['nome'])



class FabricanteDetailViewTest(APITestCase):
    def setUp(self):
        self.fabricante = Fabricante.objects.create(nome="Fabricante Detalhe")
        self.detail_url = reverse('fabricante-detail', args=[self.fabricante.id])  

    def test_retrieve_fabricante(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.fabricante.nome)

    def test_update_fabricante(self):
        updated_data = {'nome': 'Fabricante Atualizado'}
        response = self.client.put(self.detail_url, updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.fabricante.refresh_from_db()
        self.assertEqual(self.fabricante.nome, updated_data['nome'])

    def test_delete_fabricante(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Fabricante.objects.count(), 0)



class LoginViewTest(APITestCase):
    def setUp(self):
        from django.contrib.auth.models import User
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.login_url = reverse('login')  

    def test_successful_login(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Login successful!', response.data['message'])

    def test_invalid_login(self):
        response = self.client.post(self.login_url, {'username': 'wronguser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('Invalid credentials!', response.data['error'])        



class AtivoModelTest(TestCase):
    def test_create_ativo(self):
        setor = Setor.objects.create(
            nome="Setor Teste"
            )
        fabricante = Fabricante.objects.create(
            nome="Samsung"
            )
        tag = Tag.objects.create(
            tag="Tag Teste"
            )
        
        ativo = Ativo.objects.create(
            patrimonio=12345,
            serial="ABC123",
            defeito="Sem defeito",
            data="2024-01-01",
            tempo_uso="2 anos",
            setor=setor,
            modelo=fabricante,
            tag=tag
        )
        
        
        self.assertEqual(ativo.patrimonio, 12345)
        self.assertEqual(ativo.serial, "ABC123")
        self.assertEqual(ativo.defeito, "Sem defeito")
        self.assertEqual(str(ativo), "Ativo 12345")
        self.assertEqual(ativo.tempo_uso, "2 anos")

