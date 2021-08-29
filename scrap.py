import urllib.request


def getCatImage(Width=200, Height=200):
    url = f'https://placekitten.com/g/{Width}/{Height}'
    print('Processing...')
    response = urllib.request.urlopen(url)
    if int(response.getcode()) == 200:
        image = response.read()
        try:
            with open(f'C:/Users/HIPAA/Desktop/Cat{Width}X{Height}.jpg', 'wbr') as file:
                file.write(image)
                print('Finished!')
        except OSError as reason:
            print(reason)
    else:
        print('Website lost!')


width = int(input('Input the width of cat image:'))
height = int(input('Input the height of cat image:'))
getCatImage(width, height)
