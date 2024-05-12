"""JSON Schema for Departments."""
import singer_sdk.typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType, required=True),
    th.Property("name", th.StringType),
    th.Property("parent_id", th.IntegerType),
    th.Property("parent_department_external_id", th.StringType),
    th.Property("child_ids", th.ArrayType(th.IntegerType)),
    th.Property("child_department_external_ids", th.ArrayType(th.StringType)),
    th.Property("external_id", th.StringType),
)

schema_dict = schema.to_dict()
