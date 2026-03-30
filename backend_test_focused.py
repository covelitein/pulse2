#!/usr/bin/env python3
"""
Focused Backend API Testing for Pulse Mobile App
Tests core functionality with better error handling
"""

import requests
import json
from datetime import datetime, timedelta
import time

# Configuration
BASE_URL = "https://design-platform-app.preview.emergentagent.com/api"
TEST_USER_EMAIL = "sarah.wellness@example.com"
TEST_USER_PASSWORD = "SecurePass123!"
TEST_USER_NAME = "Sarah Wellness"

def test_core_functionality():
    """Test core backend functionality"""
    print("🚀 Testing Pulse Backend Core Functionality...")
    
    token = None
    test_habits = []
    
    # Test 1: Login (skip registration since user exists)
    print("\n🔐 Testing Authentication...")
    login_data = {
        "email": TEST_USER_EMAIL,
        "password": TEST_USER_PASSWORD
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data, timeout=30)
        if response.status_code == 200:
            data = response.json()
            token = data["access_token"]
            print("✅ Authentication: Login successful")
        else:
            print(f"❌ Authentication: Login failed - {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Authentication: Login error - {str(e)}")
        return False
    
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    
    # Test 2: Get current user
    try:
        response = requests.get(f"{BASE_URL}/auth/me", headers=headers, timeout=30)
        if response.status_code == 200:
            print("✅ Authentication: Get current user successful")
        else:
            print(f"❌ Authentication: Get current user failed - {response.status_code}")
    except Exception as e:
        print(f"❌ Authentication: Get current user error - {str(e)}")
    
    # Test 3: Create habits
    print("\n🎯 Testing Habits API...")
    habit_data = {
        "name": "Daily Meditation",
        "description": "10 minutes of mindfulness",
        "frequency": "daily",
        "color": "#4CAF50",
        "icon": "leaf",
        "target_per_week": 7
    }
    
    try:
        response = requests.post(f"{BASE_URL}/habits", json=habit_data, headers=headers, timeout=30)
        if response.status_code == 200:
            habit = response.json()
            test_habits.append(habit)
            print("✅ Habits: Create habit successful")
        else:
            print(f"❌ Habits: Create habit failed - {response.status_code}")
    except Exception as e:
        print(f"❌ Habits: Create habit error - {str(e)}")
    
    # Test 4: Get habits
    try:
        response = requests.get(f"{BASE_URL}/habits", headers=headers, timeout=30)
        if response.status_code == 200:
            habits = response.json()
            print(f"✅ Habits: Get habits successful ({len(habits)} habits)")
        else:
            print(f"❌ Habits: Get habits failed - {response.status_code}")
    except Exception as e:
        print(f"❌ Habits: Get habits error - {str(e)}")
    
    # Test 5: Log habit completion
    if test_habits:
        log_data = {
            "habit_id": test_habits[0]["id"],
            "date": datetime.now().strftime("%Y-%m-%d"),
            "completed": True,
            "notes": "Completed successfully"
        }
        
        try:
            response = requests.post(f"{BASE_URL}/habits/log", json=log_data, headers=headers, timeout=30)
            if response.status_code == 200:
                print("✅ Habits: Log habit completion successful")
            else:
                print(f"❌ Habits: Log habit completion failed - {response.status_code}")
        except Exception as e:
            print(f"❌ Habits: Log habit completion error - {str(e)}")
    
    # Test 6: Create mood entry
    print("\n😊 Testing Mood API...")
    mood_data = {
        "mood_level": 4,
        "energy_level": 3,
        "sleep_hours": 7.5,
        "notes": "Feeling great today",
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    
    try:
        response = requests.post(f"{BASE_URL}/mood", json=mood_data, headers=headers, timeout=30)
        if response.status_code == 200:
            print("✅ Mood: Create mood entry successful")
        else:
            print(f"❌ Mood: Create mood entry failed - {response.status_code}")
    except Exception as e:
        print(f"❌ Mood: Create mood entry error - {str(e)}")
    
    # Test 7: Get mood entries
    try:
        response = requests.get(f"{BASE_URL}/mood", headers=headers, timeout=30)
        if response.status_code == 200:
            moods = response.json()
            print(f"✅ Mood: Get mood entries successful ({len(moods)} entries)")
        else:
            print(f"❌ Mood: Get mood entries failed - {response.status_code}")
    except Exception as e:
        print(f"❌ Mood: Get mood entries error - {str(e)}")
    
    # Test 8: Create focus session
    print("\n🎯 Testing Focus API...")
    focus_data = {
        "task_name": "Deep Work Session",
        "duration_minutes": 45,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "completed": True
    }
    
    try:
        response = requests.post(f"{BASE_URL}/focus", json=focus_data, headers=headers, timeout=30)
        if response.status_code == 200:
            print("✅ Focus: Create focus session successful")
        else:
            print(f"❌ Focus: Create focus session failed - {response.status_code}")
    except Exception as e:
        print(f"❌ Focus: Create focus session error - {str(e)}")
    
    # Test 9: Get focus sessions
    try:
        response = requests.get(f"{BASE_URL}/focus", headers=headers, timeout=30)
        if response.status_code == 200:
            sessions = response.json()
            print(f"✅ Focus: Get focus sessions successful ({len(sessions)} sessions)")
        else:
            print(f"❌ Focus: Get focus sessions failed - {response.status_code}")
    except Exception as e:
        print(f"❌ Focus: Get focus sessions error - {str(e)}")
    
    # Test 10: Get analytics
    print("\n📊 Testing Analytics API...")
    try:
        response = requests.get(f"{BASE_URL}/analytics", headers=headers, timeout=30)
        if response.status_code == 200:
            analytics = response.json()
            
            # Check structure
            required_keys = ["weekly_stats", "insights", "habit_streaks", "mood_chart_data", "focus_chart_data"]
            if all(key in analytics for key in required_keys):
                print("✅ Analytics: Structure validation successful")
                
                # Check weekly stats
                stats = analytics["weekly_stats"]
                if "total_habits_completed" in stats and "total_focus_minutes" in stats:
                    print("✅ Analytics: Weekly stats validation successful")
                else:
                    print("❌ Analytics: Weekly stats missing required fields")
                
                # Check insights
                insights = analytics["insights"]
                if isinstance(insights, list):
                    print(f"✅ Analytics: Insights validation successful ({len(insights)} insights)")
                else:
                    print("❌ Analytics: Insights not in correct format")
                
                # Check sleep-focus correlation
                sleep_insights = [i for i in insights if i.get("type") == "sleep_focus"]
                if sleep_insights:
                    print("✅ Analytics: Sleep-focus correlation working")
                else:
                    print("⚠️  Analytics: No sleep-focus correlation (may need more data)")
                
            else:
                missing = [k for k in required_keys if k not in analytics]
                print(f"❌ Analytics: Missing keys - {missing}")
        else:
            print(f"❌ Analytics: Get analytics failed - {response.status_code}")
    except Exception as e:
        print(f"❌ Analytics: Get analytics error - {str(e)}")
    
    # Test 11: Test unauthorized access
    print("\n🔒 Testing Security...")
    try:
        response = requests.get(f"{BASE_URL}/auth/me", timeout=30)  # No auth header
        if response.status_code in [401, 403]:
            print("✅ Security: Unauthorized access protection working")
        else:
            print(f"❌ Security: Unauthorized access not properly blocked - {response.status_code}")
    except Exception as e:
        print(f"❌ Security: Unauthorized access test error - {str(e)}")
    
    print("\n✅ Core functionality testing completed!")
    return True

if __name__ == "__main__":
    test_core_functionality()