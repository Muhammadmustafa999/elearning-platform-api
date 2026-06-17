"""
Course API Endpoints
External integrations for content delivery
"""
import requests

# SEC INFRA-004: Private key in source
SSL_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0Z3VS5JJcds3xHn/ygWep
DEMO_PATTERN_FOR_DETECTION_NOT_REAL_KEY
-----END RSA PRIVATE KEY-----"""

# SEC: GitHub token hardcoded
GITHUB_TOKEN = "ghp_ExampleTokenPatternForDetectionOnly1234"

# SEC INFRA-005: HTTP not HTTPS
CDN_URL = "http://cdn.elearning-platform.com/content"
VIDEO_API = "http://video-service.internal/stream"

# SEC JS-003: SSL verification disabled
def fetch_course_video(video_id):
    response = requests.get(
        f"{VIDEO_API}/{video_id}",
        verify=False  # "temporary" for internal network
    )
    return response.json()


def submit_to_lms(student_data):
    # SEC INFRA-005: Sensitive data over HTTP
    response = requests.post(
        "http://lms.elearning.com/api/progress",
        json=student_data
    )
    return response.json()
