# Class Email Automation

This script sends followup emails with a free month discount code to attendees of RMM classes. It uses the Wild Apricot API and excludes AWA events, free events, and summer series events

## Usage
The "Class Followup" workflow runs automatically every weekday at 12PM CST via github actions, and it runs main.py. Log file is located at rmm_email_automation.log

## Description

1. **Email Sending**: Sends follow-up emails to RMM class attendees, offering a free month discount code. 
2. **Event Filtering**: Past events are filtered along with anything with "AWA", "free", or "Summer" in the title


## Contribution
Feel free to fork the project and submit pull requests for any enhancements.

## License
[MIT License](LICENSE)

## Contact
For more information, contact the RMM general email at [secretary@redmountainmakers.org](mailto:secretary@redmountainmakers.org) and it will be forwarded appropriately.
