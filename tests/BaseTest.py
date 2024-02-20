from datetime import datetime
import pytest


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:
    
    def generate_email_with_time_stamp(self):
        # Get the current date and time
        time_stamp = datetime.now().strftime(("%Y-%m-%d_%H-%M-%S"))
        return "mark9" + time_stamp + "@mark.com"
