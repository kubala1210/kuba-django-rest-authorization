

def acl_check(user, obj, action):

    if not user or user.is_authenticated():
        return False

    is_owner = obj.owner == user

    if action == 'read':
        return True

    if action in ['update', 'delete']:
        return is_owner

    return False
