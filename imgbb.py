import requests

def upload_image_to_imgbb(image_path, api_key):
    """
    Uploads an image to ImgBB.

    :param image_path: Path to the image to upload.
    :param api_key: Your ImgBB API key.
    :return: URL of the uploaded image or an error message.
    """
    upload_url = 'https://api.imgbb.com/1/upload'
    with open(image_path, 'rb') as image_file:
        files = {
            'image': image_file,
        }
        data = {
            'key': api_key,
        }
        response = requests.post(upload_url, files=files, data=data)
        
        if response.status_code == 200:
            response_data = response.json()
            if response_data['success']:
                return response_data['data']['url']
            else:
                return f"Error: {response_data['error']['message']}"
        else:
            return f"Error: {response.status_code}"

# Example usage
api_key = 'your_imgbb_api_key'  # Replace with your ImgBB API key
image_path = 'path/to/your/image.jpg'  # Replace with your image path
uploaded_image_url = upload_image_to_imgbb(image_path, api_key)
print(f'Uploaded image URL: {uploaded_image_url}')