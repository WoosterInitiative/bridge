import docker

from bridge.config import get_config
from bridge.service.postgres import PostgresConfig, PostgresService


def open_database_shell():
    client = docker.from_env()
    config = get_config()
    postgres_config = PostgresConfig(image=config.postgres_image)
    postgres_service = PostgresService(client=client, config=postgres_config)
    postgres_service.start()
    postgres_service.shell()


def dump_database():
    client = docker.from_env()
    postgres_service = PostgresService(client=client)
    postgres_service.start()
    postgres_service.dumpall()
