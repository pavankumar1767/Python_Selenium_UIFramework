from enum import Enum


class ConfigSection(Enum):
    CREDENTIALS = "credentials"

class CredentialsOption(Enum):
    BASE_URL = "baseURL"
    USERNAME = "useremail"
    PASSWORD = "password"
