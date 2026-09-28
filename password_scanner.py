# ==================== PASSWORD ANALYZER ====================

# Get user input
def get_user_input():
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    return username, password

#  Analyze password characters

def analyze_password(password):
    has_digit = False
    has_upper = False
    has_lower = False
    has_special = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif not char.isalnum():
            has_special = True

    return has_digit, has_upper, has_lower, has_special

#  Score the password
def score_password(password, has_digit, has_upper, has_lower, has_special):
    score = 0

    if len(password) >= 12:
        score += 1
    if has_digit:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_special:
        score += 1

    return score

#  Print the analysis report
def print_report(score, password, has_digit, has_upper, has_lower, has_special):
    print("\n========= PASSWORD ANALYSIS REPORT =========")

    # Length
    if len(password) >= 12:
        print("✔ Password length is strong")
    else:
        print("✖ Password should be at least 12 characters")

    # Character checks
    print("✔ Contains number" if has_digit else "✖ Must contain a number")
    print("✔ Uppercase present" if has_upper else "✖ Must include uppercase letters")
    print("✔ Lowercase present" if has_lower else "✖ Must include lowercase letters")
    print("✔ Special character present" if has_special else "✖ Must include special characters")

    # Final verdict
    print("\n========= FINAL VERDICT =========")
    if score <= 2:
        print("❌ WEAK PASSWORD")
    elif 3 <= score <= 4:
        print("⚠ MEDIUM PASSWORD")
    else:
        print("✅ EXCELLENT PASSWORD")

#  Main scanner controller
def scanner():
    while True:
        print("\n========= ACCOUNT SECURITY SCANNER =========")
        username, password = get_user_input()

        # Analyze
        has_digit, has_upper, has_lower, has_special = analyze_password(password)

        # Score
        score = score_password(password, has_digit, has_upper, has_lower, has_special)

        # Print report
        print_report(score, password, has_digit, has_upper, has_lower, has_special)

        # Ask to continue
        choice = input("\nCheck another password? (yes/no): ").lower()
        if choice != "yes":
            print("Scanner terminated.")
            break

# ==================== RUN SCANNER ====================
scanner()
