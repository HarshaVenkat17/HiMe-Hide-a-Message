from PIL import Image 

class Convert():
        def __init__(self):
            package=1
        def genData(self,data): 
                newd = []  
                for i in data: 
                    newd.append(format(ord(i), '08b')) 
                return newd 

        def modPix(self,pix, data): 
            datalist = self.genData(data) 
            lendata = len(datalist) 
            imdata = iter(pix) 
          
            for i in range(lendata): 
                pix = [i for i in imdata.__next__()[:3]+imdata.__next__()[:3]+
                                          imdata.__next__()[:3]] 
                for j in range(0, 8): 
                    if (datalist[i][j]=='0') and (pix[j]% 2 != 0): 
                        if (pix[j]% 2 != 0): 
                            pix[j] -= 1
                    elif (datalist[i][j] == '1') and (pix[j] % 2 == 0): 
                        pix[j] -= 1
                if (i == lendata - 1): 
                    if (pix[-1] % 2 == 0): 
                        pix[-1] -= 1
                else: 
                    if (pix[-1] % 2 != 0): 
                        pix[-1] -= 1
                pix = tuple(pix) 
                yield pix[0:3] 
                yield pix[3:6] 
                yield pix[6:9] 
          
        def encode_enc(self,newimg, data): 
            w = newimg.size[0] 
            (x, y) = (0, 0) 
              
            for pixel in self.modPix(newimg.getdata(), data):
                newimg.putpixel((x, y), pixel) 
                if (x == w - 1): 
                    x = 0
                    y += 1
                else: 
                    x += 1
                    
        def encode(self,img,data): 
            image = Image.open(img, 'r') 
            if (len(data) == 0): 
                raise ValueError('Data is empty') 
                  
            newimg = image.copy() 
            self.encode_enc(newimg, data)
            ind=img.rfind('.')
            new_img_name = img[:ind]+"(1)"+img[ind:]
            newimg.save(new_img_name, str(new_img_name.split(".")[1].upper())) 

        def decode(self,img): 
            image = Image.open(img, 'r') 
            data = '' 
            imgdata = iter(image.getdata()) 
              
            while (True): 
                pixels = [i for i in imgdata.__next__()[:3]+imgdata.__next__()[:3]
                                         +imgdata.__next__()[:3]] 
                binstr = '' 
                for i in pixels[:8]: 
                    if (i % 2 == 0): 
                        binstr += '0'
                    else: 
                        binstr += '1'     
                data += chr(int(binstr, 2)) 
                if (pixels[-1] % 2 != 0):
                    return data
 
