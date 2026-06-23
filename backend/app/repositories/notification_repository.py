from backend.app.models.notification import Notification


class NotificationRepository:

    @staticmethod
    def create(
        db,
        notification
    ):
        db.add(notification)