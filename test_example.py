# for language in languages
#     run the script and check the output matches
import docker
import pytest

@pytest.fixture
def docker_container():
    client = docker.from_env()
    image_name = 'rosetta-python:latest'
    
    # Not enough memory to run the container, only to create and stop it
    # If detach=False, container run method will just return the log output, not the 
    # container obj bc container is stopped at this point
    container = client.containers.run(image_name, detach=True)
    yield container
    
    # Clean up: Stop and remove the container
    container.stop()
    container.remove()

class TestPython:
    def test_null_char(self, docker_container):
        # Have to wait on container to get the logs
        docker_container.wait()
        assert docker_container.logs() == b'Hello World \x00\n'

# to run in command line:
# docker run -it --rm rosetta-python