import argparse
import time
import instaloader 
def download_profile(username):
    # Start downloading the profile.
    bot = instaloader.Instaloader()
    start_time = time.time()
    bot.download_profile(username)
    end_time = time.time()
    # Calculate the estimated wait time.
    estimated_wait_time = end_time - start_time
    # Print the estimated wait time.
    print("Estimated wait time:", estimated_wait_time)
if __name__ == "__main__":
    # Create an ArgumentParser object.
    parser = argparse.ArgumentParser()
    # Add the username argument.
    parser.add_argument("username", help="The username of the profile to download.")
    # Parse the arguments.
    args = parser.parse_args()
    # Download the profile.
    download_profile(args.username)
