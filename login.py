import time

from creds import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

USERNAME = username
PASSWORD = password

driver = webdriver.Chrome()

# Function to log in to Twitter
def login_to_twitter():
    driver.get("https://x.com/login")
    time.sleep(2)

    # Locate the username and password fields
    username_field = driver.find_element(By.NAME, "text")
    username_field.send_keys(USERNAME)
    username_field.send_keys(Keys.ENTER)
    time.sleep(5)

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.ENTER)
    time.sleep(10)  # Allow time for login to complete

# Function to scrape comments from a tweet
def scrape_comments(tweet_url, max_comments=50):
    
    driver.get(tweet_url)
    time.sleep(10)  # Allow time for the page to load

    comments = set()
    while len(comments) < max_comments:
        # Find all comment elements
        comment_elements = driver.find_elements(By.XPATH, '//div[@data-testid="tweetText"]')
        
        # Extract and add comment text
        for comment in comment_elements:
            comment_text = comment.text
            if comment_text and comment_text not in comments:
                comments.add(comment_text)
                
            # Stop if we have enough comments
            if len(comments) >= max_comments:
                break
        
        # Scroll down to load more comments
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)  # Wait for more comments to load

    return list(comments)

# Log in to Twitter
login_to_twitter()

# Navigate to the tweet and scrape comments
tweet_url = "https://x.com/cinema_T_farsi/status/1851211228166705571"
comments = scrape_comments(tweet_url, max_comments=50)

# Save comments to a file
with open("farsi_comments.txt", "w", encoding="utf-8") as f:
    for comment in comments:
        f.write(comment + "\n")

print("Comments have been saved to 'tweet_comments.txt'")

# Close the browser
driver.quit()
