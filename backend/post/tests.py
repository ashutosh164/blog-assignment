from django.test import TestCase
from rest_framework import status
from django.core.exceptions import ValidationError
from .models import Posts, Comment
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class PostAPITestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client_instance = APIClient()
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client_instance.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client_instance.post('/api/posts/', data={'title': 'Test Post', 'content': 'This is a test post', 'author': self.user.id}, format='json')
        self.post_id = response.data['id']
        self.post = Posts.objects.get(id=self.post_id)

    def test_get_post_list(self):
        response = self.client_instance.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_post_detail(self):
        response = self.client_instance.get(f'/api/posts/{self.post_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.post.title)

    def test_create_post(self):
        data = {'title': 'New Post', 'content': 'This is a new post'}
        response = self.client_instance.post('/api/posts/', data=data, format='json')
        print(f'Post creation response data: {response.data}')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Posts.objects.count(), 2)

    def test_update_post(self):
        data = {'title': 'Updated Post', 'content': 'This is an updated post'}
        response = self.client_instance.put(f'/api/posts/{self.post_id}/', data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')

    def test_delete_post(self):
        response = self.client_instance.delete(f'/api/posts/{self.post_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Posts.objects.count(), 0)


class TestCommentModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client_instance = APIClient()
        self.client_instance.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client_instance.post('/api/posts/', data={'title': 'Test Post', 'content': 'This is a test post', 'author': self.user.id}, format='json')

        self.post_id = response.data['id']
        self.post_instance = Posts.objects.get(id=self.post_id)

    def test_create_comment(self):
        comment = Comment.objects.create(author=self.user, post=self.post_instance, text='This is a test comment')
        self.assertEqual(comment.text, 'This is a test comment')
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.post, self.post_instance)

    def test_comment_str_representation(self):
        comment = Comment.objects.create(author=self.user, post=self.post_instance, text='This is a test comment')
        self.assertEqual(str(comment), 'This is a test comment')

    def test_create_comment_with_blank_text(self):
        comment = Comment(author=self.user, post=self.post_instance, text='')
        with self.assertRaises(ValidationError):
            comment.full_clean()

    def test_create_comment_with_null_text(self):
        comment = Comment(author=self.user, post=self.post_instance, text=None)
        with self.assertRaises(ValidationError):
            comment.full_clean()

