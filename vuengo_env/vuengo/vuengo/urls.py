
from django.urls import path, include

from rest_framework import routers # Import the router

from task.views import TaskViewSet # Import the view we just created

router = routers.DefaultRouter() # Define the router with our view
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)), # Add the view to the patterns
]