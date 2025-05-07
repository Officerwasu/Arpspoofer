# Arpspoofer

**Requirements:**

* **Root Privileges:** Necessary to send raw network packets.
* **scapy:** Install with `pip install scapy`.

**Usage:**

1.  **Save the Python code** as `arp_spoofer.py`.
2.  **Make it executable:**
    ```bash
    chmod +x arp_spoofer.py
    ```
3.  **Run with target and gateway IPs (as root):**
    ```bash
    sudo ./arp_spoofer.py
    ```
    Follow the prompts to enter the network range, target IP, and gateway IP.
4.  **Stop:** Press `Ctrl + C`.

**Important:** Use responsibly on your own network for learning.
