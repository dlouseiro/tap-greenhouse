"""Stream type classes for tap-greenhouse."""
# ruff: noqa: ARG002

from __future__ import annotations

from tap_greenhouse import schemas
from tap_greenhouse.client import GreenhouseStream


class CandidatesStream(GreenhouseStream):
    """Candidates stream."""

    name = "candidates"
    path = "candidates"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.candidates
    replication_key_param_name = "updated_after"
    accepts_pagination = True

    def get_child_context(self, record: dict, context: dict | None) -> dict | None:
        """Get child context for Child Streams."""
        return {
            "candidate_id": record["id"],
            "last_activity": record["last_activity"],
        }


class CandidateTagsStream(GreenhouseStream):
    """Candidate Tags Stream."""

    name = "candidate_tags"
    path = "tags/candidate"
    primary_keys = ["id"]
    schema = schemas.candidate_tags


class ApplicationsStream(GreenhouseStream):
    """Applications stream."""

    name = "applications"
    path = "applications"
    primary_keys = ["id"]
    replication_key = "last_activity_at"
    schema = schemas.applications
    replication_key_param_name = "last_activity_after"
    accepts_pagination = True


class JobsStream(GreenhouseStream):
    """Jobs Stream."""

    name = "jobs"
    path = "jobs"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.jobs
    replication_key_param_name = "updated_after"
    accepts_pagination = True

    def get_child_context(self, record: dict, context: dict | None) -> dict | None:
        """Get child context for Child Streams."""
        return {
            "job_id": record["id"],
            "job_updated_at": record["updated_at"],
        }


class JobOpeningsStream(GreenhouseStream):
    """Job Openings Stream."""

    name = "job_openings"
    parent_stream_type = JobsStream
    path = "jobs/{job_id}/openings"
    primary_keys = ["id"]
    replication_key = "job_updated_at"
    schema = schemas.job_openings

    def post_process(
        self,
        row: dict,
        context: dict,
    ) -> dict | None:
        """Add fields from parent to child record."""
        return row.update(
            {
                "job_id": context["job_id"],
                "job_updated_at": context["job_updated_at"],
            },
        )


class ActivityFeedStream(GreenhouseStream):
    """Candidate Activity feed stream."""

    name = "activity_feed"
    parent_stream_type = CandidatesStream
    path = "candidates/{candidate_id}/activity_feed"
    primary_keys = ["candidate_id"]
    replication_key = "last_activity"
    schema = schemas.activity_feed

    def post_process(
        self,
        row: dict,
        context: dict,
    ) -> dict | None:
        """Add fields from parent to child record."""
        row.update(
            {
                "candidate_id": context["candidate_id"],
                "last_activity": context["last_activity"],
            },
        )
        return row


class ApprovalsStream(GreenhouseStream):
    """Approvals for a job."""

    name = "approvals"
    parent_stream_type = JobsStream
    path = "jobs/{job_id}/approval_flows"
    primary_keys = ["id"]
    replication_key = "job_updated_at"
    schema = schemas.approvals

    def get_child_context(self, record: dict, context: dict | None) -> dict | None:
        """Get child context for Child Streams."""
        return {
            "id": record["id"],
        }

    def post_process(
        self,
        row: dict,
        context: dict,
    ) -> dict | None:
        """Add fields from parent to child record."""
        row.update(
            {
                "job_updated_at": context["job_updated_at"],
            },
        )
        return row


class ApprovalFlowsStream(GreenhouseStream):
    """Get: Retrieve Approval Flows."""

    name = "approval_flows"
    parent_stream_type = ApprovalsStream
    path = "approval_flows/{id}"
    primary_keys = ["id"]
    schema = schemas.approval_flows


class UsersStream(GreenhouseStream):
    """Users Stream."""

    name = "users"
    path = "users"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.users
    replication_key_param_name = "updated_after"
    accepts_pagination = True

    def get_child_context(self, record: dict, context: dict | None) -> dict | None:
        """Get child context for Child Streams."""
        return {
            "user_id": record["id"],
        }


