import requests
import time
import datetime

# Configuration
URL: str = "https://aireader.onrender.com/"
INTERVAL_MINUTES = 1
INTERVAL_SECONDS = INTERVAL_MINUTES * 60
TOTAL_REQUEST = 0

def send_request():
    """Sends a GET request to the specified URL and prints status."""
    try:
        # Get current time for logging
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - Sending GET request to {URL}...")

        # Send the GET request with a timeout (e.g., 180 seconds = 3 minutes)
        response = requests.get(URL, timeout=180)

        # Check if the request was successful (status code 2xx)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)

        print(f"    Success! Status Code: {response.status_code}")
        # Optional: You can print part of the response content if needed
        print(f"    Response Text (first 100 chars): {response.text[:100]}")

    except requests.exceptions.Timeout:
        print(f"    Error: The request timed out.")
    except requests.exceptions.ConnectionError:
        print(f"    Error: Could not connect to the server.")
    except requests.exceptions.HTTPError as http_err:
        print(f"    Error: HTTP error occurred: {http_err} (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as req_err:
        print(f"    Error: An ambiguous request error occurred: {req_err}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"    An unexpected error occurred: {e}")

if __name__ == "__main__":
    print(f"Script started. Sending request to {URL} every {INTERVAL_MINUTES} minutes.")
    print("Press Ctrl+C to stop.")

    while True:
        send_request()
        TOTAL_REQUEST += 1
        print(f"Waiting for {INTERVAL_MINUTES} minutes...")
        print(f"Total Requests made: {TOTAL_REQUEST}")
        try:
            pass
            time.sleep(INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("\nScript interrupted by user. Exiting.")
            break
