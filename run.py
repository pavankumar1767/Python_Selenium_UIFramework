# import os
#
# # Delete the 'report' directory if it exists (Windows command)
# if os.path.exists('report'):
#     os.system('rmdir /s /q report')
#
# test_cases = [
#     "testCases/data_extraction_time/test_01_login.py::test_login1",
#     "testCases/Users/test_01_CreateUser.py::test_create_user_api",
#     "testCases/Users/test_02_GetUserInfo.py::test_get_user_info_api",
#     "testCases/Users/test_03_updateUser.py::test_update_user_api",
#     "testCases/Users/test_04_ForgetPassword.py::test_forget_password_api",
#     "testCases/Users/test_05_DeleteUser.py::test_delete_user_api",
#     "testCases/Users/test_06_ReadUsers.py::test_read_users_api",
#
#     # "testCases/resource/test_getResource.py::test_get_resource_api",
#     # "testCases/resource/test_UpdateResource.py::test_update_resource_api",
#     # "testCases/resource/test_DeleteResource.py::test_delete_resource_api",
#
# ]
# # Run pytest with Allure reporting
# os.system(f"pytest -v -s --alluredir=report {' '.join(test_cases)}")
# # Serve the Allure report
# os.system("allure serve report")



















#
#
#
#
#
#
#
#
#
#

import os
import shutil

from utilities.email import send_email

report_dir = "report"

if os.path.exists(report_dir):
    shutil.rmtree(report_dir)  # ✅ Cross-platform way to delete a directory


test_cases = [
    "testCases/test_login.py"
]

os.system(f"pytest -v -s --alluredir=report {' '.join(test_cases)}")
## os.system("allure generate report -o allure-report --clean")
os.system("allure generate --single-file report -o allure-report --clean")

index_html_path = os.path.join("allure-report", "index.html")
recipients = ["pavan.karri@covalensedigital.com"]

send_email(
    subject="Allure Test Report",
    body="Please find the attached Allure test report (index.html).",
    to_email=recipients,
    attachment_path=index_html_path
)





