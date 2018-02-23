
docker run -it --rm \
        --name=certbot \
        -v /root/wordsearch_solver/nginx/prod/certs/certs:/etc/letsencrypt \
        -v /root/wordsearch_solver/nginx/prod/certs/certs_data:/data/letsencrypt \
        -v /var/log/letsencrypt:/var/log/letsencrypt certbot/certbot  certonly  --force-renew --staging --email halcyonjuly7@gmail.com -d wordsearchsolver.halcyonramirez.com --agree-tos --webroot --webroot-path=/data/letsencrypt && docker-compose kill -s HUP nginx >/dev/null 2>&1