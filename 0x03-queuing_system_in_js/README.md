This project is a back-end application focused on developing a simple platform for uploading and viewing files. It covers various aspects of back-end development including user authentication, NodeJS, MongoDB, Redis, pagination, and background processing. The primary goal is to integrate these technologies to create a functional and efficient file management service.

Features
1. User Authentication
Token-Based Authentication: Secure user authentication using tokens. Users must authenticate to access platform features.
2. File Management
List All Files: Retrieve and display a list of all uploaded files.
Upload New Files: Users can upload new files to the platform.
Change File Permissions: Users can modify the access permissions of their uploaded files.
View Files: View the content of uploaded files directly through the platform.
Generate Thumbnails: Automatically create and display thumbnails for image files.
Technologies Used
1. Node.js
Express Framework: Used for setting up the API and routing.
2. MongoDB
Data Storage: MongoDB is used to store information about users and files.
3. Redis
Temporary Data Storage: Redis is utilized for storing session data and caching.
4. Background Processing
Bull: A Node.js library used for managing background jobs like thumbnail generation.
5. Additional Tools
Nodemon: A utility that monitors for changes in the source code and automatically restarts the server.
Mocha: A JavaScript test framework used for writing test cases to ensure the functionality of the application.
Image Thumbnail: A library for generating thumbnails from images.
Mime-Types: A utility to detect the MIME type of a file, which helps in handling file uploads and viewing.
