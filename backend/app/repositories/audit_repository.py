from backend.app.models.audit_log import AuditLog


class AuditRepository:

    @staticmethod
    def create(
        db,
        audit
    ):
        db.add(audit)