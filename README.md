# multi-threaded-file-server
Implement a multi-threaded file server that supports UPLOAD, DOWNLOAD, DELETE and RENAME file operations. Use different folders to hold files downloaded to the client or uploaded to the server.

# Redme
-----------------------------
- client_dir - holds files downloaded to client side

- server_dir - holds files uploaded to server side

Step 1:
Open Command promt and start server using command:
python server.py

Step 2:
Open 2nd Command prompt and perform various operation using below commands:

Upload: python client.py upload Test_File.txt
Rename: python client.py rename Test_File.txt New_Test.txt
Download: python client.py download New_Test.txt
Delte: python client.py delete New_Test.txt

