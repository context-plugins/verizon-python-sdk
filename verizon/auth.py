from __future__ import annotations

from dataclasses import dataclass

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    thingspace_oauth: AuthScheme
    vz_m2_m_token: AuthScheme
    session_token: AuthScheme
    thingspace_oauth1: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    thingspace_oauth: AsyncAuthScheme
    vz_m2_m_token: AsyncAuthScheme
    session_token: AsyncAuthScheme
    thingspace_oauth1: AsyncAuthScheme
