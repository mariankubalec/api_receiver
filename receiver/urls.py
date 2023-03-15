from django.urls import path
# from . import views
from .views import (
    index,
    visualizer,
    ReceiveAddView,
)


urlpatterns = [
    path('index/', index, name='index'),
    path('receiver/', visualizer, name='visualizer'),
    path('api/receive/', ReceiveAddView.as_view()),
]