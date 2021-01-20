What it can do and how!

/reg/ POST - create user, need username and password in body login via Basic auth

/create_chat/ POST - create chat between logged in user and found by username (given in body "receiver") user

/messages/ GET - show message history between logged in user and found by username (given in body "receiver") user 
           POST - add message in chat between logged in user and found by username (given in body "receiver") user with text (given in body "message_text")
