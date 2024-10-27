import random

def random_ip():
    nums = [random.randint(0, 255) for _ in range(4)]

    ip_address = ".".join(str(num) for num in nums)
    return ip_address

def Gen_Ip():
    for i in range(10):
        print(random_ip())