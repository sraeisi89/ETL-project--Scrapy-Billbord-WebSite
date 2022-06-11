from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def list_files():
    service = build("drive", "v3")
    request = service.files().list()
    response = request.execute()
    print(response)

def upload_file():
    metadata = {
        "name": "Ultimate",
        "mimeType": "application/csv"
    }

    media = MediaFileUpload("Ultimate.csv", mimetype="application/csv")

    service = build("drive", "v3")
    request = service.files().create(body=metadata, media_body=media)
    response = request.execute()
    print(response)
    return response["id"]

def create_sheet():
    metadata = {
        "name": "Ultimate",
        "mimeType": "application/vnd.google-apps.spreadsheet",
    }

    media = MediaFileUpload("Ultimate.csv", mimetype="text/csv")
    service = build("drive", "v3")
    request = service.files().create(body=metadata, media_body=media)
    response = request.execute()

    print(response)
    return response["id"]

def share(file_id, role="owner"):
    metadata = {
        "type": "user",
        "emailAddress": "raisisoheil89@gmail.com",
        "role": role,
    }

    service = build("drive", "v3")
    request = service.permissions().create(
        fileId=file_id,
        body=metadata,
        transferOwnership=(role == "owner"))
    response = request.execute()

    print(response)


if __name__ == "__main__":
    share(create_sheet(), "writer")