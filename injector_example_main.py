import argparse

from injector_example.app_context import Application
from injector_example.profiles import Profiles

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--Profile", help="defines the configuration profile")
    args = parser.parse_args()
    # If user does not provide profile in command line default profile used
    profile_string = 'DEFAULT'
    if args.Profile:
        profile_string = args.Profile.upper()
    profile = Profiles[profile_string]
    application = Application(profile)
    application.run()
