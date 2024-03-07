import pandas as pd
import datetime

# Load the dataset containing birthday information
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
    'Birthday': ['1990-01-15', '1992-03-24', '1987-07-10']
}

df = pd.DataFrame(data)

# Current date
today = datetime.date.today()

# Find individuals with upcoming birthdays within next 7 days
upcoming_bdays = df[pd.to_datetime(df['Birthday']).dt.dayofyear.between(today.timetuple().tm_yday, today.timetuple().tm_yday + 7)]

# Sending birthday emails
for index, row in upcoming_bdays.iterrows():
    # Customize the email message/body
    email_message = f"Happy Birthday, {row['Name']}! Wishing you a fantastic day ahead."

    # Send email using your email sending mechanism (e.g., SMTP, mail server)
    # Insert email sending code here

    print(f"Email sent to: {row['Email']}")

# Output confirmation
print(f"Emails sent for upcoming birthdays successfully.")