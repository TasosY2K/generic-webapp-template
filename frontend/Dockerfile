FROM node:18 as builder

WORKDIR /app/frontend

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build 

FROM nginx:stable

COPY --from=builder /app/frontend/build /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/nginx.conf

EXPOSE 8000