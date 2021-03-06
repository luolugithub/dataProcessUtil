import os


class BatchRename:
    def __init__(self):
        self.path = '/home/xkjs/Downloads/data/BoPian/阿布扎比薄片照片/Habshan/image/'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 0
        for item in filelist:
            if item.endswith('.tif'):
            # if item.__contains__("煤层"):
                src = os.path.join(os.path.abspath(self.path), item)
                if i < 10:
                    dst = os.path.join(os.path.abspath(self.path), 'luolu_0000' + str(i) + '.jpg')
                else:
                    dst = os.path.join(os.path.abspath(self.path), 'luolu_000' + str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
