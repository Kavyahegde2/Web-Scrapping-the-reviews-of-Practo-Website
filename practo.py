import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

# Set up Chrome driver
chrome_driver_path = "C:/Users/kavya/Downloads/chromedriver-win64 (2)/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# URL of the website
url = "https://www.practo.com/bangalore/clinic/new-manipal-laser-dental-clinic-hsr-layout-1/reviews"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Click the "View more" button multiple times
num_clicks = 1 # Number of times to click "View more"
for _ in range(num_clicks):
    try:
        # view_more_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/button")
        view_more_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/button")
        view_more_button.click()
        time.sleep(5)  # Wait for loading more reviews
    except Exception as e:
        print("Error occurred:", e)
        break

# Get the updated page source
page_source = driver.page_source

# Parse the HTML content
soup = BeautifulSoup(page_source, 'html.parser')

# Find all review containers
review_containers = soup.find_all("div", class_="pure-u-22-24 u-lheight-default")

# Initialize lists to store data
review_data = []

# Extract review data
for i, review in enumerate(review_containers, start=1):
    review_info = {}
    
    # Extract reviewer name
    reviewer_name = review.find("span", class_="u-bold", attrs={"data-qa-id": "reviewer-name"}).text.strip()
    review_info["Reviewer Name"] = reviewer_name
    
    # Extract review time
    review_time_span = review.find("span", class_="u-color--grey3", attrs={"data-qa-id": "web-review-time"})
    review_time_text = review_time_span.text.strip() if review_time_span else "N/A"
    review_info["Review Time"] = review_time_text
    
    # Extract visited doctor
    visited_for_span = review.find("p", class_="feedback__content u-title-font u-bold")
    visited_for_text = visited_for_span.text.strip() if visited_for_span else "N/A"
    review_info["Visited Doctor"] = visited_for_text
    
    # Extract review text
    review_text = review.find("p", class_="feedback__content u-large-font")
    review_text_text = review_text.text.strip() if review_text else "N/A"
    review_info["Review Text"] = review_text_text
    
    
    # Check if recommendation is present
    recommendation = review.find("i", class_="icon-ic_like", attrs={"data-qa-id": "feedback_thumbs_up"})
    if recommendation:
        review_info["Recommendation"] = "I recommend the doctor"
    else:
        review_info["Recommendation"] = "Not available"
    
    # Append review info to the list
    review_data.append(review_info)

# Close the browser window
driver.quit()

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(review_data)

# Save DataFrame to Excel file
excel_filename = "new-manipal-laser-dental-clinic-hsr-layout.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Data saved to {excel_filename}")
