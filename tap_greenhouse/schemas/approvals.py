"""List Approvals Schema."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType, required=True),
    th.Property("offer_id", th.IntegerType),
    th.Property("sequential", th.BooleanType),
    th.Property("version", th.IntegerType),
    th.Property("approval_type", th.StringType),
    th.Property("approval_status", th.StringType),
    th.Property("job_id", th.IntegerType),
    th.Property("job_updated_at", th.DateTimeType, required=True),
    th.Property("requested_by_user_id", th.IntegerType),
    th.Property(
        "approver_groups",
        th.ArrayType(
            th.ObjectType(
                th.Property("id", th.IntegerType),
                th.Property("approvals_required", th.IntegerType),
                th.Property("created_at", th.DateTimeType),
                th.Property("resolved_at", th.DateTimeType),
                th.Property("priority", th.IntegerType),
                th.Property("job_id", th.IntegerType),
                th.Property("offer_id", th.IntegerType, required=False),
                th.Property(
                    "approvers",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("id", th.IntegerType),
                            th.Property("name", th.StringType),
                            th.Property("employee_id", th.StringType),
                            th.Property("email_addresses", th.ArrayType(th.StringType)),
                        ),
                    ),
                ),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()
