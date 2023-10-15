# Run this docker command
# Tags: https://hub.docker.com/r/skilltree/skills-service/tags
docker run --network=host --name skills-service -d -p 8080:8080 -e SPRING_PROPS="\
spring.datasource.url=jdbc:postgresql://localhost:5432/skills,\
spring.datasource.username=skills,\
spring.datasource.password=skillsPassword" skilltree/skills-service:2.10.0

# Postgres SQL
docker run --network=host -e POSTGRES_USER=skills -e POSTGRES_PASSWORD=skillsPassword -d postgres
