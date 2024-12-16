# Authentication microservice
Authentication microservice with system of roles, OAuth, tests.
### Built with
* ![Docker][Docker]
* ![Fastapi][Fastapi]
* ![PostgreSQL][PostgreSQL]
* ![Redis][Redis]
* ![Jaeger][Jaeger]
* ![Uvicorn][Uvicorn]

### Scheme of services
<image src="readme/openapi.png" alt="OpenAPI"> </image>


### Environment
Create .env file using .env.example.

### Run
```
docker compose up --build
```

### OpenAPI
```
http://127.0.0.1:8081/api/openapi
```


[Redis]: https://img.shields.io/badge/redis-000000?style=for-the-badge&logo=redis&logoColor=red
[Docker]: https://img.shields.io/badge/docker-000000?style=for-the-badge&logo=docker&logoColor=blue
[Fastapi]: https://img.shields.io/badge/fastapi-000000?style=for-the-badge&logo=fastapi&logoColor
[PostgreSQL]: https://img.shields.io/badge/postgresql-000000?style=for-the-badge&logo=postgresql&logoColor=blue
[Uvicorn]: https://img.shields.io/badge/uvicorn-000000?style=for-the-badge&logo=uvicorn&logoColor=green
[Jaeger]: https://img.shields.io/badge/jaeger-000000?style=for-the-badge&logo=jaeger&logoColor=blue