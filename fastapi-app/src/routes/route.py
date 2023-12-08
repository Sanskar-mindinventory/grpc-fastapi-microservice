from fastapi import APIRouter
from src.api.v1.ResumeParser.views import parse_view
# from src.api.v1.UserAuthentication.views import user_views

# Add route with prefix /api/v1 to manage v1 APIs.
# router = APIRouter(prefix="/api/v1/user-authentication")
router = APIRouter(prefix="/api/v1/resume-parser")
# router.include_router(user_views.user_api_router, tags=["User Management Service Endpoints"])
router.include_router(parse_view.resume_parser, tags=["User Management Service Endpoints"])
