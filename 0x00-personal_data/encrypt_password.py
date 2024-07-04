#!/usr/bin/env python3
"""
encryption
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """encrypt"""
    encoded = password.encode()
    return bcrypt.hashpw(encoded, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate password"""
    valid = False
    encoded = password.encode()
    return bcrypt.checkpw(encoded, hashed_password)
