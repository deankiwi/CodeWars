import requests

# Set up the URL for your locally hosted LLM API
url = "http://localhost:11434/api/endpoint"  # Replace with the actual endpoint and port

# Define the payload (input to your LLM)
payload = {
    "prompt": "Tell me a joke",
    "temperature": 0.7,  # Adjust parameters as needed
    "max_tokens": 100,
}

# Optional: If authentication is needed
headers = {
    "Content-Type": "application/json",
}

# Make the POST request to the LLM
response = requests.post(url, json=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Response from LLM:", response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
