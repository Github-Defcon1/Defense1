# agent_id >> id da maquina X
# composite_id >> id da detecção X
# assigned_to_name >> nome do analista X
# assigned_to_uid >> email do analista X
# created_timestamp >> data de criação da detecção X
# description >> descrição do incidente X
# groups >> id do grupo (device.groups) X
# hostname X
# os_version >> sistema operacional X
# platform_name >> tipo da plataforma X
# product_type_desc >> tipo de produto X
# display_name >> gatilho de detecção X
# filename >> nome do arquivo X
# filepath >> caminho do arquivo X
# local_prevalence >> frequencia de detecção do arquivo localmente X
# seconds_to_triaged >> tempo ate a triagem
# seconds_to_resolved >> tempo de resolução
# severity_name >> severidade da detecção
# sha256 >> hash do arquivo que gerou a detecção
# status >> status do incidente 
# tactic >> tatica detectada
# tactic_id >> id da tatica
# technique >> tecnica detectada
# technique_id >> id da tecnica

from app.database import db
from datetime import datetime

class EppTable(db.Model):
    __tablename__ = 'epp_detections_table'

    id = db.Column(db.Integer, primary_key=True)
    agent_id = db.Column(db.String(100))
    composite_id = db.Column(db.String(150))
    assigned_to_name = db.Column(db.String(100))
    assigned_to_uid = db.Column(db.String(100))
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(1000))
    id_groups = db.Column(db.String(100)) #Chave secundaria
    groups = db.Column(db.String(100))
    hostname = db.Column(db.String(100))
    os_version = db.Column(db.String(100))
    platform_name = db.Column(db.String(100))
    product_type_desc = db.Column(db.String(100))
    display_name = db.Column(db.String(100))
    filename = db.Column(db.String(1000))
    filepath = db.Column(db.String(1000))
    local_prevalence = db.Column(db.String(100))
    seconds_to_triaged = db.Column(db.Integer)
    seconds_to_resolved = db.Column(db.Integer)
    severity_name = db.Column(db.String(100))
    sha256 = db.Column(db.String(64))
    status = db.Column(db.String(100))
    tactic = db.Column(db.String(100))
    tactic_id = db.Column(db.String(100))
    technique = db.Column(db.String(100))
    technique_id = db.Column(db.String(100))

    def __init__(self, agent_id, composite_id, assigned_to_name, assigned_to_uid, created_timestamp, description, id_groups, groups, hostname, os_version, platform_name, product_type_desc, display_name, filename, filepath, local_prevalence, seconds_to_triaged, seconds_to_resolved, severity_name, sha256, status, tactic, tactic_id, technique, technique_id):
        self.agent_id = agent_id
        self.composite_id = composite_id
        self.assigned_to_name = assigned_to_name
        self.assigned_to_uid = assigned_to_uid
        self.created_timestamp = created_timestamp
        self.description = description
        self.id_groups = id_groups
        self.groups = groups
        self.hostname = hostname
        self.os_version = os_version
        self.platform_name = platform_name
        self.product_type_desc = product_type_desc
        self.display_name = display_name
        self.filename = filename
        self.filepath = filepath
        self.local_prevalence = local_prevalence
        self.seconds_to_triaged = seconds_to_triaged
        self.seconds_to_resolved = seconds_to_resolved
        self.severity_name = severity_name
        self.sha256 = sha256
        self.status = status
        self.tactic = tactic
        self.tactic_id = tactic_id
        self.technique = technique
        self.technique_id = technique_id

    def to_dict(self):
        return {
        'agent_id': self.agent_id,
        'composite_id': self.composite_id,
        'assigned_to_name': self.assigned_to_name, 
        'assigned_to_uid': self.assigned_to_uid,
        'created_timestamp': self.created_timestamp,
        'description': self.description,
        'id_groups': self.id_groups,
        'groups': self.groups,
        'hostname': self.hostname,
        'os_version': self.os_version,
        'platform_name': self.platform_name,
        'product_type_desc': self.product_type_desc,
        'display_name': self.display_name,
        'filename': self.filename,
        'filepath': self.filepath,
        'local_prevalence': self.local_prevalence,
        'seconds_to_triaged': self.seconds_to_triaged,
        'seconds_to_resolved': self.seconds_to_resolved,
        'severity_name': self.severity_name,
        'sha256': self.sha256,
        'status': self.status,
        'tactic': self.tactic,
        'tactic_id': self.tactic_id,
        'technique': self.technique,
        'technique_id': self.technique_id
        }
