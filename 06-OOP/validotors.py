class Validators:
    @staticmethod
    def is_valid_id(item_id):
        return isinstance(item_id,int) and item_id>0
    
    @staticmethod
    def is_valid_title(title,str):
        return isinstance(title,str) and len(title.strip()) > 0
    