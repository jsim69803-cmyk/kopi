import re
safe_filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', __file__)