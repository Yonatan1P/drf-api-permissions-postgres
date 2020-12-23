from django.contrib.auth import get_user_model
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_port = Post.objects.create(
            author = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)

        self.assertEqual(str(post.author), 'tester')
        self.assertEqual(post.title, 'Title of Blog')
        self.asserEqual(post.body, 'Words about the blog')

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        
        test_post = Post.objects.create(
            author=testuser1, title='Blog title', body='Body content...')
        test_post.save()
    def test_blog_content(self):
        post =  Post.objects.get(id=1)
        expected_author = f'{post.author}'
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_title, 'Blog title')
        self.assertEqual(expected_body, 'Body content...')