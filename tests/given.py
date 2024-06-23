import random
import string

class Given:
    def password(self):
        return self.alpha_num_str(random.randint(1, 24))
    
    def alpha_num_str(self, n: int) -> str:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))