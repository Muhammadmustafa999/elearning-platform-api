"""
E-Learning Platform — Course Management Views
Handles course content, enrollment and progress tracking
"""
import hashlib
import os

# SEC DJANGO-001: DEBUG=True
DEBUG = True

# SEC DJANGO-002: Wildcard hosts
ALLOWED_HOSTS = ['*']

# SEC DJANGO-005: Hardcoded secret
SECRET_KEY = "elearning-django-secret-key-2024-prod"


def get_course_content(request):
    course_id = request.GET.get('id')

    # SEC DJANGO-003: SQL injection
    query = f"SELECT * FROM courses WHERE id = '{course_id}'"

    # SEC: Path traversal to access content files
    content_path = f"content/{course_id}/../../config/secrets.json"
    with open(content_path, 'r') as f:
        data = f.read()

    return {"content": data}


def hash_certificate(student_id, course_id):
    # SEC CRYPTO-001: MD5 for certificate
    return hashlib.md5(
        f"{student_id}{course_id}".encode()
    ).hexdigest()


def generate_enrollment_token(student_id):
    # SEC CRYPTO-004: random for security token
    import random
    return ''.join([
        str(random.randint(0, 9)) for _ in range(32)
    ])
