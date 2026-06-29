build:
	docker build -t holaflask .

run:
	docker run -p 5000:5000 holaflask

compose:
	docker-compose up --build

deploy:
	docker stack deploy -c stack.yml holaflask