>>> users.delete().where(users.c.name == 'ed').execute()