import pandas as pd
import boto3
from datetime import datetime
from io import BytesIO

# Initialize AWS SES client and S3 client
ses_client = boto3.client('ses', region_name='ap-south-1')  # Replace with your AWS region
s3_client = boto3.client('s3')

# Constants for S3
BUCKET_NAME = 'food-delivery-app-assets'  # Replace with your S3 bucket name
STUDENTS_FILE_KEY = 'Students.xlsx'  # Path to Students.xlsx in S3
ATTENDANCE_FILE_KEY = 'Attendance.xlsx'  # Path to Attendance.xlsx in S3

# Function to read Excel files from S3
def read_excel_from_s3(bucket_name, file_key):
    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    return pd.read_excel(BytesIO(response['Body'].read()))

# Load Excel files from S3
students_df = read_excel_from_s3(BUCKET_NAME, STUDENTS_FILE_KEY)
attendance_df = read_excel_from_s3(BUCKET_NAME, ATTENDANCE_FILE_KEY)

# Get today's date in the correct format
today = datetime.now().strftime('%d-%m-%Y')

# Check attendance and send emails
for _, student in students_df.iterrows():
    student_id = student['student_id']
    student_email = student['email']
    
    # Check attendance for today
    attendance_record = attendance_df[(attendance_df['date'] == today) & (attendance_df['student_id'] == student_id)]
    
    if not attendance_record.empty:
        status = attendance_record['status'].values[0]
        if status == 'Present':
            message = f"You were present for the class on {today}."
        else:
            message = f"You were absent for the class on {today}."
    else:
        message = f"No attendance record found for today ({today})."

    # Send email using AWS SES
    response = ses_client.send_email(
        Source='pbot6789@gmail.com',  # Replace with your verified email in SES
        Destination={
            'ToAddresses': [student_email],
        },
        Message={
            'Subject': {
                'Data': f'Attendance Notification for {today}',
            },
            'Body': {
                'Text': {
                    'Data': message,
                },
            },
        }
    )
    print(f"Sent email to {student_email}: {message}")

# Optionally, save the final attendance status to S3
final_attendance_file_key = 'path/to/Final_Attendance.xlsx'  # Path to save the final attendance status
attendance_df.to_excel('Final_Attendance.xlsx', index=False)

# Upload the final attendance status back to S3
s3_client.upload_file('Final_Attendance.xlsx', BUCKET_NAME, final_attendance_file_key)
print("Final attendance status saved to S3 at path:", final_attendance_file_key)

