from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post


class PostModelTests(TestCase):
    def setUp(self):
        # Create a dummy user to be used as an author
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

    def test_post_creation_and_str(self):
        """Test the creation of a Post instance and its __str__ method."""
        post = Post.objects.create(
            author=self.user,
            title="Test Title",
            text="This is the test content of the post.",
            category="Test Category",
        )
        self.assertIsInstance(post, Post)
        self.assertEqual(str(post), "Test Title")
        self.assertEqual(post.author.username, "testuser")
        self.assertEqual(post.text, "This is the test content of the post.")
        self.assertEqual(post.category, "Test Category")


class PageViewTests(TestCase):
    def setUp(self):
        # Create a dummy user and a post for detail view tests
        self.user = User.objects.create_user(
            username="testuser_views", password="testpassword"
        )
        self.post = Post.objects.create(
            author=self.user,
            title="View Test Post",
            text="Content for view test post.",
            category="Views",
        )

    def test_index_page_status_code(self):
        """Test that the index page returns a 200 status code."""
        response = self.client.get(reverse("page:index"))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_page_status_code(self):
        """Test that the post detail page returns a 200 status code for an existing post."""
        response = self.client.get(reverse("page:post_detail", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_page_404_for_invalid_post(self):
        """Test that the post detail page returns a 404 for a non-existent post."""
        invalid_pk = self.post.pk + 100  # An ID that is unlikely to exist
        response = self.client.get(reverse("page:post_detail", args=[invalid_pk]))
        self.assertEqual(response.status_code, 404)

    def test_about_page_status_code(self):
        """Test that the about page returns a 200 status code."""
        response = self.client.get(reverse("page:about"))
        self.assertEqual(response.status_code, 200)

    def test_science_page_status_code(self):
        """Test that the science page returns a 200 status code."""
        response = self.client.get(reverse("page:science"))
        self.assertEqual(response.status_code, 200)

    def test_business_page_status_code(self):
        """Test that the business page returns a 200 status code."""
        response = self.client.get(reverse("page:business"))
        self.assertEqual(response.status_code, 200)

    def test_career_page_status_code(self):
        """Test that the career page returns a 200 status code."""
        response = self.client.get(reverse("page:career"))
        self.assertEqual(response.status_code, 200)

    def test_product_page_status_code(self):
        """Test that the product page returns a 200 status code."""
        response = self.client.get(reverse("page:product"))
        self.assertEqual(response.status_code, 200)

    def test_plan_page_status_code(self):
        """Test that the plan page returns a 200 status code."""
        response = self.client.get(reverse("page:plan"))
        self.assertEqual(response.status_code, 200)
