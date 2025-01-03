from app.database import db

class DspmTable(db.Model):
    __tablename__ = 'dspm_table'

    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(100))
    severity = db.Column(db.String(100))
    status = db.Column(db.String(100))
    qtd = db.Column(db.Integer)

    def __init__(self, service_type, severity, status, qtd):
        self.service_type = service_type
        self.severity = severity
        self.status = status
        self.qtd = qtd
    
    def to_dict(self):
        return {
            'id': self.id,
            'service_type': self.service_type,
            'severity': self.severity,
            'status': self.status,
            'qtd': self.qtd
        }
