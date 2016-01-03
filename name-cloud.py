from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread
import numpy as np
from PIL import Image

text = []
inp = raw_input("Enter Name:")
l = len(inp)
inp = inp.upper()

base = Image.new("RGB",(l*900,1000))
for i in range (1,100):
    text.append([inp,i])
x = 0
y = 0
for i in range(0,l):
    if inp[i] == 'A':
        a_mask = np.array(Image.open("Alphabets/A.png"))
        a = WordCloud(mask = a_mask, width = 50, height = 50).generate_from_frequencies(text).to_image()
        base.paste(a,(x,y))
        x+=900
        
    elif inp[i] == 'B':    
        b_mask = np.array(Image.open("Alphabets/B.png"))
        b = WordCloud(mask = b_mask, width = 40, height = 40).generate_from_frequencies(text).to_image()
        base.paste(b,(x,y))
        x+=900
        
    elif inp[i] == 'C':
        c_mask = np.array(Image.open("Alphabets/C.png"))
        c = WordCloud(mask = c_mask, width = 30, height = 30).generate_from_frequencies(text).to_image()
        base.paste(c,(x,y))
        x+=900
       
    elif inp[i] == 'D':
        d_mask = np.array(Image.open("Alphabets/D.png"))
        d = WordCloud(mask = d_mask, width = 50, height = 50).generate_from_frequencies(text).to_image()
        base.paste(a,(x,y))
        x+=900
        
    elif inp[i] == 'E':
        e_mask = np.array(Image.open("Alphabets/E.png"))
        e = WordCloud(mask = e_mask, width = 50, height = 50).generate_from_frequencies(text).to_image()
        base.paste(e,(x,y))
        x+=900
       
    elif inp[i] == 'F':    
        f_mask = np.array(Image.open("Alphabets/F.png"))
        f = WordCloud(mask = f_mask, width = 50, height = 50).generate_from_frequencies(text).to_image()
        base.paste(f,(x,y))
        x+=900
    elif inp[i] == 'G':
        g_mask = np.array(Image.open("Alphabets/G.png"))
        g = WordCloud(mask = g_mask, width = 50, height = 50).generate_from_frequencies(text).to_image()
        base.paste(g,(x,y))
        x+=900
        
    elif inp[i]=='H':
        h_mask=np.array(Image.open("Alphabets/H.png"))
        h= WordCloud(mask=h_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(h,(x,y))
        x+=900
    elif inp[i]=='I':
        i_mask=np.array(Image.open("Alphabets/I.png"))
        i= WordCloud(mask=i_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(i,(x,y))
        x+=900     
    elif inp[i]=='J':    
        j_mask=np.array(Image.open("Alphabets/J.png"))
        j= WordCloud(mask=j_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(j,(x,y))
        x+=900
    elif inp[i]=='K':    
        k_mask=np.array(Image.open("Alphabets/K.png"))
        k= WordCloud(mask=k_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(k,(x,y))
        x+=900
    elif inp[i]=='L':    
        l_mask=np.array(Image.open("Alphabets/L.png"))
        l= WordCloud(mask=l_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(l,(x,y))
        x+=900
    elif inp[i]=='M':    
        m_mask=np.array(Image.open("Alphabets/M.png"))
        m= WordCloud(mask=m_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(m,(x,y))
        x+=900
    elif inp[i]=='N':    
        n_mask=np.array(Image.open("Alphabets/N.png"))
        n= WordCloud(mask=n_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(n,(x,y))
        x+=900
    elif inp[i]=='O':    
        o_mask=np.array(Image.open("Alphabets/O.png"))
        o= WordCloud(mask=o_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(o,(x,y))
        x+=900
    elif inp[i]=='P':
        p_mask=np.array(Image.open("Alphabets/P.png"))
        p= WordCloud(mask=p_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(p,(x,y))
        x+=900
    elif inp[i]=='Q':    
        q_mask=np.array(Image.open("Alphabets/Q.png"))
        q= WordCloud(mask=q_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(q,(x,y))
        x+=900
    elif inp[i]=='R':    
        r_mask=np.array(Image.open("Alphabets/R.png"))
        r= WordCloud(mask=r_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(r,(x,y))
        x+=900
    elif inp[i]=='S':    
        s_mask=np.array(Image.open("Alphabets/S.png"))
        s= WordCloud(mask=s_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(s,(x,y))
        x+=900
    elif inp[i]=='T':    
        t_mask=np.array(Image.open("Alphabets/T.png"))
        t= WordCloud(mask=t_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(t,(x,y))
        x+=900
    elif inp[i]=='U':    
        u_mask=np.array(Image.open("Alphabets/U.png"))
        u= WordCloud(mask=u_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(u,(x,y))
        x+=900
    elif inp[i]=='V':    
        v_mask=np.array(Image.open("Alphabets/V.png"))
        v= WordCloud(mask=v_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(v,(x,y))
        x+=900
    elif inp[i]=='W':    
        w_mask=np.array(Image.open("Alphabets/W.png"))
        w= WordCloud(mask=w_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(w,(x,y))
        x+=900
    elif inp[i]=='X':    
        x_mask=np.array(Image.open("Alphabets/X.png"))
        x1= WordCloud(mask=x_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(x1,(x,y))
        x+=900
    elif inp[i]=='Y':
        y_mask=np.array(Image.open("Alphabets/Y.png"))
        y1= WordCloud(mask=y_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(y1,(x,y))
        x+=900
    elif inp[i]=='Z':
        z_mask=np.array(Image.open("Alphabets/Z.png"))
        z= WordCloud(mask=z_mask,width=50,height=50).generate_from_frequencies(text).to_image()
        base.paste(z,(x,y))
        x+=900
    else:
        continue

base.show()
base.save("my_name.bmp")



