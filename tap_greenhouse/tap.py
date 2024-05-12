"""greenhouse tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_greenhouse import streams


class Tapgreenhouse(Tap):
    """greenhouse tap class."""

    name = "tap-greenhouse"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            required=True,
            description="Date from which the sync should start",
            examples=["2024-01-01T00:00:00Z"],
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://harvest.greenhouse.io/v1/",
            description="The url for the API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[streams.GreenhouseStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.ActivityFeedStream(self),
            streams.ApplicationsStream(self),
            streams.ApprovalFlowsStream(self),
            streams.ApprovalsStream(self),
            streams.CandidatesStream(self),
            streams.CandidateTagsStream(self),
            streams.CloseReasonsStream(self),
            streams.CustomFieldsStream(self),
            streams.DemographicQuestionsStream(self),
            streams.DepartmentsStream(self),
            streams.EEOCStream(self),
            streams.JobOpeningsStream(self),
            streams.JobPostsStream(self),
            streams.JobsStream(self),
            streams.JobStagesStream(self),
            streams.OffersStream(self),
            streams.OfficesStream(self),
            streams.PendingApprovalsForUserStream(self),
            streams.ProspectPoolsStream(self),
            streams.RejectionReasonsStream(self),
            streams.ScheduledInterviewsStream(self),
            streams.ScorecardsStream(self),
            streams.SourcesStream(self),
            streams.UserJobPermissionsStream(self),
            streams.UserRolesStream(self),
            streams.UsersStream(self),
        ]


if __name__ == "__main__":
    Tapgreenhouse.cli()
