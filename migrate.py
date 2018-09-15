from playhouse.migrate import *

db = SqliteDatabase('todos.sqlite')
migrator = SqliteMigrator(db)

migrate(
	migrator.drop_not_null('todo', 'content'),
)