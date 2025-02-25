
from itsdangerous import URLSafeTimedSerializer as Serializer


class Tokenise:

    def get_reset_token(self,c_user_id,expires_sec=1800):
        global app
        from app import app
        s = Serializer(app.config['SECRET KEY'])
        print('DEBUG Get Reset Token (self.id): ',c_user_id)
        return s.dumps({'user_id': c_user_id})

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None

        return user_id