from django.conf.urls import url

from .views import (ProductListView, 
                            #ProductFeaturedListView,
                            # product_list_view, 
                            # ProductDetailView,
                            ProductDetailSlugView,
                            # ProductFeaturedDetailView, 
                            # product_detail_view
                            ) 

#from .views import home_page, about_page, contact_page, login_page, register_page


urlpatterns = [
    url(r'^$', ProductListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]
