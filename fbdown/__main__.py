import os
from argparse import ArgumentParser

from .api import FacebookDown


def setup_argparse():
    """
    Summary: Sets up argument parsing for downloading a video from Facebook.

    Explanation: This function configures an ArgumentParser to handle command-line arguments related to downloading a video or reels from Facebook.

    Args:
        None

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """

    parser = ArgumentParser(
        description="Download a (regular video|reels) from facebook."
    )
    parser.add_argument(
        "-u",
        "--video_url",
        type=str,
        required=True,
        help="The URL of the video to download.",
    )
    parser.add_argument(
        "-od",
        "--output_dir",
        default=os.getcwd(),
        type=str,
        help="The directory where the video will be saved. Defaults to current project directory.",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Whether to run the download quietly. Defaults to False.",
    )
    parser.add_argument(
        "-nw",
        "--no_warn",
        action="store_true",
        help="Whether to suppress warnings. Defaults to False.",
    )
    parser.add_argument(
        "-er",
        "--end_ret",
        action="store_true",
        help="Whether to return to the beginning of the line after printing progress. Defaults to False.",
    )
    return parser.parse_args()


def parse_arguments():
    """
    Summary: Returns the setup for argparse.

    Explanation: This function returns the setup for argparse, which is used for parsing command-line arguments.

    Args:
        None

    Returns:
        argparse.ArgumentParser: The setup for argparse.
    """

    return setup_argparse()


def create_download_directory(output_dir, subfolder="Facebook Videos"):
    """
    Summary: Creates a download directory for storing Facebook videos.

    Explanation: This function creates a directory for downloading files, ensuring that the directory exists or is created if it doesn't already.

    Args:
        output_dir (str): The directory where the download directory will be created. Defaults to the current working directory.
        subfolder (str): The name of the subfolder within the output directory. Defaults to "Facebook Videos".

    Returns:
        str: The path of the created download directory.
    """

    directory = os.path.join(output_dir, subfolder)
    os.makedirs(directory, exist_ok=True)
    return directory


def download_facebook_video(video_url, output_dir, quiet, no_warn, end_ret):
    """
    Summary: Main function for downloading a video from Facebook.

    Explanation: This function parses arguments, creates an output directory, and initiates the download of a video from Facebook.

    Args:
        video_url (str): The URL of the video to download.
        output_dir (str): The directory where the video will be saved.
        quiet (bool): Whether to run the download quietly.
        no_warn (bool): Whether to suppress warnings.
        end_ret (bool, optional): Whether to return to the beginning of the line after printing progress.

    Returns:
        None
    """

    FacebookDown(video_url, output_dir, quiet, no_warn, end_ret)


def main():
    """
    Summary: Initiates the process of parsing arguments, creating a download directory, and downloading a video from Facebook.

    Explanation: This function orchestrates the steps required to parse command-line arguments, set up the download directory, and initiate the video download process from Facebook.

    Args:
        None

    Returns:
        None
    """

    args = parse_arguments()
    output_dir = create_download_directory(args.output_dir)
    download_facebook_video(
        args.video_url, output_dir, args.quiet, args.no_warn, args.end_ret
    )


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
