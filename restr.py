try:
    print('Restoranimiza xos geldiz eziz musteri')
    print('Halhazirda bu secimler vardir')
    menu={

        '1 - Salatlar':'1-Toyuq salati 3 azn\n 2 -Gobelek salati 4 azn\n 3 -Sezar salat 7 azn ',
        '2 - Şorbalar':'Bors 4 azn\nMerci3azn',
        '3 - Soyuq Qəlyanaltı':'Ağ pendir 3 azn\nsuzme 3 azn\nbilincikq 1.50',
        '4 - Milli Yeməklər': '1.Hisə vərilmiş dana qabırğası 18 az\n2. Quzu antrikotu baby kartof ilə 21azn\n3. Dana antrikot tərəvəz ilə 18azn\n'
        
      
        
    
    }
  
    while True:
        for i in menu.keys():
            print(i)
        print()
        s2=input('Zehmet olmasa daxil edin:').strip()

        if s2=='1':
           
            while True:
                print(menu['1 - Salatlar'])
                s1=input('zehmet olmasa salati secin:')
                if s1=='1':
                    print('Sifarisiniz qeyde alindi')
                    input('davam etmek ucun ENTER basin')
                    break




        elif s2=='2':
            print(menu['2 - Şorbalar'])
            input('davam etmek ucun ENTER basin')

        elif s2=='3':
            print(menu['3 - Soyuq Qəlyanaltı'])
            input('davam etmek ucun ENTER basin')

        elif s2=='4':
            print(menu['4 - Milli Yeməklər'])
            input('davam etmek ucun ENTER basin')







        
        
        
            












except Exception:
    print('xeta')

finally:
    print('Bizi secdiyiniz ucun tesekkur edirik')

