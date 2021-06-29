FROM azul/zulu-openjdk:13

RUN groupadd -g 322 lavalink && useradd -r -u 322 -g lavalink lavalink

USER lavalink

WORKDIR /opt/lavalink

COPY Lavalink.jar Lavalink.jar

COPY application.yml application.yml

EXPOSE 2333

CMD ["java", "-Djdk.tls.client.protocols=TLSv1.1,TLSv1.2", "-jar", "Lavalink.jar"]