# M.Video High-Performance Async API Scraper 🛒⚡

An enterprise-grade, asynchronous data extraction pipeline that targets the internal production API endpoints of M.Video (major Russian tech retailer). It leverages concurrent network architectures to bypass frontend overhead, handles dynamic cursor-based paginations, and normalizes large-scale commercial electronics datasets into clean JSON stores.

## ⚡ Technical Highlights
- **API Payload Interception:** Exploits background POST requests using parameterized JSON structures, injecting dynamic session cookies and authorization security tokens.
- **Dynamic Cursor Pagination:** Implements a robust stateful loop tracking the tracking index via `cursorId` mutations, matching enterprise pagination flows.
- **Asynchronous Disk I/O:** Utilizes `aiohttp` for parallel non-blocking client sessions coupled with `aiofiles` to stream large dataset matrixes into local repositories with zero thread blocking.

## 🛠️ Tech Stack
- **Asynchronous Engine:** aiohttp (Asynchronous Client Sessions), aiofiles
- **Data Engineering:** Python 3, Pathlib Workspace, JSON Architecture, Tokenized Payloads

## Local setup (configuration required)

This repository contains an example of asynchronous HTTP/JSON extraction. It is **not a ready-to-run, officially supported M.Video API client**: the API endpoint and request parameters are not included, and the remote service may have changed or require authorization.

**Windows PowerShell** (from the repository root):

```powershell
py -m pip install aiohttp aiofiles
Copy-Item src/config.example.py src/config.py
# Edit src/config.py: supply an authorized API URL, headers, cookies if needed,
# and a request payload appropriate for that endpoint.
py src/scraper.py
```

**Linux/macOS**:

```bash
python3 -m pip install aiohttp aiofiles
cp src/config.example.py src/config.py
# Edit src/config.py with your authorized endpoint/request settings.
python3 src/scraper.py
```

The script imports `api_url`, `headers`, `cookies`, and `json_data` from `src/config.py`. The `json_data` object must include a positive `limit`; the script updates `cursorId` while iterating. It expects JSON responses containing `body.items`. If extraction succeeds, output is written to `data/products.json`.

`src/config.py` is excluded by `.gitignore`; **never commit real cookies, tokens, or other secrets**. `src/config.example.py` uses a deliberately invalid URL and contains no credentials. A working request depends on current endpoint behavior, correct permissions and suitable request data. This project has not been end-to-end verified against the live service as part of this documentation update.
