MOUNTS = -v "$(CURDIR)":/home/AirBnB_clone_v2
DEV_DOCKER_IMAGE_NAME = airbnbclonev2_console

build_docker_image:
	docker build -t $(DEV_DOCKER_IMAGE_NAME) .

# start container in interactive mode for in-container development
dev: build_docker_image
	docker run -ti --rm $(MOUNTS) -v /var/run/docker.sock:/var/run/docker.sock $(DEV_DOCKER_IMAGE_NAME) bash -c 'cd home/AirBnB_clone_v2; /bin/bash'
