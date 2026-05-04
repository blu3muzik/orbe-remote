#!/usr/bin/env python3
"""

research_config.py - orbe-remote research branch configuration
Branch: research
Shared: Developer1 (Windows-Lab), Developer2 (Ubuntu-Lab), Developer3 (Rocky-Lab)
Purpose: 3-way merge conflict demonstration

"""

PROJECT_NAME    = "orbe-research"
DNS_PRIMARY     = "1.1.1.1"         #Primary DNS server
DNS_SECONDARY   = "1.0.0.1"         # Secondary DNS server
MAX_THREADS     = 8                 # Worker thread count
LOG_LEVEL       = "DEBUG"         # Logging verbosity
TIMEOUT_SEC     = 30                # Connection timeout
RETRY_COUNT     = 3                 # Max retry attempts
ADMIN_USER      = "admin"           # Default admin account
