docker exec -it redis-7000 redis-cli --cluster create \
    172.23.0.6:7000 172.23.0.5:7001 172.23.0.7:7002 \
    172.23.0.2:7003 172.23.0.4:7004 172.23.0.3:7005 \
    --cluster-replicas 1

    