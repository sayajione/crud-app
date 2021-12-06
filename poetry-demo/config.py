from pydantic import BaseSettings, SecretStr, Field
from typing import Optional

# from src.models import User
# class CrudConfig(BaseSettings):
#     USER : str = None
#     PASSWORD : str = None
#     HOST : str = None
#     PORT : int = None

#     class Config:
#         env_file : str = '.env'

class CrudConfigv2(BaseSettings):
    USER : SecretStr = None     
    PASSWORD: SecretStr = None 
    HOST : SecretStr= None 
    PORT: SecretStr= None 
    # ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    class Config:
        secrets_dir = './secrets'

# class DevConfig(CrudConfigv2):
#     class Config:
#         env_prefix : str = "SYSTEM"


# class ConfigSelection:
#     def __init__(self, env_state: Optional[str]):
#         self.env_state = env_state
    
#     def __call__(self):
#         if self.env_state == "SYS":
#             return DevConfig()

#         else:
#             return CrudConfigv2()


# cnf = ConfigSelection(CrudConfigv2().ENV_STATE)()
cnf = CrudConfigv2()
print(cnf.__str__())



emp = Employee()

