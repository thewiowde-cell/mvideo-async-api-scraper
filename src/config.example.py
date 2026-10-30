"""Local configuration template for src/scraper.py.

Copy this file to src/config.py and replace the placeholders.
Do not commit src/config.py or actual cookies/access tokens.
The example endpoint is intentionally non-functional.
"""

# Supply an endpoint that you are authorized to use.
api_url = "https://example.invalid/replace-with-authorized-api-endpoint"

# Adapt these to the selected endpoint's documented/requested format.
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# Add session cookies only when you are authorized to use them.
cookies = {}

# scraper.py reads 'limit', updates 'cursorId', and expects
# an API response shaped like {'body': {'items': [...]}}.
# Replace/extend this payload to match the actual endpoint.
json_data = {
    "limit": 20,
    "cursorId": "0",
}
