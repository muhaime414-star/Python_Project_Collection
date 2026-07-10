import random

def generate_mock_logs(filename, total_lines):
    print(f"Generating {total_lines} log entries...")
    
    # 1. Create a pool of 300 random "public" IPs. 
    # (We keep the pool smaller than the total lines so we guarantee duplicates!)
    ip_pool = []
    for _ in range(300):
        # We start the first octet at 11 to avoid the 10.x.x.x private network range
        octet1 = random.randint(11, 250)
        octet2 = random.randint(0, 255)
        octet3 = random.randint(0, 255)
        octet4 = random.randint(1, 254)
        ip_pool.append(f"{octet1}.{octet2}.{octet3}.{octet4}")

    # 2. Write random choices from our pool into the log file
    with open(filename, 'w') as file:
        for _ in range(total_lines):
            # random.choice picks one IP from our pool at random
            random_ip = random.choice(ip_pool)
            file.write(f"{random_ip}\n")

    print(f"Success! Mock logs saved to {filename}")

# Generate a file with 1,000 lines
generate_mock_logs('massive_server_logs.txt', 1000)