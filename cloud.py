import dropbox 

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
    
def main():
    access_token = "sl.BHOOeQDY_4lyJhbrPakS3NDKKskT5Xw1kUCGyUkUN6oyP0tynOIkfHooP8wiM2k7H3tWF5cHU9zqLYDAgGIpKPFTrwTh391qDnMD7oqB7JKnO9dY6jiwZjbfxn42mhyktyofK5w"
    transferData = TransferData(access_token)
    file_from = input("enter the file path to transfer ")
    file_to = input("full path to upload to dropbox ")
    transferData.upload_file(file_from,file_to)
    print("file has been moved ")

main()

