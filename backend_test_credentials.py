#!/usr/bin/env python3
"""
Test with specific credentials from test_credentials.md
"""

import requests
import json

# Configuration
BASE_URL = "https://design-platform-app.preview.emergentagent.com/api"

# Test credentials from /app/memory/test_credentials.md
TEST_USERS = [
    {
        "email": "test@pulse.com",
        "password": "test123",
        "name": "Test User"
    },
    {
        "email": "demo@pulse.com", 
        "password": "demo123",
        "name": "Demo User"
    }
]

def test_with_credentials():
    """Test with the specific credentials from test_credentials.md"""
    print("🔐 Testing with Specific Test Credentials...")
    
    for i, user in enumerate(TEST_USERS, 1):
        print(f"\n👤 Testing User {i}: {user['email']}")
        
        # Try to register (might fail if user exists)
        try:
            register_response = requests.post(
                f"{BASE_URL}/auth/register",
                json=user,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            if register_response.status_code == 200:
                print(f"  ✅ Registration successful")
                token = register_response.json()["access_token"]
            elif register_response.status_code == 400:
                print(f"  ℹ️  User already exists, trying login...")
                # Try login
                login_response = requests.post(
                    f"{BASE_URL}/auth/login",
                    json={"email": user["email"], "password": user["password"]},
                    headers={"Content-Type": "application/json"},
                    timeout=30
                )
                
                if login_response.status_code == 200:
                    print(f"  ✅ Login successful")
                    token = login_response.json()["access_token"]
                else:
                    print(f"  ❌ Login failed: {login_response.status_code}")
                    continue
            else:
                print(f"  ❌ Registration failed: {register_response.status_code}")
                continue
        
        except Exception as e:
            print(f"  ❌ Auth error: {str(e)}")
            continue
        
        # Test authenticated endpoint
        try:
            me_response = requests.get(
                f"{BASE_URL}/auth/me",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json"
                },
                timeout=30
            )
            
            if me_response.status_code == 200:
                user_data = me_response.json()
                print(f"  ✅ Authenticated as: {user_data['name']} ({user_data['email']})")
            else:
                print(f"  ❌ Auth verification failed: {me_response.status_code}")
                
        except Exception as e:
            print(f"  ❌ Auth verification error: {str(e)}")

def test_all_endpoints_with_auth():
    """Test all endpoints with proper authentication"""
    print("\n🚀 Testing All Endpoints with Authentication...")
    
    # Use first test user
    user = TEST_USERS[0]
    
    # Login to get token
    try:
        login_response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"email": user["email"], "password": user["password"]},
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if login_response.status_code != 200:
            print("❌ Could not authenticate for endpoint testing")
            return
            
        token = login_response.json()["access_token"]
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        
    except Exception as e:
        print(f"❌ Authentication error: {str(e)}")
        return
    
    # Test all endpoints
    endpoints = [
        ("GET", "/auth/me", None, "Get current user"),
        ("GET", "/habits", None, "Get habits"),
        ("POST", "/habits", {
            "name": "Test Habit",
            "description": "Test habit for API verification",
            "frequency": "daily",
            "color": "#4CAF50",
            "icon": "checkmark",
            "target_per_week": 7
        }, "Create habit"),
        ("GET", "/mood", None, "Get mood entries"),
        ("POST", "/mood", {
            "mood_level": 4,
            "energy_level": 3,
            "sleep_hours": 7.5,
            "notes": "API test mood entry",
            "date": "2026-03-31"
        }, "Create mood entry"),
        ("GET", "/focus", None, "Get focus sessions"),
        ("POST", "/focus", {
            "task_name": "API Testing",
            "duration_minutes": 25,
            "date": "2026-03-31",
            "completed": True
        }, "Create focus session"),
        ("GET", "/analytics", None, "Get analytics")
    ]
    
    results = []
    
    for method, endpoint, data, description in endpoints:
        try:
            url = f"{BASE_URL}{endpoint}"
            
            if method == "GET":
                response = requests.get(url, headers=headers, timeout=30)
            elif method == "POST":
                response = requests.post(url, json=data, headers=headers, timeout=30)
            
            if response.status_code in [200, 201]:
                results.append(f"✅ {description}: Success ({response.status_code})")
            else:
                results.append(f"❌ {description}: Failed ({response.status_code})")
                
        except Exception as e:
            results.append(f"❌ {description}: Error - {str(e)}")
    
    print("\n📋 Endpoint Test Results:")
    for result in results:
        print(f"  {result}")
    
    return results

if __name__ == "__main__":
    print("🚀 Starting Credential-Specific Backend Testing...")
    print(f"Base URL: {BASE_URL}")
    
    # Test with specific credentials
    test_with_credentials()
    
    # Test all endpoints
    test_all_endpoints_with_auth()
    
    print("\n✅ Credential testing complete!")