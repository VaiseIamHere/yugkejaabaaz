import cv2
import easyocr
import matplotlib.pyplot as plt
import utils
import tableextractor

tt = utils.initialize()

# img = cv2.imread('./image/vaibhav_tt10.png')

te = tableextractor.TableExtractor('./image/vaibhav_tt.png')
img = te.execute()


reader = easyocr.Reader(['en'], gpu=False)
text = reader.readtext(img)

rows = utils.sort_row(text)
cell_height = utils.mean_cell_height(rows[0])
start_height = utils.start_point(text)

days = rows[1:]

utils.assign_loop(tt, days, start_height, cell_height)
for i in tt:
    print(i)

plt.imshow(cv2.cvtColor(img, 4))
plt.axis('off')
plt.show()

