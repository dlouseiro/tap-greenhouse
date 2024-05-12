"""Making it easy to import all Schemas."""
from .activity_feed import schema_dict as activity_feed
from .applications import schema_dict as applications
from .approval_flows import schema_dict as approval_flows
from .approvals import schema_dict as approvals
from .candidate_tags import schema_dict as candidate_tags
from .candidates import schema_dict as candidates
from .close_reasons import schema_dict as close_reasons
from .custom_fields import schema_dict as custom_fields
from .demographic_questions import schema_dict as demographic_questions
from .departments import schema_dict as departments
from .eeoc import schema_dict as eeoc
from .job_openings import schema_dict as job_openings
from .job_posts import schema_dict as job_posts
from .job_stages import schema_dict as job_stages
from .jobs import schema_dict as jobs
from .offers import schema_dict as offers
from .offices import schema_dict as offices
from .pending_approvals_for_user import schema_dict as pending_approvals_for_user
from .prospect_pools import schema_dict as prospect_pools
from .rejection_reasons import schema_dict as rejection_reasons
from .scheduled_interviews import schema_dict as scheduled_interviews
from .scorecards import schema_dict as scorecards
from .sources import schema_dict as sources
from .user_job_permissions import schema_dict as user_job_permissions
from .user_roles import schema_dict as user_roles
from .users import schema_dict as users

__all__ = [
    "activity_feed",
    "applications",
    "approval_flows",
    "approvals",
    "candidate_tags",
    "candidates",
    "close_reasons",
    "custom_fields",
    "demographic_questions",
    "departments",
    "eeoc",
    "job_openings",
    "job_posts",
    "job_stages",
    "jobs",
    "offers",
    "offices",
    "pending_approvals_for_user",
    "prospect_pools",
    "rejection_reasons",
    "scheduled_interviews",
    "scorecards",
    "sources",
    "user_job_permissions",
    "user_roles",
    "users",
]
