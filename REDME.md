# Multi-threaded File Server

## **Description:**

This project is a demonstration of a multi-threaded file server using Python's socket and threading libraries. The server supports multiple clients concurrently, each handled by a separate thread, allowing for efficient and high-volume file operations.

## **How to use:**

**Step 1:** go to project directory and open command prompt and start server using command:

```
python server.py
```

![Untitled](screenshots/step_1.png)

**Step 2:** Open another command prompt and perform various operations using below commands(use file name and file extension):

**Upload File:**

```
python client.py upload file_name.txt
```

![Untitled](screenshots/step_2_upload.png)

**Rename File:**

```
python client.py old_file_name.txt new_file_name.txt
```

![Untitled](screenshots/step_2_rename.png)

**Download File:**

```
python client.py download file_name.txt
```

![Untitled](screenshots/step_2_download.png)

**Delete File:**

```
python client.py delete file_name.txt
```

![Untitled](screenshots/step_2_delete.png)

### **Key Features**:

- **Multi-threading**: Each client connection is managed in a separate thread, allowing the server to handle multiple simultaneous connections and operations efficiently.
- **File operations**: The server supports upload, download, delete, and rename operations, allowing clients to manage files on the server.
- **Synchronization**: Implemented file operation handling to prevent race conditions when multiple threads access the same file.
- **Efficient file transfers**: Files are transferred in chunks rather than loading the entire file into memory, making the system more memory efficient and scalable.

### **Technologies Used**:

- **Python**: The project is entirely written in Python, leveraging the built-in socket and threading libraries for network communication and concurrent processing.
- **Socket Programming**: Used for network communication between the client and the server.
- **Threading**: Used for handling multiple client connections simultaneously.