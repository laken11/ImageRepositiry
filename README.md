# ImageRepository
The requirments needed to run this aplication are specifed in the reqirements.txt file
The database for the application is hosted on a live server
The application only allows registered users to create Image objectc. Register Through own/owner/
Create an Image Object through the endpoint Ima/create_image/, authentication is needed to create an Image and it is done through the endpoint api-token-auth/ by sending owner username and password to this endpoit and specifying The Authentication Token in the header like this "Authentication: Token: --the token--
Images sre search through endpoint search/<tag of image>
An image is Delete after authenticating through the endpoint image_details/<image_id>
An image is gotten through endpoint get_image/<image name>
Use postman to test the end points
