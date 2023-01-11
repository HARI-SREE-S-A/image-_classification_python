test_model = pickle.load(open('image_model','rb')
process_data = []
directory = ''
img = imread(directory)
img = resize(image,(15,15))
process_data.append(img.flatten())
process_data = np.asarray(process_data)
output = test_model.predict(process_data)
output = categories[output[0]]
                         
print(output)

                         
