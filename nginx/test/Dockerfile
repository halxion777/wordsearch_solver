FROM nginx:latest

COPY conf/nginx.conf /etc/nginx/conf.d
RUN rm /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]