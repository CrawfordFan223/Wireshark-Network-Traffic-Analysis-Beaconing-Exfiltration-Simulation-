Wireshark Network Traffic Analysis (Beaconing & Exfiltration Simulation)

# Wireshark Malware Simulation (Safe Demo)

**Objective:** Simulate C2 beaconing and HTTP exfiltration in an isolated lab and analyze the traffic with Wireshark.

**Environment**
- Host: Windows 11 (Reciever)
- VM: Windows 10 (Attacker)
- Virtualization: VirtualBox (Host-Only network)
- Tools: Wireshark, Python 3 (`requests`)

**Files**
- `beacon.py` — VM script: periodic GET /checkin (educational/demo).
- `exfil.py` — VM script: single POST /upload (sends dummy text).
- `listener_simple.py` — host listener to receive/log requests.
- `listener_log.txt` — host listener log showing receipt of POST (sanitized).
- `screenshots/` — evidence screenshots (GET/POST, TCP streams, Conversations, IO Graph).
- `Report.pdf` — short write-up with findings.

**How to reproduce (lab, isolated environment only)**
1. On host: run `python listener_simple.py`.  
2. On host: start Wireshark capturing the Host-Only adapter.  
3. On VM: `python -m pip install requests` if needed.  
4. On VM: run `python beacon.py` (periodic GETs).  
5. On VM: run `python exfil.py` (single POST).  
6. Inspect Wireshark, follow TCP streams, and view screenshots in `/screenshots`.

**Safety note**
- This repo contains no real malware and no raw pcaps. Do not run outside an isolated lab.

I Know this is nothing but its my first ever upload here so hopefully ill be better in the future


