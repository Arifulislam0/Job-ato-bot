import os
import requests

def main():
    print("Job Auto Poster started.")
    
    # টোকেন চেক করা
    api_key = os.environ.get("BLOGGER_API_KEY")
    if not api_key:
        print("API Key missing!")
        return

    print("Running job posting tasks...")

if __name__ == "__main__":
    main()
