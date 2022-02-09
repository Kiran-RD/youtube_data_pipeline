Data Source: https://www.kaggle.com/datasnaek/youtube-new?select=US_category_id.json

Azure Steps
1. Create a Storage account and then create 3 containers for raw_data, cleansed_data and analytics_data
2. create categories_data and videos_data folders under cleansed_data
3. login to azcopy using
    azcopy login --tenant-id <tenant-id>
4. Run the below commands
    azcopy copy .\*.json https://youtubedatasa.blob.core.windows.net/raw-data/categories_data/
    azcopy copy .\*.csv https://youtubedatasa.blob.core.windows.net/raw-data/videos_data/