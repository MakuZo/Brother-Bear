from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from core.forms import ShortenURLForm
from core.models import ShortenedURL
from core.utils import get_short_id


class ShortenUrlView(View):
    """View to create shortened urls"""
    form_class = ShortenURLForm
    template_name = "core/shorten_url.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        """Returns shortened url. If url is already shortened, returns saved url."""
        form = self.form_class(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            if ShortenedURL.objects.filter(url=url).exists():
                u = ShortenedURL.objects.get(url=url)
            else:
                u = ShortenedURL.objects.create(url=url, id=get_short_id())
            return render(request, "core/results.html", {"url": u, "request": request})
        return render(request, self.template_name, {"form": form})


class RedirectURLView(View):
    """View to redirect shortened url to the origin url"""

    def get(self, request, id):
        obj = get_object_or_404(ShortenedURL, pk=id)
        return redirect(obj.url)
