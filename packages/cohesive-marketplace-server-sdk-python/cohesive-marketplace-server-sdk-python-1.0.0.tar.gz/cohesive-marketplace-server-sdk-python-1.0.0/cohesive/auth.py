from dataclasses import dataclass

import jwt
import cohesive

from cohesive.error import AuthenticationError


@dataclass
class AuthDetails:
    user_id: int
    user_name: str
    role: str
    workspace_id: int
    workspace_name: str
    instance_id: int
    current_period_started_at: str
    current_period_ends_at: str
    is_in_trial: bool


def validate_token(token: str) -> AuthDetails:
    try:
        claims = jwt.decode(token, cohesive.app_secret, algorithms=["HS256"])
        return AuthDetails(
            user_id=claims.get("user_id"),
            user_name=claims.get("user_name"),
            role=claims.get("role"),
            workspace_id=claims.get("workspace_id"),
            workspace_name=claims.get("workspace_name"),
            instance_id=claims.get("instance_id"),
            current_period_started_at=claims.get("current_period_started_at"),
            current_period_ends_at=claims.get("current_period_ends_at"),
            is_in_trial=claims.get("is_in_trial"),
        )
    except jwt.exceptions.PyJWTError as e:
        raise AuthenticationError(message=str(e), http_status=None, http_body=None, http_headers=None)
