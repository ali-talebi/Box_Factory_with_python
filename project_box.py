class DRIVER : 
    driver_names = []
    drivers = []
    def __init__(self,DRIVER_USERNAME,POSITION,SERVICE_CATEGORY):
        self.USERNAME = DRIVER_USERNAME 
        self.POSITION = POSITION 
        self.SERVICE_CATEGORY = SERVICE_CATEGORY 
        self.STATUS = 'FREE' 
        self.CREDIT = 0 
        DRIVER.driver_names.append(DRIVER_USERNAME)
        DRIVER.drivers.append(self)
        self.driver_order = []
        
        
    @classmethod
    def ADD_DRIVER(cls , DRIVER_USERNAME,POSITION,SERVICE_CATEGORY):
        if DRIVER_USERNAME in DRIVER.driver_names : 
            print('user previously added')
        else : 
            print('user added successfully')
            return DRIVER(DRIVER_USERNAME,POSITION,SERVICE_CATEGORY) 
        
            

class ORDER:
    n = 1
    S_Pending_van = 0
    S_Pending_bike = 0
    S_Pending_truck = 0
    sode_sherkat = 0 
    orders = []
    
    
    def __init__(self,SERVICE_CATEGORY,START_POSITION,FINISH_POSITION):
        self.SERVICE_CATEGORY = SERVICE_CATEGORY 
        self.START_POSITION =  START_POSITION 
        self.FINISH_POSITION = FINISH_POSITION
        self.ORDER_Id =  ORDER.n 
        self.write_status = ['PENDING']
         
        print(ORDER.n)
        self.STATUS = 'PENDING'
        if SERVICE_CATEGORY == 'VAN' and self.STATUS == 'PENDING': 
            ORDER.S_Pending_van += 1 
        if SERVICE_CATEGORY == 'BIKE' and self.STATUS == 'PENDING': 
            ORDER.S_Pending_bike += 1 
        if SERVICE_CATEGORY == 'TRUCK' and self.STATUS == 'PENDING': 
            ORDER.S_Pending_truck += 1 
        ORDER.n += 1
        self.driver_for_this = None
        self.cost = self.check_cost(self.START_POSITION , self.FINISH_POSITION)
        ORDER.orders.append(self)
        
        
        
    @classmethod 
    def CREATE_ORDER(cls,SERVICE_CATEGORY,START_POSITION,FINISH_POSITION) : 
        if START_POSITION == FINISH_POSITION  : 
            print('invalid order')
        else : 
            return ORDER(SERVICE_CATEGORY,START_POSITION,FINISH_POSITION)
        
        
        
    def check_cost(self,point_one , point_two ) :
        if self.SERVICE_CATEGORY == 'VAN': 
            cost = (ORDER.S_Pending_van + abs(int(point_one[0]) - int(point_two[0])) + 
            abs(int(point_one[1]) - int(point_two[1])) ) * 100 
            #print('ORDER.S_Pending_van ',ORDER.S_Pending_van)
        elif self.SERVICE_CATEGORY == 'BIKE':
            cost = (ORDER.S_Pending_bike + abs(int(point_one[0]) - int(point_two[0])) + 
            abs(int(point_one[1]) - int(point_two[1])) ) * 100 
            #print('ORDER.S_Pending_bike ',ORDER.S_Pending_bike)
        elif self.SERVICE_CATEGORY == 'TRUCK':
            cost = (ORDER.S_Pending_truck + abs(int(point_one[0]) - int(point_two[0])) + 
            abs(int(point_one[1]) - int(point_two[1])) ) * 100 
            #print('ORDER.S_Pending_truck ',ORDER.S_Pending_truck)
        return cost 
    
    
    
    
    
    
task = []
while True :
    t = input()
    if t != 'END' : 
        task.append(t)
    else : 
        break 
    


