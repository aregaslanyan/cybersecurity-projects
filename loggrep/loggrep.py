with open("sample_logs/sample_auth.log") as f:
    for line in f:
        if "Failed password" in line:
            print(line.strip())