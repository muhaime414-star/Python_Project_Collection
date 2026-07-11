import random

def generate_mock_logs(filename, total_lines):
    print(f"Generating {total_lines} log entries...")
    
    ip_pool = []
    for _ in range(300):
        octet1 = random.randint(11, 250)
        octet2 = random.randint(0, 255)
        octet3 = random.randint(0, 255)
        octet4 = random.randint(1, 254)
        ip_pool.append(f"{octet1}.{octet2}.{octet3}.{octet4}")

    with open(filename, 'w') as file:
        for _ in range(total_lines):
            random_ip = random.choice(ip_pool)
            file.write(f"{random_ip}\n")
   
   
    print(f"Success! Mock logs saved to {filename}")

generate_mock_logs('massive_server_logs.txt', 1001)


