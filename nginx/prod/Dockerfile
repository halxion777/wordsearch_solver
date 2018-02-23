FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY conf/nginx.conf /etc/nginx/conf.d
COPY conf/ssl_params.conf /etc/nginx
CMD ["nginx", "-g", "daemon off;"]
