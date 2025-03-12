
import traceback
import pymongo

client = pymongo.MongoClient(
        "mongodb+srv://sahilisprobhai60:R8VDIcpfqOwmoIm5@cluster0.aryu0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
result = str(client)

if "connect=True" in result:
    try:
        print("MONGODB CONNECTED SUCCESSFULLY ✅")
    except:
        pass
else:
    try:
        print("MONGODB CONNECTION FAILED ❌")
    except:
        pass

folder = client["MASTER_DATABASE"]
usersdb = folder.USERSDB
chats_auth = folder.CHATS_AUTH
gcdb = folder.GCDB
sksdb = client["SKS_DATABASE"].SKS
confdb = client["SKS_DATABASE"].CONF_DATABASE
