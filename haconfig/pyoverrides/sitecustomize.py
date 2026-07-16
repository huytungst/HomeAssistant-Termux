# In the Android + udocker environment, any /proc paths that trigger a PermissionError are handled
# as if they do not exist (evaluated as False), thereby allowing Home Assistant to start without interruption.

import pathlib

_orig_exists = pathlib.Path.exists

def _safe_exists(self, *args, **kwargs):
    try:
        return _orig_exists(self, *args, **kwargs)
    except PermissionError:
        s = str(self)
        # Typical paths include: ip_forward, net/ 
        if s.startswith("/proc/sys/net/ipv4/ip_forward") or s.startswith("/proc/net"):
            return False
        # In other cases, raise an exception for debugging.
        raise

pathlib.Path.exists = _safe_exists
