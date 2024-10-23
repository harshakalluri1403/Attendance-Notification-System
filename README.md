# Attendance Notification System

This project implements an attendance notification system that reads student attendance records from AWS S3 and sends notifications via AWS Simple Email Service (SES). The system checks each student's attendance status for the day and sends an appropriate email notification.

![](https://github.com/harshakalluri1403/Attendance-Notification-System-Using-AWS/blob/02f902c92cc6ca3038ae7c55d2209db699994e83/a)

![](https://github.com/harshakalluri1403/Attendance-Notification-System-Using-AWS/blob/02f902c92cc6ca3038ae7c55d2209db699994e83/d)

## Features

- Reads student information and attendance records from Excel files stored in an AWS S3 bucket.
- Sends attendance notifications to students via email using AWS SES.
- Supports attendance status notifications for both present and absent students.
- Uploads the final attendance status back to S3 for record-keeping.

## Requirements

- Python 3.x
- `pandas` library
- `boto3` library

## Setup

1. **Install Required Libraries**

   Make sure you have the necessary libraries installed. You can install them using pip:

   ```bash
   pip install pandas boto3
   ```
2. AWS Configuration
   - Ensure you have an AWS account and have configured your AWS credentials. You can do this by setting up the AWS CLI and running aws configure.
   - The email used as the sender in the SES must be verified in the AWS SES console.

3. S3 Bucket Setup
   - Create an S3 bucket (e.g., food-delivery-app-assets).
   - Upload the following Excel files to the S3 bucket:
      - Students.xlsx: Contains student IDs and their email addresses.

   ![](https://github.com/harshakalluri1403/Attendance-Notification-System-Using-AWS/blob/02f902c92cc6ca3038ae7c55d2209db699994e83/b)
       
      - Attendance.xlsx: Contains attendance records with student IDs and dates.

   ![](https://github.com/harshakalluri1403/Attendance-Notification-System-Using-AWS/blob/02f902c92cc6ca3038ae7c55d2209db699994e83/c)

## Usage
1. Update the following constants in the script to match your configuration:
 ```python
BUCKET_NAME = 'food-delivery-app-assets'  # Your S3 bucket name
STUDENTS_FILE_KEY = 'Students.xlsx'  # Path to Students.xlsx in S3
ATTENDANCE_FILE_KEY = 'Attendance.xlsx'  # Path to Attendance.xlsx in S3
```
2. Replace the Source email address in the send_email function with your verified email in SES:
 ```python
Source='pbot6789@gmail.com',  # Replace with your verified email in SES
 ```
3. Run the script:
 ```bash
python attend.py
 ```
