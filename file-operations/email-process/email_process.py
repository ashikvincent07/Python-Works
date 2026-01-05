email_path = "file-operations\\email_process\\emails.txt"

yahoo_path = "file-operations\\email_process\\yahoo.txt"

outlook_path = "file-operations\\email_process\\outlook.txt"

gmail_path = "file-operations\\email_process\\gmail.txt"

fr_email = open(email_path, "r")

fw_yahoo = open(yahoo_path, "w")

fw_outlook = open(outlook_path, "w")

fw_gmail = open(gmail_path, "w")

for line in fr_email:
    email = line.rstrip("\n")

    if email.endswith("@outlook.com"):
        fw_outlook.write(email+"\n")

    elif email.endswith("@gmail.com"):
        fw_gmail.write(email+"\n")

    elif email.endswith("@yahoo.com"):
        fw_yahoo.write(email+"\n")

print("program end")