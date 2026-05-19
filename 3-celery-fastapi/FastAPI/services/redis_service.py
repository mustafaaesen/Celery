from redis import Redis 
import json 


redis_client=Redis(host="redis-service",port=6379,decode_responses=True)


#redis bağlantısı kubernetes serviste çalışacak

#basic operations

def get_cache(key: str):
     
    data=redis_client.get(key)
    
    if data:
        return json.loads(data)
    
    return None #veri yoksa boş dönme

def set_cache(key: str, value, ttl :int=60):
    
    redis_client.set(key,json.dumps(value), ex=ttl)   #cache ayarlama tarafı ttl 60 saniyelik cache
    

def delete_cache(key: str):
    redis_client.delete(key)