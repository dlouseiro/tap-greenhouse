"""JSON Schema for Greenhouse API: List Demographic Questions."""
from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType, required=True),
    th.Property("active", th.BooleanType),
    th.Property("demographic_question_set_id", th.IntegerType),
    th.Property("name", th.StringType),
    th.Property(
        "translations",
        th.ArrayType(
            th.Property(
                th.Property("language", th.StringType),
                th.Property("name", th.StringType),
            ),
        ),
    ),
    th.Property("required", th.BooleanType),
)


schema_dict = schema.to_dict()
