import docker
import pytest

@pytest.fixture
def docker_container(request):
    client = docker.from_env()

    image_name = request.param['image']

    build_context = request.param['path']

    image, logs = client.images.build(path=build_context, tag=image_name)

    for log_line in logs:
        print(log_line)

    
    # Not enough memory to run the container, only to create and stop it
    # If detach=False, container run method will just return the log output, not the 
    # container obj bc container is stopped at this point
    container = client.containers.run(image, detach=True)
    yield container

    # Clean up: Stop and remove the container
    container.stop()
    container.remove()

class TestPython:
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
        docker_container.wait()
        assert docker_container.logs() == b'HI HELLO HOW ARE YOU?\n'

# to run in command line:
# docker run -it --rm rosetta-python



# input_string = "Hello from STDIN!"
# container.exec_run("python std")
# # Run a command to upload the input_string to the container's STDIN
# result = subprocess.run(['docker', 'exec', container_id, 'python', '-c', 'print(input())'],input=input_string,capture_output=True,text=True)
# when testing for stdin - make sure to wait to make sure it's not discarding. 
# have the script print something out 