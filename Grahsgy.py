
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

# Prompt user to upload CV
# cv_file = input("Please upload your CV: ")

# # Extract content from CV
# cv_data = open(cv_file, 'r')
# cv_content = cv_data.read()

# Search www.linkedin.com and www.glassdoor.com for junior software developer engineering jobs
# Use selenium and beautifulsoup4

# Set up webdriver
driver = webdriver.Chrome()

# Search www.linkedin.com
driver.get('https://www.linkedin.com/jobs/search?keywords=junior%20software%20developer%20engineering&location=United%20States')

# Parse page with BeautifulSoup
page = requests.get(driver.current_url)
soup = BeautifulSoup(page.content, 'html.parser')

# Extract job descriptions
job_descriptions = soup.find_all('div', class_='description__text description__text--rich')

# Create cover letter for each job
for job_description in job_descriptions:
    # Fill up required spaces with details extracted from CV
    cover_letter = job_description + cv_content

    # Submit filled form
    driver.find_element_by_name('cover_letter').send_keys(cover_letter)
    driver.find_element_by_name('submit').click()

# Close webdriver
driver.close()