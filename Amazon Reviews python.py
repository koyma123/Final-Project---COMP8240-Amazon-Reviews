import os
import random

# Define the path to the Amazon reviews dataset
dataset_folder = r'C:\Users\PC\Downloads\Amazon Reviews\processed_acl'

# Categories in the dataset (folders within the main directory)
categories = ["books", "dvd", "electronics", "kitchen"]

# Initialize a list to store concatenated reviews with boundaries
segmented_reviews = []

# Loop through each category to load and concatenate reviews
for category in categories:
    category_path = os.path.join(dataset_folder, category, "positive.review")
    negative_path = os.path.join(dataset_folder, category, "negative.review")
    
    # Read positive reviews
    with open(category_path, 'r', encoding='latin-1') as pos_file:
        pos_reviews = pos_file.read().split("<review>")
        for review in pos_reviews:
            review_text = review.strip()
            if review_text:
                segmented_reviews.append(review_text)
                segmented_reviews.append("===END===")  # Marker for segmentation boundary
    
    # Read negative reviews
    with open(negative_path, 'r', encoding='latin-1') as neg_file:
        neg_reviews = neg_file.read().split("<review>")
        for review in neg_reviews:
            review_text = review.strip()
            if review_text:
                segmented_reviews.append(review_text)
                segmented_reviews.append("===END===")

# Combine all segments into a single document
final_text = "\n\n".join(segmented_reviews)

# Define the output path for the segmented file
output_path = r'C:\Users\PC\Downloads\Amazon Reviews\amazon_segmented_reviews.txt'
with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(final_text)

print(f"Preprocessing complete. Segmented file saved as '{output_path}'.")
