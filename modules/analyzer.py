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

