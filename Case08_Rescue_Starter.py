"""CASE 08: THE SILENT BEACON | APPDAET
Student starter: 30-minute group coding rescue investigation.
All places, agencies, and events are fictional.
Keep evidence unchanged. Complete the TODO functions and RUN them.
"""

# ======================= LOCKED EVIDENCE =======================
# Dictionary: site -> site information. The drone's auto-landing
# software can accept only certified emergency pads.
SITES = {
    "HILL_CLINIC":    {"label": "Hill Clinic",     "certified": True,  "sector": "North Ridge"},
    "CIVIC_STADIUM":  {"label": "Civic Stadium",   "certified": True,  "sector": "Central"},
    "MARKET_ROOF":    {"label": "Market Roof",     "certified": False, "sector": "Old Town"},
    "RIVER_SCHOOL":   {"label": "River School",    "certified": True,  "sector": "Riverside"},
    "PORT_WAREHOUSE": {"label": "Port Warehouse",  "certified": True,  "sector": "Harbor"},
}

# LIST of TUPLES: (time, landing-site code, receiving relay).
# Some entries are duplicates, off-channel, or outside the valid window.
SIGNAL_EVENTS = [
    ("18:38", "CIVIC_STADIUM", "NORTH"),
    ("18:39", "MARKET_ROOF", "NORTH"),
    ("18:40", "RIVER_SCHOOL", "NORTH"),
    ("18:40", "HILL_CLINIC", "NORTH"),
    ("18:40", "HILL_CLINIC", "NORTH"),  # repeated transmission
    ("18:41", "PORT_WAREHOUSE", "NORTH"),
    ("18:40", "CIVIC_STADIUM", "WEST"),
    ("18:41", "MARKET_ROOF", "SOUTH"),
    ("18:42", "RIVER_SCHOOL", "EAST"),
    ("18:44", "CIVIC_STADIUM", "NORTH"),
]

# Ground sensors detected a thermal/cargo-pod-shaped signature.
# This is supporting evidence, not by itself a unique identification.
POD_SIGNATURE_MATCHES = {
    "HILL_CLINIC", "MARKET_ROOF", "PORT_WAREHOUSE", "CIVIC_STADIUM"
}

# These sites were definitively CLEARED by continuous, independent
# visual verification during the touchdown interval.
# At Port Warehouse, a service heater caused a look-alike sensor pulse.
VERIFIED_FALSE_ALERTS = {"PORT_WAREHOUSE"}

VALID_WINDOW = ("18:39", "18:42")  # inclusive, 24-hour HH:MM
RELAYS = {"NORTH", "SOUTH", "EAST", "WEST"}
CODED_NOTE = "FHV MLIGS IVOZB"

# ======================== MISSION FUNCTIONS =======================
def decode_mirror(message):
    """Decode uppercase letters by reflecting A<->Z, B<->Y, etc."""
    decoded = ""
    for char in message:
        if "A" <= char <= "Z": 
            decoded += chr(ord("A") + ord("Z") - ord(char))                    
        else:
            decoded += char
    return decoded


def sites_from_relay(events, relay, time_window):
    """Return SET of sites whose relay handshake is within window."""
    sightings = []  # MISSION 2: append qualifying site codes to this LIST.
    start, end = time_window  # unpack the window TUPLE.
    for timestamp, site_code, receiver in events:  # unpack event TUPLES.
        # MISSION 2: filter by matching relay AND inclusive time bounds.
        pass
    return set(sightings)  # collapse duplicate transmissions.


def certified_sites(sites):
    """Return SET of keys whose site dictionary has certified == True."""
    result = set()
    for code, details in sites.items():
        if details["certified"] == True:
            result.add(code)
    return result


def locate_pod(sightings, eligible, signatures, false_alerts):
    """Intersection of positive evidence MINUS definitively cleared sites."""
    # MISSION 4: Use sets, & (intersection) and - (difference).
    return (sightings & eligible & signatures) - false_alerts


def explain_sites(sites, sightings, eligible, signatures, false_alerts):
    """Return DICTIONARY: site code -> evidence-based explanation."""
    findings = {}
    for code in sites:
        reasons = []
      
        if code not in sightings:
            reasons.append("Not in sightings")
        if code not in eligible:
            reasons.append("Not certified")
        if code not in signatures:
            reasons.append("No pod-signature match")
        if code in false_alerts:
            reasons.append("Independently cleared as false alert")
        
        # If no failures, use: 'RETAINED: all verification rules satisfied'.
        findings[code] = "; ".join(reasons) if reasons else "RETAINED: all verification rules satisfied"
    return findings


def run_checks():
    """Tests use artificial records and DO NOT disclose the real location."""
    cipher_ok = decode_mirror("Z Y A") == "A B Z"
    sample = [
        ("18:39", "TEST_PAD", "NORTH"),
        ("18:39", "TEST_PAD", "NORTH"),
        ("18:42", "EDGE_PAD", "NORTH"),
        ("18:43", "TOO_LATE", "NORTH"),
        ("18:40", "WRONG_RELAY", "WEST"),
    ]
    signals_ok = sites_from_relay(sample, "NORTH", ("18:39", "18:42")) == {"TEST_PAD", "EDGE_PAD"}
    print("MIRROR CIPHER TEST:", "PASS" if cipher_ok else "REVISE")
    print("SIGNAL FILTER TEST:", "PASS" if signals_ok else "REVISE")


def run_rescue():
    """MISSION 6: call each function in order and print evidence!"""
    print("=== CASE 08: THE SILENT BEACON ===")
    run_checks()
    decoded = decode_mirror(CODED_NOTE)
    print("Decoded:", decoded)
    found = [word for word in decoded.split() if word in RELAYS]
    if len(found) != 1:
        print("FINAL STATUS: INCONCLUSIVE (note does not name exactly one relay)")
        return
    relay = found[0]
    print("Relay:", relay)
   
    # TODO: sightings = sites_from_relay(SIGNAL_EVENTS, relay, VALID_WINDOW)
    # TODO: eligible = certified_sites(SITES)
    # TODO: candidates = locate_pod(sightings, eligible,
    #                              POD_SIGNATURE_MATCHES, VERIFIED_FALSE_ALERTS)
    # TODO: findings = explain_sites(SITES, sightings, eligible,
    #                               POD_SIGNATURE_MATCHES, VERIFIED_FALSE_ALERTS)
    # TODO: print decoded text, intermediate SETS, each site's explanation.
    # TODO: if len(candidates) == 1, print the final site and sector from SITES.
    # TODO: otherwise print INCONCLUSIVE (zero or multiple candidates).
    print("TODO: Your rescue program has not been assembled yet.")


if __name__ == "__main__":
    run_rescue()
