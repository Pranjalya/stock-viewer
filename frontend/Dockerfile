FROM node:12.2.0-alpine
COPY . /app
WORKDIR /app
EXPOSE 80

RUN npm install yarn && yarn && yarn run build