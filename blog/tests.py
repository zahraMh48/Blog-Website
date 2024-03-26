from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse



class BlogPostTest(TestCase):
    # def setUp(self): #we have self, for one object

    @classmethod  #a method that access to class not one object
    def setUpTestData(cls): #we have cls (classmethod), access to class
        cls.user = User.objects.create(username='user1')
        cls.testpost = Post.objects.create(
            title='testpost',
            text='this is the discription of testpost',
            status=Post.STATUS_CHOICES[0][0], # or status='pub
            author=cls.user,
        )

        cls.post2= Post.objects.create(
            title='post2',
            text='this is post2 status: draft',
            status=Post.STATUS_CHOICES[1][0],
            author=cls.user,
        )

    def test_post_model_str(self): # alwase write it!
        post = self.testpost
        self.assertEqual(str(post), post.title)

    def test_post_detaile(self):
        self.assertEqual(self.testpost.title, 'testpost')
        self.assertEqual(self.testpost.text, 'this is the discription of testpost')


    def test_blog_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_list_by_name(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('blog_list'))
        self.assertContains(response, self.testpost.title)

    def test_post_detail_url(self):
        response=self.client.get(f'/blog/{self.testpost.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_by_name(self):
        response = self.client.get(reverse('post_detail',args=[self.testpost.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(reverse('post_detail',args=[self.testpost.id]))
        self.assertContains(response, self.testpost.title)
        self.assertContains(response, self.testpost.text)

    def test_status_404_post_id_not_exist(self):
        response=self.client.get(reverse('post_detail',args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_post_list_template_correct(self):
        response=self.client.get(reverse('blog_list'))
        self.assertTemplateUsed(response,'blog/posts_list.html')

    def test_post_detail_template_correct(self):
        response=self.client.get(reverse('post_detail', args=[self.testpost.id]))
        self.assertTemplateUsed(response,'blog/post_detail.html')

    def test_draft_post_not_show_in_post_list(self):
        response = self.client.get(reverse('blog_list'))
        self.assertContains(response, self.testpost.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'),{
            'title': 'some title',
            'text': 'some text',
            'status': 'pub',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'some title')
        self.assertEqual(Post.objects.last().text, 'some text')
        self.assertEqual(Post.objects.last().status, 'pub')
        self.assertEqual(Post.objects.last().author, self.user)

    def test_post_update_view(self):
        response = self.client.post(reverse('post_update', args=[self.post2.id]), {
            'title': 'some title update',
            'text': 'this text update',
            'status': 'pub',
            'author': self.post2.author.id,
        })
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title, 'some title update')
        self.assertEqual(Post.objects.last().text, 'this text update')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post2.id]))
        self.assertEqual(response.status_code,302)











