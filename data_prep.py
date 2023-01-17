image_dir = ''
categories = ['x','y']

data = []
labels = []



for category_index,category in enumerate(categories):
    for file in os.listdir(os.path.join(image_dir,category)):
        image_path = os.path.join(image_dir,category,file)
        image = imread(image_path)
        image = resize(image,(15,15))
        data.append(image.flatten())
        labels.append(category_index)
data = np.asarray(data)
labels = np.asarray(labels)




