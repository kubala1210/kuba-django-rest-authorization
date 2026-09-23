def acl_check(user, obj, action: str) -> bool:
    is_owner = user == getattr(obj, "owner", None)

    if action in {"read", "list", "detail"}:
        return True

    if action in {"update", "partial_update", "delete"}:
        return is_owner

    return False
