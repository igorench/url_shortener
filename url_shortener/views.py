from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Url
from .forms import UrlForm, UrlFormCreate
from .form_utils import get_absolute_short_path
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class UrlList(View):
    def get(self, request):
        urls = Url.objects.all().order_by("-created_at")
        form = UrlFormCreate()

        page = request.GET.get("page", 1)

        paginator = Paginator(urls, 6)
        try:
            urls = paginator.page(page)
        except PageNotAnInteger:
            urls = paginator.page(1)
        except EmptyPage:
            urls = paginator.page(paginator.num_pages)

        return render(
            request=request,
            template_name="url_shortener/index.html",
            context={"urls": urls, "form": form},
        )

    def post(self, request):
        form = UrlFormCreate(request.POST)

        if form.is_valid():
            form.save()
            form = UrlFormCreate()

        urls = Url.objects.all().order_by("-created_at")

        page = request.GET.get("page", 1)

        paginator = Paginator(urls, 6)
        try:
            urls = paginator.page(page)
        except PageNotAnInteger:
            urls = paginator.page(1)
        except EmptyPage:
            urls = paginator.page(paginator.num_pages)

        return render(
            request=request,
            template_name="url_shortener/index.html",
            context={"urls": urls, "form": form},
        )


class UrlDetail(View):
    def get(self, request, pk):
        url = get_object_or_404(Url, pk=pk)
        bound_form = UrlForm(instance=url)

        return render(
            request=request,
            template_name="url_shortener/detail.html",
            context={"url": url, "form": bound_form},
        )

    def post(self, request, pk):
        url = get_object_or_404(Url, pk=pk)
        form = UrlForm(request.POST, instance=url)

        if form.is_valid():
            new_url = form.save()
            redirect(new_url)

        return render(
            request=request,
            template_name="url_shortener/detail.html",
            context={"url": url, "form": form},
        )


class FindOriginalUrl(View):
    def get(self, request, short_url):
        url = get_object_or_404(Url, short_url=get_absolute_short_path(short_url))
        if url:
            url.clicks += 1
            url.save()

            return redirect(url.original_url)


class UrlDelete(View):
    def get(self, request, pk):
        url = Url.objects.get(pk=pk)

        return render(
            request=request,
            template_name="url_shortener/delete.html",
            context={"url": url},
        )

    def post(self, request, pk):
        url = Url.objects.get(pk=pk)
        url.delete()

        return redirect("main_page")
