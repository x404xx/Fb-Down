import yt_dlp


class FacebookDown:
    """
    A class to handle downloading videos from Facebook.

    Args:
        video_url (str): The URL of the video to download.
        output_dir (str): The directory where the video will be saved. Defaults to current project directory.
        quiet (bool, optional): Whether to run the download quietly. Defaults to False.
        no_warn (bool, optional): Whether to suppress warnings. Defaults to False.
        end_ret (bool, optional): Whether to return to the beginning of the line after printing progress. Defaults to False.

    Raises:
        No specific exceptions are raised.

    Returns:
        None

    Examples:
        fb_downloader = FacebookDown(video_url="https://example.com/video", output_dir="/path/to/save")
    """

    def __init__(
        self, video_url, output_dir, quiet=False, no_warn=False, end_ret=False
    ):
        """
        Initializes the Facebook video downloader.

        Args:
            video_url (str): The URL of the video to download.
            output_dir (str): The directory where the video will be saved.
            quiet (bool, optional): Whether to run the download quietly. Defaults to False.
            no_warn (bool, optional): Whether to suppress warnings. Defaults to False.
            end_ret (bool, optional): Whether to return to the beginning of the line after printing progress. Defaults to False.

        Raises:
            No specific exceptions are raised.

        Returns:
            None
        """

        self.end_ret = end_ret
        self._download_video(video_url, output_dir, quiet, no_warn)

    def _progress_hooks(self, status):
        """
        Handles progress hooks for the video download.

        Args:
            status (dict): A dictionary containing status information about the download.

        Raises:
            No specific exceptions are raised.

        Returns:
            None
        """

        actions = {
            "finished": lambda: print(f"\n\nDownloaded - {status['filename']}"),
            "downloading": lambda: print(
                status["_percent_str"],
                status["_eta_str"],
                end="\r" if self.end_ret else "\n",
            ),
        }
        if status["status"] in actions:
            actions[status["status"]]()

    def _download_video(self, video_url, output_dir, quiet, no_warn):
        """
        Downloads a video using the provided video URL and saves it to the specified output directory.

        Args:
            video_url (str): The URL of the video to download.
            output_dir (str): The directory where the video will be saved.
            quiet (bool): Whether to run the download quietly.
            no_warn (bool): Whether to suppress warnings.

        Raises:
            No specific exceptions are raised.

        Returns:
            None
        """

        print("Download started..\n")
        with yt_dlp.YoutubeDL(
            {
                "format": "b",
                "outtmpl": f"{output_dir}/%(id)s.%(ext)s",
                "quiet": quiet,
                "no_warning": no_warn,
                "progress_hooks": [self._progress_hooks],
            }
        ) as ydl:
            ydl.download([video_url])
