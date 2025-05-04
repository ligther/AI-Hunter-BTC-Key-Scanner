import os
import hashlib
import base58
import ecdsa
import multiprocessing
import time

TARGET_FILE = "addresses.txt"
FOUND_FILE = "found.txt"
CHECKED_FILE = "checked.txt"
NUM_PROCESSES = multiprocessing.cpu_count()

with open(TARGET_FILE, "r") as f:
    target_addresses = set(line.strip() for line in f if line.strip())

if os.path.exists(CHECKED_FILE):
    with open(CHECKED_FILE, "r") as f:
        checked_keys = set(line.strip() for line in f)
else:
    checked_keys = set()

counter = multiprocessing.Value("i", 0)
found = multiprocessing.Value("i", 0)

def private_to_address(private_key_hex):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key_hex), curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key().to_string()
    public_key = b'\x04' + vk
    sha256 = hashlib.sha256(public_key).digest()
    ripemd160 = hashlib.new('ripemd160', sha256).digest()
    address = base58.b58encode_check(b'\x00' + ripemd160).decode()
    return address

def worker_process(id, counter, found):
    while True:
        private_key = os.urandom(32).hex()
        if private_key in checked_keys:
            continue

        address = private_to_address(private_key)

        with counter.get_lock():
            counter.value += 1

        if address in target_addresses:
            with found.get_lock():
                found.value += 1
            print(f"[FOUND] [{id}] Address: {address} | Private Key: {private_key}")
            with open(FOUND_FILE, "a") as f:
                f.write(f"{address}\t{private_key}\n")

        with open(CHECKED_FILE, "a") as f:
            f.write(f"{private_key}\n")

def stats_display(counter, found):
    last_count = 0
    while True:
        time.sleep(5)
        with counter.get_lock():
            total = counter.value
        with found.get_lock():
            fcount = found.value
        speed = (total - last_count) / 5
        print(f"[STATS] Total Checked: {total} | Speed: {speed:.2f}/s | Found: {fcount}")
        last_count = total

def main():
    print(f"Launching {NUM_PROCESSES} workers...")
    processes = []

    for i in range(NUM_PROCESSES):
        p = multiprocessing.Process(target=worker_process, args=(i, counter, found))
        p.start()
        processes.append(p)

    stats_proc = multiprocessing.Process(target=stats_display, args=(counter, found))
    stats_proc.start()
    processes.append(stats_proc)

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()