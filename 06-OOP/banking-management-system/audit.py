
import datetime

class AuditableMixin:
    def log_audit(self,action:str):
     
     timestamp =datetime.datetime.now.isoformat()
     self.audit_log.append(f"[{timestamp}] {action}")
    
    def get_audit_log(self)->list:
       return self.audit_log


