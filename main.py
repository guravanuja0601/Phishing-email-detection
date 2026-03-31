# Phishing Email Detection System

def calculate_score(email_text):
    score = 0
    reasons = []

    # 🔍 Rule 1: Suspicious keywords
    keywords = ["urgent", "verify", "password", "bank", "login", "click"]
    for word in keywords:
        if word in email_text.lower():
            score += 1
            reasons.append(f"Suspicious keyword: {word}")

    # 🔍 Rule 2: Check for links
    if "http://" in email_text or "https://" in email_text:
        score += 2
        reasons.append("Contains link")

    # 🔍 Rule 3: Unknown sender (basic check)
    if "@" not in email_text:
        score += 1
        reasons.append("Missing or suspicious sender")

    return score, reasons


def classify_email(score, reasons):
    if score >= 5:
        status = "HIGH RISK"
        message = "⚠️ ALERT: Phishing Email Detected"
    elif score >= 3:
        status = "MEDIUM RISK"
        message = "⚠️ Suspicious Email - Be Cautious"
    else:
        status = "LOW RISK"
        message = "✅ Email is Safe"

    return f"""{message}
Risk Score: {score}
Status: {status}
Reasons: {", ".join(reasons)}
"""


def main():
    print("📧 Phishing Email Detection System\n")

    # Take input
    email_text = input("Paste your email content:\n")

    # Calculate score
    score, reasons = calculate_score(email_text)

    # Classify result
    result = classify_email(score, reasons)

    # Output result
    print("\n--- RESULT ---")
    print(result)

    # Log (SOC style)
    print(f"\n[LOG] Email checked | Score: {score} | Status logged")


# Run program
if __name__ == "__main__":
    main()
