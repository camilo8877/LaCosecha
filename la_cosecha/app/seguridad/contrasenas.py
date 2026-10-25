from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hashear(password: str):
    return pwd_context.hash(password)

def verificar(password: str, password_hash: str):
    return pwd_context.verify(password, password_hash)