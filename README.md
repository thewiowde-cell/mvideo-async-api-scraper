# M.Video High-Performance Async API Scraper 🛒⚡

An enterprise-grade, asynchronous data extraction pipeline that targets the internal production API endpoints of M.Video (major Russian tech retailer). It leverages concurrent network architectures to bypass frontend overhead, handles dynamic cursor-based paginations, and normalizes large-scale commercial electronics datasets into clean JSON stores.

## ⚡ Technical Highlights
- **API Payload Interception:** Exploits background POST requests using parameterized JSON structures, injecting dynamic session cookies and authorization security tokens.
- **Dynamic Cursor Pagination:** Implements a robust stateful loop tracking the tracking index via `cursorId` mutations, matching enterprise pagination flows.
- **Asynchronous Disk I/O:** Utilizes `aiohttp` for parallel non-blocking client sessions coupled with `aiofiles` to stream large dataset matrixes into local repositories with zero thread blocking.

## 🛠️ Tech Stack
- **Asynchronous Engine:** aiohttp (Asynchronous Client Sessions), aiofiles
- **Data Engineering:** Python 3, Pathlib Workspace, JSON Architecture, Tokenized Payloads
