email = input("Enter your email: ").strip()
print(email)
print("_________________________")

# Basic checks before splitting
if " " in email:
    print("Invalid email: contains space.")
elif "@" not in email or email.count("@") != 1:
    print("Invalid email: '@' is missing or repeated.")
elif "." not in email:
    print("Invalid email: '.' is missing.")
else:
    try:
        local, domain = email.split("@")
        if not local or not domain:
            print("Invalid email: missing local or domain part.")
        else:
            domain_parts = domain.split(".")
            if len(domain_parts) < 2:
                print("Invalid email: domain must contain a '.' with a TLD.")
            elif any(not part for part in domain_parts):
                print("Invalid email: empty domain section.")
            elif len(domain_parts[-1]) < 2:
                print("Invalid email: TLD too short.")
            else:
                print(" Valid email!")
                print("Local part:", local)
                print("Domain part:", domain)
    except ValueError:
        print("Invalid email: splitting failed.")
