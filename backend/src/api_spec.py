"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="Web App",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Define schemas
class RegisterInputSchema(Schema):
    email = fields.Email(description="Email user wants to reserve", required=True)
    username = fields.String(description="Username user wants to reserve", required=True)
    password = fields.String(description="Password user wants to use for future logins", required=True)

class OutputSchema(Schema):
    msg = fields.String(description="A message.", required=True)

# register schemas with spec
spec.components.schema("RegisterInput", schema=RegisterInputSchema)
spec.components.schema("Output", schema=OutputSchema)

# add swagger tags that are used for endpoint annotation
tags = [
            {'name': 'Authentication functions',
             'description': 'Registration / authentication / validation / etc'
            },
            {'name': 'Calculation functions',
             'description': 'Functions for calculating.'
            },
       ]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)