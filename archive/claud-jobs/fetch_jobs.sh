#!/bin/bash

# Fetch LinkedIn job postings for Product Engineer in Italy
output_file="linkedin_jobs_raw.html"
> "$output_file"

for start in 0 25 50; do
  echo "Fetching start=$start..."
  curl -s -A "Mozilla/5.0" "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Product%20Engineer&geoId=103350119&f_TPR=r86400&start=$start" >> "$output_file"
  sleep 2
done

echo "Raw HTML saved to $output_file"
