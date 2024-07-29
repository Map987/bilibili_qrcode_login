import os
import login
import utils

def get_script_dir():
    """Get the directory of the current script."""
    return os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    script_dir = get_script_dir()
    cookie_path = os.path.join(script_dir, "cookie.json")

    # Save the cookie to a file in the same directory as the script
    utils.save_json_file(path=cookie_path, data=login.get_cookie())
