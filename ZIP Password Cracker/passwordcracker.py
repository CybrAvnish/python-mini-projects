import zipfile
import sys
from tqdm import tqdm

def brute_force_zip(zip_path, wordlist_path):
    try:
        zip_file = zipfile.ZipFile(zip_path)
    except FileNotFoundError:
        print(f"Error: ZIP file '{zip_path}' not found.")
        return
    except zipfile.BadZipFile:
        print("Error: The provided file is not a valid ZIP archive.")
        return

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_path}' not found.")
        return

    for password in tqdm(passwords, desc="Trying passwords", unit="pwd"):
        try:
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f"\nSuccess! The password is: '{password}'")
            return
        except RuntimeError as e:
            if 'Bad password' in str(e) or 'password required' in str(e):
                # Incorrect password, continue trying
                continue
            else:
                print(f"Error: {e}")
                return
        except Exception as e:
            print(f"Error: {e}")
            return

    print("\nFailure: Password not found in the wordlist.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python zip_brute_force.py <zipfile> <wordlist>")
        sys.exit(1)
    brute_force_zip(sys.argv[1], sys.argv[2])