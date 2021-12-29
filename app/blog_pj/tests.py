from django.test import TestCase
import pytest
from blog_pj.models import Blog

@pytest.mark.django_db
def test_create_blog():
    blog = Blog.objects.create(
        title='Pytest',
        blog_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Using pytest on my django project',
        published=True
    )
    assert blog.title == "Pytest"