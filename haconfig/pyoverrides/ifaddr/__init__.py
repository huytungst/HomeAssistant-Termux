# Android (udocker) workaround: If ifaddr fails due to /proc/net permission issues, return an empty list.
class Adapter:
    pass
def get_adapters():
    try:
        # Since /proc access is blocked in this environment and always fails, the original function is skipped even if it exists.
        return []
    except Exception:
        return []
