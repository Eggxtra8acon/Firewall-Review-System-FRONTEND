def generate_summary(findings_list):
    total_risks = len(findings_list)
    high_severity_count = 0
    
    for finding in findings_list:
        severity = finding.get("severity", "").lower()
        
        if severity == "high" or severity == "critical":
            high_severity_count += 1
            
    if high_severity_count > 0:
        system_status = "DANGER"
    else:
        system_status = "SECURE"

    #not sure if mas magandang gumawa ng sariling variable for thsi pero ito dapat final output    
    return {
        'total_risks': total_risks,
        'high_severity': high_severity_count,
        'status': system_status
    }

# testing part, run 'python reporter.py' on terminal, make sure nakapasok din sa modules folder (cd modules)
if __name__ == "__main__":
    sample_analyzer = [
        {"rule_id": 4, "severity": "High", "issue": "Insecure Port Allowed", "message": "Port 23 is openly permitted."},
        {"rule_id": 2, "severity": "Medium", "issue": "Wide Source Exposure", "message": "Source is set to 'any'."},
        {"rule_id": 8, "severity": "High", "issue": "Insecure Port Allowed", "message": "Port 445 is openly permitted."}
    ]
    
    final_summary = generate_summary(sample_analyzer)
    print("")
    print("Final Output:")
    print(final_summary)