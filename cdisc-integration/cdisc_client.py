"""
CDISC Library Client Integration for OpenStudyBuilder
=====================================================
Helper module for accessing CDISC Library REST API
to retrieve standards metadata for CRF building and SDTM annotation.

Usage:
    from cdisc_client import get_cdisc_client, get_sdtm_domains
    
    client = get_cdisc_client()
    domains = get_sdtm_domains("3-4")

Requires:
    - CDISC_LIBRARY_API_KEY environment variable set
    - pip install -r cdisc-integration/requirements.txt
"""

import os
from dotenv import load_dotenv
from cdisc_library_client import CDISCLibraryClient

# Load environment variables from .env file
load_dotenv()


def get_cdisc_client():
    """Initialize and return a CDISC Library API client."""
    api_key = os.environ.get("CDISC_LIBRARY_API_KEY")
    if not api_key:
        raise ValueError(
            "CDISC_LIBRARY_API_KEY environment variable not set. "
            "Copy .env.example to .env and add your API key."
        )
    return CDISCLibraryClient(api_key=api_key)


def get_sdtm_domains(ig_version="3-4"):
    """Retrieve all SDTM domains for a given IG version."""
    client = get_cdisc_client()
    return client.get_sdtmig(ig_version)


def get_controlled_terminology(package_id):
    """Retrieve a specific Controlled Terminology package."""
    client = get_cdisc_client()
    return client.get_ct_package(package_id)


def get_cdash_domains(version="2-2"):
    """Retrieve CDASH domain definitions for CRF building."""
    client = get_cdisc_client()
    return client.get_cdash(version)


if __name__ == "__main__":
    # Quick test
    print("Testing CDISC Library Client connection...")
    client = get_cdisc_client()
    print("✅ Connection successful!")
    print("Available SDTM-IG versions:", client.get_sdtmig_versions())
