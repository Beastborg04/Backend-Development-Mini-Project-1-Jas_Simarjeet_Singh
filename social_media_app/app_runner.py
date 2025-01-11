import subprocess

def run_user_service():
    subprocess.Popen(["/Users/jassimarjeet/Downloads/Social_media_app_Jas_Simarjeet_Singh/version_2/social_media_app/venv/bin/python3", "user_app/app.py"])

def run_post_service():
    subprocess.Popen(["/Users/jassimarjeet/Downloads/Social_media_app_Jas_Simarjeet_Singh/version_2/social_media_app/venv/bin/python3", "post_app/app.py"])

def run_comment_service():
    subprocess.Popen(["/Users/jassimarjeet/Downloads/Social_media_app_Jas_Simarjeet_Singh/version_2/social_media_app/venv/bin/python3", "comment_app/app.py"])

if __name__ == '__main__':
    run_user_service()
    run_post_service()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating both the processes. Alvida!")
