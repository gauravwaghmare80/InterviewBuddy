# technical_assessment/services.py
import docker

def execute_code(code, input_data):
    client = docker.from_env()
    container = client.containers.run(
        'python:3.9-slim',
        f'python -c "{code}"',
        stdin_open=True,
        detach=True
    )
    container.put_archive(input_data.encode())
    result = container.wait()
    logs = container.logs()
    container.remove()
    return logs.decode()