import base64
import json
from datetime import datetime, timezone


def decode_part(part):
    """Decode one part of a JWT token."""
    # JWT uses Base64 URL encoding without padding
    padding = "=" * (-len(part) % 4)
    decoded = base64.urlsafe_b64decode(part + padding)
    return json.loads(decoded.decode("utf-8"))


def analyze_jwt(token):
    """Decode and analyze a JWT token."""
    try:
        parts = token.strip().split(".")

        if len(parts) != 3:
            print("\nError: A JWT must have 3 parts.")
            return

        header = decode_part(parts[0])
        payload = decode_part(parts[1])

        print("\n========== JWT ANALYZER ==========")

        print("\nHeader:")
        print(json.dumps(header, indent=4))

        print("\nPayload:")
        print(json.dumps(payload, indent=4))

        # Get important time values
        issued = payload.get("iat")
        expires = payload.get("exp")

        print("\n---------- Token Information ----------")

        if issued:
            issued_time = datetime.fromtimestamp(issued, timezone.utc)
            print("Issued At :", issued_time.strftime("%Y-%m-%d %H:%M:%S UTC"))
        else:
            print("Issued At : Not available")

        if expires:
            expiry_time = datetime.fromtimestamp(expires, timezone.utc)
            print("Expires At:", expiry_time.strftime("%Y-%m-%d %H:%M:%S UTC"))

            if datetime.now(timezone.utc).timestamp() > expires:
                print("Status    : EXPIRED")
            else:
                print("Status    : VALID")
        else:
            print("Expires At: Not available")
            print("Status    : Cannot check expiry")

        # Simple security checks
        print("\n---------- Security Checks ----------")

        if "exp" in payload:
            print("[OK] Expiration claim (exp) exists.")
        else:
            print("[WARNING] Expiration claim (exp) is missing.")

        if "iat" in payload:
            print("[OK] Issued-at claim (iat) exists.")
        else:
            print("[INFO] Issued-at claim (iat) is missing.")

        print("\nNote: This program only decodes the JWT. It does not verify the signature.")


    except Exception as error:
        print("\nError: Invalid JWT token.")
        print("Details:", error)


def main():
    print("Simple JWT Security Analyzer")
    print("-----------------------------")

    token = input("Enter JWT token: ")

    if not token.strip():
        print("Error: Token cannot be empty.")
        return

    analyze_jwt(token)


if __name__ == "__main__":
    main()
