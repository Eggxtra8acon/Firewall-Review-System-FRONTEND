INSECURE_PORTS = {
    21: "FTP (Transmits passwords in plain text)",
    23: "Telnet (Unencrypted communication)",
    80: "HTTP (Unencrypted web traffic)",
    445: "SMB (Highly vulnerable to ransomware attacks)"
}


def analyze_rules(rules_list):
    findings = []
    findings += check_open_ports(rules_list)
    findings += check_overly_permissive(rules_list)

    return findings

def check_open_ports(rules):
    port_findings = []

    for rule in rules:
        action = rule.get("action", "")
        port = rule.get("port")
        rule_id = rule.get("id") or "Unknown"

        if action == "ALLOW" and port is not None:
            if port in INSECURE_PORTS:
                port_findings.append({
                    "rule_id": rule_id,
                    "severity": "High",
                    "issue": "Insecure Port Allowed",
                    "message": f"Port {port} ({INSECURE_PORTS[port]}) is openly permitted."
                })

    return port_findings



def check_overly_permissive(rules):
    """
    Flags rules that are too broad, such as 'Any-to-Any' access.
    """
    permissive_findings = []

    for rule in rules:
        action = rule.get("action", "")
        src = rule.get("src_ip", "").lower()
        dst = rule.get("dst_ip", "").lower()
        rule_id = rule.get("order") or "Unknown"

        if action in ["ALLOW", "ACCEPT"]:
            # 1. Critical Risk: Any source to Any destination
            if src == "any" and dst == "any":
                permissive_findings.append({
                    "rule_id": rule_id,
                    "severity": "High",
                    "issue": "Overly Permissive Rule",
                    "message": "Critical: Traffic is allowed from ANY source to ANY destination."
                })
            
            # 2. Medium Risk: Any source to a specific destination (External exposure)
            elif src == "any":
                permissive_findings.append({
                    "rule_id": rule_id,
                    "severity": "Medium",
                    "issue": "Wide Source Exposure",
                    "message": "The source is set to 'any', allowing public access to this destination."
                })

    return permissive_findings

