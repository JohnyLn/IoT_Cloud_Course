from pyrabbit.api import Client
#https://github.com/bkjones/pyrabbit
#pip3 install pyrabbit
#https://pyrabbit.readthedocs.io/en/latest/
#https://pyrabbit.readthedocs.io/en/latest/api.html
#https://github.com/bkjones/pyrabbit/blob/master/pyrabbit/api.py

new_client =""

#global variable
cl = Client('localhost:15672','rabbitmq','rabbitmq')
cl.is_alive()

def main():
    #Pyrabbit api


    dic_vh = cl.get_vhost_names()

    confirm = False


    while(confirm == False):
        print("Liste les vh :\n",dic_vh)
        print("Enter le nom du nouveau client")
        new_client = input()
        if(new_client==""):
            print("/!\ Nom non valide")
        elif(check_vh(new_client,dic_vh) == True) :
            print("Valider le nom ",new_client, "(y/n)?")
            confirm_res = input()
            if confirm_res == "Y" or confirm_res =="y":
                    confirm=True
    return new_client   

def check_vh(new_name,dic_vh):
    """
    Check if a name is in a dic
    """
    for _ in dic_vh: 
        if (_ == new_name):
            print("/!\ Un virtual host possède déjà ce nom")
            return False
    return True

def deploy_new_client(new_client):
    #Create vh first wit new_client
    cl.create_vhost(new_client)
    #Create fanout_ + new_client
    fanout_name ="fanout_" + new_client
    print(fanout_name)
    cl.create_exchange(vhost=new_client,name=fanout_name,xtype="fanout")
    #def create_exchange(self,vhost,name,xtype,auto_delete=False,durable=True,internal=False,arguments=None):
    #Create queues client_info and client_log inside the new lcient virtual host
    cl.create_queue(vhost=new_client,name="client_info")
    cl.create_queue(vhost=new_client,name="client_log")

    #Let's bind both queue with the fanout_client
    cl.create_binding(vhost=new_client,exchange=fanout_name,queue="client_info",rt_key="c_info")
    cl.create_binding(vhost=new_client,exchange=fanout_name,queue="client_log",rt_key="c_log")

    cl.publish(vhost=new_client,xname=fanout_name,rt_key="welcome",payload="Welcome "+new_client+" !!")

if __name__ == '__main__' :
    try : 
        new_client = main()
        deploy_new_client(new_client)
    except KeyboardInterrupt :
        print('INterrupted')
        try:
            sys.exit(0)
        except SystemExit :
            OS._exit(0)


#client_global = input("Enter le nom du nouveau client")

#cl.create_vhost('example_vhost')
#cl.delete_vhost('example_vhost')