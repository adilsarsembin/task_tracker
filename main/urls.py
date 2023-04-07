from rest_framework import routers

from .views import TaskViewSet, ReminderViewSet, StatusViewSet

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'reminders', ReminderViewSet)
router.register(r'statuses', StatusViewSet)

urlpatterns = router.urls
