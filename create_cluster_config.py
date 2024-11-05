import subprocess

# List of Redis container names with their corresponding ports
redis_containers = {
    "redis-7000": "7000",
    "redis-7001": "7001",
    "redis-7002": "7002",
    "redis-7003": "7003",
    "redis-7004": "7004",
    "redis-7005": "7005"
}

# Function to get IP address for each container
def get_container_ip(container_name):
    try:
        result = subprocess.check_output(
            ["docker", "inspect", "-f", "{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}", container_name],
            text=True
        ).strip()
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving IP for {container_name}: {e}")
        return None

# Collect IP addresses and ports for all containers
redis_nodes = []
for container, port in redis_containers.items():
    ip = get_container_ip(container)
    if ip:
        redis_nodes.append(f"{ip}:{port}")

# Check if all IPs were retrieved successfully
if len(redis_nodes) == len(redis_containers):
    # Build the Redis cluster creation command
    cluster_command = (
        "docker exec -it redis-7000 redis-cli --cluster create "
        + " ".join(redis_nodes) +
        " --cluster-replicas 1"
    )
    print("Generated Redis cluster creation command:")
    print(cluster_command)
else:
    print("Failed to retrieve all container IPs. Please check the Docker containers.")
