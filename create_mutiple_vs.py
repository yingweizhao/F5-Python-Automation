import os
def create_vs():
     network="10.10.10"
     for i in range(20,220):
         cmd='tmsh create  ltm virtual vs_%i destination %s.%i:80 profiles add { tcp }'%(i,network,i)
         modify="tmsh modify ltm virtual vs_%i rules { irules_response }"%i
         print modify
         #os.system(cmd)
if __name__=="__main__":
    create_vs()