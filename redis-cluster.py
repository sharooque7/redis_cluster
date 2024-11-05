import redis
from redis.cluster import RedisCluster as Redis
from redis.exceptions import RedisError
from redis.cluster import ClusterNode

def main():
    try:
        nodes = [
            ClusterNode('redis-7000', 7000),
            ClusterNode('redis-7001', 7001),
            ClusterNode('redis-7002', 7002),
            ClusterNode('redis-7003', 7003),
            ClusterNode('redis-7004', 7004),
            ClusterNode('redis-7005', 7005)
        ]

        cluster = Redis(startup_nodes=nodes, decode_responses=True)
        
        print("Connected to Redis Cluster:")
        print(cluster.get_nodes())

        # Set a key in the cluster
        key = "name"
        value = "sharooye"
        cluster.set(key, value)
        print(f"Set {key} = {value} in the Redis cluster.")

        # Retrieve the key from the cluster
        retrieved_value = cluster.get(key)
        print(f"Retrieved {key} = {retrieved_value} from the Redis cluster.")

        # Delete the key
        cluster.delete(key)
        print(f"Deleted {key} from the Redis cluster.")

        # Check if the key still exists
        exists = cluster.exists(key)
        print(f"Does {key} exist? {'Yes' if exists else 'No'}")

    except RedisError as e:
        print(f"Redis error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
