test_id = 57872628

import os
from datetime import datetime, timezone
from class_email_functions import*

api_key = os.environ.get("API_KEY")#Gets the API key from the environment variables
Discount_Code = os.environ.get("DISCOUNT_CODE")#Gets the discount code from the environment variables
access_token = get_access_token(api_key)#Gets the access token from the WA API

template_email_file_path = 'class_discount_email_template_new.html'

html_template = read_template_file(template_email_file_path)

filled_template = fill_email_template('Test', 'Test', Discount_Code, html_template)

send_email(access_token,filled_template, '57872628', 'Test', 'mcbehling86@gmail.com')

#test_date = datetime(2024, 1, 1, tzinfo=timezone.utc) ,test_date
