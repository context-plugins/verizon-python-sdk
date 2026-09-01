from __future__ import annotations

from dataclasses import dataclass

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    thingspace_oauth: AuthScheme
    vz_m2m_session_token: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    thingspace_oauth: AsyncAuthScheme
    vz_m2m_session_token: AsyncAuthScheme
