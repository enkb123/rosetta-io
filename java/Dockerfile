FROM eclipse-temurin:22

# downloaded from
# "" https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind/2.17.1
# "" https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-core
# "" https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-annotations/2.17.1
# some documentation: https://www.pexus.com/perflog/javadocs/index.html?overview-summary.html
# when editing classpath change java.project.referencedLibraries in settings.json
ENV CLASSPATH=jackson-annotations-2.17.1.jar:jackson-core-2.17.1.jar:jackson-databind-2.17.1.jar

WORKDIR /app
COPY ./ /app
