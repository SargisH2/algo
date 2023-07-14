import requests # request img from web
import shutil # save img locally
# import csv

# with open('links.csv', 'r') as file:
#     reader = csv.reader(file, delimiter=',')
reader=['https://imacorp.com/wp-content/uploads/2017/12/IMA-Inc-Logo.jpg'] #for example
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'} # can be different
for index, row in enumerate(reader):
    url=row
    file_name=f'img{index}.png'
    res = requests.get(url, headers=headers, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')