for _ in task : 
    if 'ADD-DRIVER' in _ : 
        x = int(_.split(' ')[2].replace('(','').replace(',',''))
        y = int( _.split(' ')[3].replace(')',''))
        point = (x,y)
        DRIVER.ADD_DRIVER( _.split(' ')[1] , point,_.split(' ')[4])
        
    elif 'CREATE-ORDER' in _ : 
        x_s = int(_.split(' ')[2].replace('(','').replace(',',''))
        y_s = int( _.split(' ')[3].replace(')',''))
        point_s = (x_s,y_s)
        x_f = int(_.split(' ')[4].replace('(','').replace(',',''))
        y_f = int(_.split(' ')[5].replace(')',''))
        point_f = (x_f,y_f)
        order = ORDER.CREATE_ORDER( _.split(' ')[1] ,point_s ,point_f)
        
    elif 'GET-DRIVER ' in _ :
        flag_for_get_driver = 0
        name = _.split(' ')[1]
        for i in DRIVER.drivers:
            try :
                if i.USERNAME == name   :
                    flag_for_get_driver = 1 
                    print(i.STATUS,'',i.POSITION,'',int(i.CREDIT))
                    break 
            except : 
                pass 
        if flag_for_get_driver == 1 : 
            flag_for_get_driver = 1
            
        else : 
            #print('#گوشت',_)
            print('invalid driver name')
            flag_for_get_driver = 0
            

    elif 'GET-ORDER ' in _ :
        flag_for_get_order= 0 
        check_order = int(_.split(' ')[1])
        for obj in ORDER.orders : 
            try:
                #print('order id of orders :  ' , obj.ORDER_Id , ' order id that you wnat : ' , check_order)
                
                if obj.ORDER_Id == check_order :
                 
                    print(obj.STATUS,'',obj.driver_for_this,'',int(obj.cost))
                    flag_for_get_order = 1 
                    break
            except:
                pass 
        if flag_for_get_order == 0 :
            print('invalid order')
            
            
    elif  'ASSIGN-NEXT-ORDER' in _ :
        name_for_search = _.split(' ')[1]
        flag_for_assing_next_order = 0 
        for person in DRIVER.drivers :
            try : 
                if person.USERNAME == name_for_search : 
                    #print('name that find : ',person.USERNAME , 'status : ' , person.STATUS )
                    
                    flag_for_assing_next_order = 1 
                    person_select = person
                    break 
                    
            except : 
                pass 
        if flag_for_assing_next_order == 0 : 
            print("invalid driver name")
            
        if flag_for_assing_next_order == 1 : 
            if person_select.STATUS == "BUSY" : 
                print("driver is already busy ")
            else :
                dict_distance = {}
                #print('distance is : ')
                for obj_order in ORDER.orders :
                    if obj_order.STATUS == 'PENDING' and person_select.SERVICE_CATEGORY == obj_order.SERVICE_CATEGORY : 
                        distance = abs( int(obj_order.START_POSITION[0]) - int(person_select.POSITION[0]) ) + abs(int(obj_order.START_POSITION[1]) - int(person_select.POSITION[1]))
                        dict_distance[obj_order.ORDER_Id] = distance
                        
                        
                        #print(distance,end = ' ')
                        
                select = min(zip(dict_distance.values() ,dict_distance.keys() ))
                
                flag_for_this_order =  0 
                for obj_order in ORDER.orders : 
                    if obj_order.ORDER_Id == int(select[1]) :
                        obj_order.STATUS = 'ARRIVED'
                        obj_order.write_status.append(obj_order.STATUS)
                        if obj_order.SERVICE_CATEGORY == 'BIKE' : 
                            obj_order.S_Pending_bike -= 1 
                        if obj_order.SERVICE_CATEGORY == 'VAN' : 
                            obj_order.S_Pending_van -= 1 
                        if obj_order.SERVICE_CATEGORY == "TRUKE" : 
                            obj_order.S_Pending_truck -= 1 
                            
                            
                        #print(select)
                        obj_order.driver_for_this = person_select.USERNAME
                        person_select.STATUS = 'BUSY'
                        flag_for_this_order = 1 
                        person_select.driver_order.append(obj_order.ORDER_Id)
                        print(f'{obj_order.ORDER_Id} assigned to {person_select.USERNAME}')
                        #print('status order',obj_order.STATUS  , 'status driver',person_select.STATUS)
                if flag_for_this_order == 0 : 
                    pass
                    # print('natonestim obect order ro paida konim ')
                    

    elif 'ORDER-UPDATE' in _ : 
        DRIVER_USERNAME = _.split(' ')[2]
        order_id_in_order_update = int(_.split(' ')[3])
        status_in_order_update = _.split(' ')[1]
        flag_for_order_update_name = 0 
        for obj_person in DRIVER.drivers :
            try : 
                if obj_person.USERNAME == DRIVER_USERNAME : 
                    flag_for_order_update_name = 1  
                    find_person = obj_person
                
            except : 
                pass 
                
        if flag_for_order_update_name == 1 :
            if order_id_in_order_update !=  find_person.driver_order[-1] : 
                print('wrong order-id')
            else : 
                for obj_in_orders in ORDER.orders:
                    if obj_in_orders.ORDER_Id ==  order_id_in_order_update : 
                        order_find = obj_in_orders 
            
                
                if status_in_order_update == 'PICKUP' :
                    if order_find.write_status[-1] == 'ARRIVED' :
                        print(f'status changed successfully')
                        order_find.STATUS = 'PICKUP' 
                        order_find.write_status.append('PICKUP')
                        find_person.POSITION = order_find.START_POSITION
                        
                    else : 
                        print('invalid status')
                        
                            
                        
                elif status_in_order_update == 'DELIVERED' : 
                    if order_find.write_status[-1] == 'PICKUP' : 
                        order_find.STATUS = 'DELIVERED'
                        order_find.write_status.append('DELIVERED')
                        find_person.CREDIT += 0.8 * order_find.cost
                        ORDER.sode_sherkat += 0.2 * order_find.cost 
                        find_person.POSITION = order_find.FINISH_POSITION
                        print(f'status changed successfully')
                            
                        find_person.STATUS = 'FREE'
                            
        elif flag_for_order_update_name == 0 : 
            print('invalid driver name')
            
            
    elif 'GET-COMPANY' in _ :
        print(int(ORDER.sode_sherkat))
        
    
    elif 'GET-DRIVER-LIST' in _ :
        #print('this is get driver list ', _)
        status_for_get_driver_list = _.split(' ')[1]
        parcham_in_get_driver_list = 0
        for person in DRIVER.drivers : 
            try: 
                if person.STATUS == status_for_get_driver_list : 
                    print(person.USERNAME,end=' ')
                    parcham_in_get_driver_list = 1 
            except:
                pass 
        if parcham_in_get_driver_list == 0 : 
            print('None')
        print()
        
    elif 'GET-ORDER-LIST' in _ : 
        want_status = _.split(' ')[1]
        flag_order_list = 0
        for obj_l in ORDER.orders : 
            if obj_l.STATUS == want_status : 
                print(obj_l.ORDER_Id , end=' ')
                flag_order_list = 1
        
        if flag_order_list == 0 : 
            print('None')
        if flag_order_list == 1 : 
            print()
        


        
    elif 'GET-NEAR-DRIVER' in _ :
        position_for_get_near_driver_x = int(_.split(' ')[1].replace('(','').replace(',',''))
        position_for_get_near_driver_y = int(_.split(' ')[2].replace(')',''))
        count_for_get_near_driver = int(_.split(' ')[3])
        dict_distance_for_get_near_driver = {}
        for person in DRIVER.drivers : 
            try: 
            
                if person.STATUS == 'FREE' : 
                    faseleh = abs(position_for_get_near_driver_x - int(person.POSITION[0])) + abs(position_for_get_near_driver_y - int(person.POSITION[1]))
                    dict_distance_for_get_near_driver[person.USERNAME] = faseleh
                    #print('d : ' , faseleh , 'name : ',persone.USERNAME)
            except:
                pass 

        select_for_get_near_driver = sorted(zip(dict_distance_for_get_near_driver.values(),dict_distance_for_get_near_driver.keys()))
        c_near = 0 
        flag_for_c_near = 0 
        for i , j in select_for_get_near_driver : 
            if c_near < count_for_get_near_driver : 
                print(j , end=' ')
                flag_for_c_near = 1 
                c_near += 1 
            else : 
                break
        if flag_for_c_near == 0 :
            print('None')
        
        print()
                    
        

                
    elif 'GET-CNT-ORDER' in _ :
        x_for_get_cnt_order = int(_.split(' ')[1].replace('(','').replace(',',''))
        y_for_get_cnt_order =  int(_.split(' ')[2].replace(')',''))
        distance_for_get_cnt_order = int(_.split(' ')[3])
        finish_or_start_get_cnt_order = _.split(' ')[4]
        dict_for_distance_get_cnt_order = {}
        counter_for_dd = 0 
        if finish_or_start_get_cnt_order == 'START' : 
            for object_order in ORDER.orders : 
                dd = abs(int(object_order.START_POSITION[0]) - x_for_get_cnt_order ) + abs(int(object_order.START_POSITION[1]) - y_for_get_cnt_order )
                if dd <= distance_for_get_cnt_order :  
                    counter_for_dd += 1 
            print(counter_for_dd)

                    
        elif  finish_or_start_get_cnt_order == 'FINISH' : 
            for object_order in ORDER.orders : 
                dd = abs(int(object_order.FINISH_POSITION[0]) - x_for_get_cnt_order ) + abs(int(object_order.FINISH_POSITION[1]) - y_for_get_cnt_order )
                if dd <= distance_for_get_cnt_order :  
                    counter_for_dd += 1 
            print(counter_for_dd)
            
            

    elif 'GET-NEAREST-PENDING-ORDER' in _ : 
        x_GET_NEAREST_PENDING_ORDER = int(_.split(' ')[1].replace('(','').replace(',',''))
        y_GET_NEAREST_PENDING_ORDER = int(_.split(' ')[2].replace('(','').replace(')',''))
        flag_here = 0 
        dict_GET_NEAREST_PENDING_ORDER = {}
        for order in ORDER.orders :
            
            if order.STATUS == 'PENDING' : 
                d2 = abs(order.START_POSITION[0] - x_GET_NEAREST_PENDING_ORDER ) + abs(order.START_POSITION[1] - y_GET_NEAREST_PENDING_ORDER )
                dict_GET_NEAREST_PENDING_ORDER[order.ORDER_Id] = d2 
        
        try:
            s = min(zip(dict_GET_NEAREST_PENDING_ORDER.values() , dict_GET_NEAREST_PENDING_ORDER.keys()))
            flag_here = 1 
        except : 
            pass 
        
        if flag_here == 0 : 
            print('None')
        else : 
            print(s[1])

            
            
  
            
                    
                    
    
                    
                    

            
        
        
        
