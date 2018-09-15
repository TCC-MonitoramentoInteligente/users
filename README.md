# User management service


### Setup
1. Create virtualenv `$ virtualenv --system-site-packages -p python3 venv`
2. Activate virtualenv `$ source venv/bin/activate`
3. Install requirements `$ pip install -r requirements.txt`

### Run
`$ python3 service/manage.py runserver <IP_SERVICE>:8000`

### SCHEMA
```
<User API "http://127.0.0.1:8000/docs/">
    cameras: {
        list()
        create(id, model_name, common_name, user, [address])
        read(id)
        update(id, id, model_name, common_name, user, [address])
        partial_update(id, [id], [model_name], [common_name], [address], [user])
        delete(id)
    }

    users: {
        list()
        create(email, password, name, cpf, [last_name], [address])
        read(id)
        update(id, email, password, name, cpf, [last_name], [address])
        partial_update(id, [email], [password], [name], [last_name], [cpf], [address])
        delete(id)
    }
```
### Usage examples
- Running  
`$ python3 service/manage.py runserver 127.0.0.1:8000`  
- Create a user (as a staff user)  
`$ python3 service/superuser.py` 
- Create a user  
![Alt text](service/create_user_sample.png?raw=true "User creation")
