from django.urls import path

# mycode
from .views import home, contact, detail, post_new, post_edit, post_delete

urlpatterns = [
    path('home/', home, name="home"),
    path('contact/', contact, name="contact"),
    path('detail/<int:id>/', detail, name="detail"),
    path('post/new/', post_new, name="post_new"),
    path('post/edit/<int:id>/', post_edit, name="post_edit"),
    path('post/delete/<int:id>/', post_delete, name="post_delete")
]