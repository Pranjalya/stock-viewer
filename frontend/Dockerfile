# FROM node:12.2.0-alpine as build
# WORKDIR /app
# ENV PATH /app/node_modules/.bin:$PATH
# COPY package.json /app/package.json
# RUN yarn --silent
# # RUN npm install react-scripts@3.0.1 -g --silent
# COPY . /app
# RUN yarn build

# # production environment
# FROM nginx:1.16.0-alpine
# COPY --from=dist /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]

FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
