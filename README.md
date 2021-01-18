# ImageRepository
The application should be tested with Postman
All dependency required by the application are listed in the reqirements.txt file
To create an Image object, User need to register through the endpoint host/own/owner. Fields needed are username, email, password, confirm_password, first_name, last_name then owner_info
When attempting to create or delete an image authentication is need.
The database for the Application is hosted on a live server
# ENDPOINTS:
  create image: host/img/create_image/ (with POST request, required fields are tag, name, image, description with optional fields tag2, tag3)
  
  search image: host/img/search/<image_tag>( with GET reguest)
  
  image_edit: host/img/image_details/<image_id> (with PUT request, required fields are tag, name, image, description with optional fields tag2, tag3)
  
  delete_image: host/img/image_details/<image_id> (with DELETE request)
  
  get_image: host/img/get_image/<name> (with GET request)
  
  autenticate: host/api-token-auth/ (with POST request, required fields are username, password. An authentication token is generated which is added to the headers with            Authentication as the key and Token <token generated> as value and sent were required in a request.
  
  register_user: host/own/owner (with POST request, required fields listed above)
  
