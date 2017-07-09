from django.conf.urls import url
from .views import show_all_cates,show_cate_detail,create_cate
urlpatterns = [
    url(r'^$',show_all_cates,name='category_list'),
    url(r'^create/$',create_cate,name="create_cate"),
    url(r'^(?P<slug>[\w-]+)/$',show_cate_detail,name='category_detail'),
]