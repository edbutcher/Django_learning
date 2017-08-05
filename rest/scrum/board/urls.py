from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'sprints', views.SprintViewSet.as_view(), 'sprint')
router.register(r'tasks', views.TaskViewSets.as_view(), 'task')
router.register(r'users', views.UserSerializer.as_view(), 'user')
