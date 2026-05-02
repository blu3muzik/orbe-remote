#!/usr/bin/env python3
"""
lab_config.py - orbe-remote shared lab configuration
Shared across: Developer1 (Latitude-5400), Developer2 (Ubuntu-Lab), Developer3 (Rocky-Lab)
"""

LAB_NAME          = "orbe-remote"
DNS_PRIMARY       = "8.8.8.8"       # Primary DNS server
DNS_SECONDARY     = "8.8.4.4"       # Secondary DNS server
MAX_THREADS       = 4               # Worder thread count
LOG_LEVEL         = "WARNING"       # Logging verbosity
TIMEOUT_SEC       = 30              # Connection timeout in seconds
ADMIN_USER        = "admin"         # Default admin account
