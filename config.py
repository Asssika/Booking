from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_NAME: str
    DB_PASS: str
    DB_HOST: str
    DB_USER: str
    DB_PORT: int
    SECRET_KEY: str
    ALGORITM: str
    @property
    def DATABASE_URL(self):
        user = f'{self.DB_USER}:{self.DB_PASS}'
        database = f'{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
        return f'postgresql+asyncpg://{user}@{database}'

    class Config:
        env_file = 'env'


settings = Settings()

print(settings.DB_NAME)
