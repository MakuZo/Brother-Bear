from django.test import TestCase
from django.shortcuts import reverse

from core.views import ShortenUrlView
from core.models import ShortenedURL

class TestShortenUrlView(TestCase):
    url = reverse("shorten-url-view")

    def test_if_url_in_database_return_same_id(self):
        """If url already exists in database, return it's id instead of creating new"""
        s = ShortenedURL.objects.create(id="XYZ", url="https://google.com")
        response = self.client.post(self.url, data={'url': "https://google.com"})
        self.assertEqual(response.context['url'].pk, s.pk)
    

class TestRedirectUrlView(TestCase):

    def test_redirect_url(self):
        """Ensure that view returns correct url"""
        s = ShortenedURL.objects.create(id="XYZ", url="https://google.com")
        url = reverse('redirect-url-view', kwargs={'id': s.id})
        response = self.client.get(url)
        self.assertEqual(response.url, "https://google.com")



