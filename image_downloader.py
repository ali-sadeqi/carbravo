import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
import string
import random
import os

# Define the path to the CSV file containing the links
csv_file_path = 'filtered_hrefs.csv'

def generate_random_filename(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))





with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for handler in csv_reader:
        for link in handler:
            link = link.replace(' ' , '')
            link = link[1:-1]
            print(link)
            options = Options()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(options=options)

            driver.get(url = link)

            try:
                image_tags = driver.find_element(By.CLASS_NAME, 'w-full.h-full.object-cover.stat-image-link')
                link_href = image_tags.get_attribute("src")
                for i in range(70):
                    num = f'0-{i}.jpg'
                    link_href = link_href[:103]
                    print('link_href: ' , link_href)
                    image_url = link_href + num
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        # Generate a random filename for the image
                        random_filename = generate_random_filename() + '.jpg'

                        # Specify the directory where you want to save the image
                        save_directory = 'images'  # Change this to your desired directory

                        # Create the save directory if it doesn't exist
                        os.makedirs(save_directory, exist_ok=True)

                        # Construct the full path for saving the image
                        save_path = os.path.join(save_directory, random_filename)

                        # Save the image to the specified directory with the random filename
                        with open(save_path, 'wb') as file:
                            file.write(response.content)

                        print(f"Image downloaded and saved as '{random_filename}' in '{save_directory}'.")
                    else:
                        print(f"Failed to download the image. Status code: {response.status_code}")
            except:
                print('error')

        # Process the image tags (you can print or save them)
        #for img_tag in image_tags:
        #    print(img_tag.get_attribute('src'))

# Close the WebDriver when done
#driver.quit()