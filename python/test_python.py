import docker
import pytest

@pytest.fixture
def docker_container(request):
    """Fixture creates a docker image based on the given image name
    and path to the dockerfile directory, returns the created container"""
    
    client = docker.from_env()
    image_name = request.param['image']
    build_context = request.param['path']

    image, logs = client.images.build(path=build_context, tag=image_name)

    for log_line in logs:
        print(log_line)

    # If detach=False, container run method will just return the log output, not the 
    # container obj bc container is stopped at this point
    container = client.containers.run(image, detach=True)
    yield container

    # Clean up: Stop and remove the container
    container.stop()
    container.remove()

class TestNullChar:

    @pytest.mark.parametrize(
            'docker_container',
            [
               {
                   'image': 'rosetta-python:null_char',
                    'path': './python/null_char'
                } 
            ],
            indirect=True,
    )
    def test_null_char(self, docker_container):
        # Have to wait on container to get the logs
        docker_container.wait()
        assert docker_container.logs() == b'Hello World \x00\n'

class TestStdIn:
    """Check that input is read from stdin line by line.
    The script executed in the docker container accepts a text file as input,
    reads each line, capitalizes it, then prints it out.
    """
    @pytest.mark.parametrize(
            'docker_container',
            [
               {
                   'image': 'rosetta-python:stdin',
                    'path': './python/stdin'
                } 
            ],
            indirect=True,
    )
    def test_stdin(self, docker_container):
        i = 1
        expected = ""
        with open('python/stdin/stdin.txt', 'r') as f:
            for line in f.readlines():
                expected += f"{i} {line.upper()}"
                i += 1
        docker_container.wait()
        assert str(docker_container.logs(), 'UTF-8') == expected

# to run in command line:
# docker run -it --rm rosetta-python