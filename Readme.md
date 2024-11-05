# Redis cluster setup local using docker for testing and practice

# Docker compose 
*  Contains 6 redis instance running from port 7000 - 7005
*  Each Instance has seperate config files for configuration

## Configuration
* The create_cluster_config.py will generate the necessary cmd to create cluster.
* I have avoided using container hostname as it's not resolving to create the cluster configuration
* This will create 3 master and 3 slaves.

### Notes

### CMD
``` INFO replication ```

``` 
docker exec -it redis-7000 redis-cli --cluster create \
    172.23.0.6:7000 172.23.0.5:7001 172.23.0.7:7002 \
    172.23.0.2:7003 172.23.0.4:7004 172.23.0.3:7005 \
    --cluster-replicas 1
```
