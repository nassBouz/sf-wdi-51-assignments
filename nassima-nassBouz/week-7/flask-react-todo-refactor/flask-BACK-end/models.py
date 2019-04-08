from app import db, marshmallow


class Todo(db.Model):
    __table_args__ = {'extend_existing': True} 
	
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    completed = db.Column(db.Boolean)
    priority=  db.Column(db.Integer)

    def __init__(self, body, completed, priority):
        self.body = body
        self.completed = completed
        self.priority = priority

    @classmethod
    def create_todo(cls, body, completed, priority):
        new_todo = Todo(body, completed, priority)
        try:
            db.session.add(new_todo)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return todo_schema.jsonify(new_todo)

    @classmethod
    def get_todo(cls,todo_id):
        todo = Todo.query.get(todo_id)
        return todo_schema.jsonify(todo)
    
    @classmethod
    def get_todos(cls):
        todos = Todo.query.all()
        return todos_schema.jsonify(todos)
    
    @classmethod
    def delete_todo(cls,todo_id):
        todo = Todo.query.get(todo_id)
        try:
            db.session.delete(todo)
            db.session.commit()
        except:
            db.session.rollback()
            raise

        return todo_schema.jsonify(todo)

    @classmethod
    def update_todo(cls,todo_id, body, completed, priority):
        todo = Todo.query.get(todo_id)
        # todo = Todo(body, completed, priority)
        todo.body = body
        todo.completed = completed
        todo.priority = priority
        try:
            db.session.update(todo)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        return todo_schema.jsonify(todo)
    # #UPDATE A Todo
    # @classmethod
    # def update_todo(cls, todoid):
    #     todo = Todo.query.get(todoid)
    #     body = request.json.get('body', todo.body)
    #     priority = request.json.get('priority', todo.priority)
    #     completed = request.json.get('completed', todo.completed)

    #     try:
    #         db.session.update(todo)
    #         db.session.commit()
    #     except:
    #         db.session.rollback
    #         raise Exception('Session rollback')
    #     return todo_schema.jsonify(todo)
    
        
class TodoSchema(marshmallow.Schema):
  class Meta:
    fields = ('id', 'body', 'completed', 'priority')

todo_schema = TodoSchema(strict=True)
todos_schema = TodoSchema(many=True, strict=True)
if __name__ == 'models':
    db.create_all()