class PendingApprovalsForUserStream(GreenhouseStream):
    """Pending Approvals for user Stream."""

    name = "pending_approvals_for_user"
    parent_stream_type = UsersStream
    ignore_parent_replication_key = True
    primary_keys = ["id"]
    path = "users/{user_id}/pending_approvals"
    schema = schemas.pending_approvals_for_user


class CloseReasonsStream(GreenhouseStream):
    """Close Reasons Stream."""

    name = "close_reasons"
    path = "close_reasons"
    primary_keys = ["id"]
    schema = schemas.close_reasons


class CustomFieldsStream(GreenhouseStream):
    """Custom Fields Stream."""

    name = "custom_fields"
    path = "custom_fields"
    primary_keys = ["id"]
    schema = schemas.custom_fields


class DemographicQuestionsStream(GreenhouseStream):
    """Demographic Question Stream."""

    name = "demographic_questions"
    path = "demographics/questions"
    primary_keys = ["id"]
    schema = schemas.demographic_questions
    accepts_pagination = True


class DepartmentsStream(GreenhouseStream):
    """Department Stream."""

    name = "departments"
    path = "departments"
    primary_keys = ["id"]
    schema = schemas.departments
    accepts_pagination = True


class EEOCStream(GreenhouseStream):
    """EEOC Stream."""

    name = "eeoc"
    path = "eeoc"
    replication_key = "submitted_at"
    primary_keys = ["application_id"]
    schema = schemas.eeoc
    replication_key_param_name = "submitted_after"
    accepts_pagination = True


class JobPostsStream(GreenhouseStream):
    """Job Posts Stream."""

    name = "job_posts"
    path = "job_posts"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.job_posts
    replication_key_param_name = "updated_after"
    accepts_pagination = True


class JobStagesStream(GreenhouseStream):
    """Job Stages Stream."""

    name = "job_stages"
    path = "job_stages"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.job_stages
    replication_key_param_name = "updated_after"
    accepts_pagination = True


class OffersStream(GreenhouseStream):
    """Offer Stream."""

    name = "offers"
    path = "offers"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.offers
    replication_key_param_name = "updated_after"
    accepts_pagination = True


class OfficesStream(GreenhouseStream):
    """Offices Stream."""

    name = "office"
    path = "offices"
    primary_keys = ["id"]
    schema = schemas.offices
    accepts_pagination = True


class ProspectPoolsStream(GreenhouseStream):
    """Prospect Pools stream."""

    name = "prospect_pools"
    path = "prospect_pools"
    primary_keys = ["id"]
    schema = schemas.prospect_pools
    accepts_pagination = True


class RejectionReasonsStream(GreenhouseStream):
    """Rejection Reasons Stream."""

    name = "rejection_reasons"
    path = "rejection_reasons"
    primary_keys = ["id"]
    schema = schemas.rejection_reasons
    accepts_pagination = True


class ScheduledInterviewsStream(GreenhouseStream):
    """Scheduled Interviews Stream."""

    name = "scheduled_interviews"
    path = "scheduled_interviews"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.scheduled_interviews
    replication_key_param_name = "updated_after"
    accepts_pagination = True


class ScorecardsStream(GreenhouseStream):
    """Scorecards Stream."""

    name = "scorecards"
    path = "scorecards"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = schemas.scorecards
    replication_key_param_name = "updated_after"
    accepts_pagination = True


class SourcesStream(GreenhouseStream):
    """Sources Stream."""

    name = "sources"
    path = "sources"
    primary_keys = ["id"]
    schema = schemas.sources
    accepts_pagination = True


class UserJobPermissionsStream(GreenhouseStream):
    """User job permissions Stream."""

    name = "user_job_permissions"
    parent_stream_type = UsersStream
    ignore_parent_replication_key = True
    path = "users/{user_id}/permissions/jobs"
    primary_keys = ["id", "job_id", "user_role_id"]
    schema = schemas.user_job_permissions


class UserRolesStream(GreenhouseStream):
    """User Roles Stream."""

    name = "user_roles"
    path = "user_roles"
    primary_keys = ["id"]
    schema = schemas.user_roles
